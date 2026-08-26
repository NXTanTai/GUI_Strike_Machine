# pyinstaller --onedir --noconsole --name="Strike Machine App" --icon=icons\strike_machine.png --add-binary "lib\snap7.dll;." --add-data "gifs;gifs" --add-data "tech_link_theme_vn.qm;." --add-data "tech_link_theme_cn.qm;." --distpath "Apps" main_edited.py

import multiprocessing
import subprocess
import tempfile
import traceback
import logging
import os
import sys
from pathlib import Path
from crash_watchdog import setup_crash_watchdog

LOADING_ENV         = "STRIKE_MACHINE_LOADING"
LOADING_PAUSE       = "STRIKE_MACHINE_LOADING_PAUSE"
SINGLE_INSTANCE_KEY = "StrikeMachine_SingleInstance"
LOCAL_SERVER_NAME   = "StrikeMachine_LocalServer"

def get_exe_dir() -> Path:
    """Thư mục chứa file .exe (hoặc .py khi dev)."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).parent

def _spawn_loading():
    """Spawn process loading GIF riêng."""
    sig = tempfile.NamedTemporaryFile(delete=False, suffix=".lock")
    pause = tempfile.NamedTemporaryFile(delete=False, suffix=".pause")
    sig.close()
    pause.close()

    env = os.environ.copy()
    env[LOADING_ENV] = sig.name
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


def ensure_single_instance(app) -> bool:
    """
    True  → được phép chạy (instance đầu tiên)
    False → đã có instance khác đang chạy
    """
    from PySide6.QtCore import QSharedMemory, QSystemSemaphore
    from PySide6.QtNetwork import QLocalServer, QLocalSocket

    semaphore = QSystemSemaphore("StrikeMachine_Sem", 1)
    semaphore.acquire()

    shared = QSharedMemory(SINGLE_INSTANCE_KEY)

    if shared.attach():
        semaphore.release()
        socket = QLocalSocket()
        socket.connectToServer(LOCAL_SERVER_NAME)
        if socket.waitForConnected(800):
            socket.write(b"raise")
            socket.flush()
            socket.waitForBytesWritten(500)
            socket.disconnectFromServer()
        return False

    if not shared.create(1):
        shared.attach()
        shared.detach()
        if not shared.create(1):
            semaphore.release()
            return False

    semaphore.release()

    QLocalServer.removeServer(LOCAL_SERVER_NAME)
    server = QLocalServer(app)
    server.listen(LOCAL_SERVER_NAME)

    def on_new_connection():
        sock = server.nextPendingConnection()
        if sock is None:
            return
        sock.waitForReadyRead(300)
        for w in app.topLevelWidgets():
            if w.isWindow() and not w.isHidden():
                w.showNormal()
                w.raise_()
                w.activateWindow()
                break
        sock.disconnectFromServer()

    server.newConnection.connect(on_new_connection)

    app._single_instance_shared = shared
    app._single_instance_server = server
    return True

WEB_INIT = (get_exe_dir() / "web_on.txt").is_file()

if os.environ.get(LOADING_ENV):
    signal_file = os.environ[LOADING_ENV]
    pause_file = os.environ.get(LOADING_PAUSE, "")

    _loading_watchdog = setup_crash_watchdog(get_exe_dir(), role="loading")

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
                    Qt.KeepAspectRatio,  # type: ignore
                    Qt.SmoothTransformation,  # type: ignore
                )
                self.setPixmap(scaled)

    app = QApplication(sys.argv)

    win = QWidget()
    win.setWindowFlags(
        Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool  # type: ignore
    )
    win.setAttribute(Qt.WA_TranslucentBackground)  # type: ignore
    win.resize(120, 120)

    layout = QVBoxLayout(win)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setAlignment(Qt.AlignCenter)  # type: ignore

    label = SmoothGifLabel()
    label.setAlignment(Qt.AlignCenter)  # type: ignore
    label.setStyleSheet("background: transparent;")
    label.setFixedSize(win.size())
    layout.addWidget(label)

    gif_path = os.path.join(resource_path("gifs"), "Loading.gif")
    movie = QMovie(gif_path)
    movie.setCacheMode(QMovie.CacheAll)  # type: ignore
    label.setMovie(movie)
    movie.start()

    screen = app.primaryScreen().availableGeometry()
    win.move(
        screen.x() + (screen.width() - win.width()) // 2,
        screen.y() + (screen.height() - win.height()) // 2,
    )
    win.show()

    signal_watcher = QFileSystemWatcher([signal_file])
    signal_watcher.fileChanged.connect(lambda: (movie.stop(), app.quit()))  # type: ignore

    if pause_file and os.path.exists(pause_file):
        pause_watcher = QFileSystemWatcher([pause_file])

        def _on_pause_changed(path):
            if not os.path.exists(path):
                win.hide()
            else:
                win.show()

        pause_watcher.fileChanged.connect(_on_pause_changed)

    _loading_exit_code = app.exec()
    _loading_watchdog.mark_clean_exit(
        f"loading window event loop returned exit_code={_loading_exit_code}"
    )
    sys.exit(_loading_exit_code)

if __name__ == "__main__":
    multiprocessing.freeze_support()

    _watchdog = setup_crash_watchdog(get_exe_dir(), role="main")

    from PySide6.QtWidgets import QApplication, QMessageBox, QStyle
    from PySide6.QtCore import QLocale, QTimer

    app = QApplication(sys.argv)
    QLocale.setDefault(QLocale(QLocale.Language.C))
    app.aboutToQuit.connect(
        lambda: _watchdog.mark_clean_exit("QApplication.aboutToQuit fired")
    )

    if not ensure_single_instance(app):
        sys.exit(0)

    _loader_proc = None
    _signal_file = None
    _pause_file = None

    try:
        if WEB_INIT:
            from web_server import run_web_server

            web_queue = multiprocessing.Queue(maxsize=10)
            web_process = multiprocessing.Process(
                target=run_web_server,
                args=(web_queue,),
                daemon=True,
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
                open(_pause_file, "w").close()
            except Exception:
                pass

        from source_edited import StrikeMachine

        def check_full_language_info():
            locale = QLocale.system()
            return {
                "System Locale": locale.name(),
                "BCP47": locale.bcp47Name(),
                "Language": locale.languageToString(locale.language()),
                "Script": locale.scriptToString(locale.script()),
                "Country": locale.territoryToString(locale.territory()),
                "Decimal Point": locale.decimalPoint(),
                "Measurement System": (
                    "Metric"
                    if locale.measurementSystem()
                    == QLocale.MeasurementSystem.MetricSystem
                    else "Imperial"
                ),
            }

        # Scale theo màn hình
        BASE_W, BASE_H = 1024, 724
        _screen_geo = app.primaryScreen().availableGeometry()
        _title_bar_h = QApplication.style().pixelMetric(
            QStyle.PM_TitleBarHeight  # type: ignore
        )
        if _title_bar_h <= 0:
            _title_bar_h = 32
        _usable_h = _screen_geo.height() - _title_bar_h
        scale_factor = max(
            min(_screen_geo.width() / BASE_W, _usable_h / BASE_H),
            0.5,
        )

        kwargs = dict(
            on_hide_loading=_pause_loading,
            on_show_loading=_resume_loading,
            info_system=check_full_language_info,
            scale_factor=scale_factor,
        )
        if WEB_INIT:
            kwargs["plc_queue"] = web_queue  # type: ignore

        window = StrikeMachine(**kwargs)

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
            f"STARTUP_EXCEPTION:\n{error_detail}",
            level=logging.CRITICAL,
        )
        QMessageBox.critical(
            None,
            "Startup errors",
            f"The app cannot be launched:\n\n{error_detail}",
        )
        sys.exit(1)

    _close_loading(_loader_proc, _signal_file, _pause_file)

    _exit_code = app.exec()
    _watchdog.log_custom(f"app.exec() returned exit_code={_exit_code}")
    sys.exit(_exit_code)