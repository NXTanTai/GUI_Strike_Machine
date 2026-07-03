import time
import bisect
import asyncio
from typing import Any, Optional

from s7 import AsyncClient
from s7.util import get_bool, get_real, get_dint, get_int, get_string
from PySide6.QtCore import QObject, Signal


SLOW_THRESHOLD_MS = 200


class PLCReaderAsync(QObject):
    init_data    = Signal()
    data_ready   = Signal(dict)
    error        = Signal(str)
    connected    = Signal(bool)
    disconnected = Signal()
    finished     = Signal()
    elapsed_time = Signal(float)

    def __init__(self, ip="172.16.100.100", rack=0, slot=1, db_number=1,
                 db_layout=None, regions=None, poll_ms=250, retry_ms=3000,
                 logger=None, parent=None):
        super().__init__(parent)

        self._ip = ip
        self._rack = rack
        self._slot = slot
        self._db_number = db_number

        self._db_layout = sorted(db_layout, key=lambda t: t[2]) if db_layout else None
        self._layout_offsets = [t[2] for t in self._db_layout] if self._db_layout else []

        self._regions = regions or []
        self._poll_ms = poll_ms
        self._retry_ms = retry_ms
        self.logger = logger

        self._client: Optional[AsyncClient] = None
        self._task: Optional[asyncio.Task] = None
        self._running = False

        self._last_error_log_time = 0.0

    def start(self):
        if self._running:
            return
        self._running = True
        self._task = asyncio.create_task(self._run_loop())

    async def stop(self):
        self._running = False
        if self._task:
            try:
                await asyncio.wait_for(self._task, timeout=5.0)
            except (asyncio.TimeoutError, asyncio.CancelledError):
                pass
            self._task = None

    async def _run_loop(self):
        if self.logger:
            self.logger.info("[PLC READ Async]: Starting...")

        while self._running:
            try:
                async with AsyncClient() as client:
                    self._client = client

                    if self.logger:
                        self.logger.info(f"[PLC READ Async]: Connecting to {self._ip} (rack={self._rack}, slot={self._slot})")

                    # Cấu hình timeout qua underlying client (cách chuẩn của s7)
                    if hasattr(client, 'client'):
                        client.client.set_param(1, 1024)   # PDURequest
                        client.client.set_param(2, 10000)  # SendTimeout (ms)
                        client.client.set_param(3, 10000)  # RecvTimeout (ms)

                    # Connect với timeout
                    await asyncio.wait_for(
                        client.connect(self._ip, self._rack, self._slot),
                        timeout=10.0
                    )

                    self.connected.emit(True)
                    self.init_data.emit()

                    if self.logger:
                        self.logger.info("[PLC READ Async]: Connected successfully")

                    await self._poll_loop(client)

            except asyncio.TimeoutError:
                self._log_error("Connect timeout (10s)")
                self.error.emit("PLC connect timeout")
            except Exception as exc:
                self._log_error(str(exc))
                self.error.emit(str(exc))
            finally:
                self._client = None
                self.connected.emit(False)

            if not self._running:
                break

            await asyncio.sleep(self._retry_ms / 1000.0)

        self.disconnected.emit()
        self.finished.emit()

    async def _poll_loop(self, client: AsyncClient):
        items = [(self._db_number, start, size) for _, start, size in self._regions]

        while self._running:
            t0 = time.perf_counter()

            try:
                buffers = await client.db_read_multi(items)

                parsed: dict[str, Any] = {}
                total_bytes = 0

                for (name, start, size), raw in zip(self._regions, buffers):
                    total_bytes += len(raw)
                    parsed.update(self._parse(raw, start))

                self.data_ready.emit(parsed)
                self.elapsed_time.emit((time.perf_counter() - t0) * 1000)

                if total_bytes == 0 and self.logger:
                    self.logger.warning("[PLC READ Async] Received empty data!")

            except Exception as exc:
                if self.logger:
                    self.logger.error("[PLC READ Async] Poll error", exc_info=True)
                raise  # thoát ra reconnect

            try:
                await asyncio.sleep(self._poll_ms / 1000.0)
            except asyncio.CancelledError:
                raise

    def _parse(self, raw: bytearray, base_offset: int = 0) -> dict:
        # (giữ nguyên hàm _parse trước đó của bạn)
        if not self._db_layout:
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
                    self.logger.error(f"Parse fail {name} @ {offset}: {e}")
        return result

    def _log_error(self, msg: str):
        now = time.time()
        if now - self._last_error_log_time >= 5:
            if self.logger:
                self.logger.error("[PLC READ Async]: %s", msg)
            self._last_error_log_time = now