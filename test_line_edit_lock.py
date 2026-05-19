import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout,
    QLineEdit, QDialog, QDialogButtonBox, QLabel,
    QMessageBox, QPushButton, QHBoxLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


CORRECT_PASSWORD = "1234"


# ──────────────────────────────────────────────
#  Password Dialog
# ──────────────────────────────────────────────
class PasswordDialog(QDialog):
    """Dialog hỏi mật khẩu; cho nhập lại nếu sai, đóng dialog = huỷ."""

    def __init__(self, field_name: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Xác thực")
        self.setFixedWidth(320)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        self.info_label = QLabel(f'Nhập mật khẩu để chỉnh sửa "{field_name}":')
        self.info_label.setWordWrap(True)
        layout.addWidget(self.info_label)

        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.setPlaceholderText("Mật khẩu…")
        layout.addWidget(self.password_edit)

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setFont(QFont("", 9))
        layout.addWidget(self.error_label)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self._check_password)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        # Nhấn Enter trong ô mật khẩu cũng submit
        self.password_edit.returnPressed.connect(self._check_password)

    def _check_password(self):
        if self.password_edit.text() == CORRECT_PASSWORD:
            self.accept()
        else:
            self.error_label.setText("❌ Mật khẩu không đúng. Vui lòng thử lại.")
            self.password_edit.clear()
            self.password_edit.setFocus()


# ──────────────────────────────────────────────
#  Protected QLineEdit
# ──────────────────────────────────────────────
class ProtectedLineEdit(QLineEdit):
    """
    QLineEdit bị khoá.
    - Khi người dùng click → hiện PasswordDialog.
    - Nếu đúng mật khẩu → mở khoá để nhập và gọi on_unlocked().
    - Nếu sai / đóng dialog → vẫn bị khoá.
    """

    def __init__(self, field_name: str, on_unlocked=None, parent=None):
        super().__init__(parent)
        self.field_name = field_name
        self.on_unlocked = on_unlocked          # callback sau khi mở khoá
        self._locked = True
        self.setReadOnly(True)
        self.setPlaceholderText("🔒 Click để nhập...")

    # ── Bắt sự kiện click ──────────────────────
    def mousePressEvent(self, event):
        if self._locked:
            self._ask_password()
        else:
            super().mousePressEvent(event)

    # ── Hiện dialog ────────────────────────────
    def _ask_password(self):
        dlg = PasswordDialog(self.field_name, parent=self)
        result = dlg.exec()

        if result == QDialog.Accepted:
            self._unlock()
        # Nếu rejected (đóng dialog) → không làm gì

    # ── Mở khoá ────────────────────────────────
    def _unlock(self):
        self._locked = False
        self.setReadOnly(False)
        self.setPlaceholderText("Nhập giá trị…")
        self.setFocus()
        if callable(self.on_unlocked):
            self.on_unlocked(self)


# ──────────────────────────────────────────────
#  Hàm kết nối mẫu (thay bằng logic thực tế)
# ──────────────────────────────────────────────
def connect_field_1(line_edit: QLineEdit):
    print(f"[Field 1] Đã mở khoá → sẵn sàng nhận dữ liệu. Widget: {line_edit}")

def connect_field_2(line_edit: QLineEdit):
    print(f"[Field 2] Đã mở khoá → sẵn sàng nhận dữ liệu. Widget: {line_edit}")

def connect_field_3(line_edit: QLineEdit):
    print(f"[Field 3] Đã mở khoá → sẵn sàng nhận dữ liệu. Widget: {line_edit}")

def connect_field_4(line_edit: QLineEdit):
    print(f"[Field 4] Đã mở khoá → sẵn sàng nhận dữ liệu. Widget: {line_edit}")


# ──────────────────────────────────────────────
#  Main Window
# ──────────────────────────────────────────────
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Protected Fields")
        self.resize(400, 220)

        form = QFormLayout(self)
        form.setSpacing(12)
        form.setContentsMargins(24, 24, 24, 24)

        fields = [
            ("Trường 1:", connect_field_1),
            ("Trường 2:", connect_field_2),
            ("Trường 3:", connect_field_3),
            ("Trường 4:", connect_field_4),
        ]

        for label_text, callback in fields:
            edit = ProtectedLineEdit(label_text.rstrip(":"), on_unlocked=callback)
            form.addRow(label_text, edit)


# ──────────────────────────────────────────────
#  Entry Point
# ──────────────────────────────────────────────
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())