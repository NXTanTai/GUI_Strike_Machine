# pyinstaller --onefile --noconsole --name="Strike Machine App" --icon=icons\hose_icon.png --add-binary "lib\snap7.dll;." --add-data "gifs;gifs" --add-data "tech_link_theme_cn.qm;." --distpath "Apps" main.py

# pyinstaller --onefile --noconsole --name="Strike Machine App" --icon=icons\strike_machine.png --add-binary "lib\snap7.dll;." --add-data "gifs;gifs" --add-data "tech_link_theme_vn.qm;." --add-data "tech_link_theme_cn.qm;." --distpath "Apps" main.py
# pyinstaller --onefile --noconsole --name="cmd" --icon=icons\cmd.png --add-data "icons;icons" --distpath "Apps" console_window.py

# pyinstaller --onefile --noconsole --name="Strike Machine App" --icon=icons\strike_machine.png --add-data "gifs;gifs" --add-data "tech_link_theme_vn.qm;." --add-data "tech_link_theme_cn.qm;." --hidden-import=web_server --hidden-import=uvicorn --hidden-import=uvicorn.logging --hidden-import=uvicorn.loops --hidden-import=uvicorn.loops.auto --hidden-import=uvicorn.protocols --hidden-import=uvicorn.protocols.http --hidden-import=uvicorn.protocols.http.auto --hidden-import=uvicorn.protocols.websockets --hidden-import=uvicorn.protocols.websockets.auto --hidden-import=uvicorn.lifespan --hidden-import=uvicorn.lifespan.on --hidden-import=fastapi --hidden-import=anyio --hidden-import=anyio.backends.asyncio --distpath "Apps" main.py

# pyinstaller --onefile --noconsole --name="Strike Machine App" --icon=icons\strike_machine.png --add-data "gifs;gifs" --add-data "tech_link_theme_vn.qm;." --add-data "tech_link_theme_cn.qm;." --distpath "Apps" main.py

import multiprocessing
import subprocess
import tempfile
import traceback
import logging
import os
import sys
from pathlib import Path

from crash_watchdog import setup_crash_watchdog

LOADING_ENV   = 'STRIKE_MACHINE_LOADING'
LOADING_PAUSE = 'STRIKE_MACHINE_LOADING_PAUSE'

def _spawn_loading():
    sig   = tempfile.NamedTemporaryFile(delete=False, suffix='.lock')
    pause = tempfile.NamedTemporaryFile(delete=False, suffix='.pause')
    sig.close()
    pause.close()

    env = os.environ.copy()
    env[LOADING_ENV]   = sig.name
    env[LOADING_PAUSE] = pause.name

    proc = subprocess.Popen(
        [sys.executable] + sys.argv,
        env=env,
        close_fds=True,
    )
    return proc, sig.name, pause.name

def _close_loading(proc, signal_file, pause_file=None):
    if proc is None:
        return
    for f in filter(None, [signal_file, pause_file]):
        try:
            os.remove(f)
        except FileNotFoundError:
            pass
    try:
        proc.wait(timeout=2)
    except subprocess.TimeoutExpired:
        proc.terminate()

def get_exe_dir():
    """Lấy thư mục chứa file .exe (hoặc .py khi dev)"""
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent
    else:
        return Path(__file__).parent

WEB_INIT = (get_exe_dir() / "web_on.txt").is_file()

if os.environ.get(LOADING_ENV):
    signal_file = os.environ[LOADING_ENV]
    pause_file  = os.environ.get(LOADING_PAUSE, '')

    _loading_watchdog = setup_crash_watchdog(
        get_exe_dir(),
        role="loading",
    )

    from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
    from PySide6.QtCore    import Qt, QFileSystemWatcher
    from PySide6.QtGui     import QMovie

    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS          # type: ignore
        except Exception:
            base_path = os.path.abspath('.')
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
                    Qt.KeepAspectRatio,  # type: ignore
                    Qt.SmoothTransformation,  # type: ignore
                )
                self.setPixmap(scaled)

    app = QApplication(sys.argv)

    win = QWidget()
    win.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)  # type: ignore
    win.setAttribute(Qt.WA_TranslucentBackground)                                    # type: ignore
    win.resize(120, 120)

    layout = QVBoxLayout(win)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setAlignment(Qt.AlignCenter)                                              # type: ignore

    label = SmoothGifLabel()
    label.setAlignment(Qt.AlignCenter)                                               # type: ignore
    label.setStyleSheet('background: transparent;')
    label.setFixedSize(win.size())
    layout.addWidget(label)

    gif_path = os.path.join(resource_path('gifs'), 'Loading.gif')
    movie = QMovie(gif_path)
    movie.setCacheMode(QMovie.CacheAll)                                              # type: ignore
    label.setMovie(movie)
    movie.start()

    screen = app.primaryScreen().availableGeometry()
    win.move(
        screen.x() + (screen.width()  - win.width())  // 2,
        screen.y() + (screen.height() - win.height()) // 2,
    )
    win.show()

    signal_watcher = QFileSystemWatcher([signal_file])
    signal_watcher.fileChanged.connect(lambda: (movie.stop(), app.quit()))          # type: ignore

    if pause_file and os.path.exists(pause_file):
        pause_watcher = QFileSystemWatcher([pause_file])

        def _on_pause_changed(path):
            if not os.path.exists(path):
                win.hide()
            else:
                win.show()

        pause_watcher.fileChanged.connect(_on_pause_changed)

    _loading_exit_code = app.exec()
    _loading_watchdog.mark_clean_exit(f"loading window event loop returned exit_code={_loading_exit_code}")
    sys.exit(_loading_exit_code)

if __name__ == '__main__':
    multiprocessing.freeze_support()

    _watchdog = setup_crash_watchdog(
        get_exe_dir(),
        role="main",
    )

    if WEB_INIT:
        from web_server import run_web_server

        web_queue = multiprocessing.Queue(maxsize=10)
        web_process = multiprocessing.Process(
            target=run_web_server,
            args=(web_queue,),
            daemon=True
        )
        web_process.start()

    _loader_proc, _signal_file, _pause_file = _spawn_loading()

    def _pause_loading():
        try:
            os.remove(_pause_file)
        except FileNotFoundError:
            pass

    def _resume_loading():
        try:
            open(_pause_file, 'w').close()
        except Exception:
            pass

    app = None
    try:
        from PySide6.QtWidgets import QApplication, QMessageBox, QStyle
        from PySide6.QtCore    import QLocale, QSharedMemory, QSystemSemaphore, QTimer
        from source            import StrikeMachine
        # from source_backup            import StrikeMachine

        def check_full_language_info():
            locale = QLocale.system()
            
            info = {
                "System Locale": locale.name(),
                "BCP47": locale.bcp47Name(),
                "Language": locale.languageToString(locale.language()),
                "Script": locale.scriptToString(locale.script()),
                "Country": locale.territoryToString(locale.territory()),
                "Decimal Point": locale.decimalPoint(),
                "Measurement System": "Metric" if locale.measurementSystem() == QLocale.MeasurementSystem.MetricSystem else "Imperial",
            }
            return info

        app = QApplication(sys.argv)
        QLocale.setDefault(QLocale(QLocale.Language.C))
        app.aboutToQuit.connect(
            lambda: _watchdog.mark_clean_exit("QApplication.aboutToQuit fired")
        )

        semaphore = QSystemSemaphore('StrikeMachine_Instance', 1)
        semaphore.acquire()
        BASE_W, BASE_H = 1024, 724
        _screen_geo = app.primaryScreen().availableGeometry()

        # availableGeometry() đã trừ taskbar, nhưng CHƯA trừ title bar của cửa sổ
        # (title bar chỉ xuất hiện sau khi show()). Nếu không trừ trước, content
        # sẽ được scale vừa khít available height, rồi title bar cộng thêm vào
        # sẽ đẩy đáy cửa sổ lọt xuống dưới, đè lên taskbar.
        _title_bar_h = QApplication.style().pixelMetric(QStyle.PM_TitleBarHeight) #type: ignore
        if _title_bar_h <= 0:
            _title_bar_h = 32  # fallback nếu platform/WM không trả về giá trị hợp lệ

        _usable_h = _screen_geo.height() - _title_bar_h

        scale_factor = min(
            _screen_geo.width() / BASE_W,
            _usable_h           / BASE_H,
        )
        scale_factor = max(scale_factor, 0.5)

        shared_memory = QSharedMemory('StrikeMachine_SharedMem')
        is_running = shared_memory.attach()
        if not is_running:
            shared_memory.create(1)
        semaphore.release()

        if is_running:
            _close_loading(_loader_proc, _signal_file, _pause_file)
            sys.exit(1)

        if WEB_INIT:
            window = StrikeMachine(
                on_hide_loading=_pause_loading,
                on_show_loading=_resume_loading,
                info_system=check_full_language_info,  # type: ignore
                plc_queue=web_queue,  # type: ignore
                scale_factor=scale_factor
            )
        else:
            window = StrikeMachine(
                on_hide_loading=_pause_loading,
                on_show_loading=_resume_loading,
                info_system=check_full_language_info,  # type: ignore
                scale_factor=scale_factor
            )

        def _center_on_screen(win):
            screen_geo = QApplication.primaryScreen().availableGeometry()
            frame = win.frameGeometry()
            frame.moveCenter(screen_geo.center())
            win.move(frame.topLeft())

        window.show()
        QTimer.singleShot(0, lambda: _center_on_screen(window))

        QTimer.singleShot(100, lambda: (window.raise_(), window.activateWindow()))

    except Exception:
        _close_loading(_loader_proc, _signal_file, _pause_file)

        error_detail = traceback.format_exc()
        _watchdog.log_custom(
            f"STARTUP_EXCEPTION (crash trước khi vào event loop chính):\n{error_detail}",
            level=logging.CRITICAL,
        )
        if app is not None:
            QMessageBox.critical(None, 'Startup errors',  # type: ignore
                                 f'The app cannot be launched:\n\n{error_detail}')
        else:
            with open('crash.log', 'w') as f:
                f.write(f'Startup errors:\n{error_detail}\n')
        sys.exit(1)

    finally:
        _close_loading(_loader_proc, _signal_file, _pause_file)

    if app is not None:
        _exit_code = app.exec()
        _watchdog.log_custom(f"app.exec() returned exit_code={_exit_code}")
        sys.exit(_exit_code)