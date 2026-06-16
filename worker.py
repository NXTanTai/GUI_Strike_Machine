"""
Worker.py — QRunnable + QThreadPool generic wrapper.
Theo pattern: https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/

Dùng cho các tác vụ "chạy 1 lần rồi xong" (fire-and-forget với kết quả trả về),
KHÔNG dùng cho các vòng lặp dài hạn (PLCRead, PLCWrite, DataSimulator) — những
cái đó vẫn nên giữ QThread + moveToThread như hiện tại vì cần chạy liên tục
theo poll_ms và emit signal nhiều lần trong suốt vòng đời.
"""

import sys
import traceback

from PySide6.QtCore import QObject, QRunnable, Signal, Slot


class WorkerSignals(QObject):
    """
    Định nghĩa các signal khả dụng từ một worker thread.

    Supported signals:
        finished : Không có data — emit khi xong (dù thành công hay lỗi)
        error    : tuple (exctype, value, traceback_str)
        result   : object — kết quả trả về từ fn, nếu thành công
        progress : int — % tiến trình (0-100), optional
    """
    finished = Signal()
    error    = Signal(tuple)
    result   = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    """
    Worker thread chạy bất kỳ function nào trong QThreadPool.

    QRunnable không kế thừa QObject nên không tự có signal — vì vậy ta
    nhúng một WorkerSignals (QObject) bên trong để giao tiếp về main thread.

    Parameters
    ----------
    fn       : function sẽ chạy trên worker thread
    *args    : positional arguments truyền cho fn
    **kwargs : keyword arguments truyền cho fn

    Nếu fn nhận được keyword 'progress_callback', Worker sẽ tự inject
    self.signals.progress.emit vào đó để fn có thể report % tiến trình.
    """

    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn      = fn
        self.args    = args
        self.kwargs  = kwargs
        self.signals = WorkerSignals()

        # Cho phép fn tự báo progress nếu cần (optional)
        if 'progress_callback' in self.fn.__code__.co_varnames:
            self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except Exception:
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()