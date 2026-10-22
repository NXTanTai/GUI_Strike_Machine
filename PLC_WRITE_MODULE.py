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
from LogFileHandler import MonthlyRotatingFileHandler
import snap7
from snap7.error import * # type: ignore
from snap7.type import * # type: ignore
from snap7.type import Parameter
from snap7.util import set_bool, set_real, set_dint, set_int, set_string, get_bool

from PySide6.QtCore import QObject, QTimer, Signal, Slot, QThread, Qt

HEARTBEAT_INTERVAL = 5.0   # giây — probe khi queue rỗng
HEARTBEAT_DB_SIZE  = 4     # byte — đọc tối thiểu để giữ kết nối sống
MAX_RETRY_COUNT    = 3     # số lần retry tối đa cho 1 item trước khi bỏ
MAX_ITEMS_PER_TICK = 20    # số lệnh tối đa xử lý trong 1 chu kỳ write_ms


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
    write_pulse        = Signal(str, int)           # name, hold_ms — ghi True, giữ hold_ms rồi ghi False

    write_bool_done    = Signal(str, bool, float)   # name, value, time.time() lúc ghi xong
    write_bool_failed  = Signal(str, bool)          # name, value — ghi thất bại / bị bỏ
    write_value_done   = Signal()
    write_multi_done   = Signal(str, bool)
    write_multi_failed = Signal(str, str)           # group, lý do — bị bỏ sau MAX_RETRY_COUNT
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

        # Ghi BOOL đúng 1 bit (WordLen.Bit): None = chưa kiểm tra, True = PLC hỗ trợ,
        # False = PLC không hỗ trợ -> dùng read-modify-write cả byte
        self._bit_write_supported: bool | None = None

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

        log_dir = self.folder / "PLC Log"
        os.makedirs(log_dir, exist_ok=True)

        file_handler = MonthlyRotatingFileHandler(
            base_log_dir=log_dir,
            prefix="PLC_WRITE",
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
        self.write_pulse.connect(self._enqueue_pulse,  Qt.QueuedConnection)  # type: ignore
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
                    if self._current_item[0] == "bool":
                        self.write_bool_failed.emit(self._current_item[1], bool(self._current_item[2]))
                    elif self._current_item[0] == "multi_vars":
                        self.write_multi_failed.emit(
                            self._current_item[2], f"Dropped after {MAX_RETRY_COUNT} failed retries"
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
            # if now - self._last_error_log_time >= 5:
            #     if self.logger:
            #         self.logger.error("[PLC WRITE]: Connection failed: %s", result["error"])
            #     self._last_error_log_time = now
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

        bools_this_tick: set[str] = set()
        processed = 0
        while processed < MAX_ITEMS_PER_TICK and self._running:
            with self._queue_lock:
                if not self._queue:
                    break
                nxt = self._queue[0]
                # Cùng 1 tag BOOL chỉ ghi 1 lần mỗi tick -> lệnh xung (True -> False)
                # giữ mức True ít nhất 1 chu kỳ write_ms để PLC kịp quét thấy
                if nxt[0] in ("bool", "pulse") and nxt[1] in bools_this_tick:
                    break
                item = self._queue.pop(0)

            if item[0] in ("bool", "pulse"):
                bools_this_tick.add(item[1])
            self._current_item = item
            self._dispatch(item)
            processed += 1
            if self._current_item is not None:
                break  # ghi lỗi -> đang reconnect, item sẽ được retry

        if processed == 0:
            self._heartbeat()

    def _heartbeat(self):
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
    @Slot(str, int)
    def _enqueue_pulse(self, name: str, hold_ms: int):
        with self._queue_lock:
            self._queue.append(("pulse", name, hold_ms))
        if self.logger:
            self.logger.info("[PLC WRITE]: Enqueued PULSE %s (%d ms)", name, hold_ms)

    def _write_pulse(self, name: str, hold_ms: int):
        """
        Xung BOOL: ghi True, sau đó hold_ms mới đưa lệnh False vào queue.
        \n Thời gian giữ tính từ lúc True đã ghi xuống PLC thành công (không phải lúc bấm nút)
        -> PLC chắc chắn quét thấy mức True dù queue/mạng chậm.
        """
        self._write_bool(name, True)
        QTimer.singleShot(hold_ms, lambda: self._enqueue_bool(name, False))

    def _enqueue_bool(self, name: str, value: bool):
        # KHÔNG dedup BOOL: các lệnh xung (STOP True -> False) phải được ghi đủ và đúng thứ tự,
        # dedup sẽ thay True bằng False khi True chưa kịp ghi -> PLC không thấy cạnh lên
        with self._queue_lock:
            self._queue.append(("bool", name, value))
        if self.logger:
            self.logger.info("[PLC WRITE]: Enqueued %s = %s", name, value)

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
        Tránh gửi hàng loạt giá trị trung gian 
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
            elif cmd_type == "pulse":
                self._write_pulse(item[1], item[2])
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
            # raise để _dispatch đưa item vào cơ chế retry thay vì bỏ mất lệnh
            raise ConnectionError("PLC not connected")

        tag = self._layout_dict.get(name)
        if not tag:
            self.write_bool_failed.emit(name, bool(value))
            return

        _, offset, bit = tag
        bit = bit or 0

        if self._bit_write_supported is not False and self._write_single_bit(offset, bit, bool(value)):
            mode = "BIT"
        else:
            # Fallback: read-modify-write cả byte (có thể đè bit khác nếu PLC ghi cùng lúc)
            raw    = self._client.db_read(self._db_number, offset, 1)  # type: ignore
            result = set_bool(raw, 0, bit, bool(value))
            self._client.db_write(self._db_number, offset, result)     # type: ignore
            mode = "BYTE"

        self.write_bool_done.emit(name, bool(value), time.time())
        if self.logger:
            self.logger.info("[PLC WRITE]: BOOL OK (%s) - %s = %s", mode, name, value)

    def _write_single_bit(self, offset: int, bit: int, value: bool) -> bool:
        """
        Ghi đúng 1 bit DBx.offset.bit, không đụng tới 7 bit còn lại trong byte.
        \n Lần đầu tiên: đọc byte trước & sau khi ghi để xác nhận PLC ghi đúng 1 bit
        (có implementation hiểu WordLen.Bit như ghi cả byte -> xoá các bit khác).
        Nếu sai thì khôi phục byte và chuyển hẳn sang read-modify-write.
        \n Trả về False nếu PLC không hỗ trợ (caller sẽ dùng fallback).
        """
        verify = self._bit_write_supported is None
        before = self._client.db_read(self._db_number, offset, 1) if verify else None  # type: ignore

        try:
            self._client.write_area(  # type: ignore
                Area.DB, self._db_number, offset * 8 + bit,
                bytearray([1 if value else 0]), WordLen.Bit,
            )
        except Exception as exc:
            if not self._client or not self._client.get_connected():
                raise  # mất kết nối -> để _dispatch retry
            if verify:
                self._bit_write_supported = False
                if self.logger:
                    self.logger.warning("[PLC WRITE]: PLC không hỗ trợ ghi Bit (%s) — dùng read-modify-write", exc)
                return False
            raise

        if not verify:
            return True

        expected = bytearray(before)  # type: ignore
        set_bool(expected, 0, bit, value)
        after = self._client.db_read(self._db_number, offset, 1)  # type: ignore
        ok = after[0] == expected[0]
        self._bit_write_supported = ok
        if not ok:
            # Khôi phục các bit khác bị ghi sai
            self._client.db_write(self._db_number, offset, expected)  # type: ignore
        if self.logger:
            self.logger.info(
                "[PLC WRITE]: Kiểm tra ghi Bit DB%d.DBX%d.%d: %s (before=%s expected=%s after=%s)",
                self._db_number, offset, bit, "OK" if ok else "FAIL — dùng read-modify-write",
                format(before[0], "08b"), format(expected[0], "08b"), format(after[0], "08b"),  # type: ignore
            )
        # FAIL: byte đã được khôi phục đúng giá trị mong muốn -> coi như đã ghi xong
        return True

    def _write_value(self, name: str, value: Any):
        """Ghi REAL, INT, DINT, STRING."""
        if not self._ensure_connected():
            raise ConnectionError("PLC not connected")

        tag = self._layout_dict.get(name)
        if not tag:
            if self.logger:
                self.logger.warning("[PLC WRITE]: Tag not found: %s", name)
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
        """
        Ghi nhiều item REAL / INT / DINT.
        \n python-snap7 3.x: write_multi_vars thực chất gửi từng item 1 request
        -> gộp các item nằm liền nhau trong DB thành 1 lần db_write để giảm số request.
        """
        if not self._ensure_connected():
            raise ConnectionError("PLC not connected")
        try:
            result = 0
            for start, data in self._merge_contiguous(items):
                self._client.db_write(self._db_number, start, data)  # type: ignore
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

    def _merge_contiguous(self, items: list) -> list[tuple[int, bytearray]]:
        """
        Gộp các item (dict từ get_item) có vùng byte nối tiếp nhau thành các khối liền.
        \n Chỉ gộp khi item sau bắt đầu đúng tại byte kết thúc của item trước
        (không lấp khoảng trống -> không ghi đè byte nào ngoài các item đã cho).
        """
        blocks: list[tuple[int, bytearray]] = []
        for it in sorted(items, key=lambda x: x["start"]):
            if it.get("db_number", self._db_number) != self._db_number:
                raise ValueError(f"Item DB{it.get('db_number')} khác DB{self._db_number}")
            start, data = it["start"], bytes(it["data"])
            if blocks and blocks[-1][0] + len(blocks[-1][1]) == start:
                blocks[-1][1].extend(data)
            else:
                blocks.append((start, bytearray(data)))
        return blocks

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
            raise ConnectionError("PLC not connected")
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