# spline_chart.py
from typing import List
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCharts import QChart, QSplineSeries, QValueAxis, QChartView, QDateTimeAxis
from PySide6.QtGui import QIcon, QPainter
from PySide6.QtCore import Qt, QTimer, QSize, QEvent, QDateTime

class SplineChartWidget(QWidget):
    def __init__(self, title: str = "Spline Chart", num_series: int = 3, parent=None):
        super().__init__(parent)

        self.title = title
        self.num_series = num_series
        self.series_list = []
        self.chart = None
        self.chart_view = None
        self.proxySetting = None
        self.btnSetting = None
        self._window_seconds = 60  # Cửa sổ thời gian hiển thị (giây)

        self.setup_ui()
        self.setup_chart()
        self.setup_setting_button()

        QTimer.singleShot(300, self.update_setting_position)

    def setup_ui(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

    def setup_chart(self):
        self.chart = QChart()
        self.chart.setTitle(self.title)
        self.chart.setAnimationOptions(QChart.AnimationOption.NoAnimation)

        colors = ["#1E88E5", "#43A047", "#FB8C00", "#E53935"]

        for i in range(self.num_series):
            series = QSplineSeries()
            series.setName(f"Series {i+1}")
            if i < len(colors):
                series.setColor(colors[i])
            self.chart.addSeries(series)
            self.series_list.append(series)

        # Trục X: thời gian thực
        self.axis_x = QDateTimeAxis()
        self.axis_x.setFormat("hh:mm:ss")
        self.axis_x.setTitleText("Time")
        self.axis_x.setTickCount(6)

        now = QDateTime.currentDateTime()
        self.axis_x.setRange(now.addSecs(-self._window_seconds), now)

        # Trục Y
        self.axis_y = QValueAxis()
        self.axis_y.setLabelFormat("%.1f")
        self.axis_y.setTitleText("Value")
        self.axis_y.setRange(0, 100)

        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)

        for series in self.series_list:
            self.chart.setAxisX(self.axis_x, series)
            self.chart.setAxisY(self.axis_y, series)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        self.layout.addWidget(self.chart_view)
        self.chart_view.installEventFilter(self)

    def setup_setting_button(self):
        self.btnSetting = QPushButton(" Setting")
        self.btnSetting.setIcon(QIcon.fromTheme("preferences-system"))
        self.btnSetting.setIconSize(QSize(20, 20))
        self.btnSetting.setFixedHeight(38)
        self.btnSetting.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btnSetting.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 235);
                border: 1px solid #CBD5E1;
                border-radius: 6px;
                padding: 6px 16px 6px 10px;
                color: #334155;
                font-size: 13.5px;
            }
            QPushButton:hover {
                background-color: rgba(241, 245, 249, 255);
                border-color: #94A3B8;
            }
        """)
        self.proxySetting = self.chart.scene().addWidget(self.btnSetting)
        self.proxySetting.setZValue(11)
        self.btnSetting.clicked.connect(self.on_setting_clicked)

    # ──────────────────────────────────────────────
    #  PUBLIC API – gọi từ bên ngoài để đẩy dữ liệu
    # ──────────────────────────────────────────────

    def push_data(self, values: List[float], timestamp: QDateTime = None):
        """
        Đẩy 1 điểm dữ liệu vào chart.

        Args:
            values   : list giá trị, mỗi phần tử tương ứng 1 series.
                       Ví dụ: [42.5, 78.1, 55.0]
            timestamp: thời điểm điểm dữ liệu (mặc định = hiện tại)
        """
        if timestamp is None:
            timestamp = QDateTime.currentDateTime()

        ts_ms = timestamp.toMSecsSinceEpoch()

        for i, series in enumerate(self.series_list):
            y = values[i] if i < len(values) else 0.0
            series.append(ts_ms, y)

        self._trim_old_points(timestamp)
        self._update_axes(timestamp, values)

    def push_data_single(self, series_index: int, value: float,
                         timestamp: QDateTime = None):
        """
        Đẩy giá trị vào đúng 1 series theo index.

        Args:
            series_index: 0-based index của series
            value       : giá trị y
            timestamp   : thời điểm (mặc định = hiện tại)
        """
        if series_index < 0 or series_index >= len(self.series_list):
            return
        if timestamp is None:
            timestamp = QDateTime.currentDateTime()

        ts_ms = timestamp.toMSecsSinceEpoch()
        self.series_list[series_index].append(ts_ms, value)

        self._trim_old_points(timestamp)
        self._update_axes(timestamp, [value])

    # ──────────────────────────────────────────────
    #  INTERNAL helpers
    # ──────────────────────────────────────────────

    def _trim_old_points(self, now: QDateTime):
        """Xoá điểm cũ hơn window_seconds để tránh tràn bộ nhớ."""
        cutoff_ms = now.addSecs(-self._window_seconds * 2).toMSecsSinceEpoch()
        for series in self.series_list:
            while series.count() > 0 and series.at(0).x() < cutoff_ms:
                series.remove(0)

    def _update_axes(self, now: QDateTime, values: List[float]):
        """Cập nhật range trục X (cuộn theo thời gian) và Y (auto-scale)."""
        # X: luôn hiển thị window_seconds gần nhất
        x_min = now.addSecs(-self._window_seconds)
        self.axis_x.setRange(x_min, now)

        # Y: auto-scale theo max của tất cả series
        all_y = []
        for series in self.series_list:
            for j in range(series.count()):
                all_y.append(series.at(j).y())

        if all_y:
            y_max = max(all_y) * 1.15
            y_min = min(0.0, min(all_y))
            self.axis_y.setRange(y_min, max(y_max, 1.0))

    # ──────────────────────────────────────────────
    #  Các tiện ích khác
    # ──────────────────────────────────────────────

    def set_window_seconds(self, seconds: int):
        """Thay đổi cửa sổ thời gian hiển thị (mặc định 60 giây)."""
        self._window_seconds = seconds

    def set_series_name(self, index: int, name: str):
        if 0 <= index < len(self.series_list):
            self.series_list[index].setName(name)

    def clear_data(self):
        for series in self.series_list:
            series.clear()
        now = QDateTime.currentDateTime()
        self.axis_x.setRange(now.addSecs(-self._window_seconds), now)
        self.axis_y.setRange(0, 100)

    def on_setting_clicked(self):
        print(f"Setting clicked on chart: {self.title}")

    def update_setting_position(self):
        if not self.proxySetting or not self.chart_view:
            return
        view_rect = self.chart_view.rect()
        self.btnSetting.adjustSize()
        btn_width = self.btnSetting.width()
        margin = 15
        scene_pos = self.chart_view.mapToScene(
            view_rect.width() - btn_width - margin, margin
        )
        self.proxySetting.setPos(scene_pos)

    def eventFilter(self, watched, event):
        if watched == self.chart_view and event.type() == QEvent.Type.Resize:
            self.update_setting_position()
        return super().eventFilter(watched, event)