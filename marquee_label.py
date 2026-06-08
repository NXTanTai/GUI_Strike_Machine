from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QFontMetrics

class MarqueeLabel(QLabel):
    def __init__(self, parent=None, speed=60):
        super().__init__(parent)
        self._text = ""
        self._offset = 0
        self._speed = speed
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._update_scroll)
        self.setMinimumHeight(28)

    def setText(self, text: str):
        self._text = text.strip() if text else ""
        self._offset = 0
        self._update_timer_state()
        self.update()

    def resizeEvent(self, event):          # ← Thêm cái này
        super().resizeEvent(event)
        self._offset = 0
        self._update_timer_state()
        self.update()

    def _update_timer_state(self):         # ← Tách logic ra hàm riêng
        if not self._text:
            self._timer.stop()
            return

        fm = QFontMetrics(self.font())
        text_width = fm.horizontalAdvance(self._text)

        if text_width > self.width() + 10:
            if not self._timer.isActive():
                self._timer.start(self._speed)
        else:
            self._timer.stop()

    def _update_scroll(self):
        if not self._text:
            self._timer.stop()
            return

        fm = QFontMetrics(self.font())
        text_width = fm.horizontalAdvance(self._text)

        if text_width <= self.width() + 10:
            self._timer.stop()
            self._offset = 0
            self.update()
            return

        self._offset += 2
        if self._offset > text_width + 60:
            self._offset = 0

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if not self._text:
            super().paintEvent(event)
            return

        fm = QFontMetrics(self.font())
        y = (self.height() + fm.ascent() - fm.descent()) // 2

        if not self._timer.isActive():
            painter.drawText(0, y, self._text)
        else:
            display = self._text + "    " + self._text
            painter.drawText(-self._offset, y, display)

        painter.end()