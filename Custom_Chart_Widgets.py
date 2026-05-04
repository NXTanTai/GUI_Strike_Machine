# spline_chart.py
from typing import List
from collections import deque
import time
import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import Qt, QTimer

SERIES_COLORS = ["#43A047", "#FB8C00", "#E53935", "#1E88E5", "#8E24AA"]

FONT_FAMILY  = "Segoe UI"
FONT_SIZE_LG = 16
FONT_SIZE_MD = 16
FONT_SIZE_SM = 13

class _FixedTickDateAxis(pg.DateAxisItem):
    """DateAxisItem với tick cố định mỗi tick_spacing giây."""
 
    def __init__(self, tick_spacing: int = 5, **kwargs):
        super().__init__(**kwargs)
        self._tick_spacing = tick_spacing
 
    def tickValues(self, minVal, maxVal, size):
        """Override hoàn toàn — tạo tick mỗi tick_spacing giây."""
        step   = self._tick_spacing
        start  = (int(minVal) // step) * step
        ticks  = list(range(start, int(maxVal) + step, step))
        return [(step, ticks)]
 
    def tickStrings(self, values, scale, spacing):
        """Hiển thị dạng hh:mm:ss."""
        import datetime
        result = []
        for v in values:
            try:
                result.append(
                    datetime.datetime.fromtimestamp(v).strftime("%H:%M:%S")
                )
            except Exception:
                result.append("")
        return result

class CustomChartWidget(QWidget):
    """
    Real-time chart widget dùng PyQtGraph.
    Trục X luôn chạy theo thời gian thực kể cả không có data.

    Parameters
    ----------
    title       : Tiêu đề chart
    num_series  : Số lượng series (tối đa 5)
    y_label     : Nhãn trục Y
    y_min       : Giá trị min trục Y
    y_max       : Giá trị max trục Y
    max_seconds : Khoảng thời gian hiển thị (giây)
    chart_font  : QFont tuỳ chỉnh (None = dùng mặc định)
    parent      : Widget cha
    """

    def __init__(
        self,
        title: str        = "Chart",
        num_series: int   = 1,
        y_label: str      = "Value",
        y_min: float      = 0,
        y_max: float      = 100,
        max_seconds: int  = 60,
        chart_font: QFont | None = None,
        type_unit: str = "temp",
        setting = True,
        parent=None,
    ):
        super().__init__(parent)
        self.title       = title
        self.num_series  = min(num_series, len(SERIES_COLORS))
        self.y_label     = y_label
        self.y_min       = y_min
        self.y_max       = y_max
        self.type_unit   = type_unit
        self.setting = setting
        self.max_seconds = max_seconds
        self._sim_timer  = None

        # Font
        if chart_font:
            self._font_family  = chart_font.family()
            self._font_size_lg = chart_font.pointSize() or FONT_SIZE_LG
        else:
            self._font_family  = FONT_FAMILY
            self._font_size_lg = FONT_SIZE_LG

        # Buffer dữ liệu — deque giúp xoá đầu O(1)
        self._data_x: list[deque] = [deque() for _ in range(self.num_series)]
        self._data_y: list[deque] = [deque() for _ in range(self.num_series)]

        self._setup_ui()
        self._setup_chart()
        self._start_axis_timer()

    # ── Setup ──────────────────────────────────────────────────────────────────
    def _setup_ui(self):
        self._root = QVBoxLayout(self)
        self._root.setContentsMargins(4, 4, 4, 4)
        self._root.setSpacing(2)

    def _setup_chart(self):
        pg.setConfigOptions(antialias=True, useOpenGL=True)

        # ── Title (QLabel nằm ngoài plot) ─────────────────────────────────────
        # font_title = QFont(self._font_family, self._font_size_lg)
        # font_title.setWeight(QFont.Weight.Bold)

        # self._lbl_title = QLabel(self.title)
        # self._lbl_title.setFont(font_title)
        # self._lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self._lbl_title.setContentsMargins(0, 4, 0, 0)

        # if self.setting:
        font_btn = QFont(self._font_family, self._font_size_lg)
        font_btn.setWeight(QFont.Weight.Bold)
        self.btn_setting = QPushButton(self.title)
        # self.btn_setting.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_setting.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_setting.setFont(font_btn)
        # self.btn_setting.setStyleSheet("""
        #     QPushButton {
        #         background: white;
        #         border: 2px solid #CBD5E1;
        #         border-radius: 6px;
        #         color: black;
        #     }
        #     QPushButton:hover {
        #         background: #F0F9FF; 
        #     }
        # """)
        
        self.btn_setting.setStyleSheet("""
            QPushButton {
                background: white;
                border: none;
                color: black;
            }
            QPushButton:hover {
                background: #F0F9FF; 
            }
        """)

        title_row = QHBoxLayout()
        title_row.setContentsMargins(0, 0, 0, 0)
        title_row.addStretch()
        title_row.addWidget(self.btn_setting)
        title_row.addStretch()

        self._root.addLayout(title_row)
        # ── Legend (QHBoxLayout nằm ngoài plot, trái → phải) ──────────────────
        self._legend_bar = QHBoxLayout()
        self._legend_bar.setContentsMargins(8, 0, 8, 2)
        self._legend_bar.setSpacing(16)
        self._legend_bar.addStretch()   # căn giữa

        self._legend_labels: list[QLabel] = []
        font_legend = QFont(self._font_family, FONT_SIZE_SM)
        font_legend.setWeight(QFont.Weight.Bold)

        for i in range(self.num_series):
            color = SERIES_COLORS[i]

            # Ô màu nhỏ
            dot = QFrame()
            dot.setFixedSize(14, 4)
            dot.setStyleSheet(f"background: {color}; border-radius: 2px;")

            # Tên series
            if self.type_unit == "temp":
                lbl = QLabel(f"SV") if i == 0 else QLabel(f"PV")
                lbl.setFont(font_legend)
            elif self.type_unit == "pressure":
                lbl = QLabel(f"SV") if i == 0 else QLabel(f"PV")
                lbl.setFont(font_legend)

            item_layout = QHBoxLayout()
            item_layout.setContentsMargins(0, 0, 0, 0)
            item_layout.setSpacing(4)
            item_layout.addWidget(dot)
            item_layout.addWidget(lbl)

            item_widget = QWidget()
            item_widget.setLayout(item_layout)
            self._legend_bar.addWidget(item_widget)
            self._legend_labels.append(lbl)

        self._legend_bar.addStretch()   # căn giữa
        self._root.addLayout(self._legend_bar)

        # ── PlotWidget ────────────────────────────────────────────────────────
        self.plot = pg.PlotWidget()

        # Trong suốt — kế thừa màu từ parent
        self.plot.setBackground(None)
        self.plot.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.plot.showGrid(x=True, y=True, alpha=0.1)
        self.plot.setYRange(self.y_min, self.y_max)

        # ── Font trục ─────────────────────────────────────────────────────────
        font_tick = QFont(self._font_family, FONT_SIZE_SM)
        axis_style = {
            "color"      : "black",
            "font-family": self._font_family,
            "font-size"  : f"{FONT_SIZE_MD}pt",
        }

        for axis_name in ("bottom", "left"):
            axis = self.plot.getAxis(axis_name)
            axis.setTickFont(font_tick)
            axis.setTextPen(pg.mkPen("#94A3B8"))
            axis.setPen(pg.mkPen("#334155"))
        self.plot.setLabel("left", self.y_label, **axis_style)
        self.plot.getAxis("left").label.setRotation(0)

        # ── Trục X: tick mỗi 5s, hiển thị hh:mm:ss ──────────────────────────
        date_axis = _FixedTickDateAxis(orientation="bottom", tick_spacing=10)
        date_axis.setTickFont(font_tick)
        self.plot.setAxisItems({"bottom": date_axis})
        self.plot.getAxis("bottom").setLabel("Time", **axis_style)

        # ── Curves (không dùng legend nội bộ của pyqtgraph) ──────────────────
        self._curves: list[pg.PlotDataItem] = []
        for i in range(self.num_series):
            pen = pg.mkPen(color=SERIES_COLORS[i], width=2)
            curve = self.plot.plot(pen=pen)
            self._curves.append(curve)

        self._root.addWidget(self.plot)

    def _start_axis_timer(self):
        """Timer riêng cập nhật trục X mỗi giây — độc lập với data."""
        self._axis_timer = QTimer(self)
        self._axis_timer.timeout.connect(self._update_axis)
        self._axis_timer.start(1000)
        self._update_axis()  # cập nhật ngay khi khởi tạo

    # ── Trục X real-time ──────────────────────────────────────────────────────
    def _update_axis(self):
        """Luôn chạy theo thời gian thực, không phụ thuộc data. Hiển thị 60s."""
        now = time.time()
        self.plot.setXRange(now - self.max_seconds, now, padding=0)

    # ── Public API ─────────────────────────────────────────────────────────────
    def append_data(self, values: List[float]):
        """
        Thêm giá trị mới vào chart.

        Parameters
        ----------
        values : list có độ dài = num_series
                 Ví dụ: [23.5, 45.2] cho 2 series
        """
        if len(values) != self.num_series:
            print(f"[{self.title}] Cần {self.num_series} giá trị, nhận {len(values)}")
            return

        now    = time.time()
        cutoff = now - self.max_seconds

        for i in range(self.num_series):
            self._data_x[i].append(now)
            self._data_y[i].append(values[i])

            # Xoá điểm cũ hơn max_seconds — O(1)
            while self._data_x[i] and self._data_x[i][0] < cutoff:
                self._data_x[i].popleft()
                self._data_y[i].popleft()

            self._curves[i].setData(
                list(self._data_x[i]),
                list(self._data_y[i]),
            )

        # Auto scale trục Y nếu vượt ngưỡng
        current_max = max(values)
        current_min = min(values)
        y_lo, y_hi  = self.plot.viewRange()[1]
        if current_max > y_hi * 0.92:
            self.plot.setYRange(y_lo, current_max * 1.15)
        if current_min < y_lo and current_min < 0:
            self.plot.setYRange(current_min * 1.15, y_hi)

    def set_series_name(self, index: int, name: str):
        """Đổi tên legend của một series."""
        if 0 <= index < self.num_series:
            self._legend_labels[index].setText(name)

    def set_y_range(self, y_min: float, y_max: float):
        """Set cứng range trục Y, tắt auto scale."""
        self.y_min = y_min
        self.y_max = y_max
        self.plot.setYRange(y_min, y_max)

    def clear(self):
        """Xoá toàn bộ dữ liệu."""
        for i in range(self.num_series):
            self._data_x[i].clear()
            self._data_y[i].clear()
            self._curves[i].setData([], [])

    # ── Simulation (test) ──────────────────────────────────────────────────────
    def start_simulation(self, interval_ms: int = 500):
        """Bật giả lập dữ liệu — chỉ dùng để test."""
        self._sim_timer = QTimer(self)
        self._sim_timer.timeout.connect(self._simulate)
        self._sim_timer.start(interval_ms)

    def stop_simulation(self):
        if self._sim_timer:
            self._sim_timer.stop()

    def _simulate(self):
        import random
        self.append_data([
            20 + random.uniform(0, 80)
            for _ in range(self.num_series)
        ])

    # ── Slots ──────────────────────────────────────────────────────────────────
    def _on_setting(self):
        print(f"[Setting] Chart: {self.title}")

    def set_y_label(self, label: str):
        self.y_label = label
        axis_style = {
            "color"      : "black",
            "font-family": self._font_family,
            "font-size"  : f"{FONT_SIZE_MD}pt",
        }
        self.plot.setLabel("left", label, **axis_style)