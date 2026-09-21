import os
import sys
import logging
import logging.handlers
from datetime import datetime


class MonthlyRotatingFileHandler(logging.handlers.RotatingFileHandler):
    """
    RotatingFileHandler mở rộng: tự động chuyển sang folder mới
    mỗi khi sang tháng mới (TL_SM_yy_mm), đồng thời vẫn giữ nguyên
    cơ chế rotate theo dung lượng (maxBytes/backupCount) như cũ.
    """

    def __init__(self, base_log_dir, prefix="TL_SM", maxBytes=0, backupCount=0, encoding=None):
        self.base_log_dir = base_log_dir
        self.prefix = prefix
        self._current_month_key = None  # ví dụ "25_09"

        # Tính path ban đầu trước khi gọi super().__init__
        log_filename = self._build_filepath()

        super().__init__(
            log_filename,
            maxBytes=maxBytes,
            backupCount=backupCount,
            encoding=encoding,
        )

    def _build_filepath(self):
        now = datetime.now()
        self._current_month_key = now.strftime("%Y_%m")
        month_folder = f"{self.prefix}_{self._current_month_key}"
        log_dir = os.path.join(self.base_log_dir, month_folder)
        os.makedirs(log_dir, exist_ok=True)

        log_date = now.strftime("%Y_%m_%d")
        return os.path.join(log_dir, f"{self.prefix}_{log_date}.log")

    def _check_month_rollover(self):
        """Kiểm tra xem tháng hiện tại có khác tháng của file đang mở không."""
        now_key = datetime.now().strftime("%Y_%m")
        if now_key != self._current_month_key:
            # Đóng file cũ
            if self.stream:
                self.stream.close()
                self.stream = None

            # Trỏ sang file/folder tháng mới
            new_path = self._build_filepath()
            self.baseFilename = os.path.abspath(new_path)

            # Mở lại stream nếu handler không ở chế độ delay
            if not self.delay:
                self.stream = self._open()

    def emit(self, record):
        try:
            self._check_month_rollover()
            super().emit(record)
        except Exception:
            self.handleError(record)