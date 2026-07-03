import time
import bisect
import threading
from ctypes import c_uint8, cast, POINTER
import snap7
from typing import Any, Optional
from snap7.error import *  # type: ignore
from snap7.type import *   # type: ignore
from snap7.type import Parameter, Area, WordLen, S7DataItem
from snap7.util import get_bool, get_real, get_dint, get_int, get_string
from PySide6.QtCore import QObject, QTimer, Signal, Slot, QThread, Qt

SLOW_THRESHOLD_MS = 150   # log warning nếu 1 lần read vượt ngưỡng này

# ── snap7 yêu cầu cài bản có optimizer (chưa release lên PyPI) ──────────────
# pip install "git+https://github.com/gijzelaerr/python-snap7.git@7637ab254e42577ad9872cdeea56456dcd2ee91f"
# Đã verify: dict_items >= 2 item tự động dùng _read_multi_vars_optimized()
# (sort -> merge -> packetize -> parallel dispatch trên 1 PDU/connection)


class PLCReader(QObject):
    """
    Object dùng để lấy TOÀN BỘ dữ liệu từ PLC qua 1 connection duy nhất,
    dùng read_multi_vars() (multi-variable read optimizer) để gộp nhiều
    vùng đọc rời rạc thành tối thiểu round-trip.

    Thay thế kiến trúc cũ (3 PLCRead object riêng biệt, 3 connection)
    bằng 1 object duy nhất đọc nhiều vùng (region) trong 1 lần gọi.
    """
    init_data    = Signal()
    data_ready   = Signal(dict)
    error        = Signal(str)
    connected    = Signal(bool)
    disconnected = Signal()
    finished     = Signal()
    elapsed_time = Signal(float)

    _stop_read   = Signal()

    def __init__(
        self,
        ip:         str                                       = "172.16.100.100",
        rack:       int                                       = 0,
        slot:       int                                       = 1,
        db_number:  int                                       = 1,
        db_layout:  Optional[list[tuple[str, str, int, Any]]] = None,
        regions:    Optional[list[tuple[str, int, int]]]      = None,
        # regions: list các vùng cần đọc, mỗi vùng (name, start_offset, size)
        # VD: [("ACTUAL", 0, 198), ("INPUT", 198, 138), ("STRING", 336, 256)]
        poll_ms:    int                                       = 250,
        retry_ms:   int                                       = 3000,
        use_optimizer:       bool                             = True,
        multi_read_max_gap:  int                               = 5,
        max_parallel:        Optional[int]                     = None,
        # None = để optimizer tự auto-tune theo PDU size sau khi connect
        logger                                                 = None,
        parent:     Optional[QObject]                          = None,
    ):
        super().__init__(parent)
        self._ip        = ip
        self._rack      = rack
        self._slot      = slot
        self._db_number = db_number

        # FIX: sort theo offset 1 lần để _parse() dùng bisect thay vì quét
        # toàn bộ db_layout cho từng region ở mỗi vòng poll (250ms).
        self._db_layout: Optional[list[tuple[str, str, int, Any]]] = (
            sorted(db_layout, key=lambda t: t[2]) if db_layout else None
        )
        self._layout_offsets: list[int] = (
            [t[2] for t in self._db_layout] if self._db_layout else []
        )

        self._regions   = regions or []
        self._poll_ms   = poll_ms
        self._retry_ms  = retry_ms
        self.logger     = logger

        self._use_optimizer      = use_optimizer
        self._multi_read_max_gap = multi_read_max_gap
        self._max_parallel       = max_parallel

        self._client:      snap7.client.Client | None = None
        self._poll_timer:  QTimer | None = None
        self._retry_timer: QTimer | None = None
        self._running   = False

        self._last_error_log_time: float = 0.0

        # FIX: cache S7DataItem + buffer ctypes, build 1 lần sau khi connect
        # thành công thay vì dựng lại dict mỗi vòng poll.
        self._items:   list[S7DataItem] = []
        self._buffers: list             = []

    # ── Lifecycle ─────────────────────────────────────────────────────────────

    @Slot()
    def run(self):
        self._running = True
        if self.logger:
            self.logger.info("[PLC READ]: PLC Read init (multi-region, optimized)")

        self._poll_timer = QTimer(self)
        self._poll_timer.setInterval(self._poll_ms)
        self._poll_timer.timeout.connect(self._poll)

        self._retry_timer = QTimer(self)
        self._retry_timer.setInterval(self._retry_ms)
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
        if self._retry_timer and self._retry_timer.isActive():
            self._retry_timer.setInterval(ms)

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

    # ── Connection ────────────────────────────────────────────────────────────

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

            # FIX: dựng sẵn item/buffer 1 lần ngay sau khi connect thành công
            if self._regions:
                self._build_read_items()

            self.init_data.emit()
            if self._poll_timer and not self._poll_timer.isActive():
                self._poll_timer.start()
            if self.logger:
                self.logger.info(
                    "[PLC READ]: Connected to PLC (max_parallel=%s, PDU=%s)",
                    getattr(self._client, "max_parallel", "?"),
                    getattr(self._client, "pdu_length", "?"),
                )
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

                # ── snap7 application-level params ────────────────────────
                c.set_param(Parameter.PDURequest,    1024)
                c.set_param(Parameter.SendTimeout,     8)
                c.set_param(Parameter.RecvTimeout,     5)
                c.set_param(Parameter.PingTimeout,     5)
                c.set_param(Parameter.KeepAliveTime,  10)

                c.connect(self._ip, self._rack, self._slot)

                # ── Cấu hình optimizer (chỉ tồn tại trên bản đã cài optimizer) ──
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

        # FIX: Nếu self._running trở thành False trong lúc đang chờ,
        # code cũ `return` ngay lập tức trong khi thread `_do_connect` vẫn
        # chạy nền. Nếu sau đó thread connect thành công, socket sẽ không
        # bao giờ được disconnect() -> rò rỉ kết nối/tài nguyên.
        # Cách sửa: vẫn CHỜ thread hoàn tất (SendTimeout/RecvTimeout đã set
        # nên connect() bị chặn có giới hạn thời gian), chỉ đánh dấu để xử lý
        # dọn dẹp sau khi thread xong, không return giữa chừng.
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
            # self.error.emit(msg)
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
            self.logger.info(f"Built Area: {[(n, s, sz) for n,s,sz in self._regions]}")

    @Slot()
    def _poll(self):
        if not self._running or not self._client or not self._client.get_connected():
            self._reconnect()
            return

        if not self._items or not self._buffers:
            return

        try:
            t0 = time.perf_counter()
            total_bytes = 0

            ret = self._client._read_multi_vars_optimized(self._items)
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
            elapsed_ms = (time.perf_counter() - t0) * 1000
            self.elapsed_time.emit(elapsed_ms)
            if elapsed_ms > (self._poll_ms * 1.5):
                if self.logger:
                    respond = "Slow response"
                    self.logger.info(
                        f"[PLC READ]: {respond} %.1fms (size=%d)",
                        elapsed_ms, total_bytes,
                    )
            if not parsed and self.logger:
                self.logger.warning(f"[PLC READ] Emitted empty dict! Check db_layout alignment.")

        except Exception as exc:
            if self.logger:
                self.logger.error("[PLC READ]: Error in _poll", exc_info=True)
            self._reconnect()

    @Slot()
    def _reconnect(self):
        if not self._running:
            return
        if self._poll_timer:
            self._poll_timer.stop()
        self._disconnect_plc()
        # FIX: sau khi mất kết nối, item/buffer cũ không còn hợp lệ để tái sử
        # dụng lâu dài (PLC có thể đổi PDU khi reconnect) -> xoá, sẽ dựng lại
        # trong _try_connect() khi connect thành công lần sau.
        self._items = []
        self._buffers = []
        if self._retry_timer:
            self._retry_timer.start()

    def _parse(self, raw: bytearray, base_offset: int = 0) -> dict:
        if not self._db_layout:
            if self.logger:
                self.logger.warning(f"[_parse] db_layout is empty for base={base_offset}")
            return {}

        raw_len = len(raw)
        lo = bisect.bisect_left(self._layout_offsets, base_offset)
        hi = bisect.bisect_right(self._layout_offsets, base_offset + raw_len - 1)

        result = {}
        found = 0

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
                    value = get_string(raw, rel_offset)        # ← Chỉ 2 tham số
                else:
                    value = None

                result[name] = value
                found += 1

            except Exception as e:
                result[name] = None
                if self.logger:
                    self.logger.error(f"Parse fail {name} (offset={offset}, dtype={dtype}): {e}")

        return result