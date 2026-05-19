import sys
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QProgressBar, QTextEdit, QGroupBox,
)
from PySide6.QtCore import (
    Qt, QThread, QTimer, QObject, Signal, QDateTime,
)
from PySide6.QtGui import QFont

class SensorWorker(QObject):
    data_ready  = Signal(float, str)
    log_message = Signal(str)
    tick_count  = Signal(int)

    def __init__(self, interval_ms: int = 500):
        super().__init__()
        self.interval_ms = interval_ms
        self._timer: QTimer | None = None
        self._count = 0

    def start_work(self):
        name = QThread.currentThread().objectName()
        self.log_message.emit(f"[Sensor] start trong {name}")
        self._timer = QTimer(self)           # parent=self → cùng thread
        self._timer.setInterval(self.interval_ms)
        self._timer.timeout.connect(self._on_tick)
        self._timer.start()
        self.log_message.emit(f"[Sensor] QTimer chạy mỗi {self.interval_ms}ms")

    def stop_work(self):
        if self._timer is not None:
            self._timer.stop()
            self._timer = None
            self.log_message.emit("[Sensor] QTimer đã dừng")
        QThread.currentThread().quit()

    def _on_tick(self):
        self._count += 1
        temp = round(25.0 + random.uniform(-3.0, 8.0), 2)
        hum  = round(60.0 + random.uniform(-10.0, 10.0), 2)
        label = f"T={temp}°C  H={hum}%"
        ts = QDateTime.currentDateTime().toString("hh:mm:ss.zzz")
        self.log_message.emit(f"[Tick #{self._count:03d}] {ts} → {label}")
        self.data_ready.emit(temp, label)
        self.tick_count.emit(self._count)

class CountdownWorker(QObject):
    tick     = Signal(int)
    finished = Signal()

    def __init__(self, seconds: int = 10):
        super().__init__()
        self.seconds = seconds
        self._remaining = seconds
        self._timer: QTimer | None = None

    def start_work(self):
        self._remaining = self.seconds
        self._timer = QTimer(self)
        self._timer.setInterval(1000)
        self._timer.timeout.connect(self._on_tick)
        self._timer.start()

    def stop_work(self):
        if self._timer is not None:
            self._timer.stop()
            self._timer = None
        QThread.currentThread().quit()

    def _on_tick(self):
        self.tick.emit(self._remaining)
        self._remaining -= 1
        if self._remaining < 0:
            self._timer.stop()
            self._timer = None
            self.finished.emit()
            QThread.currentThread().quit()


# ─────────────────────────────────────────────────────────────
# MainWindow
# ─────────────────────────────────────────────────────────────
class MainWindow(QMainWindow):
    # Signals yêu cầu worker dừng — deliver qua queued connection
    stop_sensor    = Signal()
    stop_countdown = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QThread + QTimer Demo")
        self.setMinimumSize(700, 620)
        self._setup_ui()
        self._setup_sensor_thread()
        self._setup_countdown_thread()

    # ── UI ───────────────────────────────────────────────────
    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setSpacing(12)
        root.setContentsMargins(16, 16, 16, 16)

        title = QLabel("QThread  +  QTimer")
        title.setFont(QFont("Monospace", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        root.addWidget(title)

        sub = QLabel("Worker tự gọi thread.quit() sau khi dừng timer — không deadlock, không warning")
        sub.setAlignment(Qt.AlignCenter)
        sub.setStyleSheet("color:#666; font-size:12px;")
        root.addWidget(sub)

        # Sensor group
        sg = QGroupBox("Sensor Worker  (500ms)")
        sg.setFont(QFont("", 10, QFont.Bold))
        sgl = QVBoxLayout(sg)

        self.lbl_value = QLabel("—")
        self.lbl_value.setFont(QFont("Monospace", 22, QFont.Bold))
        self.lbl_value.setAlignment(Qt.AlignCenter)
        self.lbl_value.setStyleSheet(
            "color:#1a73e8; border:1px solid #ddd;"
            "border-radius:8px; padding:10px; background:#f8f9ff;"
        )
        sgl.addWidget(self.lbl_value)

        self.lbl_ticks = QLabel("Ticks: 0")
        self.lbl_ticks.setAlignment(Qt.AlignCenter)
        sgl.addWidget(self.lbl_ticks)

        br = QHBoxLayout()
        self.btn_start = QPushButton("▶  Bắt đầu")
        self.btn_stop  = QPushButton("■  Dừng")
        self.btn_stop.setEnabled(False)
        for b in (self.btn_start, self.btn_stop):
            b.setFixedHeight(36)
            br.addWidget(b)
        sgl.addLayout(br)
        root.addWidget(sg)

        # Countdown group
        cg = QGroupBox("Countdown Worker  (10 giây)")
        cg.setFont(QFont("", 10, QFont.Bold))
        cgl = QVBoxLayout(cg)

        self.countdown_bar = QProgressBar()
        self.countdown_bar.setRange(0, 10)
        self.countdown_bar.setValue(10)
        self.countdown_bar.setFormat("%v giây còn lại")
        self.countdown_bar.setFixedHeight(28)
        cgl.addWidget(self.countdown_bar)

        self.btn_countdown = QPushButton("⏱  Chạy đếm ngược")
        self.btn_countdown.setFixedHeight(36)
        cgl.addWidget(self.btn_countdown)
        root.addWidget(cg)

        # Log
        lg = QGroupBox("Log")
        lg.setFont(QFont("", 10, QFont.Bold))
        lgl = QVBoxLayout(lg)
        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setFont(QFont("Monospace", 10))
        self.log_box.setFixedHeight(200)
        lgl.addWidget(self.log_box)
        root.addWidget(lg)

        note = QLabel(
            "💡  Pattern đúng: main thread emit stop_signal → "
            "slot chạy trong worker thread (queued) → dừng timer → "
            "worker tự gọi QThread.currentThread().quit() → "
            "main thread wait() trả về ngay."
        )
        note.setWordWrap(True)
        note.setStyleSheet(
            "background:#fffbe6; border:1px solid #ffe58f; border-radius:6px;"
            "padding:8px; font-size:11px; color:#7a5800;"
        )
        root.addWidget(note)

    # ── Sensor thread ─────────────────────────────────────────
    def _setup_sensor_thread(self):
        self.sensor_thread = QThread()
        self.sensor_thread.setObjectName("SensorThread")
        self.sensor_worker = SensorWorker(interval_ms=500)
        self.sensor_worker.moveToThread(self.sensor_thread)

        self.sensor_thread.started.connect(self.sensor_worker.start_work)
        self.stop_sensor.connect(self.sensor_worker.stop_work)   # queued ✅

        self.sensor_worker.data_ready.connect(self._on_sensor_data)
        self.sensor_worker.log_message.connect(self._append_log)
        self.sensor_worker.tick_count.connect(
            lambda n: self.lbl_ticks.setText(f"Ticks: {n}")
        )
        # Khi thread kết thúc event loop (sau quit()), cập nhật UI
        self.sensor_thread.finished.connect(self._on_sensor_stopped)

        self.btn_start.clicked.connect(self._start_sensor)
        self.btn_stop.clicked.connect(self._stop_sensor)

    def _start_sensor(self):
        self.btn_start.setEnabled(False)
        self.btn_stop.setEnabled(True)
        self._append_log("[Main] Khởi động SensorThread…")
        self.sensor_thread.start()

    def _stop_sensor(self):
        self.btn_stop.setEnabled(False)
        self._append_log("[Main] Yêu cầu dừng…")
        # emit → queued → slot chạy trong worker thread → timer stop → thread.quit()
        self.stop_sensor.emit()
        # wait() block đến khi thread thoát hẳn (sau quit() bên trong worker)
        self.sensor_thread.wait()

    def _on_sensor_stopped(self):
        self.btn_start.setEnabled(True)
        self._append_log("[Main] SensorThread đã dừng hoàn toàn.")

    def _on_sensor_data(self, value: float, label: str):
        self.lbl_value.setText(label)
        color = "#d32f2f" if value > 30 else "#f57c00" if value > 27 else "#1a73e8"
        self.lbl_value.setStyleSheet(
            f"color:{color}; border:1px solid #ddd; border-radius:8px;"
            "padding:10px; background:#f8f9ff; font-size:20px; font-weight:bold;"
        )

    # ── Countdown thread ──────────────────────────────────────
    def _setup_countdown_thread(self):
        self.cd_thread = QThread()
        self.cd_thread.setObjectName("CountdownThread")
        self.cd_worker = CountdownWorker(seconds=10)
        self.cd_worker.moveToThread(self.cd_thread)

        self.cd_thread.started.connect(self.cd_worker.start_work)
        self.stop_countdown.connect(self.cd_worker.stop_work)    # queued ✅

        self.cd_worker.tick.connect(self._on_countdown_tick)
        self.cd_worker.finished.connect(self._on_countdown_done)
        self.cd_thread.finished.connect(
            lambda: self.btn_countdown.setEnabled(True)
        )
        self.btn_countdown.clicked.connect(self._start_countdown)

    def _start_countdown(self):
        self.btn_countdown.setEnabled(False)
        self.countdown_bar.setValue(10)
        self._append_log("[Main] Khởi động CountdownThread…")
        self.cd_thread.start()

    def _on_countdown_tick(self, remaining: int):
        self.countdown_bar.setValue(remaining)
        self._append_log(f"[Countdown] Còn lại: {remaining}s")

    def _on_countdown_done(self):
        self._append_log("[Countdown] ✅ Hoàn thành!")

    # ── Tiện ích ──────────────────────────────────────────────
    def _append_log(self, msg: str):
        self.log_box.append(msg)
        sb = self.log_box.verticalScrollBar()
        sb.setValue(sb.maximum())

    def closeEvent(self, event):
        # emit → worker dừng timer + tự quit() → wait() trả về sạch
        self.stop_sensor.emit()
        self.sensor_thread.wait()
        self.stop_countdown.emit()
        self.cd_thread.wait()
        super().closeEvent(event)


# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win = MainWindow()
    win.show()
    sys.exit(app.exec())