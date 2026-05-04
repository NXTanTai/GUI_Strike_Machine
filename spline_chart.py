
# spline_chart.py
from typing import List
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCharts import QChart, QSplineSeries, QValueAxis, QChartView, QDateTimeAxis, QLineSeries
from PySide6.QtGui import QIcon, QPainter, QFont
from PySide6.QtCore import Qt, QTimer, QSize, QEvent, QDateTime, QPointF

class SplineChartWidget(QWidget):
    def __init__(self, title: str = "Spline Chart", chart_type: int = 0, 
                 num_series: int = 1, chart_font: QFont = None, parent=None):
        super().__init__(parent)
        self.font = chart_font if chart_font else QFont("Segoe UI", 10)
        self.title = title
        self.num_series = num_series
        self.series_list = []
        self.chart_type = chart_type
        self.chart = None
        self.chart_view = None
        self.proxySetting = None
        self.btnSetting = None
        self.timer = None   # timer giả lập (có thể tắt)

        self.setup_ui()
        self.setup_chart()
        self.setup_setting_button()

        # Nếu muốn dùng giả lập thì mở dòng dưới, còn không thì comment lại
        # self.start_simulation()

        # Cập nhật vị trí nút Setting
        QTimer.singleShot(300, self.update_setting_position)

    # ==================== CÁC HÀM SETUP GIỮ NGUYÊN ====================
    def setup_ui(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

    def setup_chart(self):
        self.chart = QChart()
        self.chart.setTitle(self.title)
        font = QFont("Segoe UI", 13)
        font.setWeight(QFont.Weight.Bold)
        self.chart.setTitleFont(font)
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        colors = ["#43A047", "#FB8C00", "#E53935", "#1E88E5"]

        for i in range(self.num_series):
            if self.chart_type == 0:
                series = QSplineSeries()
            else:
                series = QLineSeries()
            series.setUseOpenGL(True)
            series.setName(f"Series {i+1}")
            if i < len(colors):
                series.setColor(colors[i])
            self.chart.addSeries(series)
            self.series_list.append(series)

        # Trục X: Thời gian hh:mm:ss
        self.axis_x = QDateTimeAxis()
        self.axis_x.setFormat("hh:mm:ss")
        self.axis_x.setTitleText("Time")
        self.axis_x.setTickCount(6)

        # Trục Y
        self.axis_y = QValueAxis()
        self.axis_y.setLabelFormat("%.1f")
        self.axis_y.setTitleText("Value")

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
                background-color: rgba(255, 255, 255, 245);
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

    # ==================== HÀM CẬP NHẬT GIÁ TRỊ THỰC TẾ ====================
    def append_data(self, values: List[float]):
        """
        Hàm này dùng để cập nhật giá trị thực từ bên ngoài.
        
        values: list[float] có độ dài bằng num_series
        Ví dụ: [23.5, 45.2, 67.8] cho 3 series
        """
        if len(values) != self.num_series:
            print(f"Lỗi: Cần {self.num_series} giá trị, nhưng nhận {len(values)}")
            return
        
        current_time = QDateTime.currentDateTime()   # thời gian hiện tại

        for i, series in enumerate(self.series_list):
            y_value = values[i]
            series.append(current_time.toMSecsSinceEpoch(), y_value)

        # Cập nhật trục X: chỉ hiển thị 60 giây gần nhất
        max_time = current_time.toMSecsSinceEpoch()
        min_time = max_time - 60 * 1000   # 60 giây

        self.axis_x.setRange(QDateTime.fromMSecsSinceEpoch(min_time),
                             QDateTime.fromMSecsSinceEpoch(max_time))

        # Tự động scale trục Y theo giá trị lớn nhất
        current_max = max(values)
        if current_max > self.axis_y.max() * 0.92:
            new_max = current_max * 1.15
            self.axis_y.setRange(0, new_max)

    # ==================== GIẢ LẬP (có thể comment nếu không cần) ====================
    def start_simulation(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.simulate_data)
        self.timer.start(500)

    def simulate_data(self):
        """Giả lập dữ liệu - chỉ dùng để test"""
        import random
        fake_values = [20 + random.uniform(0, 80) for _ in range(self.num_series)]
        self.append_data(fake_values)

    def on_setting_clicked(self):
        print(f"Setting clicked on chart: {self.title}")

    # ==================== Vị trí nút Setting (đã tối ưu) ====================
    def update_setting_position(self):
        if not self.proxySetting or not self.chart_view:
            return

        # Lấy kích thước view
        view_rect = self.chart_view.rect()

        # Cập nhật kích thước nút chính xác
        self.btnSetting.adjustSize()
        btn_width = self.btnSetting.width()
        btn_height = self.btnSetting.height()

        # Vị trí góc phải trên (cách lề 15px)
        margin = 15
        scene_pos = self.chart_view.mapToScene(
            view_rect.width() - btn_width - margin,
            margin
        )

        self.proxySetting.setPos(scene_pos)

    def eventFilter(self, watched, event):
        if watched == self.chart_view and event.type() == QEvent.Type.Resize:
            self.update_setting_position()
        return super().eventFilter(watched, event)
