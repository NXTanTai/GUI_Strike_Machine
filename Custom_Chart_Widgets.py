# spline_chart.py
from typing import List
from collections import deque
import time
import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QTimer

# Temp series: xanh lá / cam / đỏ
TEMP_COLORS     = ["#43A047", "#FB8C00", "#E53935"]
# Pressure series: xanh dương / tím / cyan  (dùng nét đứt để phân biệt)
PRESSURE_COLORS = ["#1E88E5", "#8E24AA", "#00ACC1"]

FONT_FAMILY  = "Segoe UI"
FONT_SIZE_LG = 16
FONT_SIZE_MD = 16
FONT_SIZE_SM = 13


class _FixedTickDateAxis(pg.DateAxisItem):
    """DateAxisItem với tick cố định mỗi tick_spacing giây."""

    def __init__(self, tick_spacing: int = 10, **kwargs):
        super().__init__(**kwargs)
        self._tick_spacing = tick_spacing

    def tickValues(self, minVal, maxVal, size):
        step  = self._tick_spacing
        start = (int(minVal) // step) * step
        ticks = list(range(start, int(maxVal) + step, step))
        return [(step, ticks)]

    def tickStrings(self, values, scale, spacing):
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
    Real-time chart — dual Y-axis:
      • Trục trái  : nhiệt độ (°C)   — nét liền
      • Trục phải  : áp suất (bar)   — nét đứt, ViewBox riêng

    Parameters
    ----------
    title          : Tiêu đề / nút setting
    num_temp       : Số series nhiệt độ  (max 3)
    num_pressure   : Số series áp suất   (max 3)
    temp_label     : Nhãn trục trái
    pressure_label : Nhãn trục phải
    temp_range     : (min, max) trục trái
    pressure_range : (min, max) trục phải
    max_seconds    : Cửa sổ thời gian hiển thị (giây)
    chart_font     : QFont tuỳ chỉnh (None = mặc định)
    parent         : Widget cha
    """

    def __init__(
        self,
        title: str              = "Chart",
        num_temp: int           = 1,
        num_pressure: int       = 1,
        temp_label: str         = "Temperature (°C)",
        pressure_label: str     = "Pressure (bar)",
        temp_range: tuple       = (0, 200),
        pressure_range: tuple   = (0, 10),
        max_seconds: int        = 60,
        chart_font: QFont | None = None,
        parent=None,
    ):
        super().__init__(parent)
        self.title          = title
        self.num_temp       = min(num_temp, len(TEMP_COLORS))
        self.num_pressure   = min(num_pressure, len(PRESSURE_COLORS))
        self.temp_label     = temp_label
        self.pressure_label = pressure_label
        self.temp_range     = temp_range
        self.pressure_range = pressure_range
        self.max_seconds    = max_seconds
        self._sim_timer     = None

        if chart_font:
            self._font_family  = chart_font.family()
            self._font_size_lg = chart_font.pointSize() or FONT_SIZE_LG
        else:
            self._font_family  = FONT_FAMILY
            self._font_size_lg = FONT_SIZE_LG

        # Buffers
        self._tx: list[deque] = [deque() for _ in range(self.num_temp)]
        self._ty: list[deque] = [deque() for _ in range(self.num_temp)]
        self._px: list[deque] = [deque() for _ in range(self.num_pressure)]
        self._py: list[deque] = [deque() for _ in range(self.num_pressure)]

        self._setup_ui()
        self._setup_chart()
        self._start_axis_timer()

    # ── Root layout ───────────────────────────────────────────────────────────
    def _setup_ui(self):
        self._root = QVBoxLayout(self)
        self._root.setContentsMargins(4, 4, 4, 4)
        self._root.setSpacing(2)

    # ── Build chart ───────────────────────────────────────────────────────────
    def _setup_chart(self):
        pg.setConfigOptions(antialias=True, useOpenGL=True)

        # ── Title / Setting button ────────────────────────────────────────────
        font_btn = QFont(self._font_family, self._font_size_lg)
        font_btn.setWeight(QFont.Weight.Bold)
        self.btn_setting = QPushButton(self.title)
        self.btn_setting.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_setting.setFont(font_btn)
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

        # ── Legend bar ────────────────────────────────────────────────────────
        legend_bar = QHBoxLayout()
        legend_bar.setContentsMargins(8, 0, 8, 2)
        legend_bar.setSpacing(16)
        legend_bar.addStretch()

        self._legend_temp: list[QLabel]     = []
        self._legend_pressure: list[QLabel] = []
        font_legend = QFont(self._font_family, FONT_SIZE_SM)
        font_legend.setWeight(QFont.Weight.Bold)

        temp_names     = ["T1", "T2", "T3"]
        pressure_names = ["P1", "P2", "P3"]

        for i in range(self.num_temp):
            color = TEMP_COLORS[i]
            dot   = QFrame(); dot.setFixedSize(14, 4)
            dot.setStyleSheet(f"background: {color}; border-radius: 2px;")
            lbl = QLabel(temp_names[i]); lbl.setFont(font_legend)
            self._legend_temp.append(lbl)
            row = QHBoxLayout(); row.setContentsMargins(0,0,0,0); row.setSpacing(4)
            row.addWidget(dot); row.addWidget(lbl)
            w = QWidget(); w.setLayout(row)
            legend_bar.addWidget(w)

        # Separator giữa 2 nhóm
        sep = QFrame(); sep.setFixedSize(1, 14)
        sep.setStyleSheet("background: #CBD5E1;")
        legend_bar.addWidget(sep)

        for i in range(self.num_pressure):
            color = PRESSURE_COLORS[i]
            # Dùng gradient nét đứt để phân biệt pressure
            dot = QFrame(); dot.setFixedSize(14, 4)
            dot.setStyleSheet(
                f"background: qlineargradient(x1:0,y1:0,x2:1,y2:0,"
                f"stop:0 {color}, stop:0.4 {color},"
                f"stop:0.5 transparent, stop:0.9 transparent, stop:1 {color});"
                f"border-radius: 1px;"
            )
            lbl = QLabel(pressure_names[i]); lbl.setFont(font_legend)
            self._legend_pressure.append(lbl)
            row = QHBoxLayout(); row.setContentsMargins(0,0,0,0); row.setSpacing(4)
            row.addWidget(dot); row.addWidget(lbl)
            w = QWidget(); w.setLayout(row)
            legend_bar.addWidget(w)

        legend_bar.addStretch()
        self._root.addLayout(legend_bar)

        # ── PlotWidget (ViewBox chính — nhiệt độ) ─────────────────────────────
        self.plot = pg.PlotWidget()
        self.plot.setBackground(None)
        self.plot.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.plot.showGrid(x=True, y=True, alpha=0.1)
        self.plot.setYRange(*self.temp_range)
        self.plot.plotItem.getViewBox().setDefaultPadding(0)

        font_tick  = QFont(self._font_family, FONT_SIZE_SM)
        axis_style = {
            "color"      : "black",
            "font-family": self._font_family,
            "font-size"  : f"{FONT_SIZE_MD}pt",
        }

        for axis_name in ("bottom", "left"):
            ax = self.plot.getAxis(axis_name)
            ax.setTickFont(font_tick)
            ax.setTextPen(pg.mkPen("#94A3B8"))
            ax.setPen(pg.mkPen("#334155"))
        self.plot.setLabel("left", self.temp_label, **axis_style)
        self.plot.getAxis("left").label.setRotation(0)

        # Trục X thời gian
        date_axis = _FixedTickDateAxis(orientation="bottom", tick_spacing=10)
        date_axis.setTickFont(font_tick)
        self.plot.setAxisItems({"bottom": date_axis})
        self.plot.getAxis("bottom").setLabel("Time", **axis_style)

        # ── ViewBox phụ — áp suất ─────────────────────────────────────────────
        self._vb_pressure = pg.ViewBox()
        self._vb_pressure.setDefaultPadding(0)
        self._vb_pressure.setYRange(*self.pressure_range)
        self.plot.plotItem.scene().addItem(self._vb_pressure)

        # Trục phải — setWidth đủ lớn để label không bị che bởi end-of-line text
        self._axis_right = pg.AxisItem(orientation="right")
        self._axis_right.setTickFont(font_tick)
        self._axis_right.setTextPen(pg.mkPen("#94A3B8"))
        self._axis_right.setPen(pg.mkPen("#334155"))
        self._axis_right.setWidth(90)          # ← chỗ cho " P1: 9.99 bar "
        self.plot.plotItem.layout.addItem(self._axis_right, 2, 3)
        self._axis_right.linkToView(self._vb_pressure)
        self.plot.setLabel("right", self.pressure_label, **axis_style)

        # Sync kích thước ViewBox phụ với chính
        self.plot.plotItem.getViewBox().sigResized.connect(self._sync_pressure_vb)

        # ── Curves nhiệt độ ────────────────────────────────────────────────────
        self._temp_curves: list[pg.PlotDataItem] = []
        for i in range(self.num_temp):
            pen   = pg.mkPen(color=TEMP_COLORS[i], width=2)
            curve = self.plot.plot(pen=pen)
            self._temp_curves.append(curve)

        # ── Curves áp suất (gắn vào ViewBox phụ) ─────────────────────────────
        self._pressure_curves: list[pg.PlotDataItem] = []
        for i in range(self.num_pressure):
            pen   = pg.mkPen(color=PRESSURE_COLORS[i], width=2,
                             style=Qt.PenStyle.DashLine)
            curve = pg.PlotDataItem(pen=pen)
            self._vb_pressure.addItem(curve)
            self._pressure_curves.append(curve)

        self._root.addWidget(self.plot)

        # ── End-of-line TextItems ─────────────────────────────────────────────
        # Temp labels gắn vào ViewBox chính (toạ độ °C)
        self._temp_labels: list[pg.TextItem] = []
        for i in range(self.num_temp):
            item = pg.TextItem(text="", color=TEMP_COLORS[i], anchor=(0, 0.5))
            item.setFont(QFont(self._font_family, FONT_SIZE_SM, QFont.Weight.Bold))
            item.fill   = pg.mkBrush(255, 255, 255, 200)
            item.border = pg.mkPen(TEMP_COLORS[i], width=1)
            item.hide()
            self.plot.addItem(item)
            self._temp_labels.append(item)

        # Pressure labels gắn vào ViewBox phụ (toạ độ bar)
        self._pressure_labels: list[pg.TextItem] = []
        for i in range(self.num_pressure):
            item = pg.TextItem(text="", color=PRESSURE_COLORS[i], anchor=(0, 0.5))
            item.setFont(QFont(self._font_family, FONT_SIZE_SM, QFont.Weight.Bold))
            item.fill   = pg.mkBrush(255, 255, 255, 200)
            item.border = pg.mkPen(PRESSURE_COLORS[i], width=1)
            item.hide()
            self._vb_pressure.addItem(item)
            self._pressure_labels.append(item)

    # ── Sync ViewBox phụ ──────────────────────────────────────────────────────
    def _sync_pressure_vb(self):
        self._vb_pressure.setGeometry(
            self.plot.plotItem.getViewBox().sceneBoundingRect()
        )
        self._vb_pressure.linkedViewChanged(
            self.plot.plotItem.getViewBox(), self._vb_pressure.XAxis
        )

    # ── Timer trục X ─────────────────────────────────────────────────────────
    def _start_axis_timer(self):
        self._axis_timer = QTimer(self)
        self._axis_timer.timeout.connect(self._update_axis)
        self._axis_timer.start(1000)
        self._update_axis()

    def _update_axis(self):
        now       = time.time()
        right_pad = self.max_seconds * 0.04   # ~2.4s padding để label không bị cắt
        x_min, x_max = now - self.max_seconds, now + right_pad
        self.plot.setXRange(x_min, x_max, padding=0)
        self._vb_pressure.setXRange(x_min, x_max, padding=0)

    # ── Cập nhật end-of-line labels ───────────────────────────────────────────
    def _update_end_labels(self):
        for i in range(self.num_temp):
            if not self._tx[i]:
                self._temp_labels[i].hide(); continue
            lx, ly = self._tx[i][-1], self._ty[i][-1]
            name   = self._legend_temp[i].text()
            self._temp_labels[i].setText(f" {name}: {ly:.1f}°C ")
            self._temp_labels[i].setPos(lx + 0.3, ly)
            self._temp_labels[i].show()

        for i in range(self.num_pressure):
            if not self._px[i]:
                self._pressure_labels[i].hide(); continue
            lx, ly = self._px[i][-1], self._py[i][-1]
            name   = self._legend_pressure[i].text()
            self._pressure_labels[i].setText(f" {name}: {ly:.2f} bar ")
            self._pressure_labels[i].setPos(lx + 0.3, ly)
            self._pressure_labels[i].show()

    # ── Public API ─────────────────────────────────────────────────────────────
    def append_data(self, temp_values: List[float], pressure_values: List[float]):
        """
        Thêm dữ liệu mới vào chart.

        Parameters
        ----------
        temp_values     : list độ dài num_temp     — giá trị °C
        pressure_values : list độ dài num_pressure — giá trị bar
        """
        if len(temp_values) != self.num_temp:
            print(f"[{self.title}] Cần {self.num_temp} giá trị nhiệt độ, nhận {len(temp_values)}")
            return
        if len(pressure_values) != self.num_pressure:
            print(f"[{self.title}] Cần {self.num_pressure} giá trị áp suất, nhận {len(pressure_values)}")
            return

        now    = time.time()
        cutoff = now - self.max_seconds

        for i in range(self.num_temp):
            self._tx[i].append(now); self._ty[i].append(temp_values[i])
            while self._tx[i] and self._tx[i][0] < cutoff:
                self._tx[i].popleft(); self._ty[i].popleft()
            self._temp_curves[i].setData(list(self._tx[i]), list(self._ty[i]))

        for i in range(self.num_pressure):
            self._px[i].append(now); self._py[i].append(pressure_values[i])
            while self._px[i] and self._px[i][0] < cutoff:
                self._px[i].popleft(); self._py[i].popleft()
            self._pressure_curves[i].setData(list(self._px[i]), list(self._py[i]))

        self._update_end_labels()

    def set_temp_series_name(self, index: int, name: str):
        """Đổi tên legend nhiệt độ."""
        if 0 <= index < self.num_temp:
            self._legend_temp[index].setText(name)

    def set_pressure_series_name(self, index: int, name: str):
        """Đổi tên legend áp suất."""
        if 0 <= index < self.num_pressure:
            self._legend_pressure[index].setText(name)

    def set_temp_range(self, y_min: float, y_max: float):
        self.temp_range = (y_min, y_max)
        self.plot.setYRange(y_min, y_max)

    def set_pressure_range(self, y_min: float, y_max: float):
        self.pressure_range = (y_min, y_max)
        self._vb_pressure.setYRange(y_min, y_max)

    def clear(self):
        """Xoá toàn bộ dữ liệu."""
        for i in range(self.num_temp):
            self._tx[i].clear(); self._ty[i].clear()
            self._temp_curves[i].setData([], [])
            self._temp_labels[i].hide()
        for i in range(self.num_pressure):
            self._px[i].clear(); self._py[i].clear()
            self._pressure_curves[i].setData([], [])
            self._pressure_labels[i].hide()

    # ── Simulation ─────────────────────────────────────────────────────────────
    def start_simulation(self, interval_ms: int = 500):
        """Bật giả lập — chỉ dùng để test."""
        self._sim_timer = QTimer(self)
        self._sim_timer.timeout.connect(self._simulate)
        self._sim_timer.start(interval_ms)

    def stop_simulation(self):
        if self._sim_timer:
            self._sim_timer.stop()

    def _simulate(self):
        import random
        self.append_data(
            temp_values     = [random.uniform(*self.temp_range)     for _ in range(self.num_temp)],
            pressure_values = [random.uniform(*self.pressure_range) for _ in range(self.num_pressure)],
        )