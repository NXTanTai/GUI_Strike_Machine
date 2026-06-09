# pyinstaller --onefile --noconsole --name="Strike Machine App" --icon=icons\strike_machine.png --add-binary "lib\snap7.dll;." --add-data "gifs;gifs" --add-data "tech_link_theme_cn.qm;." --distpath "Apps" main.py
# pyinstaller --onefile --noconsole --name="Strike Machine App" --icon=icons\hose_icon.png  --add-binary "lib\snap7.dll;." --add-data "gifs;gifs" --add-data "tech_link_theme_cn.qm;." --distpath "Apps" main.py

import multiprocessing
import subprocess
import tempfile
import traceback
import os
import sys

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

if os.environ.get(LOADING_ENV):
    signal_file = os.environ[LOADING_ENV]
    pause_file  = os.environ.get(LOADING_PAUSE, '')

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
        (screen.width()  - win.width())  // 2,
        (screen.height() - win.height()) // 2,
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

    sys.exit(app.exec())

if __name__ == '__main__':
    multiprocessing.freeze_support()
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
        from PySide6.QtWidgets import QApplication, QMessageBox
        from PySide6.QtCore    import QLocale, QSharedMemory, QSystemSemaphore, QTimer
        from source            import StrikeMachine

        app = QApplication(sys.argv)
        QLocale.setDefault(QLocale(QLocale.Language.C))

        semaphore = QSystemSemaphore('StrikeMachine_Instance', 1)
        semaphore.acquire()

        if sys.platform != 'win32':
            nix_fix = QSharedMemory('StrikeMachine_SharedMem')
            if nix_fix.attach():
                nix_fix.detach()

        shared_memory = QSharedMemory('StrikeMachine_SharedMem')
        is_running = shared_memory.attach()
        if not is_running:
            shared_memory.create(1)
        semaphore.release()

        if is_running:
            _close_loading(_loader_proc, _signal_file, _pause_file)
            sys.exit(1)

        window = StrikeMachine(
            on_hide_loading=_pause_loading,
            on_show_loading=_resume_loading,
        )

        screen = QApplication.primaryScreen().availableGeometry()
        window.move(
            (screen.width()  - window.width())  // 2,
            (screen.height() - window.height()) // 2,
        )
        window.show()

        QTimer.singleShot(100, lambda: (window.raise_(), window.activateWindow()))

    except Exception:
        _close_loading(_loader_proc, _signal_file, _pause_file)

        error_detail = traceback.format_exc()
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
        sys.exit(app.exec())