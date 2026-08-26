"""
HYFW Modbus RTU Serial Reader - Module
========================================
Module QObject dùng để đọc dữ liệu từ đồng hồ đo điện HYFW (Modbus RTU)
qua cổng COM (RS485/USB-RS485), thiết kế theo cùng mô hình với PLCRead:
    - chạy trong QThread riêng (moveToThread + run() slot)
    - poll dữ liệu định kỳ bằng QTimer
    - tự động reconnect khi mất kết nối, có retry timer
    - phát signal data_ser(dict) mỗi lần đọc thành công
    - có logger riêng theo từng module (ghi ra file xoay vòng)

Tự động dò cổng COM:
    - Không cần khai báo cứng "COM7" nữa. Module sẽ quét danh sách cổng COM
      (qua pyserial) và tìm cổng có mô tả (description) chứa từ khóa
      port_keyword (mặc định "CH340", khớp với "USB-SERIAL CH340").
    - Nếu tìm thấy cổng phù hợp -> tự động kết nối, nếu kết nối thất bại
      hoặc quá thời gian connect_timeout (mặc định 5s) -> thử lại (retry_ms,
      mặc định 5s/lần).
    - Nếu KHÔNG tìm thấy cổng nào có tên như vậy -> cứ mỗi scan_ms (mặc
      định 3s) quét lại danh sách cổng COM 1 lần cho đến khi tìm thấy.
    - Vẫn có thể ép cứng 1 cổng cụ thể bằng cách truyền port="COM7" khi
      khởi tạo (khi đó bỏ qua bước dò tự động).

Yêu cầu thư viện:
    pip install pymodbus pyserial PySide6

Cấu hình mặc định theo file thanh ghi (2XXX Zone Basic Setting):
    - địa chỉ Modbus (communication address, reg 0x2001) mặc định = 1
    - baud rate (reg 0x2003) mặc định = 3 -> 9600
    - kiểu khung 485 (reg 0x2002) mặc định = 0 -> 8N1

Ghi chú:
    - Các thanh ghi đo lường (1XXX, 4XXX...) dùng function code 04
      (Read Input Register).
    - Giả định thứ tự word là Big-Endian (word cao trước) cho các giá trị
      32-bit (total active energy...). Nếu đọc ra số bất thường, hãy khởi
      tạo module với word_order_big_endian=False.
"""

import os
import sys
import struct
import time
import threading
import logging
import logging.handlers
from datetime import datetime
from typing import Any, Optional

import serial.tools.list_ports as list_ports
from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException

from PySide6.QtCore import QObject, QTimer, Signal, Slot, QThread, Qt

REALTIME_REGISTERS = {
    "phase_A_voltage_V":         dict(address=4096, count=1, scale=100, signed=False),
    "phase_B_voltage_V":         dict(address=4097, count=1, scale=100, signed=False),
    "phase_C_voltage_V":         dict(address=4098, count=1, scale=100, signed=False),
    "phase_A_current_A":         dict(address=4105, count=1, scale=100, signed=False),
    "phase_B_current_A":         dict(address=4106, count=1, scale=100, signed=False),
    "phase_C_current_A":         dict(address=4107, count=1, scale=100, signed=False),
    "total_active_power_kW":     dict(address=4113, count=1, scale=1000, signed=True),
    "total_reactive_power_kvar": dict(address=4117, count=1, scale=100, signed=True),
    "total_apparent_power_kVA":  dict(address=4121, count=1, scale=100, signed=False),
    "power_factor":              dict(address=4125, count=1, scale=100, signed=True),
    "frequency_Hz":              dict(address=4126, count=1, scale=100, signed=False),
}

ENERGY_REGISTERS = {
    "total_active_energy_kWh":   dict(address=16384, count=2, scale=10),
    "forward_active_energy_kWh": dict(address=16386, count=2, scale=10),
    "reverse_active_energy_kWh": dict(address=16388, count=2, scale=10),
}


def decode_u32(high: int, low: int, word_order_big_endian: bool = True) -> int:
    """Ghép 2 thanh ghi 16-bit thành số unsigned 32-bit."""
    if word_order_big_endian:
        raw = struct.pack(">HH", high, low)
    else:
        raw = struct.pack(">HH", low, high)
    return struct.unpack(">I", raw)[0]


def decode_i16(value: int) -> int:
    """Chuyển thanh ghi 16-bit unsigned -> signed."""
    return struct.unpack(">h", struct.pack(">H", value))[0]


def find_serial_port(keyword: str = "CH340") -> Optional[str]:
    """
    Quét danh sách cổng COM hiện có, trả về tên cổng (VD: 'COM7') đầu tiên
    có description/manufacturer chứa `keyword` (không phân biệt hoa thường).
    Trả về None nếu không tìm thấy.
    """
    keyword_low = keyword.lower()
    try:
        ports = list_ports.comports()
    except Exception:
        return None

    for p in ports:
        desc = (p.description or "")
        manu = (getattr(p, "manufacturer", "") or "")
        hwid = (getattr(p, "hwid", "") or "")
        if keyword_low in desc.lower() or keyword_low in manu.lower() or keyword_low in hwid.lower():
            return p.device
    return None


class HYFWSerialRead(QObject):
    """
    Object dùng để lấy dữ liệu từ đồng hồ đo điện HYFW qua Modbus RTU (Serial).
    \n
    Có thể tạo nhiều Object để đọc nhiều đồng hồ (nhiều device_id trên cùng
    1 cổng COM - bus RS485, hoặc nhiều cổng COM khác nhau).
    \n
    Cổng COM có thể tự động dò theo `port_keyword` (mặc định "CH340"), hoặc
    ép cứng bằng cách truyền `port="COM7"`.
    """

    init_data    = Signal()
    data_ser   = Signal(dict)
    error        = Signal(str)
    connected    = Signal(bool)
    disconnected = Signal()
    finished     = Signal()
    elapsed_time = Signal(float)

    _stop_read   = Signal()

    def __init__(
        self,
        name_module: str            = "No 1.",
        port:        Optional[str]  = None,        # None -> tự động dò theo port_keyword
        port_keyword: str           = "CH340",      # từ khóa nhận diện cổng, VD "USB-SERIAL CH340"
        baudrate:    int            = 9600,
        parity:      str            = "N",
        stopbits:    int            = 1,
        bytesize:    int            = 8,
        device_id:   int            = 1,
        timeout:     float          = 2,
        word_order_big_endian: bool = True,
        poll_ms:     int            = 1000,
        retry_ms:    int            = 5000,          # thời gian chờ trước khi thử kết nối lại khi ĐÃ thấy cổng nhưng connect fail
        scan_ms:     int            = 3000,           # thời gian giữa các lần quét khi KHÔNG thấy cổng nào phù hợp
        connect_timeout: float      = 5.0,             # timeout tối đa cho 1 lần thử kết nối cổng
        logger_parent               = None,
        parent: Optional[QObject]   = None,
    ):
        super().__init__(parent)
        self._name_module   = name_module
        self._fixed_port    = port
        self._port_keyword  = port_keyword
        self._baudrate      = baudrate
        self._parity        = parity
        self._stopbits      = stopbits
        self._bytesize      = bytesize
        self._device_id     = device_id
        self._timeout       = timeout
        self._word_order_big_endian = word_order_big_endian
        self._poll_ms        = poll_ms
        self._retry_ms       = retry_ms
        self._scan_ms        = scan_ms
        self._connect_timeout = connect_timeout
        self.logger          = None
        self.folder           = logger_parent

        self._client:      Optional[ModbusSerialClient] = None
        self._active_port: Optional[str] = None
        self._poll_timer:  Optional[QTimer] = None
        self._retry_timer: Optional[QTimer] = None
        self._running     = False

        self._last_error_log_time: float = 0.0
        self._last_scan_log_time:  float = 0.0

    def _init_logger(self):
        if not self.folder:
            self.logger = None
            return

        logger_name = f"{__name__}.{self._name_module}"
        self.logger = logging.getLogger(logger_name)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        log_dir = self.folder / "Serial Log"
        os.makedirs(log_dir, exist_ok=True)
        log_date = datetime.now().strftime("%d_%m_%Y")
        log_filename = os.path.join(log_dir, f'SERIAL_READ_{self._name_module}_{log_date}.log')

        file_handler = logging.handlers.RotatingFileHandler(
            log_filename,
            maxBytes=5 * 1024 * 1024,
            backupCount=5,
            encoding='utf-8'
        )

        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

        if not getattr(sys, 'frozen', False):
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(file_formatter)
            self.logger.addHandler(stream_handler)

        self.logger.setLevel(logging.INFO)
        self.logger.propagate = True

    @Slot()
    def run(self):
        self._running = True
        self._init_logger()
        if self.logger:
            self.logger.info(f"[SERIAL READ {self._name_module}]: Serial Read {self._name_module} init")

        self._poll_timer = QTimer(self)
        self._poll_timer.setInterval(self._poll_ms)
        self._poll_timer.timeout.connect(self._poll)

        self._retry_timer = QTimer(self)
        self._retry_timer.setInterval(self._scan_ms)   # bắt đầu bằng nhịp quét (chưa biết có cổng hay không)
        self._retry_timer.timeout.connect(self._try_connect)

        self._stop_read.connect(self._do_stop, Qt.QueuedConnection)  # type: ignore

        self._try_connect()

    @Slot()
    def stop(self):
        self._running = False
        self._stop_read.emit()

    def set_poll_interval(self, ms: int):
        self._poll_ms = ms
        if self._poll_timer and self._poll_timer.isActive():
            self._poll_timer.setInterval(ms)

    def set_retry_interval(self, ms: int):
        self._retry_ms = ms

    def set_scan_interval(self, ms: int):
        self._scan_ms = ms

    @Slot(int)
    def set_interval(self, interval: int):
        if self._poll_timer:
            self._poll_timer.setInterval(interval)  # type: ignore

    @Slot()
    def _do_stop(self):
        if self._poll_timer:
            self._poll_timer.stop()
            self._poll_timer.deleteLater()
            self._poll_timer = None

        if self._retry_timer:
            self._retry_timer.stop()
            self._retry_timer.deleteLater()
            self._retry_timer = None

        self._disconnect_serial()
        self.finished.emit()
        QThread.currentThread().quit()

    @Slot()
    def _try_connect(self):
        if not self._running:
            return
        if self._client and self._client.connected:
            return

        port_found = self._connect_serial()

        if not self._running:
            self._disconnect_serial()
            return

        if self._client and self._client.connected:
            if self._retry_timer and self._retry_timer.isActive():
                self._retry_timer.stop()
            self.init_data.emit()
            if self._poll_timer and not self._poll_timer.isActive():
                self._poll_timer.start()
            if self.logger:
                self.logger.info(
                    f"[SERIAL READ {self._name_module}]: Connected to {self._active_port}, "
                    f"started reading device_id={self._device_id} every {self._poll_ms} ms"
                )
        else:
            interval = self._retry_ms if port_found else self._scan_ms
            if self._retry_timer:
                if self._retry_timer.interval() != interval:
                    self._retry_timer.setInterval(interval)
                if not self._retry_timer.isActive():
                    self._retry_timer.start()

    def _connect_serial(self) -> bool:
        """
        Thử tìm cổng COM và kết nối.
        Trả về True nếu tìm thấy cổng phù hợp (dù kết nối thành công hay
        không), False nếu không tìm thấy cổng nào khớp `port_keyword`.
        """
        if not self._running:
            return False

        # 1) Xác định cổng cần dùng
        if self._fixed_port:
            port = self._fixed_port
        else:
            port = find_serial_port(self._port_keyword)

        if not port:
            now = time.time()
            if now - self._last_scan_log_time >= 5:
                if self.logger:
                    self.logger.warning(
                        f"[SERIAL READ {self._name_module}]: Khong tim thay cong COM chua '%s', "
                        f"se quet lai moi %d ms", self._port_keyword, self._scan_ms
                    )
                self._last_scan_log_time = now
            self.connected.emit(False)
            self._client = None
            self._active_port = None
            return False  
        
        result = {"client": None, "error": None}
        done   = threading.Event()

        def _do_connect():
            try:
                c = ModbusSerialClient(
                    port=port,
                    baudrate=self._baudrate,
                    parity=self._parity,
                    stopbits=self._stopbits,
                    bytesize=self._bytesize,
                    timeout=self._timeout,
                )
                ok = c.connect()
                if ok:
                    result["client"] = c  # type: ignore
                else:
                    result["error"] = f"Khong the mo cong {port}"  # type: ignore
            except Exception as exc:
                result["error"] = exc  # type: ignore
            finally:
                done.set()

        t = threading.Thread(target=_do_connect, daemon=True)
        t.start()
        done.wait(timeout=self._connect_timeout)

        if not self._running:
            if result["client"]:
                try:
                    result["client"].close()
                except Exception:
                    pass
            return True

        if not done.is_set():
            # Quá thời gian connect_timeout mà chưa xong -> coi như thất bại
            msg = f"Timeout ({self._connect_timeout}s) khi ket noi cong {port}"
        elif result["client"]:
            self._client = result["client"]
            self._active_port = port
            self.connected.emit(True)
            return True
        else:
            msg = f"Connection failed: {result['error']}"

        now = time.time()
        if now - self._last_error_log_time >= 5:
            if self.logger:
                self.logger.error(f"[SERIAL READ {self._name_module}]: %s", msg)
            self._last_error_log_time = now
        self.error.emit(msg)
        self.connected.emit(False)
        self._client = None
        self._active_port = None
        return True 

    def _disconnect_serial(self):
        if self._client:
            try:
                self._client.close()
            except Exception:
                pass
            self._client = None
        self._active_port = None
        self.connected.emit(False)

    @Slot()
    def _poll(self):
        if not self._running or not self._client or not self._client.connected:
            self._reconnect()
            return

        try:
            t0 = time.perf_counter()
            result = self._read_all()
            elapsed_ms = (time.perf_counter() - t0) * 1000

            if self.logger and elapsed_ms > (self._poll_ms * 1.3):
                self.logger.warning(
                    f"[SERIAL READ {self._name_module}]: Slow response %.1fms",
                    elapsed_ms,
                )

            self.data_ser.emit(result)
            self.elapsed_time.emit(elapsed_ms)

        except ModbusException as exc:
            if self.logger:
                self.logger.warning(f"[SERIAL READ {self._name_module}]: Read error: %s", exc)
            self.error.emit(f"Read error: {exc}")
            self._reconnect()
        except Exception as exc:
            if self.logger:
                self.logger.error(f"[SERIAL READ {self._name_module}]: Unexpected error: %s", exc)
            self.error.emit(str(exc))
            self._reconnect()

    @Slot()
    def _reconnect(self):
        if not self._running:
            return
        if self._poll_timer:
            self._poll_timer.stop()
        self._disconnect_serial()
        if self._retry_timer:
            self._retry_timer.setInterval(self._scan_ms)
            self._retry_timer.start()

    def _read_input_registers(self, address: int, count: int):
        """Function code 04 - Read Input Registers."""
        result = self._client.read_input_registers(
            address=address, count=count, device_id=self._device_id
        )
        if result.isError():
            raise ModbusException(f"Loi doc thanh ghi @{address}: {result}")
        return result.registers

    def _read_all(self) -> dict:
        data: dict[str, Any] = {}

        for name, cfg in REALTIME_REGISTERS.items():
            try:
                regs = self._read_input_registers(cfg["address"], cfg["count"])
                raw = regs[0]
                if cfg["signed"]:
                    raw = decode_i16(raw)
                data[name] = raw / cfg["scale"]
            except Exception as exc:
                data[name] = None
                if self.logger:
                    self.logger.error(
                        f"[SERIAL READ {self._name_module}]: Parse error [%s]: %s",
                        name, exc,
                    )

        for name, cfg in ENERGY_REGISTERS.items():
            try:
                regs = self._read_input_registers(cfg["address"], cfg["count"])
                raw = decode_u32(regs[0], regs[1], self._word_order_big_endian)
                data[name] = raw / cfg["scale"]
            except Exception as exc:
                data[name] = None
                if self.logger:
                    self.logger.error(
                        f"[SERIAL READ {self._name_module}]: Parse error [%s]: %s",
                        name, exc,
                    )

        return data

if __name__ == "__main__":
    from PySide6.QtCore import QCoreApplication

    app = QCoreApplication(sys.argv)

    thread = QThread()
    reader = HYFWSerialRead(
        name_module="HYFW_1",
        port_keyword="CH340",
        device_id=1,
        poll_ms=1000,
        retry_ms=5000,
        scan_ms=3000,
        connect_timeout=5.0,
    )
    reader.moveToThread(thread)

    thread.started.connect(reader.run)
    reader.data_ser.connect(lambda d: print(d))
    reader.error.connect(lambda e: print("Error:", e))
    reader.connected.connect(lambda ok: print("Connected:", ok))
    reader.finished.connect(thread.quit)

    thread.start()
    sys.exit(app.exec())