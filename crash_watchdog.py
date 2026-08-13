"""
crash_watchdog.py
------------------
Tự động log LÝ DO app tắt vào 1 file DUY NHẤT: "sm_crash.log",
đặt ngay tại thư mục chứa app (get_exe_dir()) — không tạo folder con.

Phát hiện & phân biệt được:

    1. Thoát bình thường (clean exit)
    2. Crash do lỗi code Python không được catch (kèm traceback đầy đủ)
    3. Crash cứng / native crash (segfault, abort, illegal instruction —
       thường do driver đồ họa, Qt, pyvista/VTK, ...) qua faulthandler
    4. Bị tắt từ bên ngoài (Task Manager "End task", kill, logoff, tắt máy)
    5. Bị kill -9 / rút điện / treo cứng: không signal nào kịp chạy nên
       không log được NGAY lúc đó, nhưng lần khởi động SAU sẽ tự phát hiện
       qua file lock còn sót lại và ghi "PREVIOUS_SESSION_DID_NOT_EXIT_CLEANLY"
       vào log của lần chạy mới.

AN TOÀN KHI ĐÓNG GÓI .EXE:
    - Nếu thư mục app KHÔNG có quyền ghi (vd cài trong C:\\Program Files),
      tự động fallback sang %LOCALAPPDATA%\\StrikeMachineApp rồi tới thư
      mục temp hệ thống. Không bao giờ raise exception khiến app không
      khởi động được.
    - An toàn với build --noconsole (sys.stderr có thể là None).

Cách dùng trong main.py (gọi CÀNG SỚM CÀNG TỐT, trước khi tạo QApplication):

    from crash_watchdog import setup_crash_watchdog

    watchdog = setup_crash_watchdog(get_exe_dir(), role="main")

    app = QApplication(sys.argv)
    app.aboutToQuit.connect(lambda: watchdog.mark_clean_exit("aboutToQuit"))

    ...
    exit_code = app.exec()
    watchdog.mark_clean_exit(f"app.exec() returned {exit_code}")
    sys.exit(exit_code)
"""

from __future__ import annotations

import atexit
import faulthandler
import logging
import os
import signal
import sys
import tempfile
import traceback
from datetime import datetime
from pathlib import Path

LOG_FILENAME = "sm_crash.log"


class _NullWatchdog:
    """Watchdog rỗng, dùng khi khởi tạo thất bại hoàn toàn — đảm bảo main.py
    luôn gọi được .mark_clean_exit()/.log_custom() an toàn mà không cần
    kiểm tra None, và watchdog không bao giờ là nguyên nhân khiến app
    không khởi động được."""

    def mark_clean_exit(self, detail: str = "") -> None:
        pass

    def log_custom(self, message: str, level: int = logging.INFO) -> None:
        pass


class CrashWatchdog:
    def __init__(self, app_dir: Path, role: str = "main"):
        self.role = role
        self.app_dir = Path(app_dir)
        self._clean_exit_marked = False

        self._resolve_writable_dir()

        self._log_path = self.app_dir / LOG_FILENAME
        self._lock_path = self.app_dir / f".sm_crash_{role}.lock"

        # ---- 1) Mở 1 file duy nhất, dùng chung cho cả logging text lẫn faulthandler ----
        self._log_file = open(self._log_path, "a", buffering=1, encoding="utf-8")

        self.logger = logging.getLogger(f"crash_watchdog.{role}.{id(self)}")
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False
        handler = logging.StreamHandler(stream=self._log_file)
        handler.setFormatter(
            logging.Formatter(f"%(asctime)s - [{role}] - %(levelname)s - %(message)s")
        )
        self.logger.addHandler(handler)

        # ---- 2) faulthandler: bắt crash cứng, ghi vào CÙNG file ----
        try:
            self._log_file.write(
                f"\n===== [{role}] Process start: PID={os.getpid()} at {datetime.now()} =====\n"
            )
            self._log_file.flush()
            faulthandler.enable(file=self._log_file, all_threads=True)
        except Exception as e:
            self.logger.error(f"Không bật được faulthandler (native crash sẽ không được ghi): {e}")

        # ---- 3) sys.excepthook: bắt exception Python không được try/except xử lý ----
        self._prev_excepthook = sys.excepthook
        sys.excepthook = self._on_uncaught_exception

        # ---- 4) Signal handler: bắt các tín hiệu tắt do OS/người dùng gửi ----
        for sig_name in ("SIGINT", "SIGTERM", "SIGBREAK", "SIGHUP"):
            sig = getattr(signal, sig_name, None)
            if sig is None:
                continue
            try:
                signal.signal(sig, self._on_os_signal)
            except (ValueError, OSError):
                pass

        # ---- 5) Heartbeat / lock file: phát hiện phiên chạy TRƯỚC có thoát sạch không ----
        self._check_previous_session()
        self._write_heartbeat()

        # ---- 6) atexit: log lại lý do khi process thực sự kết thúc ----
        atexit.register(self._on_process_exit)

        self.logger.info(f"Watchdog initialized. PID={os.getpid()} log_file={self._log_path}")

    # ------------------------------------------------------------------ #
    # Chọn thư mục ghi log, fallback nếu app_dir không ghi được
    # ------------------------------------------------------------------ #
    def _resolve_writable_dir(self):
        candidates = [self.app_dir]

        local_appdata = os.environ.get("LOCALAPPDATA")
        if local_appdata:
            candidates.append(Path(local_appdata) / "StrikeMachineApp")

        candidates.append(Path(tempfile.gettempdir()) / "StrikeMachineApp")

        for candidate in candidates:
            try:
                candidate.mkdir(parents=True, exist_ok=True)
                test_file = candidate / ".write_test"
                test_file.write_text("ok", encoding="utf-8")
                test_file.unlink(missing_ok=True)  # type: ignore[call-arg]
                self.app_dir = candidate
                return
            except Exception:
                continue

        # Trường hợp cùng đường không thư mục nào ghi được -> thư mục tạm riêng
        self.app_dir = Path(tempfile.mkdtemp(prefix="strike_machine_crash_"))

    # ------------------------------------------------------------------ #
    # Kiểm tra phiên chạy trước
    # ------------------------------------------------------------------ #
    def _check_previous_session(self):
        if self._lock_path.exists():
            try:
                prev_info = self._lock_path.read_text(encoding="utf-8")
            except Exception:
                prev_info = "(không đọc được nội dung lock file)"
            self.logger.warning(
                "PREVIOUS_SESSION_DID_NOT_EXIT_CLEANLY -> lần chạy trước có thể đã bị "
                "kill cứng (Task Manager 'End task', kill -9, mất điện, treo máy...). "
                f"Thông tin phiên trước: {prev_info}"
            )
        else:
            self.logger.info("Không tìm thấy lock file cũ -> phiên chạy trước (nếu có) đã thoát sạch.")

    def _write_heartbeat(self):
        try:
            self._lock_path.write_text(
                f"pid={os.getpid()}\nstarted_at={datetime.now().isoformat()}\n",
                encoding="utf-8",
            )
        except Exception as e:
            self.logger.error(f"Không ghi được lock file: {e}")

    def _remove_heartbeat(self):
        try:
            if self._lock_path.exists():
                self._lock_path.unlink()
        except Exception as e:
            self.logger.error(f"Không xoá được lock file: {e}")

    # ------------------------------------------------------------------ #
    # Các handler bắt lỗi
    # ------------------------------------------------------------------ #
    def _on_uncaught_exception(self, exc_type, exc_value, exc_tb):
        try:
            tb_text = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
            self.logger.critical(f"PYTHON_EXCEPTION (app sẽ crash do lỗi code):\n{tb_text}")
        except Exception:
            pass
        try:
            if self._prev_excepthook and sys.stderr is not None:
                self._prev_excepthook(exc_type, exc_value, exc_tb)
        except Exception:
            pass

    def _on_os_signal(self, signum, frame):
        try:
            sig_name = signal.Signals(signum).name
        except Exception:
            sig_name = str(signum)
        self.logger.warning(
            f"OS_SIGNAL nhận được: {sig_name} ({signum}) "
            "-> app bị yêu cầu tắt từ bên ngoài (Task Manager, kill, logoff, tắt máy...)."
        )
        self.mark_clean_exit(f"terminated_by_signal={sig_name}")
        sys.exit(128 + signum)

    def _on_process_exit(self):
        if getattr(self, "_exit_already_logged", False):
            return
        self._exit_already_logged = True

        try:
            if self._clean_exit_marked:
                self.logger.info("CLEAN_EXIT xác nhận qua atexit.")
            else:
                self.logger.warning(
                    "Process kết thúc qua atexit nhưng KHÔNG có mark_clean_exit() nào được gọi "
                    "trước đó -> có thể là crash không rõ nguyên nhân."
                )
        except Exception:
            pass

        self._remove_heartbeat()
        try:
            self._log_file.flush()
            self._log_file.close()
        except Exception:
            pass

    # ------------------------------------------------------------------ #
    # API công khai để gọi từ main.py
    # ------------------------------------------------------------------ #
    def mark_clean_exit(self, detail: str = ""):
        self._clean_exit_marked = True
        try:
            self.logger.info(f"CLEAN_EXIT được đánh dấu. Detail: {detail}")
        except Exception:
            pass

    def log_custom(self, message: str, level: int = logging.INFO):
        try:
            self.logger.log(level, message)
        except Exception:
            pass


def setup_crash_watchdog(app_dir: Path, role: str = "main"):
    """Hàm tiện ích để gọi 1 dòng từ main.py.
    KHÔNG BAO GIỜ raise exception — nếu khởi tạo thất bại, trả về
    _NullWatchdog để app chính vẫn chạy bình thường."""
    try:
        return CrashWatchdog(app_dir=app_dir, role=role)
    except Exception as e:
        try:
            print(f"[crash_watchdog] Khởi tạo thất bại, bỏ qua watchdog: {e}", file=sys.stderr)
        except Exception:
            pass
        return _NullWatchdog()