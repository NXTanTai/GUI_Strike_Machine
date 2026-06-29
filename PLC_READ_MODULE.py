import struct
import time
import logging
import threading
import snap7
from typing import Any, Optional
from snap7.error import * # type: ignore
from snap7.type import * # type: ignore
from snap7.type import Parameter
from snap7.util import get_bool, get_real, get_dint, get_int, get_string
from PySide6.QtCore import QObject, QTimer, Signal, Slot, QThread, Qt

class PLCRead(QObject):
    """
    Object dùng để lấy dữ liệu từ PLC
    \n
    Có thể tạo nhiều Object để xử lí nhiều vùng dữ liệu hoặc từ nhiều PLC
    \n
    Nếu chỉ định đọc 1 vùng riêng biệt thì lên cấu hình db_layout riêng
    """
    init_data     = Signal()           # Dùng để trigger lấy dữ liệu hiện có sau khi connect thành công
    data_ready    = Signal(dict)
    error         = Signal(str)
    connected     = Signal(bool)
    disconnected  = Signal()
    finished      = Signal()           

    _stop_read    = Signal()           

    def __init__(
        self,
        ip:        str                   = "172.16.100.100",
        rack:      int                   = 0,
        slot:      int                   = 1,
        db_number: int                   = 1,
        db_layout: Optional[list[tuple[str, str, int, Any]]]        = None,
        db_size:   int                   = 584,
        poll_ms:   int                   = 500,
        retry_ms:  int                   = 3000,
        logger                           =None,
        parent:    Optional[QObject]     = None,
        ):
        super().__init__(parent)
        self._ip        = ip
        self._rack      = rack
        self._slot      = slot
        self._db_number = db_number
        self._db_layout = db_layout
        # print("DB Read Layout: ", self._db_layout)
        self._db_size   = db_size
        self._poll_ms   = poll_ms
        self._retry_ms  = retry_ms
        self.logger     = logger

        self._client:      snap7.client.Client | None = None
        self._poll_timer:  QTimer | None = None
        self._retry_timer: QTimer | None = None
        self._running   = False
        self._last_error_log_time = 0

    @Slot()
    def run(self):
        self._running = True
        if self.logger:
            self.logger.info("[PLC READ]: PLC Read init")
        self._poll_timer = QTimer(self)
        self._poll_timer.setInterval(self._poll_ms)
        self._poll_timer.timeout.connect(self._poll)

        self._retry_timer = QTimer(self)
        self._retry_timer.setInterval(self._retry_ms)
        self._retry_timer.timeout.connect(self._try_connect)

        self._stop_read.connect(self._do_stop, Qt.QueuedConnection) # type: ignore

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
        if self._retry_timer and self._retry_timer.isActive():
            self._retry_timer.setInterval(ms)

    @Slot(int)
    def set_interval(self, interval):
        self._poll_timer.setInterval(interval) # type: ignore

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

        self._disconnect_plc()

        self.finished.emit()
        QThread.currentThread().quit()

    @Slot()
    def _try_connect(self):
        if not self._running:
            return
        
        if self._client and self._client.get_connected():
            return

        self._connect_plc()
        if not self._running:
            self._disconnect_plc()
            return
        if self._client and self._client.get_connected():
            if self._retry_timer and self._retry_timer.isActive():
                self._retry_timer.stop()
            self.init_data.emit()
            if not self._poll_timer.isActive():   # type: ignore
                self._poll_timer.start() # type: ignore
            if self.logger:
                self.logger.info("[PLC READ]: Connected to PLC, started reading")
        else:
            if not self._retry_timer.isActive(): # type: ignore
                self._retry_timer.start()  # type: ignore

    def _connect_plc(self):
        if not self._running:
            return

        result = {"client": None, "error": None}
        done = threading.Event()

        def _do_connect():
            try:
                c = snap7.client.Client()
                c.set_param(Parameter.SendTimeout, 5)         # timeout gửi (giây)
                c.set_param(Parameter.RecvTimeout, 5)         # timeout nhận (giây)
                # Bởi vì kết nối bị "dead silently" sau vài phút idle nên phải set Timeout để nhanh chóng phát hiện dead connection
                c.connect(self._ip, self._rack, self._slot)
                result["client"] = c # type: ignore
            except Exception as exc:
                result["error"] = exc # type: ignore
            finally:
                done.set()

        t = threading.Thread(target=_do_connect, daemon=True)
        t.start()
        while not done.wait(timeout=0.1):
            if not self._running:
                return

        if not self._running:
            if result["client"]:
                try:
                    result["client"].disconnect()
                except:
                    pass
            return

        if result["client"]:
            self._client = result["client"]
            self.connected.emit(True)
        else:
            msg = f"Connection failed: {result['error']}"
            if self.logger:
                now = time.time()
                if now - self._last_error_log_time >= 5:
                    self.logger.error("[PLC READ]: " + msg)
                    self._last_error_log_time = now
            self.error.emit(msg)
            self.connected.emit(False)
            self._client = None

    def _disconnect_plc(self):
        if self._client:
            try:
                self._client.disconnect()
            except Exception:
                pass
            self._client = None
        self.connected.emit(False)

    @Slot()
    def _poll(self):
        if not self._running or not self._client or not self._client.get_connected():
            self._reconnect()
            return

        try:
            t0 = time.perf_counter()
            raw = self._client.db_read(self._db_number, 0, self._db_size)
            result = self._parse(raw)
            self.data_ready.emit(result)
            elapsed = (time.perf_counter() - t0) * 1000
            if elapsed > 200:
                if self.logger:
                    self.logger.warning("[PLC READ]: Slow response %.1fms", elapsed)
        except S7Error as exc:
            if self.logger:
                self.logger.warning("[PLC READ]: Read error: %s", exc)
            self.error.emit(f"Read error: {exc}")
            self._reconnect()

    @Slot()
    def _reconnect(self):
        if not self._running:
            return
        self._poll_timer.stop() # type: ignore
        self._disconnect_plc()
        self._retry_timer.start() # type: ignore

    def _parse(self, raw: bytearray) -> dict:
        if not self._db_layout:
            return {}

        result: dict[str, Any] = {}
        for name, dtype, offset, bit in self._db_layout:
            try:
                if dtype == "BOOL":
                    result[name] = get_bool(raw, offset, bit)
                elif dtype == "REAL":
                    result[name] = get_real(raw, offset)
                elif dtype == "DINT":
                    result[name] = get_dint(raw, offset)
                elif dtype == "INT":
                    result[name] = get_int(raw, offset)
                elif dtype == "STRING":
                    result[name] = get_string(raw, offset)
                else:
                    result[name] = None
            except Exception as exc:
                result[name] = None
                if self.logger:
                    self.logger.error("[PLC READ]: Parse error [%s]: %s", name, exc)

        return result