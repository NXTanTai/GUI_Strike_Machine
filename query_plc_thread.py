import snap7
import snap7.util as s7
from snap7.type import Areas as AreaType
import struct
import plc_data as db_data

from enum import Enum, auto
from dataclasses import dataclass
from collections import deque
from PySide6.QtCore import QThread, Signal, QObject, QTimer, Slot
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                                QVBoxLayout, QWidget, QPushButton)

class PLCState(Enum):
    DISCONNECTED = auto()
    CONNECTING   = auto()
    CONNECTED    = auto()
    RECONNECTING = auto()


class PLCRead(QObject):
    """PLC Worker - Hỗ trợ nhiều client ghi song song"""
    
    data_received = Signal(dict)           # Dữ liệu đọc về
    write_done    = Signal(str, bool, object)  # field_name, success, value
    state_changed = Signal(PLCState)
    error         = Signal(str)

    def __init__(self, ip: str, db_number: int = 1, interval_ms: int = 500):
        super().__init__()
        self.ip = ip
        self.db_number = db_number
        self.interval_ms = interval_ms
        self.db_size = 580

        self.client = snap7.client.Client()
        self._state = PLCState.DISCONNECTED
        self._running = False
        self._write_queue = deque()           # Hàng đợi an toàn cho nhiều writer

    # ==================== PROPERTY ====================
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state: PLCState):
        if self._state != new_state:
            self._state = new_state
            self.state_changed.emit(new_state)

    # ==================== START / STOP ====================
    def start(self):
        self._running = True
        self._write_queue.clear()

        self.poll_timer = QTimer()
        self.poll_timer.setInterval(self.interval_ms)
        self.poll_timer.timeout.connect(self._poll)

        self.retry_timer = QTimer()
        self.retry_timer.setSingleShot(True)
        self.retry_timer.timeout.connect(self._reconnect)

        self._connect()

    def stop(self):
        self._running = False
        if hasattr(self, 'poll_timer'): self.poll_timer.stop()
        if hasattr(self, 'retry_timer'): self.retry_timer.stop()
        self._disconnect()

    # ==================== KẾT NỐI ====================
    def _connect(self):
        self.state = PLCState.CONNECTING
        try:
            self.client.connect(self.ip, 0, 1)   # rack=0, slot=1
            self.state = PLCState.CONNECTED
            self.error.emit("Kết nối PLC thành công")
            self.poll_timer.start()
        except Exception as e:
            self.error.emit(f"Kết nối thất bại: {e}")
            self._schedule_reconnect()

    def _reconnect(self):
        if not self._running: return
        self._disconnect()
        self._connect()

    def _disconnect(self):
        try:
            if self.client.get_connected():
                self.client.disconnect()
        except:
            pass

    def _schedule_reconnect(self):
        self.state = PLCState.RECONNECTING
        if hasattr(self, 'poll_timer'):
            self.poll_timer.stop()
        self.retry_timer.start(2000)

    # ==================== VÒNG LẶP CHÍNH ====================
    def _poll(self):
        if not self._running:
            return
        try:
            self._read_data()

        except Exception as e:
            self.error.emit(f"Mất kết nối: {e}")
            self._schedule_reconnect()

    # ==================== ĐỌC DỮ LIỆU ====================
    def _read_data(self):
        raw = bytearray(self.client.db_read(self.db_number, 0, self.db_size))
        data = self._parse_all(raw)
        self.data_received.emit(data)
        
    # ====================== HÀM MỚI: ĐỌC AREA ======================
    def read_area(self, area: AreaType, db_number: int = 0, start: int = 0, size: int = 4):
        """
        Đọc khu vực bất kỳ (DB, Input, Output, Marker...)
        Ví dụ:
            read_area(AreaType.PE, 0, 0, 10)   # Đọc 10 bytes Input
            read_area(AreaType.PA, 0, 0, 8)    # Đọc 8 bytes Output
            read_area(AreaType.MK, 0, 50, 4)   # Đọc Marker từ M50
        """
        try:
            raw = bytearray(self.client.read_area(area, db_number, start, size))
            return raw
        except Exception as e:
            self.error.emit(f"read_area lỗi: {e}")
            return None

    # ====================== ĐỌC AREA + PARSE (Tiện dụng) ======================
    def read_area_bool(self, area: AreaType, db_number: int, byte_offset: int, bit_offset: int):
        """Đọc 1 bit từ Area"""
        try:
            raw = self.read_area(area, db_number, byte_offset, 1)
            if raw:
                return s7.get_bool(raw, 0, bit_offset)
            return None
        except:
            return None

    def read_area_real(self, area: AreaType, db_number: int, byte_offset: int):
        """Đọc REAL (4 bytes)"""
        try:
            raw = self.read_area(area, db_number, byte_offset, 4)
            if raw:
                return s7.get_real(raw, 0)
            return None
        except:
            return None

    def read_area_int(self, area: AreaType, db_number: int, byte_offset: int):
        """Đọc INT (2 bytes)"""
        try:
            raw = self.read_area(area, db_number, byte_offset, 2)
            if raw:
                return s7.get_int(raw, 0)
            return None
        except:
            return None
        
    def _parse_all(self, raw: bytearray) -> dict:
        data = {}
        for name, field in db_data.DB_MAP.items():
            try:
                offset = field.offset
                if field.data_type == "REAL":
                    data[name] = s7.get_real(raw, offset)
                elif field.data_type == "DINT":
                    data[name] = s7.get_dint(raw, offset)
                elif field.data_type == "INT":
                    data[name] = s7.get_int(raw, offset)
                elif field.data_type == "BOOL":
                    byte_idx, bit_idx = db_data.BOOL_BIT_INDEX.get(name, (offset, 0))
                    data[name] = s7.get_bool(raw, byte_idx, bit_idx)
                elif field.data_type == "STRING":
                    data[name] = s7.get_string(raw, offset)
            except:
                data[name] = None
        return data

    # Context manager
    def __enter__(self): return self
    def __exit__(self, *args): self.stop()