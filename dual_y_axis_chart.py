# spline_chart.py
from typing import List, Tuple
import time
from collections import deque

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QTimer

SERIES_COLORS = ["#43A047", "#FB8C00", "#E53935", "#1E88E5", "#8E24AA", "#8B5CF6"]

FONT_FAMILY = "Segoe UI"
FONT_SIZE_LG = 17
FONT_SIZE_SM = 13


class CustomChartWidget(QWidget):
    """
    Chart hỗ trợ Temperature (trục trái) + Pressure (trục phải)
    """

    def __init__(
        self,
        title: str = "Chart",
        num_temp: int = 1,
        num_pressure: int = 1,
        temp_label: str = "Temperature (°C)",
        pressure_label: str = "Pressure (bar)",
        temp_range: Tuple[float, float] = (0, 200),
        pressure_range: Tuple[float, float] = (0, 10),
        max_seconds: int = 60,
        chart_font: QFont | None = None,
        parent=None,
    ):
        super().__init__(parent)

        self.title = title
        self.num_temp = min(num_temp, 5)
        self.num_pressure = min(num_pressure, 3)
        self.total_series = self.num_temp + self.num_pressure
        self.max_seconds = max_seconds

        self.temp_label = temp_label
        self.pressure_label = pressure_label
        self.temp_range = temp_range
        self.pressure_range = pressure_range

        # Data buffers
        self._data_x: List[deque] = [deque(maxlen=600) for _ in range(self.total_series)]
        self._data_y: List[deque] = [deque(maxlen=600) for _ in range(self.total_series)]

        self._lines = []
        self._start_time = time.time()

        self._setup_ui()
        self._setup_matplotlib()
        self._start_update_timer()

    def _setup_ui(self):
        self._root = QVBoxLayout(self)
        self._root.setContentsMargins(4, 4, 4, 4)
        self._root.setSpacing(2)

        # Title Button
        font_btn = QFont(FONT_FAMILY, FONT_SIZE_LG)
        font_btn.setWeight(QFont.Weight.Bold)

        self.btn_setting = QPushButton(self.title)
        self.btn_setting.setFont(font_btn)
        self.btn_setting.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_setting.setStyleSheet("""
            QPushButton {
                background: white;
                border: none;
                color: black;
                padding: 8px 12px;
                border-radius: 6px;
            }
            QPushButton:hover { background: #F0F9FF; }
        """)

        title_row = QHBoxLayout()
        title_row.addStretch()
        title_row.addWidget(self.btn_setting)
        title_row.addStretch()
        self._root.addLayout(title_row)

        # Legend
        self._create_legend()

    def _create_legend(self):
        self._legend_bar = QHBoxLayout()
        self._legend_bar.setContentsMargins(8, 4, 8, 6)
        self._legend_bar.setSpacing(18)
        self._legend_bar.addStretch()

        self._legend_labels: list[QLabel] = []
        font_legend = QFont(FONT_FAMILY, FONT_SIZE_SM)
        font_legend.setWeight(QFont.Weight.Bold)

        # Temperature series
        for i in range(self.num_temp):
            self._add_legend_item(i, is_temp=True)

        # Pressure series
        for i in range(self.num_pressure):
            self._add_legend_item(self.num_temp + i, is_temp=False)

        self._legend_bar.addStretch()
        self._root.addLayout(self._legend_bar)

    def _add_legend_item(self, idx: int, is_temp: bool):
        color = SERIES_COLORS[idx % len(SERIES_COLORS)]

        dot = QFrame()
        dot.setFixedSize(18, 4)
        dot.setStyleSheet(f"background: {color}; border-radius: 2px;")

        lbl = QLabel("SV" if idx == 0 else "PV")
        lbl.setFont(QFont(FONT_FAMILY, FONT_SIZE_SM, QFont.Weight.Bold))

        item_layout = QHBoxLayout()
        item_layout.setSpacing(6)
        item_layout.addWidget(dot)
        item_layout.addWidget(lbl)

        item_widget = QWidget()
        item_widget.setLayout(item_layout)
        self._legend_bar.addWidget(item_widget)
        self._legend_labels.append(lbl)

    def _setup_matplotlib(self):
        self.fig, self.ax1 = plt.subplots(figsize=(11, 6), dpi=100)
        self.fig.patch.set_facecolor('#f8fafc')
        self.ax2 = self.ax1.twinx()

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setStyleSheet("background:transparent;")

        # Light gradient
        gradient = np.linspace(0, 1, 256).reshape(1, -1)
        self.ax1.imshow(gradient, aspect='auto', extent=[0, 1, 0, 1],
                        transform=self.ax1.transAxes, cmap='Blues', alpha=0.07, zorder=0)

        self.ax1.set_facecolor('#f8fafc')
        for spine in list(self.ax1.spines.values()) + list(self.ax2.spines.values()):
            spine.set_linewidth(1.5)

        self.ax1.grid(True, linestyle='--', alpha=0.5)

        # Labels
        self.ax1.set_ylabel(self.temp_label, fontsize=13, fontweight='bold', color='#1e40af')
        self.ax2.set_ylabel(self.pressure_label, fontsize=13, fontweight='bold', color='#6b21a8')

        self.ax1.set_xlabel("Time (Realtime)", fontsize=12, fontweight='bold')

        # Create lines
        self._lines.clear()

        # Temperature lines (ax1)
        for i in range(self.num_temp):
            line, = self.ax1.plot([], [], color=SERIES_COLORS[i], linewidth=2.8, label=f"T{i+1}")
            self._lines.append(line)

        # Pressure lines (ax2)
        for i in range(self.num_pressure):
            line, = self.ax2.plot([], [], color=SERIES_COLORS[self.num_temp + i],
                                  linewidth=2.6, linestyle='--', label=f"P{i+1}")
            self._lines.append(line)

        # Set ranges
        self.ax1.set_ylim(self.temp_range[0], self.temp_range[1])
        self.ax2.set_ylim(self.pressure_range[0], self.pressure_range[1])

        self._root.addWidget(self.canvas)

    def _start_update_timer(self):
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._update_axis)
        self._timer.start(400)
        self._update_axis()

    def _update_axis(self):
        now = time.time()
        x_min = now - self.max_seconds
        self.ax1.set_xlim(x_min, now)
        self.ax2.set_xlim(x_min, now)
        self.canvas.draw_idle()

    # ====================== PUBLIC API ======================
    def append_data(self, temp_values: List[float], pressure_values: List[float]):
        """Thêm dữ liệu: temp_values + pressure_values"""
        if len(temp_values) != self.num_temp or len(pressure_values) != self.num_pressure:
            print(f"[{self.title}] Data mismatch!")
            return

        now = time.time()
        cutoff = now - self.max_seconds * 1.2

        all_values = temp_values + pressure_values

        for i, val in enumerate(all_values):
            self._data_x[i].append(now)
            self._data_y[i].append(val)

            while self._data_x[i] and self._data_x[i][0] < cutoff:
                self._data_x[i].popleft()
                self._data_y[i].popleft()

            self._lines[i].set_data(list(self._data_x[i]), list(self._data_y[i]))

        self.canvas.draw_idle()

    def set_series_name(self, index: int, name: str):
        if 0 <= index < len(self._legend_labels):
            self._legend_labels[index].setText(name)

    def clear(self):
        for i in range(self.total_series):
            self._data_x[i].clear()
            self._data_y[i].clear()
            self._lines[i].set_data([], [])
        self.canvas.draw_idle()

    def _on_setting(self):
        print(f"[Setting] {self.title}")