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
"""

import sys
import time
import struct
from dataclasses import dataclass

from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException

# ----------------------------------------------------------------------------
# CẤU HÌNH KẾT NỐI - chỉnh lại theo máy của bạn
# ----------------------------------------------------------------------------
SERIAL_PORT = "COM7"       # Windows: "COM3", "COM4"...  Linux: "/dev/ttyUSB0"
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


# ----------------------------------------------------------------------------
# BẢNG THANH GHI (trích từ file HYFW_Modbus_Register_V2_1_2, vùng "1XXX Zone 100mA"
# - đúng loại cảm biến Hall đang dùng: tỉ số 150A / 100mA)
# address: địa chỉ decimal, scale: hệ số amplify trong file, signed: có dấu hay không
# ct_ratio: hệ số nhân để quy đổi từ dòng THỨ CẤP (mA) -> dòng SƠ CẤP thực tế (A).
#           = dòng sơ cấp định mức / dòng thứ cấp định mức = 150 / 100 (mA) = 1.5 A/mA
#   !! CHỈ áp dụng ct_ratio nếu thanh ghi CT (0x2006) và CT selection (0x2007)
#      trên thiết bị CHƯA được cấu hình đúng 150A/100mA. Nếu thiết bị đã tự quy đổi
#      nội bộ thì áp dụng ct_ratio ở đây sẽ bị nhân đôi (sai gấp 1.5 lần) -> phải
#      kiểm chứng bằng ampe kẹp thực tế trước khi dùng.
# ----------------------------------------------------------------------------
CT_RATIO = 150 / 100  # = 1.5  (150A sơ cấp / 100mA thứ cấp)

REALTIME_REGISTERS = {
    # Điện áp: không liên quan CT, giữ nguyên
    "phase_A_voltage_V":     dict(address=4096, scale=100, signed=False),
    "phase_B_voltage_V":     dict(address=4097, scale=100, signed=False),
    "phase_C_voltage_V":     dict(address=4098, scale=100, signed=False),

    # Dòng điện: bảng 100mA trả về mA (thứ cấp) -> nhân CT_RATIO để ra A (sơ cấp)
    "phase_A_current_A":     dict(address=4105, scale=100, signed=False, apply_ct=True),
    "phase_B_current_A":     dict(address=4106, scale=100, signed=False, apply_ct=True),
    "phase_C_current_A":     dict(address=4107, scale=100, signed=False, apply_ct=True),

    # Công suất: bảng 100mA đơn vị W/var/VA, scale=100 (KHÁC bảng 1.25mA dùng kW, scale=1000)
    "total_active_power_W":   dict(address=4113, scale=100, signed=True, apply_ct=True),
    "total_reactive_power_var": dict(address=4117, scale=100, signed=True, apply_ct=True),
    "total_apparent_power_VA":  dict(address=4121, scale=100, signed=False, apply_ct=True),

    "power_factor":           dict(address=4125, scale=100, signed=True),
    "frequency_Hz":           dict(address=4126, scale=100, signed=False),
}

# Thanh ghi 32-bit (2 word liên tiếp), vùng 4XXX Real-Time Energy
ENERGY_REGISTERS = {
    "total_active_energy_kWh": dict(address=16384, scale=10),
    "forward_active_energy_kWh": dict(address=16386, scale=10),
    "reverse_active_energy_kWh": dict(address=16388, scale=10),
}


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
        """Đọc các thông số điện áp/dòng điện/công suất tức thời (vùng 1XXX Zone 100mA)."""
        data = {}
        for name, cfg in REALTIME_REGISTERS.items():
            regs = self._read_input_registers(cfg["address"], 1)
            raw = regs[0]
            if cfg["signed"]:
                raw = decode_i16(raw)
            value = raw / cfg["scale"]
            if cfg.get("apply_ct"):
                value *= CT_RATIO
            data[name] = value
        return data

    def read_ct_pt_config(self) -> dict:
        """Đọc cấu hình PT/CT hiện tại trên thiết bị (vùng 2XXX Basic Setting,
        holding register, function code 03) để kiểm tra trước khi tin số liệu
        ở Zone Primary Current/Voltage."""
        result = self.client.read_holding_registers(
            address=8197, count=4, device_id=self.device_id
            # 0x2005 PT, 0x2006 CT, 0x2007 CT selection, 0x2008 secondary rated voltage
        )
        if result.isError():
            raise ModbusException(f"Loi doc cau hinh CT/PT: {result}")
        pt, ct, ct_selection, sec_v_mode = result.registers
        return {
            "PT_raw": pt,                 # phải = 1 nếu đấu trực tiếp, không qua PT ngoài
            "CT_raw": ct,
            "CT_selection_raw": ct_selection,
            "secondary_voltage_mode": "220V L-N/380V L-L" if sec_v_mode == 0 else "57.7V L-N/100V L-L",
        }

    def read_primary_current(self) -> dict:
        """Đọc dòng điện sơ cấp đã được thiết bị tự tính sẵn (vùng 1XXX Primary
        Current, địa chỉ 0x1500, thanh ghi 32-bit). Chỉ tin số này nếu
        read_ct_pt_config() xác nhận CT/PT đã cấu hình đúng thực tế."""
        addr_map = {
            "phase_A_current_primary_A": 5394,  # 0x1512
            "phase_B_current_primary_A": 5396,  # 0x1514
            "phase_C_current_primary_A": 5398,  # 0x1516
        }
        data = {}
        for name, addr in addr_map.items():
            regs = self._read_input_registers(addr, 2)
            raw = decode_u32(regs[0], regs[1])
            data[name] = raw / 1000  # amplify 1000 lần theo file thanh ghi
        return data

    def read_primary_voltage(self) -> dict:
        """Đọc điện áp sơ cấp đã được thiết bị tự tính sẵn (vùng 1XXX Primary
        Voltage, thanh ghi 32-bit). Chỉ tin số này nếu read_ct_pt_config()
        xác nhận PT đã cấu hình đúng thực tế đấu dây."""
        addr_map = {
            "phase_A_voltage_primary_V": 5376,  # 0x1500
            "phase_B_voltage_primary_V": 5378,  # 0x1502
            "phase_C_voltage_primary_V": 5380,  # 0x1504
        }
        data = {}
        for name, addr in addr_map.items():
            regs = self._read_input_registers(addr, 2)
            raw = decode_u32(regs[0], regs[1])
            data[name] = raw / 100  # amplify 100 lần theo file thanh ghi
        return data

    def compare_current_sources(self):
        """In song song: dòng thứ cấp (Zone 100mA, tự nhân CT_RATIO) vs
        dòng sơ cấp (Zone Primary Current, thiết bị tự tính) để đối chiếu
        với ampe kìm thực đo trước khi quyết định dùng zone nào."""
        rt = self.read_realtime_data()
        pri = self.read_primary_current()
        cfg = self.read_ct_pt_config()
        print("Cau hinh CT/PT hien tai tren thiet bi:", cfg)
        print(f"{'Pha':<5}{'Zone 100mA (x1.5, A)':<25}{'Zone Primary (A)':<20}")
        for ph, key_rt, key_pri in [
            ("A", "phase_A_current_A", "phase_A_current_primary_A"),
            ("B", "phase_B_current_A", "phase_B_current_primary_A"),
            ("C", "phase_C_current_A", "phase_C_current_primary_A"),
        ]:
            print(f"{ph:<5}{rt[key_rt]:<25.3f}{pri[key_pri]:<20.3f}")
        print(">> Do ampe kim thuc te tren day dang gan vong, so sanh voi 2 cot tren de biet zone nao dung.")

    def compare_voltage_sources(self):
        """In song song: điện áp thứ cấp thô (Zone 100mA) vs điện áp sơ cấp
        do thiết bị tự tính (Zone Primary Voltage), kèm cấu hình PT hiện tại.
        Đối chiếu với VOM đo thực tế tại điểm đấu dây để biết PT có đúng không."""
        rt = self.read_realtime_data()
        pri = self.read_primary_voltage()
        cfg = self.read_ct_pt_config()
        print("Cau hinh PT/CT hien tai tren thiet bi:", cfg)
        print(f"{'Pha':<5}{'Zone 100mA - tho (V)':<25}{'Zone Primary (V)':<20}")
        for ph, key_rt, key_pri in [
            ("A", "phase_A_voltage_V", "phase_A_voltage_primary_V"),
            ("B", "phase_B_voltage_V", "phase_B_voltage_primary_V"),
            ("C", "phase_C_voltage_V", "phase_C_voltage_primary_V"),
        ]:
            print(f"{ph:<5}{rt[key_rt]:<25.2f}{pri[key_pri]:<20.2f}")
        print(">> Do VOM thuc te tai diem dau day, so sanh voi 2 cot tren de biet PT da dung chua.")

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
    meter = HYFWMeter()
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