import time
import logging
import threading
import snap7
from typing import Any, Optional
from snap7.error import *  # type: ignore
from snap7.type import *   # type: ignore
from snap7.type import Parameter, Area
from snap7.util import get_bool, get_real, get_dint, get_int, get_string
from PySide6.QtCore import QObject, QTimer, Signal, Slot, QThread, Qt

SLOW_THRESHOLD_MS = 150   # log warning nếu 1 lần read vượt ngưỡng này

# ── snap7 yêu cầu cài bản có optimizer (chưa release lên PyPI) ──────────────
# pip install "git+https://github.com/gijzelaerr/python-snap7.git@7637ab254e42577ad9872cdeea56456dcd2ee91f"
# Đã verify: dict_items >= 2 item tự động dùng _read_multi_vars_optimized()
# (sort -> merge -> packetize -> parallel dispatch trên 1 PDU/connection)


class PLCRead(QObject):
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
        self._db_layout = db_layout
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
                c.set_param(Parameter.PDURequest,    960)
                c.set_param(Parameter.SendTimeout,     3)
                c.set_param(Parameter.RecvTimeout,     2)
                c.set_param(Parameter.PingTimeout,     2)
                c.set_param(Parameter.KeepAliveTime,  10)

                c.connect(self._ip, self._rack, self._slot)

                # ── Cấu hình optimizer (chỉ tồn tại trên bản đã cài optimizer) ──
                if hasattr(c, "use_optimizer"):
                    c.use_optimizer = self._use_optimizer
                if hasattr(c, "multi_read_max_gap"):
                    c.multi_read_max_gap = self._multi_read_max_gap
                if self._max_parallel is not None and hasattr(c, "max_parallel"):
                    c.max_parallel = self._max_parallel
                # Nếu max_parallel=None, để optimizer tự auto-tune theo PDU
                # (đã xảy ra ngay trong c.connect() ở bản đã verify)

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
            msg = f"Connection failed: {result['error']}"
            now = time.time()
            if now - self._last_error_log_time >= 5:
                if self.logger:
                    self.logger.error("[PLC READ]: %s", msg)
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

    # ── Poll loop ─────────────────────────────────────────────────────────────

    @Slot()
    def _poll(self):
        if not self._running or not self._client or not self._client.get_connected():
            self._reconnect()
            return

        if not self._regions:
            return

        try:
            t0 = time.perf_counter()

            # Xây danh sách item cho read_multi_vars() — mỗi region = 1 item.
            # Optimizer sẽ tự sort/merge/packetize các item này.
            items = [
                {
                    "area":      Area.DB,
                    "db_number": self._db_number,
                    "start":     start,
                    "size":      size,
                }
                for (_name, start, size) in self._regions
            ]

            result_code, data_list = self._client.read_multi_vars(items)

            if result_code != 0:
                raise S7Error(f"read_multi_vars returned non-zero: {result_code}")

            # data_list là list[bytearray], cùng thứ tự với self._regions
            parsed: dict[str, Any] = {}
            total_bytes = 0
            for (name, start, size), raw in zip(self._regions, data_list):
                total_bytes += len(raw)
                parsed.update(self._parse(raw, base_offset=start))

            self.data_ready.emit(parsed)

            elapsed_ms = (time.perf_counter() - t0) * 1000
            if elapsed_ms > SLOW_THRESHOLD_MS:
                if self.logger:
                    self.logger.warning(
                        "[PLC READ]: Slow response %.1fms (size=%d, regions=%d)",
                        elapsed_ms, total_bytes, len(self._regions),
                    )

        except S7Error as exc:
            if self.logger:
                self.logger.warning("[PLC READ]: Read error: %s", exc)
            self.error.emit(f"Read error: {exc}")
            self._reconnect()
        except Exception as exc:
            if self.logger:
                self.logger.error("[PLC READ]: Unexpected error: %s", exc)
            self.error.emit(str(exc))
            self._reconnect()

    @Slot()
    def _reconnect(self):
        if not self._running:
            return
        if self._poll_timer:
            self._poll_timer.stop()
        self._disconnect_plc()
        if self._retry_timer:
            self._retry_timer.start()

    def _parse(self, raw: bytearray, base_offset: int = 0) -> dict:
        """
        Parse 1 vùng raw bytes thành dict các tag theo db_layout.
        Chỉ parse những tag có offset thuộc vùng [base_offset, base_offset+len(raw)).
        """
        if not self._db_layout:
            return {}

        result:  dict[str, Any] = {}
        raw_len: int            = len(raw)

        for name, dtype, offset, bit in self._db_layout:
            rel_offset = offset - base_offset

            if rel_offset < 0 or rel_offset >= raw_len:
                continue  # tag này không thuộc vùng raw hiện tại, bỏ qua

            try:
                if dtype == "BOOL":
                    result[name] = get_bool(raw, rel_offset, bit)
                elif dtype == "REAL":
                    result[name] = get_real(raw, rel_offset)
                elif dtype == "DINT":
                    result[name] = get_dint(raw, rel_offset)
                elif dtype == "INT":
                    result[name] = get_int(raw, rel_offset)
                elif dtype == "STRING":
                    result[name] = get_string(raw, rel_offset)
                else:
                    result[name] = None
            except Exception as exc:
                result[name] = None
                if self.logger:
                    self.logger.error(
                        "[PLC READ]: Parse error [%s] offset=%d: %s",
                        name, offset, exc,
                    )

        return result