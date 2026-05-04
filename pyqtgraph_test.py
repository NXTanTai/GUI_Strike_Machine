import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQtGraph Example")

        # Tạo PlotWidget (widget chính của PyQtGraph)
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('w')        # nền trắng
        self.plot_widget.showGrid(x=True, y=True)

        # Dữ liệu mẫu
        x = np.linspace(0, 10, 1000)
        y = np.sin(x) * np.exp(-0.1 * x)

        # Vẽ curve (rất nhanh)
        self.curve = self.plot_widget.plot(x, y, pen=pg.mkPen(color='r', width=2))

        # Layout
        central = QWidget()
        layout = QVBoxLayout(central)
        layout.addWidget(self.plot_widget)
        self.setCentralWidget(central)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())