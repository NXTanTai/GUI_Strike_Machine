import random
from datetime import datetime, timedelta
from typing import List

import numpy as np
import matplotlib.dates as mdates
import matplotlib.patheffects as pe
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PySide6.QtGui import QFont

SERIES_COLORS = ['#00ffaa', '#ffcc00', '#ff4444', '#44aaff', '#ff66cc', '#99ff44']
FONT_FAMILY = "Segoe UI"
FONT_SIZE_LG = 17
FONT_SIZE_SM = 13

class CustomChartWidget(QWidget):
    def __init__(self, 
                 title: str = "Realtime Chart",
                 num_temp: int = 3,
                 num_pressure: int = 1,
                 temp_label: str = "Temperature (°C)",
                 pressure_label: str = "Pressure (bar)",
                 max_seconds: int = 60,
                 parent=None):
        super().__init__(parent)

        self.title = title
        self.num_temp = num_temp
        self.num_pressure = num_pressure
        self.temp_label = temp_label
        self.pressure_label = pressure_label
        self.max_seconds = max_seconds

        self.x_data: List[datetime] = []
        self.temp_data: List[List[float]] = [[] for _ in range(num_temp)]
        self.pressure_data: List[List[float]] = [[] for _ in range(num_pressure)]

        # Khởi tạo theo thứ tự đúng
        self.setup_matplotlib()
        self.setup_ui()
        self.start_animation()

    def setup_matplotlib(self):
        self.fig = Figure(figsize=(10, 6), dpi=100, facecolor='#d9e6ff')
        self.ax1 = self.fig.add_subplot(111)
        self.ax2 = self.ax1.twinx()

        # Background gradient
        gradient = np.linspace(0, 1, 256).reshape(1, -1)
        self.ax1.imshow(gradient, aspect='auto', extent=[0, 1, 0, 1],
                       transform=self.ax1.transAxes, cmap='Blues', alpha=0.25, zorder=0)

        self.fig.patch.set_facecolor('#d9e6ff')
        self.ax1.set_facecolor('#f8f9fc')

        temp_colors = ['#00ffaa', '#ffcc00', '#ff4444', '#44aaff', '#ff66cc', '#99ff44']

        self.temp_lines = []
        self.temp_texts = []
        self.pressure_lines = []
        self.pressure_texts = []

        bbox_style = dict(facecolor='black', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.3')

        for i in range(self.num_temp):
            line, = self.ax1.plot([], [], color=temp_colors[i % len(temp_colors)],
                                linewidth=1.8, label=f'T{i+1}')
            line.set_path_effects([pe.Stroke(linewidth=4, foreground='white', alpha=0.3), pe.Normal()])
            self.temp_lines.append(line)

            txt = self.ax1.text(0, 0, '', color=temp_colors[i % len(temp_colors)],
                            fontsize=10, fontweight='bold', bbox=bbox_style,
                            animated=True,
                            clip_on=True)   # ← thêm clip_on=True
            self.temp_texts.append(txt)

        for i in range(self.num_pressure):
            line, = self.ax2.plot([], [], color="#FFFFFF", linewidth=1.8,
                                linestyle='--', label=f'P{i+1}')
            line.set_path_effects([pe.Stroke(linewidth=4, foreground='white', alpha=0.3), pe.Normal()])
            self.pressure_lines.append(line)

            txt = self.ax2.text(0, 0, '', color="#FFFFFF",
                            fontsize=10, fontweight='bold', bbox=bbox_style,
                            animated=True,
                            clip_on=True)   # ← thêm clip_on=True
            self.pressure_texts.append(txt)

        # Labels & Grid
        self.ax1.set_ylabel(self.temp_label, fontsize=12, color='#2c3e50')
        self.ax2.set_ylabel(self.pressure_label, fontsize=12, color='#2c3e50')

        self.ax1.set_ylim(0, 100)
        self.ax2.set_ylim(0, 10)

        self.ax1.grid(True, linestyle='--', alpha=0.6, color='gray')
        self.ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

        # # Legend
        lines = self.temp_lines + self.pressure_lines
        labels = [f'T{i+1}' for i in range(self.num_temp)] + [f'P{i+1}' for i in range(self.num_pressure)]
        self.ax1.legend(lines, labels, loc='upper left', ncol=4, fontsize=10)

        self.fig.suptitle(self.title, fontsize=16, fontweight='bold', color='#2c3e50')
        self.fig.autofmt_xdate(rotation=0, ha='center')
        self.fig.tight_layout()
        self.fig.subplots_adjust(left=0.15, right=0.88)

    def setup_ui(self):
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(8, 8, 8, 8)
        self._layout.setSpacing(0)
        # ── Canvas ──────────────────────────────────────
        self.canvas = FigureCanvas(self.fig)
        self._layout.addWidget(self.canvas)

    def append_data(self, temperature: List[float], pressure: List[float]):
        """Cập nhật dữ liệu thật từ bên ngoài"""
        if len(temperature) != self.num_temp:
            raise ValueError(f"temperature phải có {self.num_temp} giá trị")
        if len(pressure) != self.num_pressure:
            raise ValueError(f"pressure phải có {self.num_pressure} giá trị")

        now = datetime.now()
        self.x_data.append(now)

        for i in range(self.num_temp):
            self.temp_data[i].append(float(temperature[i]))

        for i in range(self.num_pressure):
            self.pressure_data[i].append(float(pressure[i]))

    def update_chart(self, frame):
        if not self.x_data:
            return self.temp_lines + self.pressure_lines + self.temp_texts + self.pressure_texts

        now = self.x_data[-1]

        for i, line in enumerate(self.temp_lines):
            line.set_data(self.x_data, self.temp_data[i])

        for i, line in enumerate(self.pressure_lines):
            line.set_data(self.x_data, self.pressure_data[i])

        text_x = now + timedelta(seconds=-5)

        for i, txt in enumerate(self.temp_texts):
            if self.temp_data[i]:
                value = self.temp_data[i][-1]
                txt.set_position((text_x, value*1.09))
                txt.set_text(f'{value:.1f}°C')
                txt.set_visible(True)

        for i, txt in enumerate(self.pressure_texts):
            if self.pressure_data[i]:
                value = self.pressure_data[i][-1]
                txt.set_position((text_x, value*1.09))
                txt.set_text(f'{value:.2f} bar')
                txt.set_visible(True)

        left = now - timedelta(seconds=self.max_seconds)
        right = now + timedelta(milliseconds=400)

        self.ax1.set_xlim(left, right)
        self.ax2.set_xlim(left, right)

        # ← đánh dấu tất cả artists là stale để blit redraw đúng
        for txt in self.temp_texts + self.pressure_texts:
            txt.set_animated(True)

        return self.temp_lines + self.pressure_lines + self.temp_texts + self.pressure_texts

    def start_animation(self):
        self.ani = FuncAnimation(
            self.fig,
            self.update_chart,
            interval=500,
            blit=False,         # ← bật blit=True
            cache_frame_data=False
        )
        
    def stop_animation(self):
        if hasattr(self, 'ani'):
            self.ani.event_source.stop()