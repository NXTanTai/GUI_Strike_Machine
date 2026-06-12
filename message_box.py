import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QFrame, QGridLayout,
                             QScrollArea, QTabWidget, QListWidget, QTextEdit,
                             QLineEdit, QComboBox, QGroupBox, QProgressBar, QMessageBox,
                             QSpinBox, QCheckBox, QSlider, QFormLayout, QSplitter, QDialog)
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QRect, QPropertyAnimation
from PySide6.QtGui import QFont, QPixmap, QPainter, QColor, QLinearGradient, QPalette
import resources_rc

FONT_FAMILY  = "Segoe UI"
FONT_SIZE_LG = 16
FONT_SIZE_MD = 16
FONT_SIZE_SM = 13

TRANSLATIONS = {
    "en": {
        "OK":     "OK",
        "Yes":    "Yes",
        "No":     "No",
        "Save":   "Save",
        "Apply":  "Apply",
        "Cancel": "Cancel",
        "Close":  "Close",
    },
    "cn": {
        "OK":     "确定",
        "Yes":    "是",
        "No":     "否",
        "Save":   "保存",
        "Apply":  "应用",
        "Cancel": "取消",
        "Close":  "关闭",
    },
}

_PRIMARY_KEYS = {"OK", "Yes", "Save", "Apply"}
_NEGATIVE_KEYS = {"No", "Cancel", "Close"}


class LightThemeMessageBox(QDialog):
    """
    Custom message box with modern design and EN / CN language support.

    Pass ``lang="en"`` (default) or ``lang="cn"`` to any call to switch the
    button labels automatically.

    Usage:
        # Information
        LightThemeMessageBox.information(self, "Title", "Message", lang=self.lang)

        # Question (returns True/False)
        if LightThemeMessageBox.question(self, "Title", "Question?", lang=self.lang):
            ...

        # Warning / Error / Success
        LightThemeMessageBox.warning(self, "Title", "Warning", lang=self.lang)
        LightThemeMessageBox.error(self, "Title", "Error",   lang=self.lang)
        LightThemeMessageBox.success(self, "Title", "Done!",  lang=self.lang)

        # Confirm (Yes / No)
        if LightThemeMessageBox.confirm(self, "Title", "Sure?", lang=self.lang):
            ...

        # Custom buttons  ← buttons must be canonical English keys
        reply = LightThemeMessageBox.custom(
            self, "Title", "Question?",
            msg_type="success",
            buttons=["Yes", "No"],
            lang=self.lang,
        )
    """

    Yes    = True
    No     = False
    Ok     = True
    Cancel = False

    def __init__(
        self,
        parent=None,
        title: str = "Message",
        message: str = "",
        msg_type: str = "info",
        buttons: list[str] | None = None,
        lang: str = "en",
    ):
        super().__init__(parent)

        if buttons is None:
            buttons = ["OK"]

        self._lang = lang if lang in TRANSLATIONS else "en"

        self.result_value = False
        self.msg_type     = msg_type
        self._font_family  = FONT_FAMILY
        self._font_size_lg = FONT_SIZE_LG

        self.setWindowTitle(title)
        self.setModal(True)
        self.setMinimumWidth(450)
        self.setMaximumWidth(600)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)  # type: ignore

        self.setStyleSheet("""
            QDialog {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #F8FAFC, stop:1 #E2E8F0);
                border: 2px solid #E5E5E5;
                border-radius: 12px;
            }
        """)

        self.setup_ui(title, message, buttons)
        self.fade_in_animation()

    def _get_text(self, key: str) -> str:
        """Return the translated label for *key* in the current language."""
        return TRANSLATIONS.get(self._lang, TRANSLATIONS["en"]).get(key, key)

    def setup_ui(self, title: str, message: str, buttons: list[str]):
        font_label = QFont(self._font_family, self._font_size_lg)
        font_label.setWeight(QFont.Weight.Bold)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        header_frame = QFrame()
        header_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                border: 1px solid #E5E5E5;
            }
        """)

        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(20, 15, 20, 15)

        icon_label = QLabel()
        icon_label.setStyleSheet("border: none;")
        icon_label.setFixedSize(40, 40)
        pixmap = QPixmap(self.get_icon()).scaled(
            40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        icon_label.setPixmap(pixmap)

        title_label = QLabel(title)
        title_label.setStyleSheet("""
            border: none;
            font-size: 18px;
            font-weight: 600;
            color: #1E293B;
            margin-left: 10px;
        """)

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(30, 30)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #64748B;
                border: none;
                border-radius: 15px;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #F1F5F9;
                color: #1E293B;
            }
            QPushButton:pressed {
                background-color: #E2E8F0;
            }
        """)
        close_btn.clicked.connect(self.reject)

        header_layout.addWidget(icon_label)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(close_btn)

        content_frame = QFrame()
        content_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #E5E5E5;
            }
        """)

        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(20, 20, 20, 20)

        message_label = QLabel(message)
        message_label.setFont(font_label)
        message_label.setWordWrap(True)
        message_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                color: #374151;
                line-height: 1.5;
                padding: 10px;
                background-color: #F8FAFC;
                border-radius: 8px;
                border: 1px solid #E5E5E5;
            }
        """)
        message_label.setMinimumHeight(80)
        message_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        content_layout.addWidget(message_label)

        # ── Buttons ─────────────────────────────────────────────────────
        button_frame = QFrame()
        button_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
                border: 1px solid #E5E5E5;
            }
        """)

        button_layout = QHBoxLayout(button_frame)
        button_layout.setContentsMargins(20, 15, 20, 15)
        button_layout.setSpacing(10)
        button_layout.addStretch()

        for key in buttons:
            btn = self.create_button(key)
            button_layout.addWidget(btn)

        main_layout.addWidget(header_frame)
        main_layout.addWidget(content_frame)
        main_layout.addWidget(button_frame)

    def create_button(self, key: str) -> QPushButton:
        """
        Create a styled button.

        *key* is the canonical English identifier (e.g. ``"OK"``, ``"Yes"``).
        The visible label is translated according to ``self._lang``.
        """
        font_btn = QFont(self._font_family, FONT_SIZE_SM)
        font_btn.setWeight(QFont.Weight.Bold)

        label  = self._get_text(key)
        button = QPushButton(label)
        button.setFont(font_btn)
        button.setMinimumWidth(100)

        is_primary = key in _PRIMARY_KEYS

        if is_primary:
            button.setStyleSheet("""
                QPushButton {
                    background-color: #0B7EC8;
                    color: white;
                    border: none;
                    padding: 10px 24px;
                    border-radius: 8px;
                }
                QPushButton:hover  { background-color: #0968A3; }
                QPushButton:pressed { background-color: #085A91; }
            """)
        else:
            button.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: #0B7EC8;
                    border: 1px solid #0B7EC8;
                    padding: 10px 24px;
                    border-radius: 8px;
                }
                QPushButton:hover  { background-color: #F0F9FF; }
                QPushButton:pressed { background-color: #E0F2FE; }
            """)

        if key in _PRIMARY_KEYS:
            button.clicked.connect(lambda: self.accept_with_result(True))
        elif key in _NEGATIVE_KEYS:
            button.clicked.connect(lambda: self.accept_with_result(False))
        else:
            button.clicked.connect(self.accept)

        return button

    def get_icon(self) -> str:
        icons = {
            "info":     ":/message_box/information.png",
            "question": ":/message_box/question-mark.png",
            "warning":  ":/message_box/warning.png",
            "error":    ":/message_box/error.png",
            "success":  ":/message_box/check.png",
        }
        return icons.get(self.msg_type, ":/message_box/information.png")

    def get_color(self) -> str:
        colors = {
            "info":     "#0B7EC8",
            "question": "#F59E0B",
            "warning":  "#F59E0B",
            "error":    "#EF4444",
            "success":  "#10B981",
        }
        return colors.get(self.msg_type, "#0B7EC8")

    def accept_with_result(self, result: bool):
        self.result_value = result
        self.accept()

    def fade_in_animation(self):
        self.setWindowOpacity(0)
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(200)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()

    @staticmethod
    def information(parent, title: str, message: str, lang: str = "en") -> bool:
        dialog = LightThemeMessageBox(parent, title, message, "info", ["OK"], lang)
        dialog.exec_()
        return True

    @staticmethod
    def question(parent, title: str, message: str, lang: str = "en") -> bool:
        dialog = LightThemeMessageBox(parent, title, message, "question", ["Yes", "No"], lang)
        dialog.exec_()
        return dialog.result_value

    @staticmethod
    def warning(parent, title: str, message: str, lang: str = "en") -> bool:
        dialog = LightThemeMessageBox(parent, title, message, "warning", ["OK"], lang)
        dialog.exec_()
        return True

    @staticmethod
    def error(parent, title: str, message: str, lang: str = "en") -> bool:
        dialog = LightThemeMessageBox(parent, title, message, "error", ["OK"], lang)
        dialog.exec_()
        return True

    @staticmethod
    def success(parent, title: str, message: str, lang: str = "en") -> bool:
        dialog = LightThemeMessageBox(parent, title, message, "success", ["OK"], lang)
        dialog.exec_()
        return True

    @staticmethod
    def confirm(parent, title: str, message: str, lang: str = "en") -> bool:
        dialog = LightThemeMessageBox(parent, title, message, "question", ["Yes", "No"], lang)
        dialog.exec_()
        return dialog.result_value

    @staticmethod
    def custom(
        parent,
        title: str,
        message: str,
        msg_type: str = "info",
        buttons: list[str] | None = None,
        lang: str = "en",
    ) -> bool:
        if buttons is None:
            buttons = ["OK"]
        dialog = LightThemeMessageBox(parent, title, message, msg_type, buttons, lang)
        dialog.exec_()
        return dialog.result_value