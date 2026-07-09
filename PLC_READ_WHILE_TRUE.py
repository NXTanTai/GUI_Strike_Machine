import sys
import os
import time
import bisect
import threading
import logging
import logging.handlers
from datetime import datetime
from ctypes import c_uint8, cast, POINTER
import snap7
from typing import Any, Optional
from snap7.error import *  # type: ignore
from snap7.type import *   # type: ignore
from snap7.type import Parameter, Area, WordLen, S7DataItem
from snap7.util import get_bool, get_real, get_dint, get_int, get_string
from PySide6.QtCore import QObject, Signal, Slot

SLOW_THRESHOLD_MS = 150


class PLCReader(QObject):
    """
    Object dùng để lấy TOÀN BỘ dữ liệu từ PLC qua 1 connection duy nhất,
    dùng read_multi_vars() (multi-variable read optimizer) để gộp nhiều
    vùng đọc rời rạc thành tối thiểu round-trip.

    Bản này KHÔNG dùng QTimer nữa, thay bằng vòng lặp `while` chạy trong
    run() (dự kiến run() được gọi trong 1 QThread riêng qua moveToThread).
    Việc dừng vòng lặp dựa trên cờ self._running, được kiểm tra liên tục
    giữa các lần sleep ngắn để phản hồi stop() nhanh, không bị "kẹt" lâu
    trong 1 lần sleep dài.
    """
    init_data    = Signal()
    data_ready   = Signal(dict)
    error        = Signal(str)
    connected    = Signal(bool)
    disconnected = Signal()
    finished     = Signal()
    elapsed_time = Signal(float)

    def __init__(
        self,
        ip:         str                                       = "172.16.100.100",
        rack:       int                                       = 0,
        slot:       int                                       = 1,
        db_number:  int                                       = 1,
        db_layout:  Optional[list[tuple[str, str, int, Any]]] = None,
        regions:    Optional[list[tuple[str, int, int]]]      = None,
        # VD: [("INPUT", 0, 198), ("ACTUAL", 198, 138), ("STRING", 336, 256)]
        poll_ms:    int                                        = 250,
        retry_ms:   int                                        = 3000,
        use_optimizer:       bool                              = True,
        multi_read_max_gap:  int                               = 5,
        max_parallel:        Optional[int]                     = None,
        logger_parent                                          = None,
        parent:     Optional[QObject]                          = None,
    ):
        super().__init__(parent)
        self._ip        = ip
        self._rack      = rack
        self._slot      = slot
        self._db_number = db_number

        self._db_layout: Optional[list[tuple[str, str, int, Any]]] = (
            sorted(db_layout, key=lambda t: t[2]) if db_layout else None
        )
        self._layout_offsets: list[int] = (
            [t[2] for t in self._db_layout] if self._db_layout else []
        )

        self._regions   = regions or []
        self._poll_ms   = poll_ms
        self._retry_ms  = retry_ms
        self.logger     = None
        self.folder     = logger_parent

        self._use_optimizer      = use_optimizer
        self._multi_read_max_gap = multi_read_max_gap
        self._max_parallel       = max_parallel

        self._client: snap7.client.Client | None = None
        self._running   = False

        self._last_error_log_time: float = 0.0

        self._items:   list[S7DataItem] = []
        self._buffers: list             = []

        # bước sleep nhỏ (ms) giữa các lần kiểm tra self._running, giúp
        # stop() có hiệu lực gần như ngay lập tức thay vì phải chờ hết
        # 1 chu kỳ poll_ms/retry_ms dài
        self._sleep_step_ms = 50

    def _init_logger(self):
        if not self.folder:
            self.logger = None
            return

        self.logger = logging.getLogger(__name__)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        log_dir = self.folder / "PLC Log"
        os.makedirs(log_dir, exist_ok=True)
        log_date = datetime.now().strftime("%d_%m_%Y")
        log_filename = os.path.join(log_dir, f'PLC_READ_{log_date}.log')

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
        self.logger.propagate = False

    def _sleep_interruptible(self, total_ms: int):
        """Ngủ total_ms mili-giây nhưng chia nhỏ thành từng bước, kiểm tra
        self._running giữa mỗi bước để thoát sớm khi stop() được gọi."""
        remaining = max(total_ms, 0) / 1000.0
        step = self._sleep_step_ms / 1000.0
        while remaining > 0 and self._running:
            time.sleep(min(step, remaining))
            remaining -= step

    @Slot()
    def run(self):
        """Entry point chính, chạy vòng lặp while thay cho QTimer."""
        self._running = True
        self._init_logger()
        if self.logger:
            self.logger.info("[PLC READ]: PLC Read init (multi-region, optimized, while-loop)")

        while self._running:
            # ----- Giai đoạn kết nối -----
            self._connect_plc()

            if not self._running:
                break

            if not (self._client and self._client.get_connected()):
                # Kết nối thất bại -> chờ retry_ms (ngắt được) rồi thử lại
                self._sleep_interruptible(self._retry_ms)
                continue

            if self._regions:
                self._build_read_items()

            self.init_data.emit()
            if self.logger:
                self.logger.info(
                    "[PLC READ]: Connected to PLC (max_parallel=%s, PDU=%s)",
                    getattr(self._client, "max_parallel", "?"),
                    getattr(self._client, "pdu_length", "?"),
                )

            # ----- Giai đoạn polling -----
            while self._running and self._client and self._client.get_connected():
                ok = self._poll()
                if not ok:
                    break
                self._sleep_interruptible(self._poll_ms)

            # Mất kết nối hoặc lỗi -> dọn dẹp rồi vòng ngoài sẽ tự reconnect
            self._teardown_after_disconnect()

        self._disconnect_plc()
        self.finished.emit()

    @Slot()
    def stop(self):
        """Yêu cầu vòng lặp while dừng lại. An toàn gọi từ thread khác vì
        chỉ set 1 biến bool; vòng lặp sẽ tự thoát ở lần kiểm tra gần nhất
        (tối đa self._sleep_step_ms sau đó)."""
        self._running = False

    def set_poll_interval(self, ms: int):
        self._poll_ms = ms

    def set_retry_interval(self, ms: int):
        self._retry_ms = ms

    def _connect_plc(self):
        if not self._running:
            return

        result = {"client": None, "error": None}
        done   = threading.Event()

        def _do_connect():
            try:
                c = snap7.client.Client()
                c.connect(self._ip, self._rack, self._slot)

                if hasattr(c, "use_optimizer"):
                    c.use_optimizer = True
                if hasattr(c, "multi_read_max_gap"):
                    c.multi_read_max_gap = 12
                if hasattr(c, "max_parallel"):
                    c.max_parallel = 4
                optimizer_active = getattr(c, "use_optimizer", False)
                if self.logger:
                    self.logger.info(f"[PLC READ]: Optimizer active = {optimizer_active}")
                result["client"] = c  # type: ignore
            except Exception as exc:
                result["error"] = exc  # type: ignore
            finally:
                done.set()

        t = threading.Thread(target=_do_connect, daemon=True)
        t.start()

        stop_requested = False
        while not done.wait(timeout=0.1):
            if not self._running:
                stop_requested = True

        if stop_requested or not self._running:
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
            msg = f"Connection failed: {result['error']}"
            now = time.time()
            if now - self._last_error_log_time >= 5:
                if self.logger:
                    self.logger.error("[PLC READ]: %s", msg)
                self._last_error_log_time = now
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

    def _teardown_after_disconnect(self):
        self._disconnect_plc()
        # sau khi mất kết nối, item/buffer cũ không còn hợp lệ để tái sử
        # dụng lâu dài (PLC có thể đổi PDU khi reconnect) -> xoá, sẽ dựng
        # lại khi connect thành công lần sau
        self._items = []
        self._buffers = []

    def _build_read_items(self):
        self._items = []
        self._buffers = []

        for name, start, size in self._regions:
            buf = (c_uint8 * size)()
            item_dict = {
                "area": Area.DB,
                "db_number": self._db_number,
                "start": start,
                "size": size,
                "pData": cast(buf, POINTER(c_uint8))
            }
            self._items.append(item_dict)
            self._buffers.append(buf)

        if self.logger:
            self.logger.info(f"Built Area: {[(n, s, sz) for n, s, sz in self._regions]}")

    def _poll(self) -> bool:
        """Đọc 1 lần từ PLC. Trả về False nếu cần reconnect (mất kết nối,
        lỗi đọc), True nếu đọc thành công."""
        if not self._items or not self._buffers:
            return True  # không có gì để đọc, không phải lỗi kết nối

        try:
            t0 = time.perf_counter()
            total_bytes = 0

            # ret = self._client._read_multi_vars_optimized(self._items)
            ret = self._client.read_multi_vars(self._items)
            elapsed_ms = (time.perf_counter() - t0) * 1000
            self.elapsed_time.emit(elapsed_ms)
            if elapsed_ms > (self._poll_ms * 1.5):
                if self.logger:
                    self.logger.info(
                        "[PLC READ]: Slow response %.1fms (size=%d)",
                        elapsed_ms, total_bytes,
                    )

            if isinstance(ret, (list, tuple)) and len(ret) >= 2:
                result_code = ret[0]
                data_buffers = ret[1]
            else:
                result_code = ret if isinstance(ret, int) else 0
                data_buffers = None

            if result_code != 0:
                raise S7Error(f"read_multi_vars error code: {result_code}")

            parsed: dict[str, Any] = {}

            for i, (name, start, size) in enumerate(self._regions):
                if data_buffers and i < len(data_buffers):
                    raw = bytearray(data_buffers[i])
                else:
                    raw = bytearray(self._buffers[i])

                total_bytes += len(raw)
                region_data = self._parse(raw, base_offset=start)
                parsed.update(region_data)

            self.data_ready.emit(parsed)
            if not parsed and self.logger:
                self.logger.warning("[PLC READ] Emitted empty dict! Check db_layout alignment.")

            return True

        except Exception:
            if self.logger:
                self.logger.error("[PLC READ]: Error in _poll", exc_info=True)
            return False

    def _parse(self, raw: bytearray, base_offset: int = 0) -> dict:
        if not self._db_layout:
            if self.logger:
                self.logger.warning(f"[_parse] db_layout is empty for base={base_offset}")
            return {}

        raw_len = len(raw)
        lo = bisect.bisect_left(self._layout_offsets, base_offset)
        hi = bisect.bisect_right(self._layout_offsets, base_offset + raw_len - 1)

        result = {}

        for name, dtype, offset, bit in self._db_layout[lo:hi]:
            rel_offset = offset - base_offset
            if rel_offset < 0 or rel_offset >= raw_len:
                continue

            try:
                if dtype == "BOOL":
                    value = get_bool(raw, rel_offset, bit)
                elif dtype == "REAL":
                    value = get_real(raw, rel_offset)
                elif dtype == "DINT":
                    value = get_dint(raw, rel_offset)
                elif dtype == "INT":
                    value = get_int(raw, rel_offset)
                elif dtype == "STRING":
                    value = get_string(raw, rel_offset)
                else:
                    value = None

                result[name] = value

            except Exception as e:
                result[name] = None
                if self.logger:
                    self.logger.error(f"Parse fail {name} (offset={offset}, dtype={dtype}): {e}")

        return result