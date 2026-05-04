"""
ThemeWidget - PySide6 version
Converted from Qt C++ example (themewidget.cpp)
"""

import random
from PySide6.QtCore import Qt, QPointF, QTranslator
from PySide6.QtGui import QPalette, QColor, QPainter
from PySide6.QtWidgets import (
    QWidget, QGridLayout, QFormLayout, QPushButton, QHBoxLayout, QVBoxLayout,
    QComboBox, QCheckBox, QGroupBox, QLabel, QApplication, QGraphicsProxyWidget
)
from PySide6.QtCharts import (
    QChart, QChartView,
    QLineSeries, QSplineSeries, QScatterSeries,
    QAreaSeries, QPieSeries,
    QStackedBarSeries, QBarSet,
    QValueAxis
)

QChartTheme = QChart.ChartTheme
QChartAniOtp = QChart.AnimationOption
QAlign = Qt.AlignmentFlag

# Type aliases (thay cho typedef trong C++)
# Data  = (QPointF, str)
# DataList  = list[Data]
# DataTable = list[DataList]

TRANSLATIONS = {
    "en": {
        # Tiêu đề cửa sổ
        "window_title":    "Chart Themes",
        # Group Settings
        "settings":        "Settings",
        "theme_label":     "Theme:",
        "animation_label": "Animation:",
        "legend_label":    "Legend:",
        "antialias":       "Anti-aliasing",
        "language_label":  "Language:",
        # Theme names
        "Light":           "Light",
        "Blue Cerulean":   "Blue Cerulean",
        "Dark":            "Dark",
        "Brown Sand":      "Brown Sand",
        "Blue NCS":        "Blue NCS",
        "High Contrast":   "High Contrast",
        "Blue Icy":        "Blue Icy",
        "Qt":              "Qt",
        # Animation names
        "No Animations":       "No Animations",
        "GridAxis Animations": "GridAxis Animations",
        "Series Animations":   "Series Animations",
        "All Animations":      "All Animations",
        # Legend names
        "No Legend":     "No Legend",
        "Legend Top":    "Legend Top",
        "Legend Bottom": "Legend Bottom",
        "Legend Left":   "Legend Left",
        "Legend Right":  "Legend Right",
        # Chart titles
        "Area chart":    "Area chart",
        "Bar chart":     "Bar chart",
        "Line chart":    "Line chart",
        "Pie chart":     "Pie chart",
        "Spline chart":  "Spline chart",
        "Scatter chart": "Scatter chart",
        # Series / set labels
        "Series":  "Series",
        "Bar set": "Bar set",
        "Slice":   "Slice",
    },
    "vi": {
        # Tiêu đề cửa sổ
        "window_title":    "Giao diện Biểu đồ",
        # Group Settings
        "settings":        "Cài đặt",
        "theme_label":     "Giao diện:",
        "animation_label": "Hiệu ứng:",
        "legend_label":    "Chú thích:",
        "antialias":       "Khử răng cưa",
        "language_label":  "Ngôn ngữ:",
        # Theme names
        "Light":           "Sáng",
        "Blue Cerulean":   "Xanh Cerulean",
        "Dark":            "Tối",
        "Brown Sand":      "Nâu Cát",
        "Blue NCS":        "Xanh NCS",
        "High Contrast":   "Tương phản cao",
        "Blue Icy":        "Xanh Băng",
        "Qt":              "Qt",
        # Animation names
        "No Animations":       "Không hiệu ứng",
        "GridAxis Animations": "Hiệu ứng lưới/trục",
        "Series Animations":   "Hiệu ứng chuỗi",
        "All Animations":      "Tất cả hiệu ứng",
        # Legend names
        "No Legend":     "Ẩn chú thích",
        "Legend Top":    "Chú thích trên",
        "Legend Bottom": "Chú thích dưới",
        "Legend Left":   "Chú thích trái",
        "Legend Right":  "Chú thích phải",
        # Chart titles
        "Area chart":    "Biểu đồ vùng",
        "Bar chart":     "Biểu đồ cột",
        "Line chart":    "Biểu đồ đường",
        "Pie chart":     "Biểu đồ tròn",
        "Spline chart":  "Biểu đồ đường cong",
        "Scatter chart": "Biểu đồ phân tán",
        # Series / set labels
        "Series":  "Chuỗi",
        "Bar set": "Nhóm cột",
        "Slice":   "Phần",
    },
}
 
# Key gốc (EN) cho từng combobox — để lưu data không đổi theo ngôn ngữ
THEME_KEYS = [
    "Light", "Blue Cerulean", "Dark", "Brown Sand",
    "Blue NCS", "High Contrast", "Blue Icy", "Qt",
]
THEME_VALUES = [
    QChartTheme.ChartThemeLight, QChartTheme.ChartThemeBlueCerulean,
    QChartTheme.ChartThemeDark,  QChartTheme.ChartThemeBrownSand,
    QChartTheme.ChartThemeBlueNcs, QChartTheme.ChartThemeHighContrast,
    QChartTheme.ChartThemeBlueIcy, QChartTheme.ChartThemeQt,
]
ANIMATION_KEYS = [
    "No Animations", "GridAxis Animations",
    "Series Animations", "All Animations",
]
ANIMATION_VALUES = [
    QChartAniOtp.NoAnimation, QChartAniOtp.GridAxisAnimations,
    QChartAniOtp.SeriesAnimations, QChartAniOtp.AllAnimations,
]
LEGEND_KEYS = [
    "No Legend", "Legend Top", "Legend Bottom",
    "Legend Left", "Legend Right",
]
LEGEND_VALUES = [None, QAlign.AlignTop, QAlign.AlignBottom, QAlign.AlignLeft, QAlign.AlignRight]
 
CHART_TITLE_KEYS = [
    "Area chart", "Pie chart", "Line chart",
    "Bar chart", "Spline chart", "Scatter chart",
]
 
class ThemeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
 
        self.m_listCount  = 3
        self.m_valueMax   = 10
        self.m_valueCount = 7
        self.m_charts: list[QChartView] = []
        self._lang = "en"   # ngôn ngữ hiện tại
 
        self.m_dataTable = self._generate_random_data(
            self.m_listCount, self.m_valueMax, self.m_valueCount
        )
 
        self._build_ui()
        self._populate_combos()
        self._create_charts()
 
        self.antialias_check.setChecked(True)
 
        pal = QApplication.palette()
        pal.setColor(QPalette.ColorRole.Window,     QColor(0xf0f0f0))
        pal.setColor(QPalette.ColorRole.WindowText, QColor(0x404044))
        QApplication.setPalette(pal)
 
        self.update_ui()
 
    # ------------------------------------------------------------------
    # Tiện ích dịch
    # ------------------------------------------------------------------
    def _t(self, key: str) -> str:
        return TRANSLATIONS[self._lang].get(key, key)
 
    # ------------------------------------------------------------------
    # UI setup
    # ------------------------------------------------------------------
    def _build_ui(self):
        self.theme_combo     = QComboBox()
        self.animated_combo  = QComboBox()
        self.legend_combo    = QComboBox()
        self.antialias_check = QCheckBox()
 
        # Label refs để retranslate sau
        self.lbl_theme     = QLabel()
        self.lbl_animation = QLabel()
        self.lbl_legend    = QLabel()
        self.lbl_language  = QLabel()
        self.control_box   = QGroupBox()
 
        # Nút chuyển ngôn ngữ
        self.btn_en = QPushButton("🇬🇧 English")
        self.btn_vi = QPushButton("🇻🇳 Tiếng Việt")
        self.btn_en.setCheckable(True)
        self.btn_vi.setCheckable(True)
        self.btn_en.setChecked(True)
        self.btn_en.clicked.connect(lambda: self._switch_language("en"))
        self.btn_vi.clicked.connect(lambda: self._switch_language("vi"))
 
        lang_row = QHBoxLayout()
        lang_row.addWidget(self.btn_en)
        lang_row.addWidget(self.btn_vi)
        lang_row.addStretch()
 
        form = QFormLayout(self.control_box)
        form.addRow(self.lbl_theme,     self.theme_combo)
        form.addRow(self.lbl_animation, self.animated_combo)
        form.addRow(self.lbl_legend,    self.legend_combo)
        form.addRow(self.antialias_check)
        form.addRow(self.lbl_language,  lang_row)
 
        self.grid_layout = QGridLayout()
 
        root = QGridLayout(self)
        root.addWidget(self.control_box,  0, 0, 1, 3)
        root.addLayout(self.grid_layout,  1, 0, 2, 3)
 
        self.theme_combo.currentIndexChanged.connect(self.update_ui)
        self.animated_combo.currentIndexChanged.connect(self.update_ui)
        self.legend_combo.currentIndexChanged.connect(self.update_ui)
        self.antialias_check.toggled.connect(self.update_ui)
 
        self._retranslate_static()
 
    def _retranslate_static(self):
        """Cập nhật toàn bộ text tĩnh theo ngôn ngữ hiện tại."""
        self.control_box.setTitle(self._t("settings"))
        self.lbl_theme.setText(self._t("theme_label"))
        self.lbl_animation.setText(self._t("animation_label"))
        self.lbl_legend.setText(self._t("legend_label"))
        self.lbl_language.setText(self._t("language_label"))
        self.antialias_check.setText(self._t("antialias"))
        if hasattr(self, "window"):
            self.window().setWindowTitle(self._t("window_title"))
 
    def _retranslate_combos(self):
        """Cập nhật text trong comboboxes mà không mất currentIndex."""
        for combo, keys in [
            (self.theme_combo,    THEME_KEYS),
            (self.animated_combo, ANIMATION_KEYS),
            (self.legend_combo,   LEGEND_KEYS),
        ]:
            idx = combo.currentIndex()
            combo.blockSignals(True)
            for i, key in enumerate(keys):
                combo.setItemText(i, self._t(key))
            combo.setCurrentIndex(idx)
            combo.blockSignals(False)
 
    def _retranslate_chart_titles(self):
        """Cập nhật tiêu đề các chart."""
        for view, key in zip(self.m_charts, CHART_TITLE_KEYS):
            view.chart().setTitle(self._t(key))
 
    def _switch_language(self, lang: str):
        self._lang = lang
        self.btn_en.setChecked(lang == "en")
        self.btn_vi.setChecked(lang == "vi")
        self._retranslate_static()
        self._retranslate_combos()
        self._retranslate_chart_titles()
        self.window().setWindowTitle(self._t("window_title"))
 
    # ------------------------------------------------------------------
    # Populate comboboxes (lần đầu)
    # ------------------------------------------------------------------
    def _populate_combos(self):
        for key, val in zip(THEME_KEYS, THEME_VALUES):
            self.theme_combo.addItem(self._t(key), val)
        for key, val in zip(ANIMATION_KEYS, ANIMATION_VALUES):
            self.animated_combo.addItem(self._t(key), val)
        for key, val in zip(LEGEND_KEYS, LEGEND_VALUES):
            self.legend_combo.addItem(self._t(key), val)
 
    # ------------------------------------------------------------------
    # Sinh dữ liệu ngẫu nhiên
    # ------------------------------------------------------------------
    def _generate_random_data(self, list_count, value_max, value_count):
        data_table = []
        for i in range(list_count):
            data_list = []
            y_value = 0.0
            for j in range(value_count):
                y_value += random.random() * (value_max / value_count)
                x = (j + random.random()) * (value_max / value_count)
                data_list.append((QPointF(x, y_value), f"Slice {i}:{j}"))
            data_table.append(data_list)
        return data_table

    # ------------------------------------------------------------------
    # Tạo các chart
    # ------------------------------------------------------------------
    def _create_charts(self):
        charts_config = [
            (self._create_area_chart,    "Area chart",    1, 0),
            (self._create_pie_chart,     "Pie chart",     1, 1),
            (self._create_line_chart,    "Line chart",    1, 2),
            (self._create_bar_chart,     "Bar chart",     2, 0),
            (self._create_spline_chart,  "Spline chart",  2, 1),
            (self._create_scatter_chart, "Scatter chart", 2, 2),
        ]
        from PySide6.QtWidgets import QSizePolicy
        for fn, title_key, row, col in charts_config:
            chart = fn()
            view  = QChartView(chart)
            if title_key == "Pie chart":
                view.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
            self.grid_layout.addWidget(view, row, col)
            self.m_charts.append(view)
 
    @staticmethod
    def _axis_y(chart: QChart) -> QValueAxis:
        """Trả về trục Y đã cast sang QValueAxis — tránh lỗi QAbstractAxis."""
        return chart.axes(Qt.Vertical)[0]   # type: ignore[return-value]

    def _create_area_chart(self) -> QChart:
        chart = QChart()
        chart.setTitle(self._t("Area chart"))
        lower_series = None
        for i, data_list in enumerate(self.m_dataTable):
            upper_series = QLineSeries(chart)
            for j, (point, _) in enumerate(data_list):
                if lower_series:
                    pts = lower_series.points()
                    upper_series.append(QPointF(j, pts[i].y() + point.y()))
                else:
                    upper_series.append(QPointF(j, point.y()))
            area = QAreaSeries(upper_series, lower_series)
            area.setName(f"{self._t('Series')} {i}")
            chart.addSeries(area)
            lower_series = upper_series
        chart.createDefaultAxes()
        chart.axes(Qt.Orientation.Horizontal)[0].setRange(0, self.m_valueCount - 1)
        axis_y = QValueAxis()
        axis_y.setRange(0, self.m_valueMax)
        axis_y.setLabelFormat("%.1f  ")
        chart.setAxisY(axis_y)
        return chart

    def _create_bar_chart(self) -> QChart:
        chart = QChart()
        chart.setTitle(self._t("Bar chart"))
        series = QStackedBarSeries(chart)
        for i, data_list in enumerate(self.m_dataTable):
            bar_set = QBarSet(f"{self._t('Bar set')} {i}")
            for point, _ in data_list:
                bar_set.append(point.y())
            series.append(bar_set)
        chart.addSeries(series)
        chart.createDefaultAxes()
        axis_y = QValueAxis()
        axis_y.setRange(0, self.m_valueMax * 2)
        axis_y.setLabelFormat("%.1f  ")
        chart.setAxisY(axis_y, series)
        return chart
 
    def _create_line_chart(self) -> QChart:
        chart = QChart()
        chart.setTitle(self._t("Line chart"))
        all_series = []
        for i, data_list in enumerate(self.m_dataTable):
            series = QLineSeries(chart)
            for point, _ in data_list:
                series.append(point)
            series.setName(f"{self._t('Series')} {i}")
            chart.addSeries(series)
            all_series.append(series)
        chart.createDefaultAxes()
        chart.axes(Qt.Orientation.Horizontal)[0].setRange(0, self.m_valueMax)
        axis_y = QValueAxis()
        axis_y.setRange(0, self.m_valueCount)
        axis_y.setLabelFormat("%.1f  ")
        for s in all_series:
            chart.setAxisY(axis_y, s)
        return chart
 
    def _create_pie_chart(self) -> QChart:
        chart = QChart()
        chart.setTitle(self._t("Pie chart"))
        series = QPieSeries(chart)
        for idx, (point, label) in enumerate(self.m_dataTable[0]):
            slc = series.append(label, point.y())
            if idx == 0:
                slc.setLabelVisible(True)
                slc.setExploded(True)
                slc.setExplodeDistanceFactor(0.5)
        series.setPieSize(0.4)
        chart.addSeries(series)
        return chart
 
    def _create_spline_chart(self) -> QChart:
        chart = QChart()
        chart.setTitle(self._t("Spline chart"))
        all_series = []
        for i, data_list in enumerate(self.m_dataTable):
            series = QSplineSeries(chart)
            for point, _ in data_list:
                series.append(point)
            series.setName(f"{self._t('Series')} {i}")
            chart.addSeries(series)
            all_series.append(series)
        chart.createDefaultAxes()
        chart.axes(Qt.Orientation.Horizontal)[0].setRange(0, self.m_valueMax)
        axis_y = QValueAxis()
        axis_y.setRange(0, self.m_valueCount)
        axis_y.setLabelFormat("%.1f  ")
        for s in all_series:
            chart.setAxisY(axis_y, s)
        return chart

    def _create_spline_chart_realtime(self) -> QChart:
        self.chart = QChart()
        self.chart.setTitle(self._t("Spline chart"))
        self.series_list.clear()

        for i in range(len(self.m_dataTable)):          # hoặc số series bạn muốn
            series = QSplineSeries()
            series.setName(f"{self._t('Series')} {i}")
            
            # Thêm dữ liệu ban đầu nếu có
            for point, _ in self.m_dataTable[i]:
                series.append(point)
            
            self.chart.addSeries(series)
            self.series_list.append(series)

        # Tạo axes một lần
        self.chart.createDefaultAxes()
        
        self.axis_x = self.chart.axes(Qt.Orientation.Horizontal)[0]
        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, self.m_valueCount)
        self.axis_y.setLabelFormat("%.1f ")

        for series in self.series_list:
            self.chart.setAxisY(self.axis_y, series)

        # Giới hạn ban đầu cho trục X
        self.axis_x.setRange(0, self.m_valueMax)
        
        return self.chart

    def create_chart_view(self):
        chart = self._create_spline_chart()
        
        self.chart_view = QChartView(chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # === Tạo nút Setting ở góc phải trên chart ===
        self.btnSetting = QPushButton(" Setting")
        self.btnSetting.setIcon(QIcon.fromTheme("preferences-system") 
                                or QIcon(":/icons/settings.png"))  # thay icon nếu cần
        self.btnSetting.setIconSize(QSize(18, 18))
        self.btnSetting.setFixedHeight(32)
        self.btnSetting.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # Style hiện đại, trong suốt nền
        self.btnSetting.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 200);
                border: 1px solid #CBD5E1;
                border-radius: 6px;
                padding: 4px 12px 4px 8px;
                color: #334155;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: rgba(241, 245, 249, 230);
                border-color: #94A3B8;
            }
            QPushButton:pressed {
                background-color: #E2E8F0;
            }
        """)

        # Đặt nút lên chart qua proxy
        self.proxySetting = QGraphicsProxyWidget()
        self.proxySetting.setWidget(self.btnSetting)
        self.proxySetting.setZValue(10)          # đưa nút lên trên cùng

        # Thêm proxy vào scene của chart
        chart.scene().addItem(self.proxySetting)

        # Kết nối sự kiện click
        self.btnSetting.clicked.connect(self.open_settings)

        return self.chart_view

    def update_spline_value(self, new_values: list[float]):
            """
            new_values: list giá trị y tương ứng với từng series
            Ví dụ: [12.5, 8.3, 15.7] nếu bạn có 3 series
            """
            if not self.series_list or len(new_values) != len(self.series_list):
                return

            self.current_x += 1.0          # hoặc += delta_time nếu bạn có thời gian thực

            for i, series in enumerate(self.series_list):
                y_value = new_values[i]
                series.append(self.current_x, y_value)

            # Cập nhật trục X để chart cuộn theo (rolling window)
            max_x = self.current_x
            min_x = max(0, max_x - self.m_valueMax)   # giữ khoảng hiển thị cố định

            self.axis_x.setRange(min_x, max_x)

    def _create_scatter_chart(self) -> QChart:
        chart = QChart()
        chart.setTitle(self._t("Scatter chart"))
        all_series = []
        for i, data_list in enumerate(self.m_dataTable):
            series = QScatterSeries(chart)
            for point, _ in data_list:
                series.append(point)
            series.setName(f"{self._t('Series')} {i}")
            chart.addSeries(series)
            all_series.append(series)
        chart.createDefaultAxes()
        chart.axes(Qt.Orientation.Horizontal)[0].setRange(0, self.m_valueMax)
        axis_y = QValueAxis()
        axis_y.setRange(0, self.m_valueCount)
        axis_y.setLabelFormat("%.1f  ")
        for s in all_series:
            chart.setAxisY(axis_y, s)
        return chart
 
    # ------------------------------------------------------------------
    # Update UI
    # ------------------------------------------------------------------
    def update_ui(self):
        # Theme
        theme = self.theme_combo.currentData()
        if self.m_charts and self.m_charts[0].chart().theme() != theme:
            for view in self.m_charts:
                view.chart().setTheme(theme)
            theme_palette = {
                QChartTheme.ChartThemeLight:        (0xf0f0f0, 0x404044),
                QChartTheme.ChartThemeDark:         (0x121218, 0xd6d6d6),
                QChartTheme.ChartThemeBlueCerulean: (0x40434a, 0xd6d6d6),
                QChartTheme.ChartThemeBrownSand:    (0x9e8965, 0x404044),
                QChartTheme.ChartThemeBlueNcs:      (0x018bba, 0x404044),
                QChartTheme.ChartThemeHighContrast: (0xffab03, 0x181818),
                QChartTheme.ChartThemeBlueIcy:      (0xcee7f0, 0x404044),
            }
            bg, fg = theme_palette.get(theme, (0xf0f0f0, 0x404044))
            pal = self.window().palette()
            pal.setColor(QPalette.ColorRole.Window,     QColor(bg))
            pal.setColor(QPalette.ColorRole.WindowText, QColor(fg))
            self.window().setPalette(pal)
 
        # Antialiasing
        checked = self.antialias_check.isChecked()
        for view in self.m_charts:
            view.setRenderHint(QPainter.RenderHint.Antialiasing, checked)
 
        # Animation
        options = self.animated_combo.currentData()
        if self.m_charts and self.m_charts[0].chart().animationOptions() != options:
            for view in self.m_charts:
                view.chart().setAnimationOptions(options)
 
        # Legend
        alignment = self.legend_combo.currentData()
        for view in self.m_charts:
            if alignment is None:
                view.chart().legend().hide()
            else:
                view.chart().legend().setAlignment(Qt.AlignmentFlag(int(alignment)))
                view.chart().legend().show()
 
 
# ------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = ThemeWidget()
    widget.setWindowTitle(widget._t("window_title"))
    widget.resize(1200, 700)
    widget.show()
    sys.exit(app.exec())