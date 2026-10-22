import sys
import os
import struct
import time
import socket
import logging
import logging.handlers
import threading
import snap7
from datetime import datetime
from typing import Any, Optional
from snap7.error import * # type: ignore
from snap7.type import * # type: ignore
from snap7.type import Parameter
from snap7.util import get_bool, get_real, get_dint, get_int, get_string
from PySide6.QtCore import QObject, QTimer, Signal, Slot, QThread, Qt
from LogFileHandler import MonthlyRotatingFileHandler

class PLCRead(QObject):
    """
    Object dùng để lấy dữ liệu từ PLC
    \n
    Có thể tạo nhiều Object để xử lí nhiều vùng dữ liệu hoặc từ nhiều PLC
    \n
    Nếu chỉ định đọc 1 vùng riêng biệt thì lên cấu hình db_layout riêng
    """
    init_data    = Signal()
    data_ready   = Signal(dict)
    data_ready_ts = Signal(dict, float)   # data, time.time() lúc bắt đầu đọc
    error        = Signal(str)
    connected    = Signal(bool)
    disconnected = Signal()
    finished     = Signal()
    elapsed_time = Signal(float)

    _stop_read   = Signal()

    def __init__(
        self,
        name_module: str                                        = "No 1.",
        ip:        str                                          = "172.16.100.100",
        rack:      int                                          = 0,
        slot:      int                                          = 1,
        db_number: int                                          = 1,
        db_layout: Optional[list[tuple[str, str, int, Any]]]   = None,
        db_size:   int                                          = 592,
        offsets:   int                                          = 198,
        poll_ms:   int                                          = 500,
        retry_ms:  int                                          = 3000,
        logger_parent                                           = None,
        parent:    Optional[QObject]                            = None,
    ):
        super().__init__(parent)
        self._name_module = name_module
        self._ip        = ip
        self._rack      = rack
        self._slot      = slot
        self._db_number = db_number
        self._db_layout = db_layout
        self._db_size   = db_size
        self._poll_ms   = poll_ms
        self._offsets   = offsets
        self._retry_ms  = retry_ms
        self.logger     = None
        self.folder     = logger_parent

        self._client:      snap7.client.Client | None = None
        self._poll_timer:  QTimer | None = None
        self._retry_timer: QTimer | None = None
        self._running   = False

        self._last_error_log_time: float = 0.0

    def _init_logger(self):
        if not self.folder:
            self.logger = None
            return

        logger_name = f"{__name__}.{self._name_module}"
        self.logger = logging.getLogger(logger_name)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        log_dir = self.folder / "PLC Log" / f"{self._name_module}_LOG"
        os.makedirs(log_dir, exist_ok=True)

        file_handler = MonthlyRotatingFileHandler(
            base_log_dir=log_dir,
            prefix=f"PLC_READ_{self._name_module}",
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

    @Slot()
    def run(self):
        self._running = True
        self._init_logger()
        if self.logger:
            self.logger.info(f"[PLC READ {self._name_module}]: PLC Read {self._name_module} init")

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

    @Slot(int)
    def set_interval(self, interval: int):
        if self._poll_timer:
            self._poll_timer.setInterval(interval)  # type: ignore

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
            self.init_data.emit()
            if self._poll_timer and not self._poll_timer.isActive():
                self._poll_timer.start()
            if self.logger:
                self.logger.info(f"[PLC READ {self._name_module}]: Connected to PLC, started reading {self._name_module} - {self._db_size} bytes every {self._poll_ms} ms")
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

                c.set_param(Parameter.PDURequest,    960)  # max PDU size
                c.set_param(Parameter.SendTimeout,     3) 
                c.set_param(Parameter.RecvTimeout,     2)
                c.set_param(Parameter.PingTimeout,     2)
                c.set_param(Parameter.KeepAliveTime,  10)

                c.connect(self._ip, self._rack, self._slot)
                result["client"] = c                # type: ignore
            except Exception as exc:
                result["error"] = exc               # type: ignore
                self.error.emit(str(result["error"]))
                self.connected.emit(False)
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
            # if now - self._last_error_log_time >= 5:
            #     if self.logger:
            #         self.logger.error(f"[PLC READ {self._name_module}]: %s", msg)
            #     self._last_error_log_time = now
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
        self._init_reads_left = 0
        self.connected.emit(False)

    @Slot()
    def _poll(self):
        if not self._running or not self._client or not self._client.get_connected():
            self._reconnect()
            return

        try:
            t_read = time.time()
            t0 = time.perf_counter()
            raw       = self._client.db_read(self._db_number, self._offsets, self._db_size)
            elapsed_ms = (time.perf_counter() - t0) * 1000
            
            if self.logger:
                # respond = "Response"
                if elapsed_ms > (self._poll_ms * 1.3):
                    respond = "Slow response"
                    self.logger.warning(
                        f"[PLC READ {self._name_module}]: {respond} %.1fms (size=%d)",
                        elapsed_ms, len(raw),
                    )
            result = self._parse(raw, base_offset=self._offsets)
            self.data_ready.emit(result)
            self.data_ready_ts.emit(result, t_read)
            self.elapsed_time.emit(elapsed_ms)

        except S7Error as exc:
            if self.logger:
                self.logger.warning(f"[PLC READ {self._name_module}]: Read error: %s", exc)
            self.error.emit(f"Read error: {exc}")
            self._reconnect()
        except Exception as exc:
            if self.logger:
                self.logger.error(f"[PLC READ {self._name_module}]: Unexpected error: %s", exc)
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

    def _parse(self, raw: bytearray, base_offset: int = 0, layout: Optional[list] = None) -> dict:
        layout = self._db_layout if layout is None else layout
        if not layout:
            return {}

        result:  dict[str, Any] = {}
        raw_len = len(raw)

        for name, dtype, offset, bit in layout:
            rel_offset = offset - base_offset

            if rel_offset < 0 or rel_offset >= raw_len:
                # result[name] = None
                continue

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
                # if self.logger:
                #     self.logger.error(
                #         f"[PLC READ {self._name_module}]: Parse error [%s] offset=%d: %s",
                #         name, offset, exc,
                #     )

        return result


class PLCReadBlock(PLCRead):
    """
    Đọc nhiều vùng DB nằm liền nhau (INPUT / ACTUAL / ERROR) bằng 1 kết nối.
    \n regions: [(name, offset, size, read_ms), ...]
    \n - Sau khi kết nối, các vùng liền nhau được gom thành nhóm sao cho mỗi nhóm vừa
    1 request theo PDU đã thoả thuận (PDU - 18 byte). VD PDU 240 -> tối đa 222 byte/request:
    INPUT (198) | ACTUAL + ERROR (138 + 52 = 190). PDU 960 -> 1 nhóm duy nhất.
    \n - Mỗi nhóm đọc theo read_ms nhỏ nhất của các vùng trong nhóm; vùng "đi ké" trong nhóm
    được đọc thêm mà không tốn request.
    \n - Mỗi vùng được emit khi dữ liệu thay đổi, hoặc quá read_ms (heartbeat), hoặc lần đọc
    đầu tiên sau khi kết nối.
    """
    region_ready = Signal(str, dict, float)   # region name, data, time.time() lúc bắt đầu đọc

    _READ_OVERHEAD = 18   # S7 header 12 + param 2 + data item header 4

    def __init__(
        self,
        regions:          list[tuple[str, int, int, int]],
        name_module:      str                                       = "PLC",
        ip:               str                                       = "172.16.100.100",
        rack:             int                                       = 0,
        slot:             int                                       = 1,
        db_number:        int                                       = 1,
        db_layout:        Optional[list[tuple[str, str, int, Any]]] = None,
        string_max_chars: int                                       = 254,
        retry_ms:         int                                       = 3000,
        logger_parent                                               = None,
        parent:           Optional[QObject]                         = None,
    ):
        regions = sorted(regions, key=lambda r: r[1])
        super().__init__(
            name_module=name_module, ip=ip, rack=rack, slot=slot,
            db_number=db_number, db_layout=db_layout,
            db_size=0, offsets=regions[0][1],
            poll_ms=min(r[3] for r in regions), retry_ms=retry_ms,
            logger_parent=logger_parent, parent=parent,
        )

        # Mỗi vùng: dict(name, start, end, cfg_end, read_s, layout)
        self._regions: list[dict] = []
        for i, (name, off, size, read_ms) in enumerate(regions):
            cfg_end = off + size
            end = cfg_end
            # cộng offset 2 byte cho string
            for _, dtype, t_off, _ in (db_layout or []):
                if str(dtype).upper() == "STRING" and off <= t_off < cfg_end:
                    end = max(end, t_off + 2 + string_max_chars)
            if i + 1 < len(regions):
                end = min(end, regions[i + 1][1])   # không lấn sang vùng kế tiếp
            self._regions.append({
                "name": name, "start": off, "end": end, "cfg_end": cfg_end,
                "read_s": read_ms / 1000,
                "layout": [t for t in (db_layout or []) if off <= t[2] < end],
            })

        self._groups:    list[dict]       = []
        self._last_raw:  dict[str, bytes] = {}
        self._last_emit: dict[str, float] = {}
        self.init_data.connect(self._on_connected)

    @Slot()
    def _on_connected(self):
        """Lập nhóm theo PDU và emit lại toàn bộ vùng ở lần đọc đầu"""
        self._last_raw.clear()
        self._last_emit.clear()
        pdu = self._client.get_pdu_length() if self._client else 240  # type: ignore
        self._plan_groups(max(32, pdu - self._READ_OVERHEAD))
        if self.logger:
            plan = " | ".join(
                f"[{g['start']}..{g['end']}) {'+'.join(r['name'] for r in g['regions'])} {int(g['read_s'] * 1000)}ms"
                for g in self._groups
            )
            self.logger.info(f"[PLC READ {self._name_module}]: PDU=%d -> %s", pdu, plan)

    def _plan_groups(self, max_payload: int):
        """Gom các vùng liền nhau (theo thứ tự offset) vào nhóm và <= max_payload byte"""
        self._groups = []
        for r in self._regions:
            g = self._groups[-1] if self._groups else None
            if g and g["end"] == r["start"] and r["end"] - g["start"] <= max_payload:
                g["end"] = r["end"]
                g["regions"].append(r)
                g["read_s"] = min(g["read_s"], r["read_s"])
            else:
                self._groups.append({"start": r["start"], "end": r["end"], "regions": [r],
                                     "read_s": r["read_s"], "last_read": 0.0})

    @Slot()
    def _poll(self):
        if not self._running or not self._client or not self._client.get_connected():
            self._reconnect()
            return

        try:
            now = time.monotonic()
            max_ms = 0.0  
            for g in self._groups:
                # -0.02s: bù sai số QTimer 
                if now - g["last_read"] < g["read_s"] - 0.02:
                    continue
                g["last_read"] = now
                max_ms = max(max_ms, self._read_group(g, now))
            if max_ms:
                self.elapsed_time.emit(max_ms)

        except S7Error as exc:
            if self.logger:
                self.logger.warning(f"[PLC READ {self._name_module}]: Read error: %s", exc)
            self.error.emit(f"Read error: {exc}")
            self._reconnect()
        except Exception as exc:
            if self.logger:
                self.logger.error(f"[PLC READ {self._name_module}]: Unexpected error: %s", exc)
            self.error.emit(str(exc))
            self._reconnect()

    def _read_group(self, g: dict, now: float) -> float:
        t_read = time.time()
        t0     = time.perf_counter()
        try:
            raw = self._client.db_read(self._db_number, g["start"], g["end"] - g["start"])  # type: ignore
        except S7ProtocolError as exc:
            last = g["regions"][-1]
            protocol_error = not isinstance(exc, (S7PacketLostError, S7StalePacketError))
            if not (protocol_error and self._client and self._client.get_connected()
                    and last["end"] > last["cfg_end"]):
                raise
            if self.logger:
                self.logger.warning(
                    f"[PLC READ {self._name_module}]: Read [%d..%d) failed (%s) — fallback to %d",
                    g["start"], g["end"], exc, last["cfg_end"],
                )
            last["end"] = g["end"] = last["cfg_end"]
            last["layout"] = [t for t in last["layout"] if t[2] < last["cfg_end"]]
            raw = self._client.db_read(self._db_number, g["start"], g["end"] - g["start"])  # type: ignore
        elapsed_ms = (time.perf_counter() - t0) * 1000

        if self.logger and elapsed_ms > (g["read_s"] * 1000 * 1.3):
            self.logger.warning(
                f"[PLC READ {self._name_module}]: Slow response %.1fms (size=%d)", elapsed_ms, len(raw),
            )

        for r in g["regions"]:
            chunk   = bytes(raw[r["start"] - g["start"]:r["end"] - g["start"]])
            changed = self._last_raw.get(r["name"]) != chunk
            due     = now - self._last_emit.get(r["name"], 0.0) >= r["read_s"] - 0.02
            if not (changed or due):
                continue
            self._last_raw[r["name"]]  = chunk
            self._last_emit[r["name"]] = now
            self.region_ready.emit(r["name"], self._parse(raw, base_offset=g["start"], layout=r["layout"]), t_read)
        return elapsed_ms
