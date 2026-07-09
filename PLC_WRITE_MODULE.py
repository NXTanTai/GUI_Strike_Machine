import os
import sys
import struct
import time
import socket
import logging
import threading
import logging
import logging.handlers
from datetime import datetime
from typing import Any, Optional
import snap7
from snap7.error import * # type: ignore
from snap7.type import * # type: ignore
from snap7.type import Parameter
from snap7.util import set_bool, set_real, set_dint, set_int, set_string

from PySide6.QtCore import QObject, QTimer, Signal, Slot, QThread, Qt

HEARTBEAT_INTERVAL = 5.0   # giây — probe khi queue rỗng
HEARTBEAT_DB_SIZE  = 4     # byte — đọc tối thiểu để giữ kết nối sống
MAX_RETRY_COUNT    = 3     # số lần retry tối đa cho 1 item trước khi bỏ


class PLCWrite(QObject):
    """
    Object dùng để ghi dữ liệu xuống PLC
    \n
    Có thể tạo nhiều Object để xử lí nhiều vùng dữ liệu hoặc từ nhiều PLC
    \n
    Nếu chỉ định ghi 1 vùng riêng biệt thì lên cấu hình db_layout riêng
    """
    write_bool         = Signal(str, bool)
    write_value        = Signal(str, object)
    write_multi        = Signal(object, str)
    write_full_db      = Signal(object)

    write_bool_done    = Signal()
    write_value_done   = Signal()
    write_multi_done   = Signal(str, bool)
    write_full_db_done = Signal()

    error              = Signal(str)
    connected          = Signal(bool)
    disconnected       = Signal()
    finished           = Signal()

    _stop_write        = Signal()

    def __init__(
        self,
        ip:        str                                         = "192.168.1.1",
        rack:      int                                         = 0,
        slot:      int                                         = 1,
        db_number: int                                         = 1,
        db_layout: Optional[list[tuple[str, str, int, Any]]]  = None,
        db_size:   int                                         = 592,
        write_ms:  int                                         = 300,
        retry_ms:  int                                         = 3000,
        logger_parent                                          = None,
        parent:    Optional[QObject]                           = None,
    ):
        super().__init__(parent)

        self._ip        = ip
        self._rack      = rack
        self._slot      = slot
        self._db_number = db_number
        self._db_layout = db_layout
        self._db_size   = db_size
        self._write_ms  = write_ms
        self._retry_ms  = retry_ms
        self.logger     = None
        self.folder     = logger_parent

        self._layout_dict: dict[str, tuple[str, int, Any]] = self._build_layout_dict()
        self._client: snap7.client.Client | None = None

        self._queue:      list[tuple] = []
        self._queue_lock              = threading.Lock()

        self._current_item:         tuple | None = None
        self._current_item_retries: int          = 0

        self._last_heartbeat:      float = 0.0
        self._last_error_log_time: float = 0.0

        self._poll_timer:  QTimer | None = None
        self._retry_timer: QTimer | None = None

        self._running = False

    def _init_logger(self):
        if not self.folder:
            self.logger = None
            return

        self.logger = logging.getLogger(__name__)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        # Tạo thư mục log nếu chưa có
        log_dir = self.folder / "PLC Log"
        os.makedirs(log_dir, exist_ok=True)
        log_date = datetime.now().strftime("%d_%m_%Y")
        log_filename = os.path.join(log_dir, f'PLC_WRITE_{log_date}.log')

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

    def _build_layout_dict(self) -> dict:
        """
        Xử lý trường hợp tag name trùng nhau.
        Nếu tag trùng tên, ưu tiên dùng tag Actual (_Act) nếu có.
        """
        layout = {}
        for item in self._db_layout:  # type: ignore
            if len(item) >= 4:
                name, dtype, offset, bit = item[:4]
                if name in layout and "_Act" not in name and "Number_Test_Times" not in name:
                    continue
                layout[name] = (dtype, offset, bit)
        return layout

    @Slot()
    def run(self):
        self._running = True
        self._init_logger()
        if self.logger:
            self.logger.info("[PLC WRITE]: PLC Write init")

        self._poll_timer = QTimer(self)
        self._poll_timer.setInterval(self._write_ms)
        self._poll_timer.timeout.connect(self._drain_queue)

        self._retry_timer = QTimer(self)
        self._retry_timer.setInterval(self._retry_ms)
        self._retry_timer.timeout.connect(self._try_connect)

        self.write_bool.connect(self._enqueue_bool,    Qt.QueuedConnection)  # type: ignore
        self.write_value.connect(self._enqueue_value,  Qt.QueuedConnection)  # type: ignore
        self.write_multi.connect(self._enqueue_multi,  Qt.QueuedConnection)  # type: ignore
        self.write_full_db.connect(self._enqueue_full_db, Qt.QueuedConnection)  # type: ignore

        self._stop_write.connect(self._do_stop, Qt.QueuedConnection)  # type: ignore

        self._try_connect()

    @Slot()
    def stop(self):
        self._running = False
        self._stop_write.emit()

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
            if self._poll_timer and not self._poll_timer.isActive():
                self._poll_timer.start()

            if self._current_item is not None:
                if self._current_item_retries < MAX_RETRY_COUNT:
                    if self.logger:
                        self.logger.info(
                            "[PLC WRITE]: Reconnected — retrying item (attempt %d/%d)",
                            self._current_item_retries + 1, MAX_RETRY_COUNT,
                        )
                    with self._queue_lock:
                        self._queue.insert(0, self._current_item)
                else:
                    if self.logger:
                        self.logger.warning(
                            "[PLC WRITE]: Dropped item after %d failed retries: %s",
                            MAX_RETRY_COUNT, self._current_item,
                        )
                    self._current_item         = None
                    self._current_item_retries = 0

            if self.logger:
                self.logger.info("[PLC WRITE]: Connected to PLC, started writing")
        else:
            if self._retry_timer and not self._retry_timer.isActive():
                self._retry_timer.start()

    def _connect_plc(self):
        if not self._running:
            return

        result = {"client": None, "error": None}
        done   = threading.Event()

        def _do_connect():
            try:
                c = snap7.client.Client()

                c.set_param(Parameter.PDURequest,    960)
                c.set_param(Parameter.SendTimeout,     3)  # giây
                c.set_param(Parameter.RecvTimeout,     2)  # ← 2s (phát hiện dead conn nhanh)
                c.set_param(Parameter.PingTimeout,     2)
                c.set_param(Parameter.KeepAliveTime,  10)  # ← 10s S7 app-level ping

                c.connect(self._ip, self._rack, self._slot)
                result["client"] = c  # type: ignore
            except Exception as exc:
                result["error"] = exc  # type: ignore
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
                except Exception:
                    pass
            return

        if result["client"]:
            self._client = result["client"]
            self.connected.emit(True)
        else:
            now = time.time()
            if now - self._last_error_log_time >= 5:
                if self.logger:
                    self.logger.error("[PLC WRITE]: Connection failed: %s", result["error"])
                self._last_error_log_time = now
            self.error.emit(str(result["error"]))
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
    def _drain_queue(self):
        if not self._running:
            return

        with self._queue_lock:
            item = self._queue.pop(0) if self._queue else None

        if item is not None:
            self._current_item = item
            self._dispatch(item)
        else:
            self._heartbeat()

    def _heartbeat(self):
        """
        Gửi db_read nhỏ để giữ kết nối sống khi queue rỗng.
        Nếu PLC không phản hồi → reconnect ngay.
        """
        now = time.time()
        if now - self._last_heartbeat < HEARTBEAT_INTERVAL:
            return
        if not self._client or not self._client.get_connected():
            self._reconnect()
            return
        try:
            self._client.db_read(self._db_number, 2, HEARTBEAT_DB_SIZE)
            self._last_heartbeat = now
        except Exception as exc:
            if self.logger:
                self.logger.warning("[PLC WRITE]: Heartbeat failed: %s — reconnecting", exc)
            self._reconnect()

    @Slot(str, bool)
    def _enqueue_bool(self, name: str, value: bool):
        self._enqueue_dedup(("bool", name, value), key=f"bool:{name}")

    @Slot(str, object)
    def _enqueue_value(self, name: str, value: object):
        self._enqueue_dedup(("value", name, value), key=f"value:{name}")

    @Slot(object, str)
    def _enqueue_multi(self, items: object, group: str = ""):
        with self._queue_lock:
            self._queue.append(("multi_vars", items, group))
        if self.logger:
            self.logger.info(
                "[PLC WRITE]: MULTI enqueued: %d items | group=%s", len(items), group
            )

    @Slot(object)
    def _enqueue_full_db(self, data: object):
        with self._queue_lock:
            self._queue.append(("full_db", data))
        if self.logger:
            self.logger.info("[PLC WRITE]: Full DB enqueued: %d tags", len(data))

    def _enqueue_dedup(self, item: tuple, key: str):
        """
        Nếu trong queue đã có item cùng key (cùng loại + cùng tag),
        thay bằng giá trị mới nhất thay vì thêm vào cuối.
        Tránh gửi hàng loạt giá trị trung gian khi user thay đổi nhanh.
        """
        with self._queue_lock:
            for i, existing in enumerate(self._queue):
                existing_key = (
                    f"{existing[0]}:{existing[1]}" if len(existing) > 1 else ""
                )
                if existing_key == key:
                    self._queue[i] = item
                    if self.logger:
                        self.logger.debug("[PLC WRITE]: Dedup — replaced %s in queue", key)
                    return
            self._queue.append(item)
        if self.logger:
            self.logger.info(
                "[PLC WRITE]: Enqueued %s = %s",
                item[1], item[2] if len(item) > 2 else "",
            )

    def _dispatch(self, item: tuple):
        cmd_type = item[0]
        try:
            if cmd_type == "bool":
                self._write_bool(item[1], item[2])
            elif cmd_type == "value":
                self._write_value(item[1], item[2])
            elif cmd_type == "multi_vars":
                self._write_multi_vars(item[1], item[2])
            elif cmd_type == "full_db":
                self._write_full_db(item[1])

            self._current_item         = None
            self._current_item_retries = 0

        except Exception as e:
            if self.logger:
                self.logger.error("[PLC WRITE]: Dispatch error: %s", e)
            self._current_item_retries += 1
            self._handle_write_error(f"dispatch [{cmd_type}]", e)

    def _write_bool(self, name: str, value: bool):
        """Ghi BOOL riêng biệt (read-modify-write để giữ các bit khác)."""
        if not self._ensure_connected():
            return

        tag = self._layout_dict.get(name)
        if not tag:
            return

        _, offset, bit = tag
        try:
            raw    = self._client.db_read(self._db_number, offset, 1)  # type: ignore
            result = set_bool(raw, 0, bit or 0, bool(value))
            self._client.db_write(self._db_number, offset, result)     # type: ignore
            if self.logger:
                self.logger.info("[PLC WRITE]: BOOL OK - %s = %s", name, value)
        except Exception as exc:
            raise exc

    def _write_value(self, name: str, value: Any):
        """Ghi REAL, INT, DINT, STRING."""
        if not self._ensure_connected():
            return

        tag = self._layout_dict.get(name)
        if not tag:
            return

        dtype, offset, bit = tag
        try:
            if dtype == "BOOL":
                size = 1
                raw  = bytearray(self._client.db_read(self._db_number, offset, size))  # type: ignore
                self._pack(raw, dtype, bit, value, offset=0)
            else:
                size = self._get_dtype_size(dtype)
                raw  = bytearray(size)
                self._pack(raw, dtype, bit, value, offset=0)

            self._client.db_write(self._db_number, offset, raw)  # type: ignore
            if self.logger:
                self.logger.info(
                    "[PLC WRITE]: Value OK → %s = %s | Offset: %d | DB%d",
                    name, value, offset, self._db_number,
                )
        except Exception as exc:
            raise exc

    def _write_multi_vars(self, items: list, group: str = ""):
        """Ghi nhiều item REAL / INT / DINT trong 1 request."""
        if not self._ensure_connected():
            return
        try:
            result = self._client.write_multi_vars(items)  # type: ignore
            if result == 0:
                self.write_multi_done.emit(group, True)
                if self.logger:
                    self.logger.info(
                        "[PLC WRITE]: write_multi_vars OK: %d tags | group=%s",
                        len(items), group,
                    )
            else:
                err = f"write_multi_vars returned: {result}"
                self.error.emit(err)
                raise RuntimeError(err)
        except Exception as exc:
            raise exc

    def get_item(self, tag_name: str, value: Any) -> dict:
        tag = self._layout_dict.get(tag_name)
        if not tag:
            raise ValueError(f"Tag not found: {tag_name}")

        dtype, offset, bit = tag

        item: dict[str, Any] = {
            "area":      Area.DB,
            "db_number": self._db_number,
            "start":     offset,
        }

        if dtype == "BOOL":
            mask        = 1 << (7 - (bit or 0))
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

    def _write_full_db(self, data: dict):
        """Ghi toàn bộ DB trong 1 lần (read-modify-write)."""
        if not self._ensure_connected():
            return
        try:
            raw = bytearray(
                self._client.db_read(self._db_number, 0, self._db_size)  # type: ignore
            )
            for name, value in data.items():
                tag = self._layout_dict.get(name)
                if not tag:
                    continue
                dtype, offset, bit = tag
                self._pack(raw, dtype, bit, value, offset=offset)
            self._client.db_write(self._db_number, 0, raw)  # type: ignore
            if self.logger:
                self.logger.info("[PLC WRITE]: Full DB OK — %d tags", len(data))
        except Exception as exc:
            raise exc

    def _ensure_connected(self) -> bool:
        if not self._client or not self._client.get_connected():
            self._reconnect()
            return False
        return True

    def _handle_write_error(self, context: str, exc: Exception):
        msg = f"[PLC WRITE]: {context} failed: {exc}"
        if self.logger:
            self.logger.error(msg)
        self.error.emit(msg)
        self._reconnect()

    @Slot()
    def _reconnect(self):
        if not self._running:
            return
        if self._poll_timer and self._poll_timer.isActive():
            self._poll_timer.stop()
        self._disconnect_plc()
        if self._retry_timer and not self._retry_timer.isActive():
            self._retry_timer.start()

    def _get_dtype_size(self, dtype: str) -> int:
        return {"BOOL": 1, "INT": 2, "DINT": 4, "REAL": 4, "STRING": 256}.get(dtype, 1)

    def _pack(self, data: bytearray, dtype: str, bit: Any, value: Any, offset: int = 0):
        if dtype == "BOOL":
            set_bool(data, offset, bit or 0, bool(value))
        elif dtype == "REAL":
            set_real(data, offset, float(value))
        elif dtype == "DINT":
            set_dint(data, offset, int(value))
        elif dtype == "INT":
            set_int(data, offset, int(value))
        elif dtype == "STRING":
            set_string(data, offset, str(value))