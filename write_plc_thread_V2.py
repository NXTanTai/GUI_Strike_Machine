import struct
import logging
from typing import Any, Optional
from queue import Queue

import snap7
from snap7.error import *
from snap7.type import Area
from snap7.util import set_bool, set_real, set_dint, set_int, set_string

from PySide6.QtCore import QObject, QTimer, Signal, Slot, QThread, Qt

logger = logging.getLogger(__name__)


# ── Helpers for Write ───────────────────────────────────────────────────────
def _set_bool(data: bytearray, byte_idx: int, bit_idx: int, value: bool) -> None:
    if value:
        data[byte_idx] |= (1 << (7 - bit_idx))
    else:
        data[byte_idx] &= ~(1 << (7 - bit_idx))


def _set_real(data: bytearray, offset: int, value: float) -> None:
    struct.pack_into(">f", data, offset, value)


def _set_dint(data: bytearray, offset: int, value: int) -> None:
    struct.pack_into(">i", data, offset, value)


def _set_int(data: bytearray, offset: int, value: int) -> None:
    struct.pack_into(">h", data, offset, value)


def _set_string(data: bytearray, offset: int, value: str) -> None:
    max_len = data[offset]                      # Byte đầu tiên là max length
    encoded = value.encode("utf-8", errors="replace")
    if len(encoded) > max_len:
        encoded = encoded[:max_len]
    data[offset + 1] = len(encoded)
    data[offset + 2: offset + 2 + len(encoded)] = encoded


# ── PLCWrite ────────────────────────────────────────────────────────────────

class PLCWrite(QObject):
    # Incoming signals (gọi từ main thread)
    write_bool   = Signal(str, bool)      # (tag_name, value)
    write_value   = Signal(str, object)      # (tag_name, value)
    write_multi = Signal(dict)             # {tag_name: value, ...}
    write_full_db  = Signal(dict)             # Ghi toàn bộ DB một lần

    # Outgoing signals
    write_done    = Signal(str)               # tag_name hoặc "full_db"
    error         = Signal(str)
    connected     = Signal(bool)
    disconnected  = Signal()
    finished      = Signal()

    _request_stop = Signal()

    def __init__(
        self,
        ip:        str = "192.168.1.1",
        rack:      int = 0,
        slot:      int = 1,
        db_number: int = 1,
        db_layout: Optional[list[tuple[str, str, int, Any]]] = None,
        db_size:   int = 584,
        write_gap_ms: int = 300,          # Khoảng cách giữa các lần ghi
        retry_ms:  int = 3000,
        parent:    Optional[QObject] = None,
    ):
        super().__init__(parent)

        self._ip          = ip
        self._rack        = rack
        self._slot        = slot
        self._db_number   = db_number
        self._db_layout   = db_layout
        self._db_size     = db_size
        self._write_gap_ms = write_gap_ms
        self._retry_ms    = retry_ms
        print("DB Layout:", db_layout)
        # Layout dict để tra cứu nhanh
        self._layout_dict: dict[str, tuple[str, int, Any]] = self._build_layout_dict()

        self._client: snap7.client.Client | None = None
        self._queue: Queue = Queue()
        self._timer: QTimer | None = None
        self._retry_timer: QTimer | None = None
        self._running = False

    def _build_layout_dict(self) -> dict:
        """Xử lý trường hợp tag name trùng nhau"""
        layout = {}
        for item in self._db_layout:
            if len(item) >= 4:
                name, dtype, offset, bit = item[:4]
                # Nếu tag trùng tên, ưu tiên dùng tag Actual (_Act) nếu có
                if name in layout and "_Act" not in name and "Number_Test_Times" not in name:
                    continue  # Giữ tag Actual
                layout[name] = (dtype, offset, bit)
        return layout

    # ── Public API ──────────────────────────────────────────────────────────
    @Slot()
    def run(self):
        self._running = True

        self._request_stop.connect(self._do_stop, Qt.QueuedConnection) #type: ignore

        # Timer chính để ghi dữ liệu
        self._timer = QTimer(self)
        self._timer.setInterval(self._write_gap_ms)
        self._timer.timeout.connect(self._drain_queue)

        # Retry timer
        self._retry_timer = QTimer(self)
        self._retry_timer.setInterval(self._retry_ms)
        self._retry_timer.timeout.connect(self._try_connect)

        # Kết nối signals
        self.write_bool.connect(self._enqueue_bool, Qt.QueuedConnection) #type: ignore
        self.write_value.connect(self._enqueue_value, Qt.QueuedConnection) #type: ignore
        self.write_multi.connect(self._enqueue_multi, Qt.QueuedConnection) #type: ignore
        self.write_full_db.connect(self._enqueue_full_db, Qt.QueuedConnection) #type: ignore

        self._try_connect()

    @Slot()
    def stop(self):
        self._running = False
        self._request_stop.emit()

    # ── Stop Handler ────────────────────────────────────────────────────────
    @Slot()
    def _do_stop(self):
        if self._timer:
            self._timer.stop()
            self._timer.deleteLater()
        if self._retry_timer:
            self._retry_timer.stop()
            self._retry_timer.deleteLater()

        self._disconnect_plc()
        self.finished.emit()
        QThread.currentThread().quit()

    def get_item(self, tag_name: str, value: Any) -> dict:
        tag = self._layout_dict.get(tag_name)
        if not tag:
            raise ValueError(f"Tag not found: {tag_name}")

        dtype, offset, bit = tag

        item = {
            "area": Area.DB,
            "db_number": self._db_number,
            "start": offset,
        }

        if dtype == "BOOL":
            mask = 1 << (7 - (bit or 0))
            item["data"] = bytearray([mask if bool(value) else 0])
        elif dtype == "REAL":
            item["data"] = struct.pack(">f", float(value))
        elif dtype == "INT":
            item["data"] = struct.pack(">h", int(value))
        elif dtype == "DINT":
            item["data"] = struct.pack(">i", int(value))
        else:
            raise ValueError(f"Unsupported dtype {dtype} for tag {tag_name}")

        return item
    # ── Enqueue ─────────────────────────────────────────────────────────────
    @Slot(str, bool)
    def _enqueue_bool(self, name: str, value: bool):
        self._queue.put(("bool", name, value))
        print(f"BOOL Enqueued → {name} = {value}")

    @Slot(str, object)
    def _enqueue_value(self, name: str, value: object):
        """Enqueue riêng cho REAL, INT, DINT, STRING"""
        self._queue.put(("value", name, value))
        print(f"Value Enqueued → {name} = {value}")

    @Slot(list)
    def _enqueue_multi(self, items: list):
        self._queue.put(("multi_vars", items))
        print(f"Cmd Area recv: \n{items}")

    @Slot(dict)
    def _enqueue_full_db(self, data: dict):
        self._queue.put(("full_db", data))

    # ── Drain Queue ─────────────────────────────────────────────────────────
    @Slot()
    def _drain_queue(self):
        if not self._running or self._queue.empty():
            return

        try:
            item = self._queue.get_nowait()
            cmd_type = item[0]

            if cmd_type == "bool":
                self._write_bool(item[1], item[2])

            if cmd_type == "value":
                self._write_value(item[1], item[2])

            elif cmd_type == "multi_vars":
                self._write_multi_vars(item[1])

            elif cmd_type == "full_db":
                self._write_full_db(item[1])

        except Exception as e:
            logger.debug("Drain error: %s", e)
    # ── Connection ──────────────────────────────────────────────────────────
    @Slot()
    def _try_connect(self):
        if not self._running:
            return
        if self._client and self._client.get_connected():
            return

        self._connect_plc()

        if self._client and self._client.get_connected():
            if self._retry_timer and self._retry_timer.isActive():
                self._retry_timer.stop()
            if not self._timer.isActive():
                self._timer.start()
        else:
            if not self._retry_timer.isActive():
                self._retry_timer.start()

    def _connect_plc(self):
        try:
            self._client = snap7.client.Client()
            self._client.connect(self._ip, self._rack, self._slot)
            print("Connected to PLC, started writing queue")
            self.connected.emit(True)
        except Exception as exc:
            msg = f"Connection failed: {exc}"
            logger.error(msg)
            self.error.emit(msg)
            self.connected.emit(False)
            self._client = None

    def _disconnect_plc(self):
        if self._client:
            try:
                self._client.disconnect()
            except:
                pass
            self._client = None
        self.connected.emit(False)

    # ── Write Methods ───────────────────────────────────────────────────────
    def _write_bool(self, name: str, value: bool):
        """Ghi BOOL riêng biệt"""
        if not self._ensure_connected():
            return

        tag = self._layout_dict.get(name)
        if not tag:
            return

        _, offset, bit = tag

        try:
            raw = self._client.db_read(self._db_number, offset, 1)
            result = set_bool(raw, 0, bit or 0, bool(value))

            self._client.db_write(self._db_number, offset, result)
            print(f"[BOOL] {name} = {value} | Offset: {offset}.{(bit or 0)} | DB{self._db_number}")
            self.write_done.emit(name)
            logger.debug(f"BOOL OK → {name} = {value}")
        except Exception as exc:
            self._handle_write_error(f"Write BOOL [{name}]", exc)


    def _write_value(self, name: str, value: Any):
        """Ghi REAL, INT, DINT, STRING"""
        if not self._ensure_connected():
            return

        tag = self._layout_dict.get(name)
        if not tag:
            self.error.emit(f"Tag not found: {name}")
            return

        dtype, offset, bit = tag

        try:
            size = self._get_dtype_size(dtype)
            raw = bytearray(self._client.db_read(self._db_number, offset, size))

            self._pack(raw, dtype, bit, value, offset=0)
            self._client.db_write(self._db_number, offset, raw)

            print(f"[Value] {name} = {value} | Offset: {offset} | DB{self._db_number}")
            self.write_done.emit(name)
            
        except Exception as exc:
            self._handle_write_error(f"Write value [{name}]", exc)

    def _write_multi_vars(self, items: list):
        if not self._ensure_connected():
            return
        try:
            result = self._client.write_multi_vars(items)
            if result == 0:
                self.write_done.emit("multi_vars")
                logger.info(f"write_multi_vars OK: {len(items)} items: {items}")
            else:
                self.error.emit(f"write_multi_vars returned: {result}")
        except Exception as exc:
            self._handle_write_error("write_multi_vars", exc)

    def _write_full_db(self, data: dict):
        if not self._ensure_connected():
            return
        try:
            raw = bytearray(self._client.db_read(self._db_number, 0, self._db_size))

            for name, value in data.items():
                tag = self._layout_dict.get(name)
                if not tag:
                    continue
                dtype, offset, bit = tag
                self._pack(raw, dtype, bit, value, offset=offset)

            self._client.db_write(self._db_number, 0, raw)
            self.write_done.emit("full_db")
            logger.info("Full DB write successful (%d tags)", len(data))

        except Exception as exc:
            self._handle_write_error("Full DB write", exc)

    def _ensure_connected(self) -> bool:
        if not self._client or not self._client.get_connected():
            return False
        return True

    def _handle_write_error(self, context: str, exc: Exception):
        msg = f"{context} failed: {exc}"
        logger.warning(msg)
        self.error.emit(msg)
        self._reconnect()

    @Slot()
    def _reconnect(self):
        if not self._running:
            return
        if self._timer and self._timer.isActive():
            self._timer.stop()
        self._disconnect_plc()
        if self._retry_timer and not self._retry_timer.isActive():
            self._retry_timer.start()

    # ── Helper ──────────────────────────────────────────────────────────────
    def _get_dtype_size(self, dtype: str) -> int:
        return {"BOOL": 1, "INT": 2, "DINT": 4, "REAL": 4, "STRING": 256}.get(dtype, 1)

    def _pack(self, data: bytearray, dtype: str, bit: Any, value: Any, offset: int = 0):
        if dtype == "BOOL":
            _set_bool(data, offset, bit or 0, bool(value))
        elif dtype == "REAL":
            _set_real(data, offset, float(value))
        elif dtype == "DINT":
            _set_dint(data, offset, int(value))
        elif dtype == "INT":
            _set_int(data, offset, int(value))
        elif dtype == "STRING":
            _set_string(data, offset, str(value))