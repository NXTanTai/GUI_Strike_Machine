
from __future__ import annotations

import datetime
import time
from typing import List

import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import Qt, QMutex, QMutexLocker, QTimer, Signal  
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QGraphicsOpacityEffect,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# ── Màu sắc ───────────────────────────────────────────────────────────────────
TEMP_COLORS     = ["#E53935", "#4C1083", "#FB8C00", "#F72668"]   # tối đa 4 series
PRESSURE_COLORS = ["#8E24AA", "#1E88E5", "#00ACC1"]              # tối đa 3 series

# ── Font ──────────────────────────────────────────────────────────────────────
FONT_FAMILY  = "Segoe UI"
FONT_SIZE_LG = 14
FONT_SIZE_MD = 14
FONT_SIZE_SM = 13

# ── Ngưỡng skip setRange() ────────────────────────────────────────────────────
_Y_THRESH = 0.02   # 2% — chỉ update Y khi max thay đổi > 2%
_X_THRESH = 0.5    # 0.5 s — chỉ update X khi window dịch > 0.5 s


# ══════════════════════════════════════════════════════════════════════════════
# Circular buffer
# ══════════════════════════════════════════════════════════════════════════════

class _CircBuf:
    """
    Pre-allocated 1-D numpy circular buffer — theo SO approach.

    - append()  O(1), không malloc, ghi thẳng vào slot.
    - get()     trả về np.roll() theo thứ tự thời gian.
    - last()    phần tử cuối cùng.
    - reset()   xoá sạch.

    Capacity = max_seconds × sample_rate — caller chịu trách nhiệm
    đặt đủ lớn; buffer tự wrap-around khi đầy (oldest bị ghi đè).
    """

    __slots__ = ("_buf", "_head", "_cap", "_filled", "_out")

    def __init__(self, capacity: int) -> None:
        self._buf    = np.zeros(capacity, dtype=np.float64)
        self._head   = 0
        self._cap    = capacity
        self._filled = False
        self._out = np.empty(capacity, dtype=np.float64)

    def append(self, val: float) -> None:
        """Ghi val vào slot hiện tại, O(1)."""
        self._buf[self._head] = val
        self._head += 1
        if self._head >= self._cap:
            self._head   = 0
            self._filled = True

    def get(self) -> np.ndarray:
        if self._filled:
            n = self._cap - self._head
            self._out[:n] = self._buf[self._head:]
            self._out[n:self._cap] = self._buf[:self._head]
            return self._out
        return self._buf[: self._head]
    
    def last(self) -> float | None:
        """Giá trị mới nhất, hoặc None nếu chưa có data."""
        if self._head == 0 and not self._filled:
            return None
        return float(self._buf[(self._head - 1) % self._cap])

    def reset(self) -> None:
        """Xoá sạch buffer."""
        self._buf[:] = 0.0
        self._head   = 0
        self._filled = False

    def __len__(self) -> int:
        return self._cap if self._filled else self._head


# ══════════════════════════════════════════════════════════════════════════════
# Trục tuỳ chỉnh
# ══════════════════════════════════════════════════════════════════════════════

class _FixedTickDateAxis(pg.DateAxisItem):
    """DateAxisItem với tick cố định mỗi tick_spacing giây."""

    def __init__(self, tick_spacing: int = 10, **kwargs) -> None:
        super().__init__(**kwargs)
        self._tick_spacing = tick_spacing

    def tickValues(self, minVal, maxVal, size):
        step  = self._tick_spacing
        start = (int(minVal) // step) * step
        ticks = list(range(start, int(maxVal) + step, step))
        return [(step, ticks)]

    def tickStrings(self, values, scale, spacing):
        result = []
        for v in values:
            try:
                result.append(datetime.datetime.fromtimestamp(v).strftime("%H:%M:%S"))
            except Exception:
                result.append("")
        return result


class _FixedAxis(pg.AxisItem):
    """AxisItem hiển thị 2 chữ số thập phân."""

    def tickStrings(self, values, scale, spacing):
        return [f"{v:.2f}" for v in values]


# ══════════════════════════════════════════════════════════════════════════════
# CustomChartWidget
# ══════════════════════════════════════════════════════════════════════════════

class CustomChartWidget(QWidget):
    """
    Real-time chart với dual Y-axis.

    Trục trái  : nhiệt độ  — nét liền
    Trục phải  : áp suất   — nét đứt, ViewBox riêng

    Parameters
    ----------
    title            : Tiêu đề hiển thị / nút setting
    num_temp         : Số series nhiệt độ  (1-4)
    num_pressure     : Số series áp suất   (0-3)
    temp_label       : Nhãn trục trái
    pressure_label   : Nhãn trục phải
    temp_range       : (min, max) trục trái   — dùng khi chưa có data
    pressure_range   : (min, max) trục phải   — dùng khi chưa có data
    max_seconds      : Cửa sổ thời gian hiển thị (giây)
    render_interval  : Chu kỳ render (ms), mặc định 100 ms ≈ 10 Hz
    chart_font       : QFont tuỳ chỉnh (None = dùng mặc định)
    parent           : Widget cha
    """
    clicked = Signal()
    
    def __init__(
        self,
        title: str                       = "Chart",
        num_temp: int                    = 1,
        num_pressure: int                = 1,
        temp_label: str                  = "Temperature (°C)",
        pressure_label: str              = "Pressure (bar)",
        temp_range: tuple[float, float]  = (0, 200),
        pressure_range: tuple[float, float] = (0, 10),
        max_seconds: int                 = 60,
        render_interval: int             = 100,
        chart_font: QFont | None         = None,
        parent: QWidget | None           = None,
    ) -> None:
        super().__init__(parent)

        # ── Lưu config ────────────────────────────────────────────────────────
        self.title           = title
        self.num_temp        = min(max(num_temp, 0), len(TEMP_COLORS))
        self.num_pressure    = min(max(num_pressure, 0), len(PRESSURE_COLORS))
        self.temp_label      = temp_label
        self.pressure_label  = pressure_label
        self.temp_range      = temp_range
        self.pressure_range  = pressure_range
        self.max_seconds     = max_seconds
        self._temp_unit      = "°C"
        self._sim_timer: QTimer | None = None
        self._last_temp_label_pos:     list[tuple[float, float] | None] = [None] * self.num_temp
        self._last_pressure_label_pos: list[tuple[float, float] | None] = [None] * self.num_pressure

        if chart_font:
            self._font_family  = chart_font.family()
            self._font_size_lg = chart_font.pointSize() or FONT_SIZE_LG
        else:
            self._font_family  = FONT_FAMILY
            self._font_size_lg = FONT_SIZE_LG

        # ── Circular buffers (pre-allocated) ──────────────────────────────────
        # Dự phòng tối đa 20 sample/s × max_seconds
        _cap = max_seconds * 20
        self._tx: list[_CircBuf] = [_CircBuf(_cap) for _ in range(self.num_temp)]
        self._ty: list[_CircBuf] = [_CircBuf(_cap) for _ in range(self.num_temp)]
        self._px: list[_CircBuf] = [_CircBuf(_cap) for _ in range(self.num_pressure)]
        self._py: list[_CircBuf] = [_CircBuf(_cap) for _ in range(self.num_pressure)]

        # ── Mutex bảo vệ buffer khi worker thread ghi ─────────────────────────
        self._mutex = QMutex()

        # ── Cache Y/X range để skip setRange() thừa ───────────────────────────
        self._last_temp_ymax: float | None = None
        self._last_pres_ymax: float | None = None
        self._last_x_min:     float | None = None

        # ── Legend visibility — True = hiển thị, False = ẩn (toggle độc lập) ──
        self._vis_temp:     list[bool] = [True] * self.num_temp
        self._vis_pressure: list[bool] = [True] * self.num_pressure

        # ── Build UI & chart ──────────────────────────────────────────────────
        self._setup_ui()
        self._setup_chart()

        # ── Render timer (main thread only) ───────────────────────────────────
        self._render_timer = QTimer(self)
        self._render_timer.timeout.connect(self._render_frame)
        self._render_timer.start(render_interval)

    # ══════════════════════════════════════════════════════════════════════════
    # UI setup
    # ══════════════════════════════════════════════════════════════════════════
    def mouseDoubleClickEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mouseDoubleClickEvent(event)
        
    def _setup_ui(self) -> None:
        self._root = QVBoxLayout(self)
        self._root.setContentsMargins(4, 4, 4, 4)
        self._root.setSpacing(2)

    def _setup_chart(self) -> None:
        pg.setConfigOptions(antialias=False, useOpenGL=True)

        self._create_title()
        self._create_legend()
        self._create_plot_widget()
        self._create_axes()

        if self.num_pressure > 0:
            self._create_pressure_viewbox()

        self._create_temp_curves()

        if self.num_pressure > 0:
            self._create_pressure_curves()

        self._create_end_labels()
        self._root.addWidget(self.plot)

    # ── Title ─────────────────────────────────────────────────────────────────

    def _create_title(self) -> None:
        font_btn = QFont(self._font_family, self._font_size_lg, QFont.Weight.Bold)

        self.btn_setting = QPushButton(self.title)
        self.btn_setting.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_setting.setFont(font_btn)
        self.btn_setting.setStyleSheet(
            "QPushButton { border: none; color: black; }"
            "QPushButton:hover { background: #F0F9FF; }"
        )

        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)
        row.addStretch()
        row.addWidget(self.btn_setting)
        row.addStretch()
        self._root.addLayout(row)

    # ── Legend ────────────────────────────────────────────────────────────────

    def _create_legend(self) -> None:
        bar = QHBoxLayout()
        bar.setContentsMargins(8, 0, 8, 2)
        bar.setSpacing(16)
        bar.addStretch()

        self._legend_temp:             list[QLabel]  = []
        self._legend_pressure:         list[QLabel]  = []
        self._legend_temp_widgets:     list[QWidget] = []
        self._legend_pressure_widgets: list[QWidget] = []

        font = QFont(self._font_family, FONT_SIZE_SM, QFont.Weight.Bold)

        _temp_names     = ["SV", "T1", "T2", "T3"]
        _pressure_names = ["Pressure SV", "Pressure", "P3"]

        for i in range(self.num_temp):
            w = self._build_legend_item(
                _temp_names[i], TEMP_COLORS[i], font,
                dashed=False, kind="t", index=i,
                label_list=self._legend_temp,
            )
            bar.addWidget(w)
            self._legend_temp_widgets.append(w)

        if self.num_temp > 0 and self.num_pressure > 0:
            sep = QFrame()
            sep.setFixedSize(1, 14)
            sep.setStyleSheet("background: #CBD5E1;")
            bar.addWidget(sep)

        for i in range(self.num_pressure):
            w = self._build_legend_item(
                _pressure_names[i], PRESSURE_COLORS[i], font,
                dashed=True, kind="p", index=i,
                label_list=self._legend_pressure,
            )
            bar.addWidget(w)
            self._legend_pressure_widgets.append(w)

        bar.addStretch()
        self._root.addLayout(bar)

    def _build_legend_item(
        self,
        text: str,
        color: str,
        font: QFont,
        *,
        dashed: bool,
        kind: str,
        index: int,
        label_list: list[QLabel],
    ) -> QWidget:
        dot = QFrame()
        dot.setFixedSize(14, 4)
        if dashed:
            dot.setStyleSheet(f"""
                background: qlineargradient(
                    x1:0,y1:0,x2:1,y2:0,
                    stop:0 {color}, stop:0.4 {color},
                    stop:0.5 transparent, stop:0.9 transparent,
                    stop:1 {color}
                );
                border-radius: 1px;
            """)
        else:
            dot.setStyleSheet(f"background: {color}; border-radius: 2px;")

        lbl = QLabel(text)
        lbl.setStyleSheet("background: transparent;")
        lbl.setFont(font)
        label_list.append(lbl)

        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(4)
        row.addWidget(dot)
        row.addWidget(lbl)

        w = QWidget()
        w.setLayout(row)
        w.setCursor(Qt.CursorShape.PointingHandCursor)
        # w.setToolTip(f"Click để chỉ hiện {text} / click lại để hiện tất cả")

        def _on_click(_, k=kind, i=index):
            self._on_legend_click(k, i)

        w.mousePressEvent = _on_click
        return w

    # ── Legend toggle ─────────────────────────────────────────────────────────

    def _on_legend_click(self, kind: str, index: int) -> None:
        """Toggle ẩn/hiện series được click — độc lập với các series khác."""
        if kind == "t":
            self._vis_temp[index] = not self._vis_temp[index]
            visible = self._vis_temp[index]
            self._temp_curves[index].setVisible(visible)
            if not visible:
                self._temp_labels[index].hide()
            self._set_legend_dim(self._legend_temp_widgets[index], not visible)
        else:
            self._vis_pressure[index] = not self._vis_pressure[index]
            visible = self._vis_pressure[index]
            self._pressure_curves[index].setVisible(visible)
            if not visible:
                self._pressure_labels[index].hide()
            self._set_legend_dim(self._legend_pressure_widgets[index], not visible)

    def _apply_visibility(self) -> None:
        """Áp dụng lại toàn bộ trạng thái visibility (dùng sau clear/reset)."""
        for i in range(self.num_temp):
            vis = self._vis_temp[i]
            self._temp_curves[i].setVisible(vis)
            if not vis:
                self._temp_labels[i].hide()
            self._set_legend_dim(self._legend_temp_widgets[i], not vis)

        for i in range(self.num_pressure):
            vis = self._vis_pressure[i]
            self._pressure_curves[i].setVisible(vis)
            if not vis:
                self._pressure_labels[i].hide()
            self._set_legend_dim(self._legend_pressure_widgets[i], not vis)

    @staticmethod
    def _set_legend_dim(widget: QWidget, dimmed: bool) -> None:
        fx = QGraphicsOpacityEffect(widget)
        fx.setOpacity(0.25 if dimmed else 1.0)
        widget.setGraphicsEffect(fx)

    # ── PlotWidget ────────────────────────────────────────────────────────────

    def _create_plot_widget(self) -> None:
        self.plot = pg.PlotWidget()
        self.plot.setBackground(None)
        self.plot.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.plot.showGrid(x=True, y=True, alpha=0.1)
        self.plot.setYRange(*self.temp_range)
        self.plot.disableAutoRange()
        self.plot.setMouseEnabled(x=False, y=False)
        self.plot.plotItem.getViewBox().setDefaultPadding(0)
        self.plot.plotItem.layout.setContentsMargins(0, 0, 0, 0)
        self.plot.plotItem.layout.setHorizontalSpacing(0)

        # SO: tắt antialiasing adjust và dùng NoIndex để scene nhanh hơn
        self.plot.setAntialiasing(False)
        self.plot.setOptimizationFlag(
            pg.QtWidgets.QGraphicsView.OptimizationFlag.DontAdjustForAntialiasing
        )
        self.plot.scene().setItemIndexMethod(
            pg.QtWidgets.QGraphicsScene.ItemIndexMethod.NoIndex
        )

    # ── Axes ──────────────────────────────────────────────────────────────────

    def _create_axes(self) -> None:
        font_tick  = QFont(self._font_family, FONT_SIZE_SM)
        axis_style = {
            "color":       "black",
            "font-family": self._font_family,
            "font-size":   f"{FONT_SIZE_MD}pt",
            "font-weight": 500,
        }

        for name in ("bottom", "left", "right"):
            ax = self.plot.getAxis(name)
            ax.setTickFont(font_tick)
            ax.setTextPen(pg.mkPen("#94A3B8"))
            ax.setPen(pg.mkPen("#334155"))

        self.plot.setLabel("left", self.temp_label, **axis_style)

        date_axis = _FixedTickDateAxis(orientation="bottom", tick_spacing=15)
        date_axis.setTickFont(font_tick)
        self.plot.setAxisItems({"bottom": date_axis})
        self.plot.getAxis("bottom").setLabel("Time", **axis_style)
        self.plot.getAxis("left").setWidth(65)
        self.plot.getAxis("bottom").setHeight(60)

    # ── Pressure ViewBox (trục phải) ──────────────────────────────────────────

    def _create_pressure_viewbox(self) -> None:
        font_tick  = QFont(self._font_family, FONT_SIZE_SM)
        axis_style = {
            "color":       "black",
            "font-family": self._font_family,
            "font-size":   f"{FONT_SIZE_MD}pt",
            "font-weight": 500,
        }

        self._vb_pressure = pg.ViewBox()
        self._vb_pressure.setDefaultPadding(0)
        self._vb_pressure.disableAutoRange()
        self._vb_pressure.setYRange(*self.pressure_range)
        self._vb_pressure.setMouseEnabled(x=False, y=False)
        self.plot.scene().addItem(self._vb_pressure)

        # Thay thế trục phải mặc định
        old_axis = self.plot.getAxis("right")
        self.plot.plotItem.layout.removeItem(old_axis)
        old_axis.hide()

        axis_right = _FixedAxis(orientation="right")
        self.plot.plotItem.axes["right"]["item"] = axis_right
        self.plot.plotItem.layout.addItem(axis_right, 2, 3)
        axis_right.setTickFont(font_tick)
        axis_right.setTextPen(pg.mkPen("#94A3B8"))
        axis_right.setPen(pg.mkPen("#334155"))
        axis_right.setWidth(65)
        axis_right.enableAutoSIPrefix(False)
        axis_right.linkToView(self._vb_pressure)
        axis_right.setLabel(self.pressure_label, **axis_style)

        # Sync geometry khi main ViewBox thay đổi
        self.plot.getViewBox().sigResized.connect(self._sync_views)
        self.plot.getViewBox().sigRangeChanged.connect(self._sync_views)

    def _sync_views(self) -> None:
        self._vb_pressure.setGeometry(self.plot.getViewBox().sceneBoundingRect())

    # ── Curves ────────────────────────────────────────────────────────────────

    def _create_temp_curves(self) -> None:
        self._temp_curves: list[pg.PlotDataItem] = []
        for i in range(self.num_temp):
            curve = pg.PlotCurveItem(
                pen=pg.mkPen(color=TEMP_COLORS[i], width=2),
                skipFiniteCheck=True, clipToView=True,
            )
            self.plot.addItem(curve)
            self._temp_curves.append(curve)

    def _create_pressure_curves(self) -> None:
        self._pressure_curves: list[pg.PlotDataItem] = []
        for i in range(self.num_pressure):
            pen   = pg.mkPen(color=PRESSURE_COLORS[i], width=2, style=Qt.PenStyle.DashLine)
            curve = pg.PlotCurveItem(
                pen=pen,
                skipFiniteCheck=True,
                clipToView=True,
            )
            self._vb_pressure.addItem(curve)
            self._pressure_curves.append(curve)

    # ── End-of-line labels ────────────────────────────────────────────────────

    def _create_end_labels(self) -> None:
        self._temp_labels:     list[pg.TextItem] = []
        self._pressure_labels: list[pg.TextItem] = []

        font = QFont(self._font_family, FONT_SIZE_SM, QFont.Weight.Bold)

        for i in range(self.num_temp):
            item = pg.TextItem(text="", color=TEMP_COLORS[i], anchor=(0, 0.5))
            item.setFont(font)
            item.fill = pg.mkBrush(0, 0, 0, 0)
            item.hide()
            self.plot.addItem(item)
            self._temp_labels.append(item)

        for i in range(self.num_pressure):
            item = pg.TextItem(text="", color=PRESSURE_COLORS[i], anchor=(0, 0.5))
            item.setFont(font)
            item.fill = pg.mkBrush(0, 0, 0, 0)
            item.hide()
            self._vb_pressure.addItem(item)
            self._pressure_labels.append(item)

    # ══════════════════════════════════════════════════════════════════════════
    # Render frame — chạy trên main thread mỗi render_interval ms
    # ══════════════════════════════════════════════════════════════════════════

    def _render_frame(self) -> None:
        """
        Điểm DUY NHẤT cập nhật UI.
        Lock mutex để đọc snapshot buffer, sau đó render ngoài lock.
        """
        # ── Snapshot buffer (lock ngắn nhất có thể) ───────────────────────────
        if not self._mutex.tryLock(5):
            return  # render frame này bỏ qua, frame sau render bù

        try:
            tx_snap = [buf.get() for buf in self._tx]
            ty_snap = [buf.get() for buf in self._ty]
            px_snap = [buf.get() for buf in self._px]
            py_snap = [buf.get() for buf in self._py]
        finally:
            self._mutex.unlock()
        # ── Cập nhật temp curves ──────────────────────────────────────────────
        for i in range(self.num_temp):
            if len(tx_snap[i]) == 0:
                continue
            self._temp_curves[i].setData(tx_snap[i], ty_snap[i])

        # ── Cập nhật pressure curves ──────────────────────────────────────────
        for i in range(self.num_pressure):
            if len(px_snap[i]) == 0:
                continue
            self._pressure_curves[i].setData(px_snap[i], py_snap[i])

        # ── X-range ───────────────────────────────────────────────────────────
        now       = time.time()
        x_min     = now - self.max_seconds
        x_max     = now + self.max_seconds * 0.2

        if self._last_x_min is None or abs(x_min - self._last_x_min) > _X_THRESH:
            self.plot.setXRange(x_min, x_max, padding=0)
            if self.num_pressure > 0:
                self._vb_pressure.setRange(xRange=(x_min, x_max), padding=0)
            self._last_x_min = x_min

        # ── Y-range temp ──────────────────────────────────────────────────────
        t_max = None
        for arr in ty_snap:
            if len(arr):
                m = float(arr.max())
                if t_max is None or m > t_max:
                    t_max = m
        if t_max is not None:
            new_ymax = t_max + max(t_max * 0.1, 1)
            new_ymin = -max(t_max * 0.03, 2)
            prev     = self._last_temp_ymax
            if prev is None or abs(new_ymax - prev) / max(abs(prev), 1.0) > _Y_THRESH:
                self.plot.setRange(yRange=(new_ymin, new_ymax), padding=0)
                self._last_temp_ymax = new_ymax

        # ── Y-range pressure ──────────────────────────────────────────────────
        if self.num_pressure > 0:
            p_max = None
            for arr in py_snap:
                if len(arr):
                    m = float(arr.max())
                    if p_max is None or m > p_max:
                        p_max = m
            if p_max is not None:
                new_ymax = p_max + max(p_max * 0.25, 1)
                prev     = self._last_pres_ymax
                if prev is None or abs(new_ymax - prev) / max(abs(prev), 1.0) > _Y_THRESH:
                    self._vb_pressure.setYRange(-0.1, new_ymax, padding=0)
                    self._last_pres_ymax = new_ymax

        # ── End-of-line labels ────────────────────────────────────────────────
        for i in range(self.num_temp):
            if not self._vis_temp[i] or len(tx_snap[i]) == 0:
                self._temp_labels[i].hide()
                self._last_temp_label_pos[i] = None
                continue
            lx = float(tx_snap[i][-1])
            ly = float(ty_snap[i][-1])
            if self._last_temp_label_pos[i] != (lx, ly):
                self._temp_labels[i].setText(f"{ly:.1f}{self._temp_unit} ")
                self._temp_labels[i].setPos(lx - 0.1, ly)
                self._last_temp_label_pos[i] = (lx, ly)
            self._temp_labels[i].show()

        for i in range(self.num_pressure):
            if not self._vis_pressure[i] or len(px_snap[i]) == 0:
                self._pressure_labels[i].hide()
                self._last_pressure_label_pos[i] = None
                continue
            lx = float(px_snap[i][-1])
            ly = float(py_snap[i][-1])
            if self._last_pressure_label_pos[i] != (lx, ly):
                self._pressure_labels[i].setText(f"{ly:.2f} bar ")
                self._pressure_labels[i].setPos(lx - 0.1, ly)
                self._last_pressure_label_pos[i] = (lx, ly)
            self._pressure_labels[i].show()

    # ══════════════════════════════════════════════════════════════════════════
    # Public API
    # ══════════════════════════════════════════════════════════════════════════

    def append_data(
        self,
        temp_values: List[float],
        pressure_values: List[float] | None = None,
    ) -> None:
        """
        Ghi data vào buffer.

        Thread-safe — có thể gọi từ worker thread.
        KHÔNG đụng bất kỳ UI object nào.

        Parameters
        ----------
        temp_values      : list có đúng num_temp phần tử
        pressure_values  : list có đúng num_pressure phần tử (None → [])
        """
        if pressure_values is None:
            pressure_values = []

        if len(temp_values) != self.num_temp:
            print(f"[{self.title}] Cần {self.num_temp} temp values, nhận {len(temp_values)}")
            return
        if len(pressure_values) != self.num_pressure:
            print(f"[{self.title}] Cần {self.num_pressure} pressure values, nhận {len(pressure_values)}")
            return

        now = time.time()

        with QMutexLocker(self._mutex):
            for i in range(self.num_temp):
                self._tx[i].append(now)
                self._ty[i].append(temp_values[i])
            for i in range(self.num_pressure):
                self._px[i].append(now)
                self._py[i].append(pressure_values[i])

    def set_temp_series_name(self, index: int, name: str) -> None:
        """Đổi tên legend series nhiệt độ."""
        if 0 <= index < self.num_temp:
            self._legend_temp[index].setText(name)

    def set_pressure_series_name(self, index: int, name: str) -> None:
        """Đổi tên legend series áp suất."""
        if 0 <= index < self.num_pressure:
            self._legend_pressure[index].setText(name)

    def set_temp_range(self, y_min: float, y_max: float) -> None:
        """Đặt Y-range trục nhiệt độ và reset cache."""
        self.temp_range      = (y_min, y_max)
        self._last_temp_ymax = None
        self.plot.setYRange(y_min, y_max)

    def set_pressure_range(self, y_min: float, y_max: float) -> None:
        """Đặt Y-range trục áp suất và reset cache."""
        self.pressure_range  = (y_min, y_max)
        self._last_pres_ymax = None
        if self.num_pressure > 0:
            self._vb_pressure.setYRange(y_min, y_max)

    def set_temp_label(self, label: str, unit: str = "°C") -> None:
        """Đổi nhãn và đơn vị trục nhiệt độ."""
        axis_style = {
            "color":       "black",
            "font-family": self._font_family,
            "font-size":   f"{FONT_SIZE_MD}pt",
            "font-weight": 500,
        }
        self.plot.setLabel("left", label, **axis_style)
        self.temp_label = label
        self._temp_unit = unit

    def set_render_interval(self, interval_ms: int) -> None:
        """Thay đổi chu kỳ render (ms)."""
        self._render_timer.setInterval(interval_ms)

    def clear(self) -> None:
        """Xoá toàn bộ data và reset cache."""
        with QMutexLocker(self._mutex):
            for i in range(self.num_temp):
                self._tx[i].reset()
                self._ty[i].reset()
            for i in range(self.num_pressure):
                self._px[i].reset()
                self._py[i].reset()

        # Reset UI trực tiếp (clear() luôn gọi từ main thread)
        for i in range(self.num_temp):
            self._temp_curves[i].setData([], [])
            self._temp_labels[i].hide()
        if self.num_pressure > 0:
            for i in range(self.num_pressure):
                self._pressure_curves[i].setData([], [])
                self._pressure_labels[i].hide()

        self._last_temp_ymax = None
        self._last_pres_ymax = None
        self._last_x_min     = None
        self._last_temp_label_pos     = [None] * self.num_temp
        self._last_pressure_label_pos = [None] * self.num_pressure

    # ══════════════════════════════════════════════════════════════════════════
    # Simulation (chỉ dùng để test)
    # ══════════════════════════════════════════════════════════════════════════

    def start_simulation(self, interval_ms: int = 500) -> None:
        """Bật giả lập dữ liệu ngẫu nhiên."""
        if self._sim_timer is None:
            self._sim_timer = QTimer(self)
            self._sim_timer.timeout.connect(self._simulate)
        self._sim_timer.start(interval_ms)

    def stop_simulation(self) -> None:
        """Tắt giả lập."""
        if self._sim_timer:
            self._sim_timer.stop()

    def _simulate(self) -> None:
        import random
        self.append_data(
            temp_values     = [random.uniform(*self.temp_range)     for _ in range(self.num_temp)],
            pressure_values = [random.uniform(*self.pressure_range) for _ in range(self.num_pressure)],
        )

    def showEvent(self, event) -> None:
        super().showEvent(event)
        if not self._render_timer.isActive():
            self._render_timer.start()

    def hideEvent(self, event) -> None:
        super().hideEvent(event)
        self._render_timer.stop()