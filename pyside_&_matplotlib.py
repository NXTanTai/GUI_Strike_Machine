import sys
import multiprocessing as mp
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QLabel, QPushButton, QHBoxLayout)
from PySide6.QtCore import Qt, QTimer
import matplotlib
matplotlib.use('QtAgg')
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Strike Machine - 6 Sine Waves (Separate Process)")
        self.resize(1450, 920)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        title = QLabel("6 Composite Sine Waves\n(Running in Separate Process)")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold; margin: 15px;")
        layout.addWidget(title)

        # Matplotlib Canvas
        self.canvas = FigureCanvas(Figure(figsize=(14, 8), dpi=100))
        self.fig = self.canvas.figure
        self.axes = self.fig.subplots(2, 3)
        self.fig.suptitle('6 Sine Composite Waves', fontsize=16)

        self.lines = []
        for i, ax in enumerate(self.axes.flat):
            ax.set_xlim(0, 500)
            ax.set_ylim(10, 90)
            ax.set_title(f'Sine Composite {i+1}')
            ax.grid(True, alpha=0.4)
            line, = ax.plot([], [], '-', linewidth=2.8, color=f'C{i}')
            self.lines.append(line)

        self.fig.tight_layout()
        layout.addWidget(self.canvas)

        # Buttons
        btn_layout = QHBoxLayout()
        self.btn_start = QPushButton("🚀 Start Animation")
        self.btn_stop = QPushButton("⛔ Stop Animation")
        self.btn_start.clicked.connect(self.start_animation)
        self.btn_stop.clicked.connect(self.stop_animation)
        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_stop)
        layout.addLayout(btn_layout)

        # Process variables
        self.data_queue = None
        self.process = None
        self.stop_event = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)

        self.start_animation()   # Tự động chạy

    def start_animation(self):
        if self.process and self.process.is_alive():
            return

        self.data_queue = mp.Queue(maxsize=8)
        self.stop_event = mp.Event()

        from test_6_chart import data_producer

        self.process = mp.Process(
            target=data_producer,
            args=(self.data_queue, self.stop_event),
            daemon=True
        )
        self.process.start()

        self.timer.start(20)   # Cập nhật mỗi 20ms
        print("✅ Process riêng đã khởi động")

    def update_plot(self):
        if not self.data_queue:
            return
        try:
            # Lấy frame mới nhất
            data = None
            while not self.data_queue.empty():
                data = self.data_queue.get_nowait()

            if data:
                for i, (x, y) in enumerate(data):
                    self.lines[i].set_data(x, y)
                self.canvas.draw_idle()
        except:
            pass

    def stop_animation(self):
        if self.stop_event:
            self.stop_event.set()
        if self.process and self.process.is_alive():
            self.process.terminate()
            self.process.join(timeout=1)
        self.timer.stop()
        print("⛔ Animation stopped")

    def closeEvent(self, event):
        self.stop_animation()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())