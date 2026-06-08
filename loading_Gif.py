import os
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QFileSystemWatcher
from PySide6.QtGui import QMovie

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # type: ignore
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class SmoothGifLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._movie = None

    def setMovie(self, movie: QMovie):
        self._movie = movie
        movie.frameChanged.connect(self._on_frame_changed)
        super().setMovie(movie)

    def _on_frame_changed(self, _):
        if self._movie is None:
            return
        pixmap = self._movie.currentPixmap()
        if not pixmap.isNull():
            scaled = pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.setPixmap(scaled)


def run_loading(signal_file: str):
    app = QApplication(sys.argv)

    win = QWidget()
    win.setWindowFlags(
        Qt.FramelessWindowHint |
        Qt.WindowStaysOnTopHint |
        Qt.Tool
    )
    win.setAttribute(Qt.WA_TranslucentBackground)
    win.resize(120, 120)

    layout = QVBoxLayout(win)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setAlignment(Qt.AlignCenter)

    label = SmoothGifLabel()
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet("background: transparent;")
    label.setFixedSize(win.size())  
    layout.addWidget(label)

    gif_path = os.path.join(resource_path('gifs'), 'Loading.gif')
    movie = QMovie(gif_path)
    movie.setCacheMode(QMovie.CacheAll)
    label.setMovie(movie)
    movie.start()

    # Căn giữa màn hình
    screen = app.primaryScreen().availableGeometry()
    win.move(
        (screen.width() - win.width()) // 2,
        (screen.height() - win.height()) // 2
    )
    win.show()

    # Theo dõi signal_file — khi main process xóa file → tự đóng
    watcher = QFileSystemWatcher([signal_file])
    watcher.fileChanged.connect(lambda: (movie.stop(), app.quit()))

    sys.exit(app.exec())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    run_loading(sys.argv[1])