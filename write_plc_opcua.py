"""
write_plc_opcua.py
==================
Thay thế write_plc_thread_V2.py khi PLC hỗ trợ OPC UA Server.

Yêu cầu phía PLC:
    • Giống query_plc_opcua.py — xem file đó để biết chi tiết cấu hình.
    • Các tag cần được đánh dấu "Writable" trong TIA Portal.

Cài đặt:
    pip install asyncua

Interface Signal giữ nguyên 100% so với PLCWrite (write_plc_thread_V2.py).
source.py không cần sửa bất kỳ dòng nào — chỉ đổi import.

Cách dùng trong source.py:
    # Thay dòng cũ:
    # from write_plc_thread_V2 import PLCWrite

    # Bằng:
    from write_plc_opcua import PLCWriteOPCUA as PLCWrite

    worker = PLCWrite(
        endpoint = "opc.tcp://172.16.100.100:4840",
        node_map = {
            "P1_Start_Heat":         'ns=3;s="DB100"."P1_Start_Heat"',
            "P1_TemperatureSetting": 'ns=3;s="DB100"."P1_TemperatureSetting"',
            ...
        },
        write_ms = 300,
        username = "",
        password = "",
        logger   = self.logger
    )

Lưu ý quan trọng về get_item():
    Phiên bản OPC UA không dùng struct.pack hay Area.DB.
    get_item() trả về dict đơn giản hơn:
        {"tag_name": "P1_TemperatureSetting", "value": 85.5}
    write_multi nhận list[dict] này và ghi tuần tự.
    source.py cần cập nhật cách gọi get_item() nếu dùng write_multi.
    (Xem chi tiết ở phần get_item() bên dưới)

Các cải tiến giống write_plc_thread_V2.py mới:
    1. Heartbeat khi queue rỗng
    2. Retry item khi reconnect (tối đa MAX_RETRY_COUNT lần)
    3. Dedup trong queue cho write_bool và write_value
"""

import asyncio
import time
import logging
import threading

from typing import Any, Optional

from PySide6.QtCore import QObject, Signal, Slot, QThread, Qt


# ─── Hằng số ────────────────────────────────────────────────────────────────

RETRY_DELAY_SEC     = 3.0
HEARTBEAT_INTERVAL  = 5.0    # giây — probe khi queue rỗng
LOG_THROTTLE_SEC    = 5.0
MAX_RETRY_COUNT     = 3


# ─── PLCWriteOPCUA ───────────────────────────────────────────────────────────

class PLCWriteOPCUA(QObject):
    """
    Ghi dữ liệu xuống OPC UA Server (thường là PLC Siemens S7-1200/1500).

    Signal interface giống hệt PLCWrite trong write_plc_thread_V2.py:
        write_bool       = Signal(str, bool)
        write_value      = Signal(str, object)
        write_multi      = Signal(object, str)
        write_full_db    = Signal(object)
        write_multi_done = Signal(str, bool)
        connected        = Signal(bool)
        error            = Signal(str)
        finished         = Signal()
    """

    # ── Signals nhận lệnh từ UI ──────────────────────────────────────────────
    write_bool      = Signal(str, bool)     # (tag_name, value)
    write_value     = Signal(str, object)   # (tag_name, value)
    write_multi     = Signal(object, str)   # (list[{"tag_name":..,"value":..}], group)
    write_full_db   = Signal(object)        # dict{tag_name: value}

    # ── Signals phản hồi lên UI ──────────────────────────────────────────────
    write_bool_done     = Signal()
    write_value_done    = Signal()
    write_multi_done    = Signal(str, bool)   # (group_name, success)
    write_full_db_done  = Signal()

    error        = Signal(str)
    connected    = Signal(bool)
    disconnected = Signal()
    finished     = Signal()

    _stop_signal = Signal()

    # ────────────────────────────────────────────────────────────────────────

    def __init__(
        self,
        endpoint:        str,
        node_map:        dict[str, str],
        write_ms:        int  = 300,
        retry_ms:        int  = 3000,
        username:        str  = "",
        password:        str  = "",
        security_string: str  = "",
        logger:          Optional[logging.Logger] = None,
        parent:          Optional[QObject] = None,
    ):
        """
        Args:
            endpoint:        URL OPC UA, ví dụ "opc.tcp://172.16.100.100:4840"
            node_map:        dict{tag_name → NodeId string}
            write_ms:        chu kỳ drain queue (ms)
            retry_ms:        chu kỳ thử kết nối lại (ms) — giữ tương thích interface
            username:        OPC UA username (để trống nếu không bật auth)
            password:        OPC UA password
            security_string: để trống nếu không bật security
            logger:          logging.Logger
        """
        super().__init__(parent)
        self._endpoint        = endpoint
        self._node_map        = node_map
        self._write_ms        = write_ms
        self._retry_ms        = retry_ms
        self._username        = username
        self._password        = password
        self._security_string = security_string
        self.logger           = logger

        self._running  = False
        self._loop:    Optional[asyncio.AbstractEventLoop] = None
        self._client   = None          # asyncua.Client — chỉ dùng trong asyncio thread
        self._nodes:   dict = {}       # {tag_name: Node} — cache sau khi resolve

        # Queue giao tiếp giữa Qt thread (enqueue) và asyncio thread (drain)
        # Dùng asyncio.Queue vì _drain chạy trong asyncio loop
        self._async_queue: Optional[asyncio.Queue] = None

        # Retry state
        self._current_item:          tuple | None = None
        self._current_item_retries:  int = 0

        # Heartbeat
        self._last_heartbeat:  float = 0.0
        self._last_error_log:  float = 0.0

        # Lock cho queue (cần vì enqueue từ Qt thread, drain từ asyncio thread)
        self._queue_lock = threading.Lock()
        self._pending:   list[tuple] = []   # buffer tạm, drain vào async_queue

    # ── Lifecycle ────────────────────────────────────────────────────────────

    @Slot()
    def run(self):
        """Gọi từ QThread.started."""
        self._running = True
        if self.logger:
            self.logger.info("[OPC UA WRITE]: Worker started — endpoint: %s", self._endpoint)

        # Kết nối Signal ghi → enqueue (từ Qt main thread)
        self.write_bool.connect(self._enqueue_bool,     Qt.ConnectionType.QueuedConnection)
        self.write_value.connect(self._enqueue_value,   Qt.ConnectionType.QueuedConnection)
        self.write_multi.connect(self._enqueue_multi,   Qt.ConnectionType.QueuedConnection)
        self.write_full_db.connect(self._enqueue_full_db, Qt.ConnectionType.QueuedConnection)
        self._stop_signal.connect(self._on_stop,        Qt.ConnectionType.QueuedConnection)

        # Khởi động asyncio loop trong QThread hiện tại
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        self._async_queue = asyncio.Queue()

        try:
            self._loop.run_until_complete(self._supervisor())
        except Exception as exc:
            if self.logger:
                self.logger.error("[OPC UA WRITE]: Event loop crashed: %s", exc)
        finally:
            try:
                self._loop.close()
            except Exception:
                pass
            self.finished.emit()
            QThread.currentThread().quit()

    def stop(self):
        self._running = False
        self._stop_signal.emit()

    @Slot()
    def _on_stop(self):
        if self._loop and not self._loop.is_closed():
            self._loop.call_soon_threadsafe(self._loop.stop)

    # ── Supervisor: reconnect tự động ────────────────────────────────────────

    async def _supervisor(self):
        while self._running:
            try:
                await self._session()
            except asyncio.CancelledError:
                break
            except Exception as exc:
                now = time.time()
                if now - self._last_error_log >= LOG_THROTTLE_SEC:
                    if self.logger:
                        self.logger.error("[OPC UA WRITE]: Session error: %s", exc)
                    self.error.emit(str(exc))
                    self._last_error_log = now
                self.connected.emit(False)
                self._client = None
                self._nodes  = {}

                # ── Retry item sau reconnect ─────────────────────────────────
                if self._current_item is not None:
                    if self._current_item_retries < MAX_RETRY_COUNT:
                        if self.logger:
                            self.logger.info(
                                "[OPC UA WRITE]: Sẽ retry item sau reconnect (lần %d/%d)",
                                self._current_item_retries + 1, MAX_RETRY_COUNT
                            )
                    else:
                        if self.logger:
                            self.logger.warning(
                                "[OPC UA WRITE]: Dropped item sau %d lần retry thất bại",
                                MAX_RETRY_COUNT
                            )
                        self._current_item = None
                        self._current_item_retries = 0

                if self._running:
                    await asyncio.sleep(RETRY_DELAY_SEC)

    # ── Session: 1 vòng kết nối → ghi dữ liệu ───────────────────────────────

    async def _session(self):
        try:
            from asyncua import Client
        except ImportError:
            raise RuntimeError(
                "Thư viện 'asyncua' chưa được cài đặt. "
                "Chạy: pip install asyncua"
            )

        client = Client(url=self._endpoint, timeout=10)

        if self._username:
            client.set_user(self._username)
            client.set_password(self._password)

        if self._security_string:
            await client.set_security_string(self._security_string)

        async with client:
            self._client = client
            if self.logger:
                self.logger.info("[OPC UA WRITE]: Connected to %s", self._endpoint)
            self.connected.emit(True)

            # Resolve nodes 1 lần, cache lại
            self._nodes = await self._resolve_nodes(client)

            # Đưa retry item vào đầu queue nếu có
            if self._current_item is not None:
                await self._async_queue.put(self._current_item)

            # Vòng lặp chính: drain queue + heartbeat
            await self._run_loop()

    async def _resolve_nodes(self, client) -> dict:
        """Chuyển NodeId string → Node object, cache lại để ghi nhanh."""
        nodes = {}
        for tag_name, node_id_str in self._node_map.items():
            try:
                node = client.get_node(node_id_str)
                # Đọc thử để xác nhận node tồn tại và writable
                await node.read_value()
                nodes[tag_name] = node
            except Exception as exc:
                if self.logger:
                    self.logger.warning(
                        "[OPC UA WRITE]: Node không resolve được — tag=%s (%s)",
                        tag_name, exc
                    )
        if self.logger:
            self.logger.info(
                "[OPC UA WRITE]: Resolved %d/%d nodes",
                len(nodes), len(self._node_map)
            )
        return nodes

    # ── Vòng lặp chính ───────────────────────────────────────────────────────

    async def _run_loop(self):
        """
        Drain queue theo chu kỳ write_ms.
        Nếu queue rỗng → heartbeat probe.
        """
        interval = self._write_ms / 1000.0

        # Flush pending items từ Qt thread vào async queue trước
        self._flush_pending_to_async_queue()

        while self._running:
            t0 = time.perf_counter()

            # Đẩy các item mới từ pending buffer (do Qt thread enqueue) vào async queue
            self._flush_pending_to_async_queue()

            try:
                item = self._async_queue.get_nowait()
                self._current_item = item
                await self._dispatch(item)
            except asyncio.QueueEmpty:
                # Queue rỗng → heartbeat
                await self._heartbeat()

            elapsed = time.perf_counter() - t0
            await asyncio.sleep(max(0.0, interval - elapsed))

    def _flush_pending_to_async_queue(self):
        """
        Chuyển items từ _pending (Qt thread đã enqueue)
        sang _async_queue (asyncio thread xử lý).
        Thread-safe qua _queue_lock.
        """
        with self._queue_lock:
            batch = list(self._pending)
            self._pending.clear()
        for item in batch:
            if self._async_queue:
                try:
                    self._async_queue.put_nowait(item)
                except asyncio.QueueFull:
                    pass

    async def _heartbeat(self):
        """
        Đọc 1 node bất kỳ để xác nhận kết nối còn sống.
        Nếu thất bại → raise exception → supervisor reconnect.
        """
        now = time.time()
        if now - self._last_heartbeat < HEARTBEAT_INTERVAL:
            return
        if not self._nodes:
            return
        probe_node = next(iter(self._nodes.values()))
        try:
            await probe_node.read_value()
            self._last_heartbeat = now
        except Exception as exc:
            if self.logger:
                self.logger.warning("[OPC UA WRITE]: Heartbeat failed: %s", exc)
            raise exc   # bubble lên → supervisor reconnect

    # ── Dispatch ─────────────────────────────────────────────────────────────

    async def _dispatch(self, item: tuple):
        cmd_type = item[0]
        try:
            if cmd_type == "bool":
                _, name, value = item
                await self._write_single(name, bool(value))
                if self.logger:
                    self.logger.info("[OPC UA WRITE]: BOOL OK → %s = %s", name, value)

            elif cmd_type == "value":
                _, name, value = item
                await self._write_single(name, value)
                if self.logger:
                    self.logger.info("[OPC UA WRITE]: Value OK → %s = %s", name, value)

            elif cmd_type == "multi":
                _, items, group = item
                await self._write_multi_items(items, group)

            elif cmd_type == "full_db":
                _, data = item
                await self._write_full_db_data(data)

            # Ghi thành công → xóa retry state
            self._current_item = None
            self._current_item_retries = 0

        except Exception as exc:
            self._current_item_retries += 1
            if self.logger:
                self.logger.error(
                    "[OPC UA WRITE]: Ghi thất bại [%s] lần %d: %s",
                    cmd_type, self._current_item_retries, exc
                )
            self.error.emit(str(exc))
            raise exc   # bubble lên → supervisor reconnect + retry

    # ── Ghi thực tế ──────────────────────────────────────────────────────────

    async def _write_single(self, tag_name: str, value: Any):
        """Ghi 1 tag đơn lẻ."""
        node = self._nodes.get(tag_name)
        if node is None:
            if self.logger:
                self.logger.warning("[OPC UA WRITE]: Tag không có trong node cache: %s", tag_name)
            return
        from asyncua import ua
        # OPC UA tự xác định kiểu dữ liệu qua variant — không cần struct.pack
        dv = await node.read_data_value()
        variant_type = dv.Value.VariantType
        typed_value = self._cast_value(value, variant_type)
        await node.write_value(ua.DataValue(ua.Variant(typed_value, variant_type)))

    async def _write_multi_items(self, items: list, group: str):
        """
        Ghi nhiều tag cùng lúc.
        items = [{"tag_name": "P1_Temp", "value": 85.5}, ...]
        — format đơn giản hơn S7comm, không cần Area.DB hay struct.pack
        """
        errors = []
        for item in items:
            tag_name = item.get("tag_name", "")
            value    = item.get("value")
            try:
                await self._write_single(tag_name, value)
            except Exception as exc:
                errors.append(f"{tag_name}: {exc}")

        if errors:
            err_msg = "; ".join(errors)
            self.error.emit(f"write_multi partial error: {err_msg}")
            self.write_multi_done.emit(group, False)
            if self.logger:
                self.logger.error("[OPC UA WRITE]: write_multi lỗi: %s", err_msg)
        else:
            self.write_multi_done.emit(group, True)
            if self.logger:
                self.logger.info(
                    "[OPC UA WRITE]: write_multi OK — %d tags | group=%s",
                    len(items), group
                )

    async def _write_full_db_data(self, data: dict):
        """
        Ghi toàn bộ dict{tag_name: value} — tương đương write_full_db của S7comm.
        """
        errors = []
        for tag_name, value in data.items():
            try:
                await self._write_single(tag_name, value)
            except Exception as exc:
                errors.append(f"{tag_name}: {exc}")

        if errors:
            self.error.emit(f"write_full_db errors: {'; '.join(errors)}")
            if self.logger:
                self.logger.error("[OPC UA WRITE]: write_full_db partial errors: %s", errors)
        else:
            self.write_full_db_done.emit()
            if self.logger:
                self.logger.info("[OPC UA WRITE]: write_full_db OK — %d tags", len(data))

    # ── Cast giá trị cho đúng kiểu OPC UA ────────────────────────────────────

    @staticmethod
    def _cast_value(value: Any, variant_type) -> Any:
        """
        OPC UA yêu cầu giá trị phải đúng kiểu với VariantType của node.
        Hàm này tự động cast để tránh lỗi "type mismatch".
        """
        try:
            from asyncua import ua
            vt = ua.VariantType
            mapping = {
                vt.Boolean: bool,
                vt.Float:   float,
                vt.Double:  float,
                vt.Int16:   int,
                vt.Int32:   int,
                vt.Int64:   int,
                vt.UInt16:  int,
                vt.UInt32:  int,
                vt.UInt64:  int,
                vt.String:  str,
            }
            cast_fn = mapping.get(variant_type)
            return cast_fn(value) if cast_fn else value
        except Exception:
            return value

    # ── Enqueue (từ Qt main thread → thread-safe) ─────────────────────────────

    @Slot(str, bool)
    def _enqueue_bool(self, name: str, value: bool):
        self._enqueue_dedup(("bool", name, value), key=f"bool:{name}")

    @Slot(str, object)
    def _enqueue_value(self, name: str, value: object):
        self._enqueue_dedup(("value", name, value), key=f"value:{name}")

    @Slot(object, str)
    def _enqueue_multi(self, items: object, group: str = ""):
        # multi không dedup — mỗi batch là 1 lần import riêng
        with self._queue_lock:
            self._pending.append(("multi", items, group))
        if self.logger:
            self.logger.info(
                "[OPC UA WRITE]: MULTI enqueued — %d items | group=%s",
                len(items), group
            )

    @Slot(object)
    def _enqueue_full_db(self, data: object):
        with self._queue_lock:
            self._pending.append(("full_db", data))
        if self.logger:
            self.logger.info("[OPC UA WRITE]: Full DB enqueued — %d tags", len(data))

    def _enqueue_dedup(self, item: tuple, key: str):
        """
        Nếu đã có item cùng key trong pending → thay giá trị mới nhất.
        Tránh gửi hàng loạt giá trị trung gian khi người dùng kéo spinbox.
        """
        with self._queue_lock:
            for i, existing in enumerate(self._pending):
                existing_key = f"{existing[0]}:{existing[1]}" if len(existing) > 1 else ""
                if existing_key == key:
                    self._pending[i] = item
                    return
            self._pending.append(item)

    # ── get_item() — tương thích với source.py ────────────────────────────────

    def get_item(self, tag_name: str, value: Any) -> dict:
        """
        Tạo item cho write_multi — format OPC UA đơn giản hơn S7comm.

        So sánh:
            S7comm: {"area": Area.DB, "db_number": 100, "start": 10, "data": b"..."}
            OPC UA: {"tag_name": "P1_TemperatureSetting", "value": 85.5}

        Cách dùng trong source.py (không đổi cách gọi):
            items = [
                self.plc_writer_worker.get_item("P1_TemperatureSetting", 85.5),
                self.plc_writer_worker.get_item("P1_PressureSetting", 8.0),
            ]
            self.plc_writer_worker.write_multi.emit(items, "A")
        """
        if tag_name not in self._node_map:
            raise ValueError(f"Tag không có trong node_map: {tag_name}")
        return {"tag_name": tag_name, "value": value}