import sys
import requests
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                                QVBoxLayout, QPushButton, QLabel)
from PySide6.QtCore import QThread, Signal


# ── Worker chạy API ở thread riêng ──────────────────────────
class ApiWorker(QThread):
    result = Signal(dict)   # emit khi thành công
    error  = Signal(str)    # emit khi lỗi

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            self.result.emit(response.json())
        except Exception as e:
            self.error.emit(str(e))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("API Demo")
        self.resize(400, 200)

        widget = QWidget()
        layout = QVBoxLayout(widget)
        self.setCentralWidget(widget)

        self.label  = QLabel("Nhấn nút để gọi API")
        self.button = QPushButton("Gọi API")
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.fetch_data)

    def fetch_data(self):
        self.button.setEnabled(False)
        self.label.setText("Đang tải...")

        self.worker = ApiWorker("https://jsonplaceholder.typicode.com/todos/1")
        self.worker.result.connect(self.on_success)
        self.worker.error.connect(self.on_error)
        self.worker.start()

    def on_success(self, data):
        self.label.setText(f"✅ {data['title']}")
        self.button.setEnabled(True)

    def on_error(self, message):
        self.label.setText(f"❌ Lỗi: {message}")
        self.button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())