import asyncio
import time
import logging
import threading
from typing import Any, Optional, Dict
import snap7
from snap7.error import S7Error
from snap7.type import Parameter
from snap7.util import get_bool, get_real, get_dint, get_int, get_string
from PySide6.QtCore import QObject, Signal

class PLCAreaRead(QObject):

    data_ready = Signal(dict)   # (area_name, data_dict)
    error      = Signal(str, str)    # (area_name, error_msg)
    connected  = Signal(str, bool)   # (area_name, status)

    def __init__(self, 
                 area_name: str,
                 start_offset: int,
                 read_size: int,
                 db_layout: list,
                 ip: str = "172.16.100.100",
                 rack: int = 0,
                 slot: int = 1,
                 db_number: int = 1,
                 poll_ms: int = 500,
                 logger=None,
                 parent=None):
        
        super().__init__(parent)
        self.area_name = area_name
        self.start_offset = start_offset
        self.read_size = read_size
        self.db_layout = db_layout
        self._ip = ip
        self._rack = rack
        self._slot = slot
        self._db_number = db_number
        self._poll_ms = poll_ms
        self.logger = logger

        self._client: snap7.client.Client | None = None
        self._running = False
        self._task: asyncio.Task | None = None

    async def _connect(self):
        try:
            c = snap7.client.Client()
            c.set_param(Parameter.PDURequest, 1024)
            c.set_param(Parameter.SendTimeout, 5)
            c.set_param(Parameter.RecvTimeout, 5)
            c.set_param(Parameter.KeepAliveTime, 15)
            c.connect(self._ip, self._rack, self._slot)
            self._client = c
            self.connected.emit(self.area_name, True)
            if self.logger:
                self.logger.info(f"[PLC {self.area_name}]: Connected")
            return True
        except Exception as e:
            self.error.emit(self.area_name, f"Connect failed: {e}")
            return False

    async def _read_loop(self):
        while self._running:
            try:
                if not self._client:
                    await asyncio.sleep(1)
                    continue

                raw = self._client.db_read(self._db_number, self.start_offset, self.read_size)
                data = self._parse(raw, self.start_offset)
                self.data_ready.emit(self.area_name, data)

            except Exception as e:
                self.error.emit(self.area_name, str(e))
                await asyncio.sleep(2)
                if self._client:
                    try:
                        self._client.disconnect()
                    except:
                        pass
                    self._client = None

            await asyncio.sleep(self._poll_ms / 1000)

    def _parse(self, raw: bytearray, base_offset: int) -> dict:
        result: Dict[str, Any] = {}
        raw_len = len(raw)

        for name, dtype, offset, bit in self.db_layout:
            rel = offset - base_offset
            if rel < 0 or rel >= raw_len:
                result[name] = None
                continue
            try:
                if dtype == "BOOL":
                    result[name] = get_bool(raw, rel, bit)
                elif dtype == "REAL":
                    result[name] = get_real(raw, rel)
                elif dtype == "DINT":
                    result[name] = get_dint(raw, rel)
                elif dtype == "INT":
                    result[name] = get_int(raw, rel)
                elif dtype == "STRING":
                    result[name] = get_string(raw, rel)
                else:
                    result[name] = None
            except:
                result[name] = None
        return result

    def start(self):
        self._running = True
        self._task = asyncio.create_task(self._read_loop())

    def stop(self):
        self._running = False
        if self._task:
            self._task.cancel()
        if self._client:
            try:
                self._client.disconnect()
            except:
                pass

class PLCRead(QObject):

    area_1_ready = Signal(dict)
    area_2_ready = Signal(dict)
    area_3_ready = Signal(dict)

    def __init__(self, full_db_layout: list, ip: str = "172.16.100.100", logger=None, parent=None):
        super().__init__(parent)
        self.logger = logger

        self.a1 = PLCAreaRead("A1_0-194",     0, 195, ip=ip, db_layout = full_db_layout, poll_ms=200, logger=logger, parent=self)
        self.a2 = PLCAreaRead("A2_198-332", 198, 135, ip=ip, db_layout = full_db_layout, poll_ms=100, logger=logger, parent=self)
        self.a3 = PLCAreaRead("A3_336-end", 336, 256, ip=ip, db_layout = full_db_layout, poll_ms=500, logger=logger, parent=self)

        self.a1.data_ready.connect(self.area_1_ready)
        self.a2.data_ready.connect(self.area_2_ready)
        self.a3.data_ready.connect(self.area_3_ready)

    def start(self):
        self.a1.start()
        self.a2.start()
        self.a3.start()

    def stop(self):
        self.a1.stop()
        self.a2.stop()
        self.a3.stop()