from __future__ import annotations

import datetime
import time
from typing import List

import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import Qt, Signal
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

TEMP_COLORS     = ["#E53935", "#4C1083", "#FB8C00", "#F72668"]    # tối đa 4 series
PRESSURE_COLORS = ["#8E24AA", "#1E88E5", "#00ACC1"]                 # tối đa 3 series

FONT_FAMILY  = "Segoe UI"
FONT_SIZE_LG = 12
FONT_SIZE_MD = 12
FONT_SIZE_SM = 11

_Y_THRESH = 0.02   # 2% — chỉ update Y khi max thay đổi > 2%
# Dịch X mỗi tick → cuộn mượt. (Trước đây = 0.5 s để giảm repaint & tránh nét
# đứt bị trượt; giờ nét đứt đã neo pha trong _dashed_data nên không cần nữa.
# Đo được: chỉ tốn thêm ~1 ms/tick cho 4 chart.) Đặt lại 0.5 nếu máy yếu.
_X_THRESH = 0.0
# Nét đứt của đường SV được tự cắt (không dùng Qt DashLine) — đơn vị pixel.
# Pen width 2 + square cap → trông giống Qt.DashLine (nét ~10px, trống ~2px).
_DASH_ON     = 8.0
_DASH_PERIOD = 12.0


def _is_sv(index: int) -> bool:
    """Series đầu tiên của mỗi nhóm (nhiệt độ / áp suất) là SV → nét đứt; PV → nét liền."""
    return index == 0

# Cấu hình global của pyqtgraph — chỉ cần set 1 lần cho cả module
pg.setConfigOptions(antialias=False, useOpenGL=False)


class _CircBuf:
    """
    Circular buffer 1-D dạng "ghi đôi" (double-write), pre-allocated.

    Mảng nội bộ dài 2×cap; mỗi giá trị được ghi vào cả slot i và i+cap.
    Nhờ vậy dữ liệu theo thứ tự thời gian luôn là 1 đoạn liền mạch
    buf[head : head+cap] → get() trả về view, KHÔNG copy, O(1).

    - append()  O(1), không malloc.
    - get()     view theo thứ tự thời gian (cũ → mới).
    - reset()   xoá sạch.

    Lưu ý: get() trả về view vào buffer nội bộ — append() tiếp theo có
    thể ghi đè phần tử cũ nhất của view trước đó. Caller phải setData()
    lại mỗi lần render sau khi append (đúng như _render_frame đang làm).
    """

    __slots__ = ("_buf", "_head", "_cap", "_size")

    def __init__(self, capacity: int) -> None:
        self._buf  = np.zeros(2 * capacity, dtype=np.float64)
        self._head = 0          # slot ghi tiếp theo, trong [0, cap)
        self._cap  = capacity
        self._size = 0

    def append(self, val: float) -> None:
        h = self._head
        self._buf[h] = val
        self._buf[h + self._cap] = val
        h += 1
        self._head = 0 if h == self._cap else h
        if self._size < self._cap:
            self._size += 1

    def get(self) -> np.ndarray:
        if self._size < self._cap:
            # chưa đầy: head == size, data nằm ở [0, size)
            return self._buf[: self._size]
        return self._buf[self._head : self._head + self._cap]

    def reset(self) -> None:
        self._head = 0
        self._size = 0

    def __len__(self) -> int:
        return self._size


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


class CustomChartWidget(QWidget):
    """
    Real-time chart với dual Y-axis.

    Trục trái  : nhiệt độ  — nét liền
    Trục phải  : áp suất   — nét đứt, ViewBox riêng (X link với trục chính)

    Chart không tự render: caller gọi append_data() để thêm điểm và
    _render_frame() để vẽ (cả hai trên GUI thread).

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
    render_interval  : Không còn dùng (giữ để tương thích chữ ký cũ)
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

        self.title           = title
        self.num_temp        = min(max(num_temp, 0), len(TEMP_COLORS))
        self.num_pressure    = min(max(num_pressure, 0), len(PRESSURE_COLORS))
        self.temp_label      = temp_label
        self.pressure_label  = pressure_label
        self.temp_range      = temp_range
        self.pressure_range  = pressure_range
        self.max_seconds     = max_seconds
        self._temp_unit      = "°C"

        if chart_font:
            self._font_family  = chart_font.family()
            self._font_size_lg = chart_font.pointSize() or FONT_SIZE_LG
        else:
            self._font_family  = FONT_FAMILY
            self._font_size_lg = FONT_SIZE_LG

        self._axis_style = {
            "color":       "black",
            "font-family": self._font_family,
            "font-size":   f"{FONT_SIZE_MD}pt",
            "font-weight": 500,
        }

        # ── Circular buffers (pre-allocated) ──────────────────────────────────
        # Dự phòng tối đa 20 sample/s × max_seconds. Mọi series được append
        # cùng lúc nên dùng CHUNG 1 buffer thời gian (_t).
        _cap = max_seconds * 20
        self._t:  _CircBuf       = _CircBuf(_cap)
        self._ty: list[_CircBuf] = [_CircBuf(_cap) for _ in range(self.num_temp)]
        self._py: list[_CircBuf] = [_CircBuf(_cap) for _ in range(self.num_pressure)]

        # ── Cache Y-range để skip setRange() thừa ─────────────────────────────
        self._last_temp_ymax: float | None = None
        self._last_pres_ymax: float | None = None
        self._last_x_min:     float | None = None

        # ── Giữ pha nét đứt (đường SV) cố định khi cắt bớt điểm đầu ──────────
        self._n_total = 0                                            # tổng số mẫu đã append
        self._t_anchor: list[int | None] = [None] * self.num_temp      # index tuyệt đối điểm đầu đã vẽ
        self._t_phase:  list[float]      = [0.0] * self.num_temp       # pha nét đứt (px) tại điểm đầu
        self._p_anchor: list[int | None] = [None] * self.num_pressure
        self._p_phase:  list[float]      = [0.0] * self.num_pressure

        # ── Cache text nhãn cuối đường — chỉ setText() khi chuỗi hiển thị đổi ─
        self._last_temp_text:     list[str | None] = [None] * self.num_temp
        self._last_pressure_text: list[str | None] = [None] * self.num_pressure

        # ── Legend visibility — True = hiển thị, False = ẩn (toggle độc lập) ──
        self._vis_temp:     list[bool] = [True] * self.num_temp
        self._vis_pressure: list[bool] = [True] * self.num_pressure

        self._setup_ui()
        self._setup_chart()

    def mouseDoubleClickEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mouseDoubleClickEvent(event)

    def _setup_ui(self) -> None:
        self._root = QVBoxLayout(self)
        self._root.setContentsMargins(4, 4, 4, 4)
        self._root.setSpacing(2)

    def _setup_chart(self) -> None:
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

        _temp_names = ["SV", "T1", "T2", "T3"] if self.num_temp > 2 else ["SV", "T0"]
        _pressure_names = ["Pressure SV", "Pressure"]

        for i in range(self.num_temp):
            w = self._build_legend_item(
                _temp_names[i], TEMP_COLORS[i], font,
                dashed=_is_sv(i), kind="t", index=i,
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
                dashed=_is_sv(i), kind="p", index=i,
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

        # Tạo opacity effect 1 lần, các lần toggle chỉ đổi opacity
        fx = QGraphicsOpacityEffect(w)
        fx.setOpacity(1.0)
        w.setGraphicsEffect(fx)

        def _on_click(_, k=kind, i=index):
            self._on_legend_click(k, i)

        w.mousePressEvent = _on_click
        return w

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

    @staticmethod
    def _set_legend_dim(widget: QWidget, dimmed: bool) -> None:
        fx = widget.graphicsEffect()
        if fx is not None:
            fx.setOpacity(0.25 if dimmed else 1.0)

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

        # Tắt antialiasing adjust và dùng NoIndex để scene nhanh hơn
        self.plot.setAntialiasing(False)
        self.plot.setOptimizationFlag(
            pg.QtWidgets.QGraphicsView.OptimizationFlag.DontAdjustForAntialiasing
        )
        self.plot.scene().setItemIndexMethod(
            pg.QtWidgets.QGraphicsScene.ItemIndexMethod.NoIndex
        )

    def _create_axes(self) -> None:
        font_tick = QFont(self._font_family, FONT_SIZE_SM)

        for name in ("bottom", "left", "right"):
            ax = self.plot.getAxis(name)
            ax.setTickFont(font_tick)
            ax.setTextPen(pg.mkPen("#94A3B8"))
            ax.setPen(pg.mkPen("#334155"))

        self.plot.setLabel("left", self.temp_label, **self._axis_style)

        date_axis = _FixedTickDateAxis(orientation="bottom", tick_spacing=15)
        date_axis.setTickFont(font_tick)
        self.plot.setAxisItems({"bottom": date_axis})
        self.plot.getAxis("left").setWidth(65)

    def _create_pressure_viewbox(self) -> None:
        font_tick = QFont(self._font_family, FONT_SIZE_SM)

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
        axis_right.setLabel(self.pressure_label, **self._axis_style)

        # X của ViewBox áp suất bám theo ViewBox chính → chỉ cần setRange 1 lần
        main_vb = self.plot.getViewBox()
        self._vb_pressure.setXLink(main_vb)
        # Geometry chỉ đổi khi resize, không cần sync mỗi lần range đổi
        main_vb.sigResized.connect(self._sync_views)
        self._sync_views()

    def _sync_views(self) -> None:
        self._vb_pressure.setGeometry(self.plot.getViewBox().sceneBoundingRect())
        self._vb_pressure.linkedViewChanged(self.plot.getViewBox(), self._vb_pressure.XAxis)

    def _create_temp_curves(self) -> None:
        self._temp_curves: list[pg.PlotCurveItem] = []
        for i in range(self.num_temp):
            curve = pg.PlotCurveItem(
                pen=pg.mkPen(color=TEMP_COLORS[i], width=2),
                skipFiniteCheck=True,
            )
            self.plot.addItem(curve)
            self._temp_curves.append(curve)

    def _create_pressure_curves(self) -> None:
        self._pressure_curves: list[pg.PlotCurveItem] = []
        for i in range(self.num_pressure):
            # Pen luôn nét LIỀN — đường SV được cắt thành nét đứt bằng mảng
            # connect (xem _dashed_data)
            pen   = pg.mkPen(color=PRESSURE_COLORS[i], width=2)
            curve = pg.PlotCurveItem(pen=pen, skipFiniteCheck=True)
            self._vb_pressure.addItem(curve)
            self._pressure_curves.append(curve)

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

    @staticmethod
    def _update_end_label(
        item: pg.TextItem,
        last_text: list[str | None],
        i: int,
        text: str,
        x: float,
        y: float,
    ) -> None:
        # Chỉ setText khi chuỗi hiển thị thực sự đổi → không nhấp nháy,
        # và không bao giờ bị "đứng" khi giá trị tăng/giảm chậm.
        if text != last_text[i]:
            item.setText(text)
            last_text[i] = text
        item.setPos(x - 0.1, y)
        if not item.isVisible():
            item.show()

    def _render_frame(self) -> None:
        """Vẽ lại chart từ buffer. Gọi trên GUI thread."""
        now   = time.time()
        x_min = now - self.max_seconds
        x_max = now + self.max_seconds * 0.2

        x_changed = self._last_x_min is None or abs(x_min - self._last_x_min) > _X_THRESH
        if x_changed:
            self._last_x_min = x_min
        view_x_min = self._last_x_min   # mép trái thực tế đang hiển thị

        t_all = self._t.get()
        n_all = len(t_all)

        # Chỉ lấy phần data nằm trong cửa sổ hiển thị (+1 điểm bên trái để
        # đường vẽ chạm mép trái). t tăng dần → searchsorted O(log n).
        # PlotCurveItem không tự clip, nên đây là chỗ cắt bớt số điểm vẽ.
        start = max(int(np.searchsorted(t_all, view_x_min)) - 1, 0) if n_all else 0
        t = t_all[start:]
        has_data = len(t) > 0
        lx = float(t[-1]) if has_data else 0.0

        base_abs = self._n_total - n_all      # index tuyệt đối của t_all[0]

        # ── Nhiệt độ: cập nhật range TRƯỚC, rồi mới vẽ ────────────────────────
        # (đường SV nét đứt cần tỉ lệ pixel đúng của frame này)
        # Y-max tính trên TOÀN buffer (không chỉ phần đang hiện) để thang Y
        # ổn định — đỉnh cũ giữ trục thêm một lúc thay vì co lại liên tục.
        ty_alls = [buf.get() for buf in self._ty]
        t_max = max(float(ya.max()) for ya in ty_alls) if (has_data and ty_alls) else None

        y_range = None
        if t_max is not None:
            candidate_ymax = t_max + max(t_max * 0.1, 1)
            prev = self._last_temp_ymax
            if prev is None or abs(candidate_ymax - prev) / max(abs(prev), 1.0) > _Y_THRESH:
                y_range = (-max(t_max * 0.03, 2), candidate_ymax)
                self._last_temp_ymax = candidate_ymax

        if x_changed and y_range is not None:
            self.plot.setRange(xRange=(x_min, x_max), yRange=y_range, padding=0)
        elif x_changed:
            self.plot.setXRange(x_min, x_max, padding=0)
        elif y_range is not None:
            self.plot.setYRange(*y_range, padding=0)

        sx, sy = self._px_scale(self.plot.getViewBox())
        for i in range(self.num_temp):
            y_all = ty_alls[i]
            if not self._vis_temp[i] or not has_data:
                self._temp_labels[i].hide()
                self._last_temp_text[i] = None
                self._t_anchor[i] = None
                continue
            if _is_sv(i):
                X, Y, conn = self._dashed_data(self._t_anchor, self._t_phase, i,
                                               t_all, y_all, base_abs, start, sx, sy)
                self._temp_curves[i].setData(X, Y, connect=conn)
            else:
                self._temp_curves[i].setData(t, y_all[start:])
            ly = float(y_all[-1])
            self._update_end_label(
                self._temp_labels[i], self._last_temp_text, i,
                f"{ly:.1f}{self._temp_unit} ", lx, ly,
            )

        if self.num_pressure == 0:
            return

        # ── Áp suất (X đã được link với ViewBox chính) ────────────────────────
        # Cập nhật Y-range TRƯỚC khi vẽ để tỉ lệ pixel dùng cắt nét đứt khớp
        # với tỉ lệ thực tế của frame này.
        y_alls = [buf.get() for buf in self._py]
        if has_data:
            p_max = max(float(ya.max()) for ya in y_alls)
            new_p_ymax = p_max + max(p_max * 0.25, 1)
            prev       = self._last_pres_ymax
            if prev is None or abs(new_p_ymax - prev) / max(abs(prev), 1.0) > _Y_THRESH:
                self._vb_pressure.setYRange(-0.1, new_p_ymax, padding=0)
                self._last_pres_ymax = new_p_ymax

        sx, sy = self._px_scale(self._vb_pressure)
        for i in range(self.num_pressure):
            y_all = y_alls[i]
            if not self._vis_pressure[i] or not has_data:
                self._pressure_labels[i].hide()
                self._last_pressure_text[i] = None
                self._p_anchor[i] = None
                continue
            if _is_sv(i):
                X, Y, conn = self._dashed_data(self._p_anchor, self._p_phase, i,
                                               t_all, y_all, base_abs, start, sx, sy)
                self._pressure_curves[i].setData(X, Y, connect=conn)
            else:
                self._pressure_curves[i].setData(t, y_all[start:])
            ly = float(y_all[-1])
            self._update_end_label(
                self._pressure_labels[i], self._last_pressure_text, i,
                f"{ly:.2f} bar ", lx, ly,
            )

    @staticmethod
    def _px_scale(vb: pg.ViewBox) -> tuple[float, float]:
        """Tỉ lệ data → pixel (sx, sy) của ViewBox."""
        (vx0, vx1), (vy0, vy1) = vb.viewRange()
        sx = vb.width()  / (vx1 - vx0) if vx1 > vx0 else 0.0
        sy = vb.height() / (vy1 - vy0) if vy1 > vy0 else 0.0
        return sx, sy

    @staticmethod
    def _dashed_data(
        anchors: list[int | None],
        phases: list[float],
        i: int,
        t_all: np.ndarray,
        y_all: np.ndarray,
        base_abs: int,
        start: int,
        sx: float,
        sy: float,
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Tự cắt đường thành nét đứt, neo pha theo độ dài cung TUYỆT ĐỐI.

        Qt DashLine bắt đầu mẫu từ điểm đầu tiên của đường → mỗi lần cắt bớt
        điểm đầu (đã trôi khỏi màn hình), toàn bộ nét đứt bị trượt. Ở đây
        pha tại điểm đầu (phases[i]) được cộng thêm đúng độ dài pixel của đoạn
        vừa bị cắt, rồi chèn điểm ngắt tại mỗi biên nét/trống và vẽ bằng pen
        nét liền + mảng connect → các nét đứt đứng yên trên đường.
        """
        start_abs = base_abs + start
        prev_abs  = anchors[i]
        if prev_abs is not None and start_abs > prev_abs and prev_abs >= base_abs:
            i0 = prev_abs - base_abs
            cut = np.hypot(np.diff(t_all[i0 : start + 1]) * sx,
                           np.diff(y_all[i0 : start + 1]) * sy).sum()
            phases[i] = (phases[i] + float(cut)) % _DASH_PERIOD
        elif prev_abs is None or start_abs < prev_abs or prev_abs < base_abs:
            phases[i] = 0.0
        anchors[i] = start_abs

        x = t_all[start:]
        y = y_all[start:]
        n = len(x)
        if n < 2:
            return x, y, np.zeros(n, dtype=bool)

        seg = np.hypot(np.diff(x) * sx, np.diff(y) * sy)          # độ dài pixel từng đoạn
        s   = np.empty(n)
        s[0] = phases[i]
        np.cumsum(seg, out=s[1:])
        s[1:] += s[0]

        # Biên nét/trống: k*P (bắt đầu nét) và k*P+ON (bắt đầu trống)
        k  = np.arange(np.floor(s[0] / _DASH_PERIOD), np.floor(s[-1] / _DASH_PERIOD) + 1)
        b  = np.concatenate((k * _DASH_PERIOD, k * _DASH_PERIOD + _DASH_ON))
        b  = b[(b > s[0]) & (b < s[-1])]

        s_all = np.sort(np.concatenate((s, b)), kind="stable")
        idx   = np.clip(np.searchsorted(s, s_all, side="right") - 1, 0, n - 2)
        L     = seg[idx]
        f     = np.divide(s_all - s[idx], L, out=np.zeros_like(s_all), where=L > 0)
        np.clip(f, 0.0, 1.0, out=f)
        X = x[idx] + f * (x[idx + 1] - x[idx])
        Y = y[idx] + f * (y[idx + 1] - y[idx])

        mid  = 0.5 * (s_all[:-1] + s_all[1:])
        conn = np.empty(len(s_all), dtype=bool)
        conn[:-1] = np.mod(mid, _DASH_PERIOD) < _DASH_ON
        conn[-1]  = False
        return X, Y, conn

    def append_data(
        self,
        temp_values: List[float],
        pressure_values: List[float] | None = None,
    ) -> None:
        """
        Ghi 1 mẫu (cùng timestamp) cho tất cả series vào buffer.

        KHÔNG thread-safe — phải gọi trên GUI thread (hiện được gọi từ
        chart_timer trong source_edited.py).

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

        self._t.append(time.time())
        self._n_total += 1
        for buf, v in zip(self._ty, temp_values):
            buf.append(v)
        for buf, v in zip(self._py, pressure_values):
            buf.append(v)

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
        self.plot.setLabel("left", label, **self._axis_style)
        self.temp_label = label
        if unit != self._temp_unit:
            self._temp_unit = unit
            self._last_temp_text = [None] * self.num_temp   # ép vẽ lại nhãn

    def clear(self) -> None:
        """Xoá toàn bộ data và reset cache."""
        self._t.reset()
        for buf in self._ty:
            buf.reset()
        for buf in self._py:
            buf.reset()

        for i in range(self.num_temp):
            self._temp_curves[i].setData([], [])
            self._temp_labels[i].hide()
        for i in range(self.num_pressure):
            self._pressure_curves[i].setData([], [])
            self._pressure_labels[i].hide()

        self._last_temp_ymax = None
        self._last_pres_ymax = None
        self._last_x_min     = None
        self._n_total        = 0
        self._t_anchor       = [None] * self.num_temp
        self._t_phase        = [0.0] * self.num_temp
        self._p_anchor       = [None] * self.num_pressure
        self._p_phase        = [0.0] * self.num_pressure
        self._last_temp_text     = [None] * self.num_temp
        self._last_pressure_text = [None] * self.num_pressure
