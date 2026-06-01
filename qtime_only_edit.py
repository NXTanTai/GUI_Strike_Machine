from PySide6.QtWidgets import QDateTimeEdit
from PySide6.QtCore import QDate, QDateTime, QTime, Qt

class TimeOnlyEdit(QDateTimeEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDisplayFormat("HH:mm - dd/MM/yyyy")
        self._locked_date = QDate.currentDate()

    def stepBy(self, steps: int):
        """Chỉ cho chỉnh giờ/phút, khóa ngày/tháng/năm."""
        section = self.currentSection()
        if section in (
            QDateTimeEdit.Section.HourSection,
            QDateTimeEdit.Section.MinuteSection,
        ):
            old_date = self.date()
            super().stepBy(steps)
            # Nếu vô tình qua ngày (23:59 → 00:00) → giữ nguyên ngày
            if self.date() != old_date:
                self.setDate(old_date)

    def keyPressEvent(self, event):
        """Chặn keyboard trên phần ngày."""
        section = self.currentSection()
        if section in (
            QDateTimeEdit.Section.DaySection,
            QDateTimeEdit.Section.MonthSection,
            QDateTimeEdit.Section.YearSection,
        ):
            # Cho phép Tab/Shift+Tab để chuyển section
            if event.key() in (Qt.Key.Key_Tab, Qt.Key.Key_Backtab):
                super().keyPressEvent(event)
            # Chặn tất cả phím khác trên phần ngày
            return
        super().keyPressEvent(event)

    def set_lock_date(self, date: QDate):
        """Nhận ngày từ QCalendarWidget và lock lại."""
        self._locked_date = date
        current_time = self.time()
        self.setDateTime(QDateTime(date, current_time))

    def get_datetime(self) -> QDateTime:
        """Trả về QDateTime hiện tại."""
        return self.dateTime()

    def set_rounded_time(self, time: QTime = None):
        """Set giờ làm tròn đến 30 phút gần nhất."""
        if time is None:
            time = QTime.currentTime()

        if time.minute() <= 30:
            rounded = QTime(time.hour(), 30, 0)
            extra_day = 0
        else:
            next_hour = time.hour() + 1
            if next_hour >= 24:
                rounded = QTime(0, 0, 0)
                extra_day = 1
            else:
                rounded = QTime(next_hour, 0, 0)
                extra_day = 0

        locked = self._locked_date.addDays(extra_day)
        self._locked_date = locked
        self.setDateTime(QDateTime(locked, rounded))