import sys
import os
import struct
import time
import socket
import logging
import logging.handlers
import threading
import snap7
from typing import Any, Optional
from snap7.error import * # type: ignore
from snap7.type import * # type: ignore
from snap7.type import Parameter
from snap7.util import get_bool, get_real, get_dint, get_int, get_string
from PySide6.QtCore import QObject, QTimer, Signal, Slot, QThread, Qt

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

        self.logger = logging.getLogger(__name__)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        # Tạo thư mục log nếu chưa có
        log_dir = self.folder / "PLC Log"
        os.makedirs(log_dir, exist_ok=True)
        log_date = datetime.now().strftime("%d_%m_%Y")
        log_filename = os.path.join(log_dir, f'PLC_READ_{self._name_module}_{log_date}.log')

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
                    self.logger.error(f"[PLC READ {self._name_module}]: %s", msg)
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
        self._init_reads_left = 0
        self.connected.emit(False)

    @Slot()
    def _poll(self):
        if not self._running or not self._client or not self._client.get_connected():
            self._reconnect()
            return

        try:
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
            result    = self._parse(raw, base_offset=self._offsets)
            self.data_ready.emit(result)
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

    def _parse(self, raw: bytearray, base_offset: int = 0) -> dict:
        if not self._db_layout:
            return {}

        result:  dict[str, Any] = {}
        raw_len = len(raw)

        for name, dtype, offset, bit in self._db_layout:
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
                if self.logger:
                    self.logger.error(
                        f"[PLC READ {self._name_module}]: Parse error [%s] offset=%d: %s",
                        name, offset, exc,
                    )

        return result