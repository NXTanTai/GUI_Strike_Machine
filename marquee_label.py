from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter

class MarqueeLabel(QLabel):
    def __init__(self, parent=None, speed=50):
        super().__init__(parent)
        self._text = ""
        self._offset = 0
        self._speed = speed  # ms mỗi bước dịch

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._update_scroll)

    def setText(self, text: str):
        self._text = text
        self._offset = 0
        self._update_scroll()  # tách logic ra hàm riêng

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_scroll()  # gọi lại khi widget bị resize

    def _update_scroll(self):
        if not self._text:
            return

        fm = self.fontMetrics()
        text_width = fm.horizontalAdvance(self._text)
        widget_width = self.width()

        if text_width > widget_width:
            self._offset += 2                    # Tốc độ di chuyển (pixel mỗi lần)
            if self._offset > text_width + 50:   # Reset khi chạy hết
                self._offset = 0

            self.update()                        # Vẽ lại
            self._timer.start(self._speed)
        else:
            self._timer.stop()
            self.update()

    def paintEvent(self, event):
        if not self._timer.isActive():
            super().paintEvent(event)
            return

        painter = QPainter(self)
        fm = self.fontMetrics()

        # Vẽ text dịch theo offset
        display = self._text + "     " + self._text
        x = -self._offset
        y = (self.height() + fm.ascent() - fm.descent()) // 2

        painter.setPen(self.palette().color(self.foregroundRole()))
        painter.drawText(x, y, display)
        painter.end()