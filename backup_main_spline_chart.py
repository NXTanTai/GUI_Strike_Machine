# main.py
import sys
import random
import math
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from PySide6.QtCore import QTimer, QDateTime
from backup_spline_chart import SplineChartWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("4 Real-time Spline Charts")
        self.resize(1200, 900)

        central = QWidget()
        grid = QGridLayout(central)
        grid.setSpacing(10)

        # ── Tạo 4 chart ──────────────────────────────────────────
        self.chart1 = SplineChartWidget(title="Temperature (°C)", num_series=1)
        self.chart2 = SplineChartWidget(title="Temperature (°C)",   num_series=2)
        self.chart3 = SplineChartWidget(title="Temperature (°C)",      num_series=3)
        self.chart4 = SplineChartWidget(title="Temperature (°C)",      num_series=4)

        self.chart1.set_series_name(0, "Oven")
        self.chart2.set_series_name(0, "Inlet 1");  self.chart2.set_series_name(1, "Inlet 2")
        self.chart3.set_series_name(0, "Inlet 1"); self.chart3.set_series_name(1, "Inlet 2"); self.chart3.set_series_name(2, "Inlet 3")
        self.chart4.set_series_name(0, "Inlet 1"); self.chart4.set_series_name(1, "Inlet 2")
        self.chart4.set_series_name(2, "Inlet 3"); self.chart4.set_series_name(3, "Oven")

        grid.addWidget(self.chart1, 0, 0)
        grid.addWidget(self.chart2, 0, 1)
        grid.addWidget(self.chart3, 1, 0)
        grid.addWidget(self.chart4, 1, 1)

        self.setCentralWidget(central)

        # ── Trạng thái giả lập ───────────────────────────────────
        self._t = 0.0          # biến thời gian để tạo sóng
        self._noise = lambda base, amp: base + amp * random.gauss(0, 1)

        # ── Timer giả lập – 500ms/tick ───────────────────────────
        self.sim_timer = QTimer(self)
        self.sim_timer.timeout.connect(self._simulate_tick)
        self.sim_timer.start(150)

        # ── Setting callbacks ─────────────────────────────────────
        self.chart1.on_setting_clicked = lambda: print("⚙ Chart 1 settings")
        self.chart2.on_setting_clicked = lambda: print("⚙ Chart 2 settings")
        self.chart3.on_setting_clicked = lambda: print("⚙ Chart 3 settings")
        self.chart4.on_setting_clicked = lambda: print("⚙ Chart 4 settings")

    # ─────────────────────────────────────────────────────────────
    def _simulate_tick(self):
        """Tạo dữ liệu giả lập sóng sin + nhiễu Gaussian cho 4 chart."""
        now = QDateTime.currentDateTime()
        t   = self._t

        # Chart 1 – Temperature (°C): dao động 20-40°C
        self.chart1.push_data([
            self._noise(30 + 8  * math.sin(t * 0.3),         1.2),   # Indoor
            self._noise(25 + 10 * math.sin(t * 0.2 + 1.0),   2.0),   # Outdoor
        ], now)

        # Chart 2 – Pressure (bar): 0.8-1.4 bar
        self.chart2.push_data([
            self._noise(1.1 + 0.25 * math.sin(t * 0.4),        0.03),  # Line A
            self._noise(1.0 + 0.20 * math.cos(t * 0.35 + 0.5), 0.04),  # Line B
            self._noise(0.9 + 0.30 * math.sin(t * 0.5 + 1.2),  0.02),  # Line C
        ], now)

        # Chart 3 – Voltage (V): 210-230V
        self.chart3.push_data([
            self._noise(220 + 8 * math.sin(t * 0.6),           0.8),   # Phase 1
            self._noise(218 + 6 * math.sin(t * 0.6 + 2.094),   0.9),   # Phase 2 (lệch 120°)
        ], now)

        # Chart 4 – Speed (rpm): 1000-3000 rpm
        self.chart4.push_data([
            self._noise(1500 + 400 * math.sin(t * 0.25),          20),  # Motor 1
            self._noise(2000 + 300 * math.cos(t * 0.30 + 0.8),    25),  # Motor 2
            self._noise(2500 + 350 * math.sin(t * 0.20 + 1.5),    30),  # Motor 3
            self._noise(1800 + 450 * math.cos(t * 0.28 + 2.2),    18),  # Motor 4
        ], now)

        self._t += 0.5   # bước thời gian khớp với interval 500ms

    # ─────────────────────────────────────────────────────────────
    def closeEvent(self, event):
        self.sim_timer.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

