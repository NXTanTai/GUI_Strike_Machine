"""
plc_worker.py  (PySide6)
─────────────────────────────────────────────────────────────
PLCWorker  – QObject designed to run inside a QThread.

Usage (main / UI thread):
    self.thread = QThread()
    self.worker = PLCWorker(ip="192.168.1.1", db_number=1)
    self.worker.moveToThread(self.thread)

    self.thread.started.connect(self.worker.run)
    self.worker.data_ready.connect(self.on_data_ready)
    self.worker.error.connect(self.on_error)
    self.worker.connected.connect(self.on_connected)
    self.worker.disconnected.connect(self.on_disconnected)

    self.thread.start()

    # Stop gracefully:
    self.worker.stop()
    self.thread.quit()
    self.thread.wait()
"""

import struct
import logging
from typing import Any

import snap7
from snap7.error import S7Error

from PySide6.QtCore import QObject, QTimer, Signal

logger = logging.getLogger(__name__)

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


# ─────────────────────────────────────────────────────────────
#  DB layout definition
#  Each entry: (name, type, byte_offset, bit_index_or_None)
# ─────────────────────────────────────────────────────────────

DB_LAYOUT: list[tuple[str, str, int, Any]] = [
    # ── Booleans  byte 0 ──────────────────────────────────────
    ("START",               "BOOL",   0,    0),
    ("STOP",                "BOOL",   0,    1),
    ("T0_Start_Heat",       "BOOL",   0,    2),
    ("T0_StopHeat",         "BOOL",   0,    3),
    ("P1_Start_Heat",       "BOOL",   0,    4),
    ("P1_Start_Pressure",   "BOOL",   0,    5),
    ("P1_Start_Oil",        "BOOL",   0,    6),
    ("P1_BitCountTimes",    "BOOL",   0,    7),
    # ── Booleans  byte 1 ──────────────────────────────────────
    ("P2_Start_Heat",       "BOOL",   1,    0),
    ("P2_Start_Pressure",   "BOOL",   1,    1),
    ("P2_Start_Oil",        "BOOL",   1,    2),
    ("P2_BitCountTimes",    "BOOL",   1,    3),
    ("P3_Start_Heat",       "BOOL",   1,    4),
    ("P3_Start_Pressure",   "BOOL",   1,    5),
    ("P3_Start_Oil",        "BOOL",   1,    6),
    ("P3_BitCountTimes",    "BOOL",   1,    7),
    # ── T0 Reals ──────────────────────────────────────────────
    ("T0_TemperatureSetting", "REAL",  2,   None),
    ("T0_TempLimitHIGH",      "REAL",  6,   None),
    ("T0_TempLimitLOW",       "REAL",  10,  None),
    ("T0_TempOffset",         "REAL",  14,  None),
    # ── P1 Settings ───────────────────────────────────────────
    ("P1_TemperatureSetting", "REAL",  18,  None),
    ("P1_TempLimitHIGH",      "REAL",  22,  None),
    ("P1_TempLimitLOW",       "REAL",  26,  None),
    ("P1_Temp1Offset",        "REAL",  30,  None),
    ("P1_Temp2Offset",        "REAL",  34,  None),
    ("P1_Temp3Offset",        "REAL",  38,  None),
    ("P1_PressureSetting",    "REAL",  42,  None),
    ("P1_PressureHoseOffset", "REAL",  46,  None),
    ("P1_PressureITVOffset",  "REAL",  50,  None),
    ("P1_Air_FillingTime",    "DINT",  54,  None),
    ("P1_Air_HoldingTime",    "DINT",  58,  None),
    ("P1_Air_ReleaseTime",    "DINT",  62,  None),
    ("P1_Oil_Start_Time",     "DINT",  66,  None),
    ("P1_Oil_End_Time",       "DINT",  70,  None),
    ("P1_CountTimes",         "INT",   74,  None),
    # ── P2 Settings ───────────────────────────────────────────
    ("P2_TemperatureSetting", "REAL",  76,  None),
    ("P2_TempLimitHIGH",      "REAL",  80,  None),
    ("P2_TempLimitLOW",       "REAL",  84,  None),
    ("P2_Temp1Offset",        "REAL",  88,  None),
    ("P2_Temp2Offset",        "REAL",  92,  None),
    ("P2_Temp3Offset",        "REAL",  96,  None),
    ("P2_PressureSetting",    "REAL",  100, None),
    ("P2_PressureHoseOffset", "REAL",  104, None),
    ("P2_PressureITVOffset",  "REAL",  108, None),
    ("P2_Air_FillingTime",    "DINT",  112, None),
    ("P2_Air_HoldingTime",    "DINT",  116, None),
    ("P2_Air_ReleaseTime",    "DINT",  120, None),
    ("P2_Oil_Start_Time",     "DINT",  124, None),
    ("P2_Oil_End_Time",       "DINT",  128, None),
    ("P2_CountTimes",         "INT",   132, None),
    # ── P3 Settings ───────────────────────────────────────────
    ("P3_TemperatureSetting", "REAL",  134, None),
    ("P3_TempLimitHIGH",      "REAL",  138, None),
    ("P3_TempLimitLOW",       "REAL",  142, None),
    ("P3_Temp1Offset",        "REAL",  146, None),
    ("P3_Temp2Offset",        "REAL",  150, None),
    ("P3_Temp3Offset",        "REAL",  154, None),
    ("P3_PressureSetting",    "REAL",  158, None),
    ("P3_PressureHoseOffset", "REAL",  162, None),
    ("P3_PressureITVOffset",  "REAL",  166, None),
    ("P3_Air_FillingTime",    "DINT",  170, None),
    ("P3_Air_HoldingTime",    "DINT",  174, None),
    ("P3_Air_ReleaseTime",    "DINT",  178, None),
    ("P3_Oil_Start_Time",     "DINT",  182, None),
    ("P3_Oil_End_Time",       "DINT",  186, None),
    ("P3_CountTimes",         "INT",   190, None),
    # ── Alarm flag + T0 current ───────────────────────────────
    ("Bit_Alarm",             "BOOL",  192, 0),
    ("T0_Current_Temp",       "REAL",  194, None),
    # ── P1 Actuals ────────────────────────────────────────────
    ("P1_Current_Temp1",          "REAL",  198, None),
    ("P1_Current_Temp2",          "REAL",  202, None),
    ("P1_Current_Temp3",          "REAL",  206, None),
    ("P1_Current_PressureHose",   "REAL",  210, None),
    ("P1_Current_PressureITV",    "REAL",  214, None),
    ("P1_Air_FillingTime_Act",    "DINT",  218, None),
    ("P1_Air_HoldingTime_Act",    "DINT",  222, None),
    ("P1_Air_ReleaseTime_Act",    "DINT",  226, None),
    ("P1_Oil_Start_Time_Act",     "DINT",  230, None),
    ("P1_Oil_End_Time_Act",       "DINT",  234, None),
    ("P1_Number_Test_Times",      "INT",   238, None),
    # ── P2 Actuals ────────────────────────────────────────────
    ("P2_Current_Temp1",          "REAL",  240, None),
    ("P2_Current_Temp2",          "REAL",  244, None),
    ("P2_Current_Temp3",          "REAL",  248, None),
    ("P2_Current_PressureHose",   "REAL",  252, None),
    ("P2_Current_PressureITV",    "REAL",  256, None),
    ("P2_Air_FillingTime_Act",    "DINT",  260, None),
    ("P2_Air_HoldingTime_Act",    "DINT",  264, None),
    ("P2_Air_ReleaseTime_Act",    "DINT",  268, None),
    ("P2_Oil_Start_Time_Act",     "DINT",  272, None),
    ("P2_Oil_End_Time_Act",       "DINT",  276, None),
    ("P2_Number_Test_Times",      "INT",   280, None),
    # ── P3 Actuals ────────────────────────────────────────────
    ("P3_Current_Temp1",          "REAL",  282, None),
    ("P3_Current_Temp2",          "REAL",  286, None),
    ("P3_Current_Temp3",          "REAL",  290, None),
    ("P3_Current_PressureHose",   "REAL",  294, None),
    ("P3_Current_PressureITV",    "REAL",  298, None),
    ("P3_Air_FillingTime_Act",    "DINT",  302, None),
    ("P3_Air_HoldingTime_Act",    "DINT",  306, None),
    ("P3_Air_ReleaseTime_Act",    "DINT",  310, None),
    ("P3_Oil_Start_Time_Act",     "DINT",  314, None),
    ("P3_Oil_End_Time_Act",       "DINT",  318, None),
    ("P3_Number_Test_Times",      "INT",   322, None),
    # ── Alarm string ──────────────────────────────────────────
    ("Alarm_Info",                "STRING", 324, None),
]

# Total bytes to read: String at 324 + 2-byte header + 254 max chars = 580
DB_TOTAL_BYTES = 580


# ─────────────────────────────────────────────────────────────
#  PLCWorker
# ─────────────────────────────────────────────────────────────

class PLCWorker(QObject):
    """
    Reads a Siemens S7 DB block periodically and emits parsed data.

    Signals
    -------
    data_ready(dict)   – emitted every poll cycle with full tag dict
    error(str)         – emitted on connection / read error
    connected()        – emitted once the PLC connection is established
    disconnected()     – emitted when the connection is lost or stopped
    """

    data_ready   = Signal(dict)
    error        = Signal(str)
    connected    = Signal()
    disconnected = Signal()

    def __init__(
        self,
        ip: str         = "192.168.1.1",
        rack: int       = 0,
        slot: int       = 1,
        db_number: int  = 1,
        poll_ms: int    = 500,       # polling interval in milliseconds
        parent: QObject = None,
    ):
        super().__init__(parent)
        self._ip         = ip
        self._rack       = rack
        self._slot       = slot
        self._db_number  = db_number
        self._poll_ms    = poll_ms

        self._client: snap7.client.Client | None = None
        self._timer:  QTimer | None = None
        self._running = False

    # ── Public API (call from any thread via Qt signals or direct) ──

    def run(self):
        """Entry point – connect to thread.started signal."""
        self._running = True
        self._connect_plc()

        self._timer = QTimer()
        self._timer.setInterval(self._poll_ms)
        self._timer.timeout.connect(self._poll)
        self._timer.start()

    def stop(self):
        """Request a graceful stop (call from UI thread)."""
        self._running = False
        if self._timer:
            self._timer.stop()
        self._disconnect_plc()

    def set_poll_interval(self, ms: int):
        """Change polling interval at runtime."""
        self._poll_ms = ms
        if self._timer:
            self._timer.setInterval(ms)

    # ── Private ────────────────────────────────────────────────

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

    def _poll(self):
        if not self._running:
            return

        # Auto-reconnect if not connected
        if self._client is None or not self._client.get_connected():
            self._connect_plc()
            if self._client is None:
                return

        try:
            raw = self._client.db_read(self._db_number, 0, DB_TOTAL_BYTES)
            result = self._parse(raw)
            self.data_ready.emit(result)

        except S7Error as exc:
            msg = f"Read error: {exc}"
            logger.warning(msg)
            self.error.emit(msg)
            self._client = None          # trigger reconnect on next poll

    @staticmethod
    def _parse(raw: bytes) -> dict:
        result: dict[str, Any] = {}
        for name, dtype, offset, bit in DB_LAYOUT:
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