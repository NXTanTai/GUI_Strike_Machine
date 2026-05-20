# spline_chart.py
from typing import List
from collections import deque
import time
import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame
from PySide6.QtGui import QFont, QLinearGradient, QColor, QPalette, QBrush
from PySide6.QtCore import Qt, QTimer

# Temp series: xanh lá / cam / đỏ
TEMP_COLORS     = ["#E53935", "#4C1083" , "#FB8C00", "#F72668"]
# Pressure series: xanh dương / tím / cyan  (dùng nét đứt để phân biệt)
PRESSURE_COLORS = ["#8E24AA", "#1E88E5", "#00ACC1"]

FONT_FAMILY  = "Segoe UI"
FONT_SIZE_LG = 14
FONT_SIZE_MD = 14
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

class FixedAxis(pg.AxisItem):

    def tickStrings(self, values, scale, spacing):

        return [
            f"{value:.2f}"
            for value in values
        ]
    
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
        temp_range: tuple[float, float] = (0, 200),
        pressure_range: tuple[float, float] = (0, 10),
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
        self._temp_unit = "°C"

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

        # ── Legend toggle state ───────────────────────────────────────────────
        # None  = hiển thị tất cả
        # ("t", i) = chỉ hiện temp[i]
        # ("p", i) = chỉ hiện pressure[i]
        self._solo: tuple | None = None

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
        pg.setConfigOptions(
            antialias=True,
            useOpenGL=False
        )

        self._create_title()
        self._create_legend()
        self._create_plot_widget()
        self._create_axes()

        # ===== Only create pressure system if needed =====
        if self.num_pressure > 0:
            self._create_pressure_viewbox()

        self._create_temp_curves()

        if self.num_pressure > 0:
            self._create_pressure_curves()

        self._create_end_labels()

        self._root.addWidget(self.plot)

    def _create_title(self):
        font_btn = QFont(self._font_family, self._font_size_lg)
        font_btn.setWeight(QFont.Weight.Bold)

        self.btn_setting = QPushButton(self.title)
        self.btn_setting.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_setting.setFont(font_btn)

        self.btn_setting.setStyleSheet("""
            QPushButton {
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

    def _create_legend(self):
        legend_bar = QHBoxLayout()
        legend_bar.setContentsMargins(8, 0, 8, 2)
        legend_bar.setSpacing(16)

        legend_bar.addStretch()

        self._legend_temp = []
        self._legend_pressure = []
        self._legend_temp_widgets = []
        self._legend_pressure_widgets = []

        font_legend = QFont(self._font_family, FONT_SIZE_SM)
        font_legend.setWeight(QFont.Weight.Bold)

        temp_names = ["SV","T1", "T2", "T3"]
        pressure_names = ["Pressure SV", "Pressure", "P3"]

        for i in range(self.num_temp):
            widget = self._build_temp_legend(
                temp_names[i],
                TEMP_COLORS[i],
                font_legend,
                i
            )
            legend_bar.addWidget(widget)
            self._legend_temp_widgets.append(widget)

        if self.num_temp > 0 and self.num_pressure > 0:
            sep = QFrame()

            sep.setFixedSize(1, 14)

            sep.setStyleSheet(
                "background: #CBD5E1;"
            )

            legend_bar.addWidget(sep)

            for i in range(self.num_pressure):
                widget = self._build_pressure_legend(
                    pressure_names[i],
                    PRESSURE_COLORS[i],
                    font_legend,
                    i
                )
                legend_bar.addWidget(widget)
                self._legend_pressure_widgets.append(widget)

        legend_bar.addStretch()

        self._root.addLayout(legend_bar)

    def _build_temp_legend(self, text, color, font, index):
        dot = QFrame()
        dot.setFixedSize(14, 4)
        dot.setStyleSheet(
            f"background: {color}; border-radius: 2px;"
        )

        lbl = QLabel(text)
        lbl.setStyleSheet("background: transparent;")
        lbl.setFont(font)

        self._legend_temp.append(lbl)

        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(4)

        row.addWidget(dot)
        row.addWidget(lbl)

        w = QWidget()
        w.setLayout(row)
        w.setCursor(Qt.CursorShape.PointingHandCursor)
        w.setToolTip(f"Click để chỉ hiện {text} / click lại để hiện tất cả")

        # Store index for closure
        _i = index
        def on_click(event, i=_i):
            self._on_legend_click("t", i)
        w.mousePressEvent = on_click

        return w

    def _build_pressure_legend(self, text, color, font, index):
        dot = QFrame()
        dot.setFixedSize(14, 4)

        dot.setStyleSheet(
            f"""
            background: qlineargradient(
                x1:0,y1:0,x2:1,y2:0,
                stop:0 {color},
                stop:0.4 {color},
                stop:0.5 transparent,
                stop:0.9 transparent,
                stop:1 {color}
            );
            border-radius: 1px;
            """
        )

        lbl = QLabel(text)
        lbl.setStyleSheet("background: transparent;")
        lbl.setFont(font)

        self._legend_pressure.append(lbl)

        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(4)

        row.addWidget(dot)
        row.addWidget(lbl)

        w = QWidget()
        w.setLayout(row)
        w.setCursor(Qt.CursorShape.PointingHandCursor)
        w.setToolTip(f"Click để chỉ hiện {text} / click lại để hiện tất cả")

        _i = index
        def on_click(event, i=_i):
            self._on_legend_click("p", i)
        w.mousePressEvent = on_click

        return w

    # ── Legend toggle logic ────────────────────────────────────────────────────
    def _on_legend_click(self, kind: str, index: int):
        """
        Click vào legend:
          - Nếu đang hiện tất cả  → solo series được click
          - Nếu đang solo series này → trả về hiện tất cả
          - Nếu đang solo series khác → chuyển sang solo series mới
        """
        if self._solo == (kind, index):
            # Click lại cùng series → hiện tất cả
            self._solo = None
        else:
            self._solo = (kind, index)

        self._apply_visibility()

    def _apply_visibility(self):
        """Áp dụng trạng thái solo/all lên curves, labels, và legend widgets."""
        solo = self._solo

        for i in range(self.num_temp):
            visible = (solo is None) or (solo == ("t", i))
            self._temp_curves[i].setVisible(visible)
            if not visible:
                self._temp_labels[i].hide()
            # Làm mờ legend widget nếu bị ẩn
            self._set_legend_dim(self._legend_temp_widgets[i], not visible)

        for i in range(self.num_pressure):
            visible = (solo is None) or (solo == ("p", i))
            self._pressure_curves[i].setVisible(visible)
            if not visible:
                self._pressure_labels[i].hide()
            self._set_legend_dim(self._legend_pressure_widgets[i], not visible)

    def _set_legend_dim(self, widget: QWidget, dimmed: bool):
        """Làm mờ widget legend khi series bị ẩn."""
        widget.setProperty("dimmed", dimmed)
        widget.setStyleSheet(
            "opacity: 0.3;" if dimmed else ""
        )
        # QWidget không hỗ trợ CSS opacity trực tiếp — dùng setGraphicsEffect
        from PySide6.QtWidgets import QGraphicsOpacityEffect
        effect = QGraphicsOpacityEffect(widget)
        effect.setOpacity(0.25 if dimmed else 1.0)
        widget.setGraphicsEffect(effect)

    def _create_plot_widget(self):
        self.plot = pg.PlotWidget()

        self.plot.setBackground(None)

        self.plot.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.plot.showGrid(x=True, y=True, alpha=0.1)

        self.plot.setYRange(*self.temp_range)
        self.plot.disableAutoRange()
        self.plot.setMouseEnabled(
            x=True,
            y=False
        )
        self.plot.plotItem.getViewBox().setDefaultPadding(0)
        self.plot.plotItem.layout.setContentsMargins(0, 0, 0, 0)
        self.plot.plotItem.layout.setHorizontalSpacing(0)
        
    def _create_axes(self):
        font_tick = QFont(self._font_family, FONT_SIZE_SM)

        axis_style = {
            "color": "black",
            "font-family": self._font_family,
            "font-size": f"{FONT_SIZE_MD}pt",
            "font-weight": 500,
        }

        for axis_name in ("bottom", "left", "right"):
            ax = self.plot.getAxis(axis_name)

            ax.setTickFont(font_tick)
            ax.setTextPen(pg.mkPen("#94A3B8"))
            ax.setPen(pg.mkPen("#334155"))

        self.plot.setLabel("left", self.temp_label, **axis_style)

        date_axis = _FixedTickDateAxis(
            orientation="bottom",
            tick_spacing=15
        )

        date_axis.setTickFont(font_tick)

        self.plot.setAxisItems({
            "bottom": date_axis
        })

        self.plot.getAxis("bottom").setLabel(
            "Time",
            **axis_style
        )
        
    def _create_pressure_viewbox(self):

        font_tick = QFont(self._font_family, FONT_SIZE_SM)

        self._vb_pressure = pg.ViewBox()

        self._vb_pressure.setDefaultPadding(0)

        self._vb_pressure.disableAutoRange()

        self._vb_pressure.setYRange(
            *self.pressure_range
        )

        self.plot.scene().addItem(
            self._vb_pressure
        )

        old_axis = self.plot.getAxis("right")

        self.plot.plotItem.layout.removeItem(old_axis)

        old_axis.hide()

        axis_right = FixedAxis(
            orientation="right"
        )

        self.plot.plotItem.axes["right"]["item"] = axis_right

        self.plot.plotItem.layout.addItem(
            axis_right,
            2,
            3
        )

        axis_right.setTickFont(font_tick)

        axis_right.setTextPen(
            pg.mkPen("#94A3B8")
        )

        axis_right.setPen(
            pg.mkPen("#334155")
        )

        axis_right.setWidth(55)

        axis_right.enableAutoSIPrefix(False)

        axis_right.linkToView(
            self._vb_pressure
        )

        axis_style = {
            "color": "black",
            "font-family": self._font_family,
            "font-size": f"{FONT_SIZE_MD}pt",
            "font-weight": 500,
        }

        axis_right.setLabel(
            self.pressure_label,
            **axis_style
        )

        self._vb_pressure.setMouseEnabled(
            x=False,
            y=False
        )

        self.plot.getViewBox().sigResized.connect(
            self._sync_views
        )

        self.plot.getViewBox().sigRangeChanged.connect(
            self._sync_views
        )
            
    def _create_temp_curves(self):
        self._temp_curves = []

        for i in range(self.num_temp):
            pen = pg.mkPen(
                color=TEMP_COLORS[i],
                width=2
            )

            curve = self.plot.plot(pen=pen)

            self._temp_curves.append(curve)
        
    def _create_pressure_curves(self):
        self._pressure_curves = []

        for i in range(self.num_pressure):
            pen = pg.mkPen(
                color=PRESSURE_COLORS[i],
                width=2,
                style=Qt.PenStyle.DashLine
            )

            curve = pg.PlotDataItem(pen=pen)

            self._vb_pressure.addItem(curve)

            self._pressure_curves.append(curve)
            
    def _create_end_labels(self):
        self._create_temp_labels()
        if self.num_pressure > 0:
            self._create_pressure_labels()
        
    def _create_temp_labels(self):
        self._temp_labels = []

        for i in range(self.num_temp):
            
            item = pg.TextItem(
                text="",
                color=TEMP_COLORS[i],
                anchor=(0, 0.5),
                border=None
            )

            item.setFont(
                QFont(
                    self._font_family,
                    FONT_SIZE_SM,
                    QFont.Weight.Bold
                )
            )
            item.fill = pg.mkBrush(0, 0, 0, 0)

            item.hide()

            self.plot.addItem(item)

            self._temp_labels.append(item)

    def _create_pressure_labels(self):
        self._pressure_labels = []

        for i in range(self.num_pressure):
            
            item = pg.TextItem(
                text="",
                color=PRESSURE_COLORS[i],
                anchor=(0, 0.5),
                border=None
            )

            item.setFont(
                QFont(
                    self._font_family,
                    FONT_SIZE_SM,
                    QFont.Weight.Bold
                )
            )
            item.fill = pg.mkBrush(0, 0, 0, 0)

            item.hide()

            self._vb_pressure.addItem(item)

            self._pressure_labels.append(item)

    # ── Sync ViewBox phụ ──────────────────────────────────────────────────────
    def _sync_pressure_vb(self):
        self._vb_pressure.setGeometry(
            self.plot.getViewBox().sceneBoundingRect()
        )

    def _sync_views(self):

        main_vb = self.plot.getViewBox()

        self._vb_pressure.setGeometry(
            main_vb.sceneBoundingRect()
        )

    # ── Timer trục X ─────────────────────────────────────────────────────────
    def _start_axis_timer(self):
        self._axis_timer = QTimer(self)
        self._axis_timer.timeout.connect(self._update_axis)
        self._axis_timer.start(1000)
        self._update_axis()

    def _update_axis(self):

        now = time.time()

        right_pad = self.max_seconds * 0.2

        x_min = now - self.max_seconds
        x_max = now + right_pad

        self.plot.setXRange(
            x_min,
            x_max,
            padding=0
        )

        if self.num_pressure > 0:
            self._vb_pressure.setRange(
                xRange=(x_min, x_max),
                padding=0
            )

    def _update_y_ranges(self):

        # ===== Temperature =====
        temp_values = []

        for arr in self._ty:
            temp_values.extend(arr)

        if temp_values:

            t_max = max(temp_values)

            top_pad = max(t_max * 0.1, 1)
            bottom_pad = max(t_max * 0.03, 2)

            self.plot.setRange(
                yRange=(-bottom_pad, t_max + top_pad),
                padding=0
            )
        # ===== Pressure =====
        if self.num_pressure > 0:
            pressure_values = []

            for arr in self._py:
                pressure_values.extend(arr)

            if pressure_values:

                p_max = max(pressure_values)

                top_pad = max(p_max * 0.25, 1)
                bottom_pad = -0.1

                self._vb_pressure.setYRange(
                    bottom_pad, 
                    p_max + top_pad,
                    padding=0
                )

    # ── Cập nhật end-of-line labels ───────────────────────────────────────────
    def _update_end_labels(self):
        solo = self._solo

        for i in range(self.num_temp):
            visible = (solo is None) or (solo == ("t", i))
            if not self._tx[i] or not visible:
                self._temp_labels[i].hide()
                continue
            lx, ly = self._tx[i][-1], self._ty[i][-1]
            self._temp_labels[i].setText(f"{ly:.1f}{self._temp_unit} ")
            self._temp_labels[i].setPos(lx - 0.1, ly)
            self._temp_labels[i].show()

        for i in range(self.num_pressure):
            visible = (solo is None) or (solo == ("p", i))
            if not self._px[i] or not visible:
                self._pressure_labels[i].hide()
                continue
            lx, ly = self._px[i][-1], self._py[i][-1]
            self._pressure_labels[i].setText(f"{ly:.2f} bar ")
            self._pressure_labels[i].setPos(lx - 0.1, ly)
            self._pressure_labels[i].show()

    # ── Public API ─────────────────────────────────────────────────────────────
    def append_data(
        self,
        temp_values: List[float],
        pressure_values: List[float] | None = None
        ):

        if pressure_values is None:
            pressure_values = []

        if len(temp_values) != self.num_temp:
            print(
                f"[{self.title}] "
                f"Cần {self.num_temp} giá trị nhiệt độ, "
                f"nhận {len(temp_values)}"
            )
            return

        if len(pressure_values) != self.num_pressure:
            print(
                f"[{self.title}] "
                f"Cần {self.num_pressure} giá trị áp suất, "
                f"nhận {len(pressure_values)}"
            )
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

        self._update_y_ranges()
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

        if self.num_pressure > 0:
            self._vb_pressure.setYRange(
                y_min,
                y_max
            )

    def set_temp_label(self, label: str, unit: str = "°C"):
        axis_style = {
            "color": "black",
            "font-family": self._font_family,
            "font-size": f"{FONT_SIZE_MD}pt",
            "font-weight": 500,
        }
        self.plot.setLabel("left", label, **axis_style)
        self.temp_label = label
        self._temp_unit = unit

    def clear(self):
        """Xoá toàn bộ dữ liệu."""
        for i in range(self.num_temp):
            self._tx[i].clear(); self._ty[i].clear()
            self._temp_curves[i].setData([], [])
            self._temp_labels[i].hide()
        if self.num_pressure > 0:
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