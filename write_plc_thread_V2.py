import struct
import logging
from typing import Any, Optional
from queue import Queue

import snap7
from snap7.error import S7Error

from PySide6.QtCore import QObject, QTimer, Signal

logger = logging.getLogger(__name__)

def _set_bool(data: bytearray, byte_idx: int, bit_idx: int, value: bool) -> None:
    if value:
        data[byte_idx] |= (1 << (7 - bit_idx))   # set bit
    else:
        data[byte_idx] &= ~(1 << (7 - bit_idx))  # clear bit


def _set_real(data: bytearray, offset: int, value: float) -> None:
    struct.pack_into(">f", data, offset, value)


def _set_dint(data: bytearray, offset: int, value: int) -> None:
    struct.pack_into(">i", data, offset, value)


def _set_int(data: bytearray, offset: int, value: int) -> None:
    struct.pack_into(">h", data, offset, value)


def _set_string(data: bytearray, offset: int, value: str) -> None:
    max_len = data[offset]                        # đọc max_len từ byte 0 (do PLC định nghĩa)
    encoded = value.encode("utf-8", errors="replace")
    if len(encoded) > max_len:
        encoded = encoded[:max_len]
    data[offset + 1] = len(encoded)              # actual length
    data[offset + 2 : offset + 2 + len(encoded)] = encoded

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
_DB_LOOKUP: dict[str, tuple[str, int, Any]] = {
    name: (dtype, offset, bit)
    for name, dtype, offset, bit in DB_LAYOUT
}
# Total bytes to read: String at 324 + 2-byte header + 254 max chars = 580
DB_TOTAL_BYTES = 584

class PLCWrite(QObject):
    """
    3 chế độ ghi:
      - write_single   : ghi 1 tag đơn lẻ
      - write_area     : ghi 1 nhóm tag (dict)
      - write_full_db  : ghi toàn bộ DB (dict đầy đủ)
    """

    # ── Incoming signals (UI → PLCWrite) ────────────────────────
    write_single  = Signal(str, object)  # (tag_name, value)
    write_area    = Signal(dict)         # {"tag": value, ...}
    write_full_db = Signal(dict)         # toàn bộ DB_LAYOUT tags

    # ── Outgoing signals (PLCWrite → UI) ────────────────────────
    write_done   = Signal(str)           # tag name vừa ghi xong
    error        = Signal(str)
    connected    = Signal()
    disconnected = Signal()

    def __init__(
        self,
        ip: str        = "192.168.1.1",
        rack: int      = 0,
        slot: int      = 1,
        db_number: int = 1,
        write_gap_ms: int = 500,
        parent: Optional[QObject] = None,
    ):
        super().__init__(parent)
        self._ip           = ip
        self._rack         = rack
        self._slot         = slot
        self._db_number    = db_number
        self._write_gap_ms = write_gap_ms

        self._client: snap7.client.Client | None = None
        self._queue: Queue = Queue()
        self._timer: QTimer | None = None
        self._running = False

    # ── Public API ──────────────────────────────────────────────

    def run(self):
        self._running = True
        self._connect_plc()

        # Nối 3 signals vào queue
        self.write_single.connect(self._enqueue_single)
        self.write_area.connect(self._enqueue_area)
        self.write_full_db.connect(self._enqueue_full_db)

        self._timer = QTimer()
        self._timer.setInterval(self._write_gap_ms)
        self._timer.timeout.connect(self._drain)
        self._timer.start()

    def stop(self):
        self._running = False
        if self._timer:
            self._timer.stop()
        self._disconnect_plc()

    # ── Enqueue handlers ────────────────────────────────────────

    def _enqueue_single(self, name: str, value: object):
        """Ghi 1 tag đơn lẻ → đẩy 1 lệnh vào queue."""
        self._queue.put(("single", name, value))
        logger.debug("Enqueued single [%s] = %s", name, value)

    def _enqueue_area(self, data: dict):
        """Ghi 1 nhóm tag → đẩy từng tag vào queue, cách nhau 500ms."""
        for name, value in data.items():
            self._queue.put(("single", name, value))
        logger.debug("Enqueued area (%d tags)", len(data))

    def _enqueue_full_db(self, data: dict):
        """
        Ghi toàn bộ DB → build 1 bytearray rồi db_write 1 lần duy nhất.
        Không đi qua queue từng tag, ghi thẳng luôn.
        """
        self._queue.put(("full_db", data))
        logger.debug("Enqueued full_db (%d tags)", len(data))

    # ── Drain ───────────────────────────────────────────────────

    def _drain(self):
        if not self._running or self._queue.empty():
            return

        item = self._queue.get_nowait()
        mode = item[0]

        if mode == "single":
            _, name, value = item
            self._write_single(name, value)

        elif mode == "full_db":
            _, data = item
            self._write_full_db(data)

    # ── Write implementations ────────────────────────────────────

    def _write_single(self, name: str, value: Any):
        """Đọc byte hiện tại → patch → ghi lại (an toàn cho BOOL)."""
        if not self._ensure_connected():
            return

        if self._client is None:
            self.error.emit("PLC client not initialized")
            return

        tag = next((t for t in DB_LAYOUT if t[0] == name), None)
        if tag is None:
            self.error.emit(f"Tag not found: {name}")
            return

        try:
            _, dtype, offset, bit = tag
            size = _dtype_size(dtype)
            raw  = bytearray(self._client.db_read(self._db_number, offset, size))
            _pack(raw, dtype, bit, value)
            self._client.db_write(self._db_number, offset, raw)
            self.write_done.emit(name)
            logger.info("Single write OK [%s] = %s", name, value)

        except S7Error as exc:
            self._handle_error(f"Single write error [{name}]: {exc}")

    def _write_full_db(self, data: dict):
        if not self._ensure_connected():
            return

        client = self._client          # snapshot local — tránh race condition
        if client is None:
            return

        try:
            raw = bytearray(client.db_read(self._db_number, 0, DB_TOTAL_BYTES))

            for name, value in data.items():
                tag = _DB_LOOKUP.get(name)
                if tag is None:
                    logger.warning("Tag not found (full_db): %s", name)
                    continue
                dtype, offset, bit = tag
                _pack_at(raw, dtype, offset, bit, value)

            client.db_write(self._db_number, 0, raw)   # ← dùng local client
            self.write_done.emit("full_db")
            logger.info("Full DB write OK (%d tags)", len(data))

        except S7Error as exc:
            self._handle_error(f"Full DB write error: {exc}")
    # ── Helpers ─────────────────────────────────────────────────

    def _ensure_connected(self) -> bool:
        if self._client is None or not self._client.get_connected():
            self._connect_plc()
        return self._client is not None

    def _handle_error(self, msg: str):
        logger.warning(msg)
        self.error.emit(msg)
        self._client = None

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

def _dtype_size(dtype: str) -> int:
    return {"BOOL": 1, "INT": 2, "DINT": 4, "REAL": 4, "STRING": 256}.get(dtype, 1)

def _pack(raw: bytearray, dtype: str, bit: Any, value: Any) -> None:
    """Pack vào bytearray bắt đầu từ index 0 (dùng cho single write)."""
    if dtype == "BOOL":   _set_bool(raw, 0, bit, bool(value))
    elif dtype == "REAL":  _set_real(raw, 0, float(value))
    elif dtype == "DINT":  _set_dint(raw, 0, int(value))
    elif dtype == "INT":   _set_int(raw, 0, int(value))
    elif dtype == "STRING": _set_string(raw, 0, str(value))

def _pack_at(raw: bytearray, dtype: str, offset: int, bit: Any, value: Any) -> None:
    """Pack vào đúng offset trong bytearray (dùng cho full_db write)."""
    if dtype == "BOOL":    _set_bool(raw, offset, bit, bool(value))
    elif dtype == "REAL":  _set_real(raw, offset, float(value))
    elif dtype == "DINT":  _set_dint(raw, offset, int(value))
    elif dtype == "INT":   _set_int(raw, offset, int(value))
    elif dtype == "STRING": _set_string(raw, offset, str(value))