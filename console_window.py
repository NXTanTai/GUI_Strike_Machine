import sys
import os
import socket
import tempfile
import threading
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QColor, QTextCharFormat, QTextCursor, QFont, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                                QVBoxLayout, QHBoxLayout, QTextEdit,
                                QLabel, QLineEdit)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

class ConsoleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Strike Machine Console [Version 1.3]")
        self.resize(1080, 720)
        self.setStyleSheet("background:#0c0c0c;")
        self._awaiting_confirm = False
        self._stdin_running = True

        icon_path = resource_path(os.path.join("icons", "cmd.png"))
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.text = QTextEdit()
        self.text.setReadOnly(True)
        self.text.setFont(QFont("Consolas", 15))
        self.text.setStyleSheet("""
            QTextEdit {
                background: #0c0c0c;
                color: #cccccc;
                border: none;
                padding: 4px 8px;
            }
            QScrollBar:vertical {
                background: #1a1a1a;
                width: 8px;
            }
            QScrollBar::handle:vertical {
                background: #444;
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        layout.addWidget(self.text)

        input_row = QHBoxLayout()
        input_row.setContentsMargins(8, 4, 8, 8)
        input_row.setSpacing(0)

        self._prompt = QLabel("C:\\SM_PRD>")
        self._prompt.setFont(QFont("Consolas", 15))
        self._prompt.setStyleSheet(
            "color:#cccccc; background:#0c0c0c; padding: 2px 4px 2px 0;"
        )

        self._input = QLineEdit()
        self._input.setFont(QFont("Consolas", 15))
        self._input.setStyleSheet("""
            QLineEdit {
                background: #0c0c0c;
                color: #cccccc;
                border: none;
                padding: 2px 0;
            }
        """)
        self._input.returnPressed.connect(self._on_command)

        input_row.addWidget(self._prompt)
        input_row.addWidget(self._input)
        layout.addLayout(input_row)

        self._colors = {
            "DEBUG":    "#888888",
            "INFO":     "#cccccc",
            "WARNING":  "#ffb74d",
            "ERROR":    "#e57373",
            "CRITICAL": "#ff1744",
        }

        self._setup_stdin_reader()

        self.append_log(
            "Strike Machine Console [Version 1.3]\n"
            "(c) Tech-Link Silicones. All rights reserved.\n",
            "INFO"
        )

    def _setup_stdin_reader(self):
        from PySide6.QtCore import QMetaObject, Q_ARG

        def _read_loop():
            while self._stdin_running:
                try:
                    line = sys.stdin.readline()
                    if not line:
                        break
                    QMetaObject.invokeMethod(
                        self, "_on_stdin_line",
                        Qt.ConnectionType.QueuedConnection,
                        Q_ARG(str, line.rstrip())
                    )
                except Exception:
                    break

        self._stdin_thread = threading.Thread(target=_read_loop, daemon=True)
        self._stdin_thread.start()

    @Slot(str)
    def _on_stdin_line(self, line: str):
        level = "INFO"
        if " - WARNING - "   in line: level = "WARNING"
        elif " - ERROR - "   in line: level = "ERROR"
        elif " - CRITICAL - " in line: level = "CRITICAL"
        elif " - DEBUG - "   in line: level = "DEBUG"
        self.append_log(line, level)

    def _on_command(self):
        cmd = self._input.text().strip()
        self._input.clear()
        if not cmd:
            return

        if self._awaiting_confirm:
            self._awaiting_confirm = False
            self.append_log(f"C:\\SM_PRD> {cmd}", "INFO")
            if cmd.lower() == "y":
                self.append_log("[WARN] Force quitting application...", "WARNING")
                flag_path = os.path.join(tempfile.gettempdir(), "sm_force_quit.flag")
                with open(flag_path, "w") as f:
                    f.write("FORCE_QUIT")
            else:
                self.append_log("Force quit cancelled.", "INFO")
            return

        self.append_log(f"C:\\SM_PRD> {cmd}", "INFO")

        if cmd.lower() == "cls":
            self.text.clear()
        elif cmd.lower() == "help":
            self.append_log(
                "  cls                - Clear screen\n"
                "  help               - Show commands\n"
                "  ipconfig           - Show network info\n",
                "DEBUG"
            )
        elif cmd.lower() == "ipconfig":
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            self.append_log(
                f"  Host Name . . . . : {hostname}\n"
                f"  IPv4 Address. . . : {ip}\n"
                f"  Subnet Mask . . . : 255.255.255.0\n"
                f"  Default Gateway . : {'.'.join(ip.split('.')[:3])}.1",
                "INFO"
            )
        elif cmd.lower() == "force quitting app":
            self.append_log("Are you sure you want to force quit? (Y/N)", "WARNING")
            self._awaiting_confirm = True
        else:
            self.append_log(f"'{cmd}' is not recognized as a command. ", "WARNING")

    def append_log(self, msg: str, level: str):
        fmt = QTextCharFormat()
        fmt.setForeground(QColor(self._colors.get(level, "#cccccc")))
        
        scrollbar = self.text.verticalScrollBar()
        was_at_bottom = scrollbar.value() >= scrollbar.maximum() - 5

        cursor = self.text.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.insertText(msg + "\n", fmt)

        if was_at_bottom:
            self.text.ensureCursorVisible()
            
    def closeEvent(self, event):
        self.hide()
        self._stdin_running = False
        try:
            sys.stdin.close()
        except Exception:
            pass
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ConsoleWindow()
    win.show()
    sys.exit(app.exec())