import snap7
import snap7.util as s7
import struct
from collections import deque
from PySide6.QtCore import QObject, QTimer, Signal, Slot
from enum import Enum, auto
import plc_data as db_data

class PLCState(Enum):
    DISCONNECTED = auto()
    CONNECTING   = auto()
    CONNECTED    = auto()
    RECONNECTING = auto()


class PLCWrite(QObject):
    """PLC Worker - Chỉ ghi khi UI gửi lệnh"""

    data_received = Signal(dict)
    write_done    = Signal(str, bool, object)   # field_name, success, value
    state_changed = Signal(PLCState)
    error         = Signal(str)

    def __init__(self, ip: str = "192.168.0.1", db_number: int = 1, interval_ms: int = 500):
        super().__init__()
        self.ip = ip
        self.db_number = db_number
        self.interval_ms = interval_ms
        self.db_size = 580

        self.client = snap7.client.Client()
        self._state = PLCState.DISCONNECTED
        self._running = False
        
        # Hàng chờ ghi - chỉ ghi khi có lệnh từ UI
        self._write_queue = deque(maxlen=50)

    @property
    def state(self): return self._state

    @state.setter
    def state(self, new_state):
        if self._state != new_state:
            self._state = new_state
            self.state_changed.emit(new_state)

    # ====================== START / STOP ======================
    def start(self):
        self._running = True
        self._write_queue.clear()

        self.poll_timer = QTimer()
        self.poll_timer.setInterval(self.interval_ms)
        self.poll_timer.timeout.connect(self._poll)

        self._connect()

    def stop(self):
        self._running = False
        if hasattr(self, 'poll_timer'):
            self.poll_timer.stop()
        self._disconnect()

    # ====================== KẾT NỐI ======================
    def _connect(self):
        self.state = PLCState.CONNECTING
        try:
            self.client.connect(self.ip, 0, 1)
            self.state = PLCState.CONNECTED
            self.error.emit("✅ Kết nối PLC thành công")
            self.poll_timer.start()
        except Exception as e:
            self.error.emit(f"❌ Kết nối thất bại: {e}")
            self._schedule_reconnect()

    def _schedule_reconnect(self):
        self.state = PLCState.RECONNECTING
        if hasattr(self, 'poll_timer'):
            self.poll_timer.stop()
        QTimer.singleShot(2500, self._connect)

    def _disconnect(self):
        try:
            if self.client.get_connected():
                self.client.disconnect()
        except:
            pass

    # ====================== VÒNG LẶP CHÍNH ======================
    def _poll(self):
        """Chỉ chạy đọc + ghi theo yêu cầu từ UI"""
        if not self._running:
            return

        try:
            # 1. Xử lý ghi trước (nếu có lệnh từ UI)
            while self._write_queue:
                cmd = self._write_queue.popleft()
                self._execute_write(cmd)

        except Exception as e:
            self.error.emit(f"Mất kết nối: {e}")
            self._schedule_reconnect()

    @Slot(str, object)
    def write(self, field_name: str, value):
        """UI gọi hàm này để ghi dữ liệu"""
        if field_name not in db_data.WRITABLE_FIELDS:
            self.error.emit(f"Field {field_name} không được phép ghi")
            self.write_done.emit(field_name, False, value)
            return

        # Đẩy lệnh vào queue
        self._write_queue.append({"name": field_name, "value": value})

    def _execute_write(self, cmd: dict):
        try:
            self._write_single(cmd["name"], cmd["value"])
            self.write_done.emit(cmd["name"], True, cmd["value"])
        except Exception as e:
            self.error.emit(f"Ghi {cmd['name']} thất bại: {e}")
            self.write_done.emit(cmd["name"], False, cmd["value"])

    def _write_single(self, field_name: str, value):
        field = db_data.DB_MAP[field_name]

        if field.data_type == "BOOL":
            byte_idx, bit_idx = db_data.BOOL_BIT_INDEX[field_name]
            raw = bytearray(self.client.db_read(self.db_number, byte_idx, 1))
            s7.set_bool(raw, 0, bit_idx, bool(value))
            self.client.db_write(self.db_number, byte_idx, raw)

        elif field.data_type == "REAL":
            packed = struct.pack(">f", float(value))
            self.client.db_write(self.db_number, field.offset, bytearray(packed))

        elif field.data_type == "DINT":
            packed = struct.pack(">i", int(value))
            self.client.db_write(self.db_number, field.offset, bytearray(packed))

        elif field.data_type == "INT":
            packed = struct.pack(">h", int(value))
            self.client.db_write(self.db_number, field.offset, bytearray(packed))

    def __enter__(self): return self
    def __exit__(self, *args): self.stop()