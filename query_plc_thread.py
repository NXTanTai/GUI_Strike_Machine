import snap7
import snap7.util as s7
import struct
from dataclasses import dataclass
from collections import deque
from PySide6.QtCore import QThread, Signal, QObject, QTimer, Slot
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                                QVBoxLayout, QWidget, QPushButton)


# ─── PLC Worker ───────────────────────────────────────────────────────
class PLCWorker(QObject):
    # ── Signals OUT (Worker → UI) ──
    data_received = Signal(dict)
    write_done    = Signal(str, bool)   # (field_name, success)
    connected     = Signal()
    disconnected  = Signal()
    error         = Signal(str)

    def __init__(self, ip: str, rack: int = 0, slot: int = 1,
                 db_number: int = 1, interval_ms: int = 500):
        super().__init__()
        self.ip          = ip
        self.rack        = rack
        self.slot        = slot
        self.db_number   = db_number
        self.interval_ms = interval_ms
        self.db_size     = 580
        self._running    = False
        self.client      = snap7.client.Client()

        # Queue chứa các lệnh write chờ thực thi
        self._write_queue: list[dict] = []

    # ── Slot nhận lệnh write từ UI ────────────────────────────────────
    @Slot(str, object)
    def request_write_field(self, field_name: str, value):
        """UI gọi signal → slot này, đưa vào queue."""
        self._write_queue.append({
            "type":  "field",
            "name":  field_name,
            "value": value,
        })

    @Slot(dict)
    def request_write_fields(self, data: dict):
        """Ghi nhiều field cùng lúc."""
        self._write_queue.append({
            "type": "fields",
            "data": data,
        })

    # ── Lifecycle ─────────────────────────────────────────────────────
    def start_polling(self):
        self._running = True
        self._connect()
        self._timer = QTimer()
        self._timer.setInterval(self.interval_ms)
        self._timer.timeout.connect(self._poll)
        self._timer.start()

    def stop_polling(self):
        self._running = False
        if hasattr(self, "_timer"):
            self._timer.stop()
        try:
            self.client.disconnect()
        except Exception:
            pass

    def _connect(self):
        try:
            self.client.connect(self.ip, self.rack, self.slot)
            self.connected.emit()
        except Exception as e:
            self.error.emit(f"Kết nối thất bại: {e}")

    # ── Poll: mỗi tick xử lý write queue trước, sau đó read ──────────
    def _poll(self):
        if not self._running:
            return

        try:
            if not self.client.get_connected():
                self._connect()
                return

            # 1. Xử lý tất cả lệnh write đang chờ
            while self._write_queue:
                cmd = self._write_queue.pop(0)
                self._execute_write(cmd)

            # 2. Đọc dữ liệu
            self._read()

        except Exception as e:
            self.error.emit(str(e))
            self.disconnected.emit()

    # ── Execute write ─────────────────────────────────────────────────
    def _execute_write(self, cmd: dict):
        try:
            if cmd["type"] == "field":
                self._write_single(cmd["name"], cmd["value"])
                self.write_done.emit(cmd["name"], True)

            elif cmd["type"] == "fields":
                self._write_batch(cmd["data"])
                self.write_done.emit("batch", True)

        except Exception as e:
            self.error.emit(f"Write thất bại: {e}")
            self.write_done.emit(cmd.get("name", "batch"), False)

    def _write_single(self, field_name: str, value):
        field = DB_MAP[field_name]

        if field.data_type == "BOOL":
            byte_idx, bit_idx = BOOL_BIT_INDEX[field_name]
            raw = bytearray(self.client.db_read(self.db_number, byte_idx, 1))
            s7.set_bool(raw, 0, bit_idx, bool(value))
            self.client.db_write(self.db_number, byte_idx, raw)

        else:
            if field.data_type == "REAL":
                packed = struct.pack(">f", float(value))
            elif field.data_type == "DINT":
                packed = struct.pack(">i", int(value))
            elif field.data_type == "INT":
                packed = struct.pack(">h", int(value))
            else:
                raise TypeError(f"Không hỗ trợ: {field.data_type}")

            self.client.db_write(self.db_number, field.offset, bytearray(packed))

    def _write_batch(self, data: dict):
        """Read-modify-write toàn DB, chỉ 1 lần db_write."""
        raw = bytearray(self.client.db_read(self.db_number, 0, self.db_size))

        for field_name, value in data.items():
            field = DB_MAP[field_name]

            if field.data_type == "BOOL":
                byte_idx, bit_idx = BOOL_BIT_INDEX[field_name]
                s7.set_bool(raw, byte_idx, bit_idx, bool(value))
            elif field.data_type == "REAL":
                raw[field.offset:field.offset + 4] = struct.pack(">f", float(value))
            elif field.data_type == "DINT":
                raw[field.offset:field.offset + 4] = struct.pack(">i", int(value))
            elif field.data_type == "INT":
                raw[field.offset:field.offset + 2] = struct.pack(">h", int(value))

        self.client.db_write(self.db_number, 0, raw)

    # ── Read output ───────────────────────────────────────────────────
    def _read(self):
        raw_slice = bytearray(self.client.db_read(self.db_number, 192, 134))
        padded    = bytearray(192) + raw_slice

        data = {
            "T0_CurrentTemp":         s7.get_real(padded, 194),
            "P1_CurrentTemp1":        s7.get_real(padded, 198),
            "P1_CurrentTemp2":        s7.get_real(padded, 202),
            "P1_CurrentTemp3":        s7.get_real(padded, 206),
            "P1_CurrentPressureHose": s7.get_real(padded, 210),
            "P1_CurrentPressureITV":  s7.get_real(padded, 214),
            "P2_CurrentTemp1":        s7.get_real(padded, 240),
            "P2_CurrentTemp2":        s7.get_real(padded, 244),
            "P2_CurrentTemp3":        s7.get_real(padded, 248),
            "P2_CurrentPressureHose": s7.get_real(padded, 252),
            "P2_CurrentPressureITV":  s7.get_real(padded, 256),
            "P3_CurrentTemp1":        s7.get_real(padded, 282),
            "P3_CurrentTemp2":        s7.get_real(padded, 286),
            "P3_CurrentTemp3":        s7.get_real(padded, 290),
            "P3_CurrentPressureHose": s7.get_real(padded, 294),
            "P3_CurrentPressureITV":  s7.get_real(padded, 298),
            "Bit_Alarm":              s7.get_bool(padded, 192, 0),
        }
        self.data_received.emit(data)


# ─── Main Window ──────────────────────────────────────────────────────
class MainWindow(QMainWindow):
    # ── Signals IN (UI → Worker) ──
    sig_write_field  = Signal(str, object)
    sig_write_fields = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PLC Monitor")
        self._setup_ui()
        self._setup_plc_thread()

    def _setup_ui(self):
        self.lbl_status = QLabel("⚪ Đang kết nối...")
        self.lbl_temp   = QLabel("Temp P1: --")
        self.lbl_press  = QLabel("Pressure P1: --")
        self.lbl_alarm  = QLabel("")
        self.lbl_write  = QLabel("")

        # Nút test write
        btn_write_one   = QPushButton("Write P1 Temp Setting = 180.0")
        btn_write_multi = QPushButton("Write P1 Full Setting")
        btn_start       = QPushButton("START")
        btn_stop        = QPushButton("STOP")

        btn_write_one.clicked.connect(self._write_one)
        btn_write_multi.clicked.connect(self._write_multi)
        btn_start.clicked.connect(lambda: self.sig_write_field.emit("START", True))
        btn_stop.clicked.connect(lambda: self.sig_write_field.emit("STOP", True))

        layout = QVBoxLayout()
        for w in [self.lbl_status, self.lbl_temp, self.lbl_press,
                  self.lbl_alarm, self.lbl_write,
                  btn_write_one, btn_write_multi, btn_start, btn_stop]:
            layout.addWidget(w)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _setup_plc_thread(self):
        self.plc_thread = QThread()
        self.plc_worker = PLCWorker(ip="192.168.0.1", interval_ms=500)
        self.plc_worker.moveToThread(self.plc_thread)

        # Worker → UI
        self.plc_thread.started.connect(self.plc_worker.start_polling)
        self.plc_worker.data_received.connect(self._on_data)
        self.plc_worker.write_done.connect(self._on_write_done)
        self.plc_worker.connected.connect(lambda: self.lbl_status.setText("🟢 Đã kết nối"))
        self.plc_worker.disconnected.connect(lambda: self.lbl_status.setText("🔴 Mất kết nối"))
        self.plc_worker.error.connect(lambda msg: self.lbl_status.setText(f"⚠️ {msg}"))

        # UI → Worker (cross-thread safe qua Signal)
        self.sig_write_field.connect(self.plc_worker.request_write_field)
        self.sig_write_fields.connect(self.plc_worker.request_write_fields)

        self.plc_thread.start()

    # ── Slots UI ──────────────────────────────────────────────────────
    @Slot(dict)
    def _on_data(self, data: dict):
        self.lbl_temp.setText(f"Temp P1:     {data['P1_CurrentTemp1']:.1f} °C")
        self.lbl_press.setText(f"Pressure P1: {data['P1_CurrentPressureHose']:.2f} bar")
        self.lbl_alarm.setText("🔴 ALARM!" if data["Bit_Alarm"] else "🟢 Normal")

    @Slot(str, bool)
    def _on_write_done(self, field_name: str, success: bool):
        status = "✅ OK" if success else "❌ Thất bại"
        self.lbl_write.setText(f"Write [{field_name}]: {status}")

    def _write_one(self):
        self.sig_write_field.emit("P1_TemperatureSetting", 180.0)

    def _write_multi(self):
        self.sig_write_fields.emit({
            "P1_TemperatureSetting": 180.0,
            "P1_TempLimitHIGH":     190.0,
            "P1_TempLimitLOW":      170.0,
            "P1_AirFillingTime":    5000,
            "P1_CountTimes":        10,
        })

    def closeEvent(self, event):
        self.plc_worker.stop_polling()
        self.plc_thread.quit()
        self.plc_thread.wait()
        event.accept()
