"""
HYFW Modbus RTU Serial Reader
==============================
Đọc dữ liệu từ đồng hồ đo điện HYFW (Modbus RTU) qua cổng COM (RS485/USB-RS485),
baud rate 9600, dựa theo file "HYFW_Modbus_Register_V2_1_2".

Yêu cầu thư viện:
    pip install pymodbus pyserial

Cấu hình mặc định theo file thanh ghi (2XXX Zone Basic Setting):
    - địa chỉ Modbus (communication address, reg 0x2001) mặc định = 1
    - baud rate (reg 0x2003) mặc định = 3 -> 9600
    - kiểu khung 485 (reg 0x2002) mặc định = 0 -> 8N1 (8 data bit, No parity, 1 stop bit)

Ghi chú:
    - Các thanh ghi đo lường (1XXX, 4XXX...) dùng function code 04 (Read Input Register).
    - Các thanh ghi cấu hình (2XXX...) dùng function code 03/06/10 (Holding Register).
    - Giả định thứ tự word là Big-Endian (word cao trước) cho các giá trị 32-bit
      (total active energy...). Nếu đọc ra số bất thường, hãy đổi WORD_ORDER_BIG_ENDIAN = False.
    - SERIAL_PORT = "AUTO": chương trình sẽ tự liệt kê tất cả cổng COM đang có trên máy,
      lần lượt thử kết nối và đọc thử 1 thanh ghi (tần số) để tìm cổng nào có thiết bị
      HYFW đang phản hồi thật sự — không chỉ liệt kê cổng có tồn tại mà còn xác nhận
      có thiết bị đang giao tiếp trên đó.
"""

import sys
import time
import struct
from dataclasses import dataclass

from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException
from serial.tools import list_ports

# ----------------------------------------------------------------------------
# CẤU HÌNH KẾT NỐI - chỉnh lại theo máy của bạn
# ----------------------------------------------------------------------------
# Đặt "AUTO" để chương trình tự dò cổng COM đang có thiết bị Modbus phản hồi.
# Hoặc gõ tên cổng cụ thể như "COM3", "/dev/ttyUSB0" để dùng cố định.
SERIAL_PORT = "AUTO"
BAUDRATE = 9600
PARITY = "N"                # N / E / O  (mặc định thiết bị: 8N1 -> N)
STOPBITS = 1
BYTESIZE = 8
DEVICE_ID = 1                # địa chỉ Modbus của thiết bị (reg 0x2001, mặc định = 1)
TIMEOUT = 2                  # giây
WORD_ORDER_BIG_ENDIAN = True  # thứ tự word cho thanh ghi 32-bit


def decode_u32(high: int, low: int) -> int:
    """Ghép 2 thanh ghi 16-bit thành số unsigned 32-bit."""
    if WORD_ORDER_BIG_ENDIAN:
        raw = struct.pack(">HH", high, low)
    else:
        raw = struct.pack(">HH", low, high)
    return struct.unpack(">I", raw)[0]


def decode_i16(value: int) -> int:
    """Chuyển thanh ghi 16-bit unsigned -> signed."""
    return struct.unpack(">h", struct.pack(">H", value))[0]

REALTIME_REGISTERS = {
    "phase_A_voltage_V":     dict(address=4096, scale=100, signed=False),
    "phase_B_voltage_V":     dict(address=4097, scale=100, signed=False),
    "phase_C_voltage_V":     dict(address=4098, scale=100, signed=False),
    "phase_A_current_A":     dict(address=4105, scale=1000, signed=False),
    "phase_B_current_A":     dict(address=4106, scale=1000, signed=False),
    "phase_C_current_A":     dict(address=4107, scale=1000, signed=False),
    "total_active_power_kW": dict(address=4113, scale=1000, signed=True),
    "total_reactive_power_kvar": dict(address=4117, scale=1000, signed=True),
    "total_apparent_power_kVA": dict(address=4121, scale=1000, signed=False),
    "power_factor":           dict(address=4125, scale=1000, signed=True),
    "frequency_Hz":           dict(address=4126, scale=100, signed=False),
}

# Thanh ghi 32-bit (2 word liên tiếp), vùng 4XXX Real-Time Energy
ENERGY_REGISTERS = {
    "total_active_energy_kWh": dict(address=16384, scale=10),
    "forward_active_energy_kWh": dict(address=16386, scale=10),
    "reverse_active_energy_kWh": dict(address=16388, scale=10),
}


def list_serial_ports():
    """Liệt kê tất cả cổng COM/serial đang tồn tại trên máy."""
    ports = list(list_ports.comports())
    if not ports:
        print("Khong tim thay cong COM nao tren may.")
    else:
        print("Cac cong COM hien co:")
        for p in ports:
            print(f"  {p.device:<15} - {p.description}")
    return [p.device for p in ports]


def probe_port(port: str, device_id: int = DEVICE_ID, baudrate: int = BAUDRATE,
                parity: str = PARITY, stopbits: int = STOPBITS,
                bytesize: int = BYTESIZE, probe_timeout: float = 5.0) -> bool:
    """Thử mở 1 cổng và đọc 1 thanh ghi (frequency, 0x101E) để kiểm tra
    xem thiết bị Modbus có đang phản hồi trên cổng đó không.
    Nếu sau `probe_timeout` giây (mặc định 5s) không có phản hồi,
    tự động ngắt kết nối cổng đó và coi như không có thiết bị."""
    client = ModbusSerialClient(
        port=port, baudrate=baudrate, parity=parity,
        stopbits=stopbits, bytesize=bytesize,
        timeout=probe_timeout, retries=1,
    )
    try:
        if not client.connect():
            return False
        result = client.read_input_registers(address=4126, count=1, device_id=device_id)
        return not result.isError()
    except Exception:
        return False
    finally:
        # Luôn ngắt kết nối cổng sau khi thử, dù thành công hay hết thời gian chờ
        client.close()


def auto_detect_port(device_id: int = DEVICE_ID) -> str | None:
    """Dò qua tất cả cổng COM đang có trên máy, trả về cổng đầu tiên
    mà thiết bị HYFW phản hồi đúng. Trả về None nếu không tìm thấy."""
    candidates = list_serial_ports()
    if not candidates:
        return None

    print(f"\nDang do {len(candidates)} cong voi dia chi thiet bi = {device_id} ...")
    for port in candidates:
        print(f"  -> Thu {port} ...", end=" ", flush=True)
        if probe_port(port, device_id=device_id):
            print("CO THIET BI PHAN HOI!")
            return port
        print("khong phan hoi")
    return None


@dataclass
class HYFWMeter:
    port: str = SERIAL_PORT
    baudrate: int = BAUDRATE
    parity: str = PARITY
    stopbits: int = STOPBITS
    bytesize: int = BYTESIZE
    device_id: int = DEVICE_ID
    timeout: float = TIMEOUT

    def __post_init__(self):
        self.client = ModbusSerialClient(
            port=self.port,
            baudrate=self.baudrate,
            parity=self.parity,
            stopbits=self.stopbits,
            bytesize=self.bytesize,
            timeout=self.timeout,
        )

    def connect(self) -> bool:
        return self.client.connect()

    def close(self):
        self.client.close()

    def _read_input_registers(self, address: int, count: int):
        """Function code 04 - Read Input Registers."""
        result = self.client.read_input_registers(
            address=address, count=count, device_id=self.device_id
        )
        if result.isError():
            raise ModbusException(f"Loi doc thanh ghi @{address}: {result}")
        return result.registers

    def read_realtime_data(self) -> dict:
        """Đọc các thông số điện áp/dòng điện/công suất tức thời (vùng 1XXX)."""
        data = {}
        for name, cfg in REALTIME_REGISTERS.items():
            regs = self._read_input_registers(cfg["address"], 1)
            raw = regs[0]
            if cfg["signed"]:
                raw = decode_i16(raw)
            data[name] = raw / cfg["scale"]
        return data

    def read_energy_data(self) -> dict:
        """Đọc năng lượng (thanh ghi 32-bit, vùng 4XXX)."""
        data = {}
        for name, cfg in ENERGY_REGISTERS.items():
            regs = self._read_input_registers(cfg["address"], 2)
            raw = decode_u32(regs[0], regs[1])
            data[name] = raw / cfg["scale"]
        return data


def print_reading(realtime: dict, energy: dict):
    print("-" * 46)
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    for k, v in realtime.items():
        print(f"  {k:<28}: {v}")
    for k, v in energy.items():
        print(f"  {k:<28}: {v}")


def main():
    port = SERIAL_PORT
    if port.upper() == "AUTO":
        detected = auto_detect_port(device_id=DEVICE_ID)
        if not detected:
            print("\nKhong tim thay cong COM nao co thiet bi HYFW phan hoi.")
            print("Kiem tra: cap RS485 da cam chua, dia chi thiet bi (DEVICE_ID) "
                  "co dung khong, thiet bi co dang cap dien khong.")
            sys.exit(1)
        port = detected
        print(f"\nDa tim thay thiet bi tren cong: {port}\n")

    meter = HYFWMeter(port=port)
    print(f"Dang ket noi {meter.port} @ {meter.baudrate} baud (8{meter.parity}{meter.stopbits}), "
          f"dia chi thiet bi = {meter.device_id} ...")

    if not meter.connect():
        print(f"KHONG the mo cong {meter.port}. Kiem tra lai ten cong COM va cap RS485.")
        sys.exit(1)

    print("Ket noi thanh cong. Nhan Ctrl+C de dung.\n")
    try:
        while True:
            try:
                realtime = meter.read_realtime_data()
                energy = meter.read_energy_data()
                print_reading(realtime, energy)
            except ModbusException as exc:
                print(f"Loi Modbus: {exc}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nDa dung theo yeu cau nguoi dung.")
    finally:
        meter.close()


if __name__ == "__main__":
    main()