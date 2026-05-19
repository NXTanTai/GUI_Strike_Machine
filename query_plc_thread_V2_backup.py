"""
plc_worker.py  (PySide6)
─────────────────────────────────────────────────────────────
PLCRead  – QObject designed to run inside a QThread.

Usage (main / UI thread):
    self.plc_read_thread = QThread()
    self.plc_read_worker = PLCRead(ip="192.168.1.1", db_number=1)
    self.plc_read_worker.moveToThread(self.plc_read_thread)

    self.plc_read_thread.started.connect(self.plc_read_worker.run)
    self.plc_read_worker.data_ready.connect(self.on_plc_data_received)
    self.plc_read_worker.error.connect(self.on_error)
    self.plc_read_worker.connected.connect(self.on_connected)
    self.plc_read_worker.disconnected.connect(self.on_disconnected)

    # Khi worker báo xong → mới quit thread
    self.plc_read_worker.finished.connect(self.plc_read_thread.quit)

    self.plc_read_thread.start()

    # Stop gracefully (gọi từ main thread hoàn toàn an toàn):
    self.plc_read_worker.stop()
    self.plc_read_thread.wait(5000)
"""

import struct
import logging
from typing import Any, Optional

import snap7
from snap7.error import S7Error

from PySide6.QtCore import QObject, QTimer, Signal, Slot

logger = logging.getLogger(__name__)


# ── Helpers ─────────────────────────────────────────────────────────────────

def _get_bool(data: bytes, byte_idx: int, bit_idx: int) -> bool:
    return bool(data[byte_idx] & (1 << (7 - bit_idx)))


def _get_real(data: bytes, offset: int) -> float:
    return struct.unpack_from(">f", data, offset)[0]


def _get_dint(data: bytes, offset: int) -> int:
    return struct.unpack_from(">i", data, offset)[0]


def _get_int(data: bytes, offset: int) -> int:
    return struct.unpack_from(">h", data, offset)[0]


def _get_string(data: bytes, offset: int) -> str:
    act_len = data[offset + 1]
    raw = data[offset + 2: offset + 2 + act_len]
    return raw.decode("utf-8", errors="replace")


# ── PLCRead ─────────────────────────────────────────────────────────────────

class PLCRead(QObject):
    """
    Đọc DB Siemens S7 định kỳ và emit dict đã parse.

    Signals
    -------
    data_ready(dict)  – emit mỗi poll cycle
    error(str)        – emit khi lỗi kết nối / đọc
    connected()       – emit khi kết nối thành công
    disconnected()    – emit khi mất kết nối
    finished()        – emit sau khi stop() hoàn tất (dùng để quit thread)
    """

    data_ready    = Signal(dict)
    error         = Signal(str)
    connected     = Signal()
    disconnected  = Signal()
    finished      = Signal()   # báo main thread biết worker đã dọn xong

    # Signal nội bộ — Qt tự dispatch sang worker thread qua QueuedConnection
    _request_stop = Signal()

    def __init__(
        self,
        ip:        str                   = "192.168.1.1",
        rack:      int                   = 0,
        slot:      int                   = 1,
        db_number: int                   = 1,
        db_layout: Optional[list[tuple]] = None,
        db_size:   int                   = 584,
        poll_ms:   int                   = 500,
        retry_ms:  int                   = 3_000,
        parent:    Optional[QObject]     = None,
    ):
        super().__init__(parent)
        self._ip        = ip
        self._rack      = rack
        self._slot      = slot
        self._db_number = db_number
        self._db_layout = db_layout
        self._db_size   = db_size
        self._poll_ms   = poll_ms
        self._retry_ms  = retry_ms

        self._client:      snap7.client.Client | None = None
        self._poll_timer:  QTimer | None = None
        self._retry_timer: QTimer | None = None
        self._running = False

    # ── Public API ──────────────────────────────────────────────────────────

    @Slot()
    def run(self):
        """
        Gọi từ QThread.started signal.
        Tạo timer TRONG worker thread — đảm bảo đúng thread affinity.
        """
        self._running = True

        self._poll_timer = QTimer(self)          # parent=self → cùng thread
        self._poll_timer.setInterval(self._poll_ms)
        self._poll_timer.timeout.connect(self._poll)

        self._retry_timer = QTimer(self)         # parent=self → cùng thread
        self._retry_timer.setInterval(self._retry_ms)
        self._retry_timer.timeout.connect(self._try_connect)

        # Kết nối _request_stop ở đây → slot _do_stop chạy đúng worker thread
        self._request_stop.connect(self._do_stop)

        self._try_connect()
        
    @Slot()
    def stop(self):
        # print(f">>> stop() called, _running={self._running}")
        self._running = False
        self._request_stop.emit()
        # print(">>> _request_stop emitted")

    def set_poll_interval(self, ms: int):
        """Thay đổi poll interval lúc runtime."""
        self._poll_ms = ms
        if self._poll_timer:
            self._poll_timer.setInterval(ms)

    def set_retry_interval(self, ms: int):
        """Thay đổi retry interval lúc runtime."""
        self._retry_ms = ms
        if self._retry_timer:
            self._retry_timer.setInterval(ms)

    # ── Internal stop (chạy trong worker thread) ────────────────────────────

    @Slot()
    def _do_stop(self):
        # print(">>> _do_stop called")   # thêm tạm để debug
        if self._poll_timer and self._poll_timer.isActive():
            self._poll_timer.stop()
            # print(">>> poll_timer stopped")

        if self._retry_timer and self._retry_timer.isActive():
            self._retry_timer.stop()
            # print(">>> retry_timer stopped")

        self._disconnect_plc()
        # print(">>> finished.emit()")
        self.finished.emit()

    # ── Connection ──────────────────────────────────────────────────────────

    @Slot()
    def _try_connect(self):
        """
        Thử kết nối PLC.
        - Thành công → dừng retry_timer, bắt đầu poll_timer.
        - Thất bại   → retry_timer tiếp tục chạy.
        """
        if not self._running:
            return

        # Đã kết nối rồi thì bỏ qua
        if self._client is not None and self._client.get_connected():
            return

        self._connect_plc()

        if self._client is not None:
            logger.info("Connected — switching to poll mode")
            self._retry_timer.stop()
            self._poll_timer.start()
        else:
            if not self._retry_timer.isActive():
                self._retry_timer.start()
            logger.info("Connection failed — retrying in %d ms", self._retry_ms)

    def _connect_plc(self):
        try:
            self._client = snap7.client.Client()
            self._client.connect(self._ip, self._rack, self._slot)
            logger.info("PLC connected: %s", self._ip)
            self.connected.emit()
        except S7Error as exc:
            msg = f"Connection failed: {exc}"
            logger.error(msg)
            self.error.emit(msg)
            self._client = None

    def _disconnect_plc(self):
        if self._client:
            try:
                self._client.disconnect()
            except Exception:
                pass
            self._client = None
        self.disconnected.emit()
        logger.info("PLC disconnected")

    @Slot()
    def _reconnect(self):
        """
        Mất kết nối trong lúc poll → dừng poll, chuyển sang retry mode.
        """
        if not self._running:
            return
        logger.info("Connection lost — switching to retry mode")
        self._poll_timer.stop()
        self._disconnect_plc()
        self._retry_timer.start()

    # ── Poll ────────────────────────────────────────────────────────────────

    @Slot()
    def _poll(self):
        if not self._running:
            self._poll_timer.stop()
            return

        if self._client is None or not self._client.get_connected():
            self._reconnect()
            return

        client = self._client   # snapshot local tránh race condition
        if client is None:
            return

        try:
            raw    = client.db_read(self._db_number, 0, self._db_size)
            result = self._parse(raw)
            self.data_ready.emit(result)

        except S7Error as exc:
            msg = f"Read error: {exc}"
            logger.warning(msg)
            self.error.emit(msg)
            self._client = None
            self._reconnect()

    # ── Parse ───────────────────────────────────────────────────────────────

    def _parse(self, raw: bytes) -> dict:
        if self._db_layout is None:
            logger.warning("db_layout is None, skipping parse")
            return {}

        result: dict[str, Any] = {}
        for name, dtype, offset, bit in self._db_layout:
            try:
                if dtype == "BOOL":
                    result[name] = _get_bool(raw, offset, bit)
                elif dtype == "REAL":
                    result[name] = _get_real(raw, offset)
                elif dtype == "DINT":
                    result[name] = _get_dint(raw, offset)
                elif dtype == "INT":
                    result[name] = _get_int(raw, offset)
                elif dtype == "STRING":
                    result[name] = _get_string(raw, offset)
            except Exception as exc:
                result[name] = None
                logger.debug("Parse error [%s]: %s", name, exc)
        return result