import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QLabel
)
from PySide6.QtCore import QTimer, QDateTime
from spline_chart import SplineChartWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("4 Real-time Spline Charts")
        self.resize(1280, 1024)

        # Widget trung tâm
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Sử dụng Grid Layout để sắp xếp 4 chart (2x2)  
        grid = QGridLayout(central_widget)
        grid.setSpacing(10)
        grid.setContentsMargins(10, 10, 10, 10)

        # ==================== Tạo 4 đồ thị ====================
        self.chart_temp = SplineChartWidget(title="Temperature 1 (°C)", chart_type=1, num_series=1)
        self.chart_pressure = SplineChartWidget(title="Temperature 2 (°C)", chart_type=1, num_series=3)
        self.chart_voltage = SplineChartWidget(title="Temperature 3 (°C)", chart_type=1, num_series=3)
        self.chart_speed = SplineChartWidget(title="Temperature 4 (°C)", chart_type=1, num_series=3)

        # Thêm vào grid
        grid.addWidget(self.chart_temp,    0, 0)
        grid.addWidget(self.chart_pressure,0, 1)
        grid.addWidget(self.chart_voltage, 1, 0)
        grid.addWidget(self.chart_speed,   1, 1)

        # ==================== Ví dụ cập nhật dữ liệu giả lập ====================
        # Bạn có thể xóa phần này khi dùng dữ liệu thật
        self.simulation_timer = QTimer(self)
        self.simulation_timer.timeout.connect(self.update_all_charts)
        self.simulation_timer.start(500)   # cập nhật mỗi 500ms

        # Lưu ý: Khi dùng dữ liệu thật, bạn sẽ gọi append_data() trực tiếp

    def update_all_charts(self):
        """Ví dụ cập nhật dữ liệu giả lập cho 4 chart"""
        import random

        # Chart 1: Temperature - 2 series
        temp_values = [22.5 + random.uniform(-0.5, 2)]
        self.chart_temp.append_data(temp_values)

        # Chart 2: Pressure - 3 series
        pressure_values = [1.2 + random.uniform(0, 0.8),
                          2.5 + random.uniform(0, 0.5),
                          3.8 + random.uniform(0, 0.3)]
        self.chart_pressure.append_data(pressure_values)

        # Chart 3: Voltage - 2 series
        voltage_values = [220 + random.uniform(-1, 2),
                         110 + random.uniform(-1, 2),
                         60 + random.uniform(-1, 2)]
        self.chart_voltage.append_data(voltage_values)

        # Chart 4: Speed - 4 series
        speed_values = [1450 + random.uniform(-1, 5),
                       980 + random.uniform(-1, 5),
                       500 + random.uniform(-1, 5)]
        self.chart_speed.append_data(speed_values)

    def closeEvent(self, event):
        """Dừng tất cả timer khi đóng cửa sổ"""
        self.simulation_timer.stop()

        # Dừng update của từng chart
        for chart in [self.chart_temp, self.chart_pressure,
                      self.chart_voltage, self.chart_speed]:
            chart.stop_update()

        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())