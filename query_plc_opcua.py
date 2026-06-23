"""
query_plc_opcua.py
==================
Thay thế query_plc_thread_V2.py khi PLC hỗ trợ OPC UA Server.

Yêu cầu phía PLC:
    • S7-1500: bật OPC UA Server trong TIA Portal
      Properties → OPC UA → Server → Enable
    • S7-1200 fw >= V4.4: tương tự
    • S7-300/400: cần gateway trung gian (Kepware, Prosys...)

Cài đặt:
    pip install asyncua

Interface Signal giữ nguyên 100% so với PLCRead (query_plc_thread_V2.py).
source.py không cần sửa bất kỳ dòng nào — chỉ đổi import.

Cách dùng trong source.py:
    # Thay dòng cũ:
    # from query_plc_thread_V2 import PLCRead

    # Bằng:
    from query_plc_opcua import PLCReadOPCUA as PLCRead

    # Và truyền node_map thay vì db_layout:
    node_map = {
        "P1_TemperatureSetting": 'ns=3;s="DB100"."P1_TemperatureSetting"',
        "P1_Start_Heat":         'ns=3;s="DB100"."P1_Start_Heat"',
        ...
    }
    worker = PLCRead(
        endpoint  = "opc.tcp://172.16.100.100:4840",
        node_map  = node_map,
        poll_ms   = 500,
        username  = "",       # để trống nếu PLC không bật xác thực
        password  = "",
        logger    = self.logger
    )

Hai chế độ hoạt động:
    • POLLING (mặc định):  đọc toàn bộ node theo chu kỳ poll_ms
    • SUBSCRIPTION:        PLC tự đẩy khi giá trị thay đổi (tiết kiệm CPU hơn)
      Bật bằng: use_subscription=True
"""

import asyncio
import threading
import time
import logging

from typing import Optional

from PySide6.QtCore import QObject, Signal, Slot, QThread, Qt


# ─── Hằng số ────────────────────────────────────────────────────────────────

RETRY_DELAY_SEC     = 3.0    # giây chờ trước khi thử kết nối lại
SUBSCRIPTION_MS     = 100    # chu kỳ kiểm tra phía server khi dùng Subscription
LOG_THROTTLE_SEC    = 5.0    # tránh log lỗi kết nối liên tục


# ─── PLCReadOPCUA ────────────────────────────────────────────────────────────

class PLCReadOPCUA(QObject):
    """
    Đọc dữ liệu từ OPC UA Server (thường là PLC Siemens S7-1200/1500).

    Signal interface giống hệt PLCRead trong query_plc_thread_V2.py:
        init_data  = Signal()          — trigger sau khi connect để load giá trị ban đầu
        data_ready = Signal(dict)      — dict{tag_name: value} mỗi chu kỳ
        connected  = Signal(bool)      — True/False khi trạng thái kết nối thay đổi
        error      = Signal(str)       — thông báo lỗi
        finished   = Signal()          — worker đã dừng hoàn toàn
    """

    init_data   = Signal()
    data_ready  = Signal(dict)
    error       = Signal(str)
    connected   = Signal(bool)
    finished    = Signal()

    _stop_signal = Signal()

    def __init__(
        self,
        endpoint:         str,
        node_map:         dict[str, str],
        poll_ms:          int  = 500,
        username:         str  = "",
        password:         str  = "",
        use_subscription: bool = False,
        security_string:  str  = "",
        logger:           Optional[logging.Logger] = None,
        parent:           Optional[QObject] = None,
    ):
        """
        Args:
            endpoint:         URL OPC UA, ví dụ "opc.tcp://172.16.100.100:4840"
            node_map:         dict{tag_name → NodeId string}
                              ví dụ {"P1_Temp": 'ns=3;s="DB100"."P1_Temp"'}
            poll_ms:          chu kỳ đọc (ms) khi dùng polling mode
            username:         user OPC UA (để trống nếu không bật auth)
            password:         password OPC UA
            use_subscription: True → dùng Subscription (PLC push)
                              False → polling theo chu kỳ poll_ms
            security_string:  ví dụ "Basic256Sha256,SignAndEncrypt,..."
                              để trống nếu không bật security
            logger:           logging.Logger
        """
        super().__init__(parent)
        self._endpoint         = endpoint
        self._node_map         = node_map          # {tag_name: NodeId_str}
        self._poll_ms          = poll_ms
        self._username         = username
        self._password         = password
        self._use_subscription = use_subscription
        self._security_string  = security_string
        self.logger            = logger

        self._running          = False
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._last_error_log   = 0.0

    # ── Lifecycle ────────────────────────────────────────────────────────────

    @Slot()
    def run(self):
        """Gọi từ QThread.started — chạy asyncio event loop trong thread riêng."""
        self._running = True
        if self.logger:
            self.logger.info("[OPC UA READ]: Worker started — endpoint: %s", self._endpoint)

        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)

        try:
            self._loop.run_until_complete(self._supervisor())
        except Exception as exc:
            if self.logger:
                self.logger.error("[OPC UA READ]: Event loop crashed: %s", exc)
        finally:
            try:
                self._loop.close()
            except Exception:
                pass
            self.finished.emit()
            QThread.currentThread().quit()

    def stop(self):
        """Gọi từ bên ngoài để dừng worker."""
        self._running = False
        if self._loop and not self._loop.is_closed():
            self._loop.call_soon_threadsafe(self._loop.stop)

    # ── Supervisor: tự reconnect khi mất kết nối ────────────────────────────

    async def _supervisor(self):
        """
        Vòng lặp bên ngoài — reconnect tự động khi _session() kết thúc vì lỗi.
        """
        while self._running:
            try:
                await self._session()
            except asyncio.CancelledError:
                break
            except Exception as exc:
                now = time.time()
                if now - self._last_error_log >= LOG_THROTTLE_SEC:
                    if self.logger:
                        self.logger.error("[OPC UA READ]: Session error: %s", exc)
                    self.error.emit(str(exc))
                    self._last_error_log = now
                self.connected.emit(False)
                if self._running:
                    await asyncio.sleep(RETRY_DELAY_SEC)

    # ── Session: 1 vòng kết nối → đọc dữ liệu ──────────────────────────────

    async def _session(self):
        """
        Tạo kết nối OPC UA, đọc dữ liệu cho đến khi mất kết nối.
        Raise exception → supervisor sẽ reconnect.
        """
        try:
            from asyncua import Client
        except ImportError:
            raise RuntimeError(
                "Thư viện 'asyncua' chưa được cài đặt. "
                "Chạy: pip install asyncua"
            )

        client = Client(url=self._endpoint, timeout=10)

        # ── Xác thực ────────────────────────────────────────────────────────
        if self._username:
            client.set_user(self._username)
            client.set_password(self._password)

        # ── Security (tùy chọn) ─────────────────────────────────────────────
        if self._security_string:
            await client.set_security_string(self._security_string)

        async with client:
            if self.logger:
                self.logger.info("[OPC UA READ]: Connected to %s", self._endpoint)
            self.connected.emit(True)

            # Cache node objects — tra cứu 1 lần, dùng nhiều lần
            nodes = await self._resolve_nodes(client)

            # Báo source.py load giá trị ban đầu từ PLC
            self.init_data.emit()

            if self._use_subscription:
                await self._run_subscription(client, nodes)
            else:
                await self._run_polling(nodes)

    async def _resolve_nodes(self, client) -> dict:
        """
        Chuyển NodeId string → Node object.
        Log cảnh báo cho các NodeId không tìm thấy trên server.
        """
        from asyncua import ua

        nodes = {}
        for tag_name, node_id_str in self._node_map.items():
            try:
                node = client.get_node(node_id_str)
                # Thử đọc 1 lần để xác nhận node tồn tại
                await node.read_value()
                nodes[tag_name] = node
            except Exception as exc:
                if self.logger:
                    self.logger.warning(
                        "[OPC UA READ]: Node không tìm thấy — tag=%s NodeId=%s (%s)",
                        tag_name, node_id_str, exc
                    )
        if self.logger:
            self.logger.info(
                "[OPC UA READ]: Resolved %d/%d nodes",
                len(nodes), len(self._node_map)
            )
        return nodes

    # ── Chế độ Polling ───────────────────────────────────────────────────────

    async def _run_polling(self, nodes: dict):
        """
        Đọc toàn bộ node mỗi poll_ms — đơn giản, tương đương S7comm db_read.
        """
        interval = self._poll_ms / 1000.0
        if self.logger:
            self.logger.info("[OPC UA READ]: Polling mode — interval=%dms", self._poll_ms)

        while self._running:
            t0 = time.perf_counter()

            result = await self._read_all(nodes)
            if result:
                self.data_ready.emit(result)

            elapsed = time.perf_counter() - t0
            sleep_time = max(0.0, interval - elapsed)
            await asyncio.sleep(sleep_time)

    async def _read_all(self, nodes: dict) -> dict:
        """Đọc song song tất cả node trong 1 lần gọi."""
        if not nodes:
            return {}

        tag_names = list(nodes.keys())
        node_list = [nodes[n] for n in tag_names]

        try:
            # read_values đọc batch — hiệu quả hơn đọc từng cái
            values = await asyncio.gather(
                *[n.read_value() for n in node_list],
                return_exceptions=True
            )
            result = {}
            for name, val in zip(tag_names, values):
                if isinstance(val, Exception):
                    if self.logger:
                        self.logger.debug("[OPC UA READ]: Read error [%s]: %s", name, val)
                    result[name] = None
                else:
                    result[name] = val
            return result
        except Exception as exc:
            raise exc   # bubble lên _session → supervisor reconnect

    # ── Chế độ Subscription ──────────────────────────────────────────────────

    async def _run_subscription(self, client, nodes: dict):
        """
        PLC tự đẩy dữ liệu về khi giá trị thay đổi.
        Tiết kiệm CPU và băng thông hơn polling.
        """
        if self.logger:
            self.logger.info(
                "[OPC UA READ]: Subscription mode — server interval=%dms",
                SUBSCRIPTION_MS
            )

        handler = _SubscriptionHandler(
            node_map_reversed={
                node: name for name, node in nodes.items()
            },
            on_data=lambda data: self.data_ready.emit(data),
            logger=self.logger
        )

        subscription = await client.create_subscription(
            period=SUBSCRIPTION_MS,
            handler=handler
        )
        await subscription.subscribe_data_change(list(nodes.values()))

        try:
            while self._running:
                await asyncio.sleep(1.0)   # giữ vòng lặp, PLC tự push dữ liệu
        finally:
            try:
                await subscription.delete()
            except Exception:
                pass


# ─── Subscription Handler ────────────────────────────────────────────────────

class _SubscriptionHandler:
    """
    Callback handler cho OPC UA Subscription.
    Gom các thay đổi trong 1 dict rồi emit data_ready.
    """

    def __init__(self, node_map_reversed: dict, on_data, logger=None):
        self._node_map_reversed = node_map_reversed   # {Node: tag_name}
        self._on_data   = on_data
        self.logger     = logger
        self._cache: dict = {}

    def datachange_notification(self, node, val, data):
        """Gọi bởi asyncua mỗi khi PLC báo có thay đổi."""
        try:
            node_id_str = node.nodeid.to_string()
            # Tìm tag_name tương ứng
            tag_name = None
            for n, name in self._node_map_reversed.items():
                if n.nodeid.to_string() == node_id_str:
                    tag_name = name
                    break

            if tag_name:
                self._cache[tag_name] = val
                self._on_data(dict(self._cache))
        except Exception as exc:
            if self.logger:
                self.logger.debug("[OPC UA SUBSCRIPTION]: Callback error: %s", exc)

    def event_notification(self, event):
        pass