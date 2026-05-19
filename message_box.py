import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QFrame, QGridLayout,
                             QScrollArea, QTabWidget, QListWidget, QTextEdit,
                             QLineEdit, QComboBox, QGroupBox, QProgressBar, QMessageBox,
                             QSpinBox, QCheckBox, QSlider, QFormLayout, QSplitter, QDialog)
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QRect, QPropertyAnimation
from PySide6.QtGui import QFont, QPixmap, QPainter, QColor, QLinearGradient, QPalette

FONT_FAMILY  = "Segoe UI"
FONT_SIZE_LG = 16
FONT_SIZE_MD = 16
FONT_SIZE_SM = 13

class LightThemeMessageBox(QDialog):
    """
    Custom message box with modern design matching the main window style.
    
    Usage:
        # Information
        LightThemeMessageBox.information(self, "Title", "Message content")
        
        # Question (returns True/False)
        if LightThemeMessageBox.question(self, "Title", "Question?"):
            # User clicked Yes
            
        # Warning
        LightThemeMessageBox.warning(self, "Title", "Warning message")
        
        # Error
        LightThemeMessageBox.error(self, "Title", "Error message")
        
        # Success
        LightThemeMessageBox.success(self, "Title", "Success message")
    """
    
    Yes = True
    No = False
    Ok = True
    Cancel = False
    
    def __init__(self, parent=None, title="Message", message="", msg_type="info", buttons=["OK"]):
        super().__init__(parent)
        self.result_value = False
        self.msg_type = msg_type
        self._font_family  = FONT_FAMILY
        self._font_size_lg = FONT_SIZE_LG
        self.setWindowTitle(title)
        self.setModal(True)
        self.setMinimumWidth(450)
        self.setMaximumWidth(600)
        
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        
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
    
    def setup_ui(self, title, message, buttons):

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
        
        icon_label = QLabel(self.get_icon())
        icon_label.setFont(font_label)
        icon_label.setStyleSheet(f"""
            font-size: 28px;
            border: none;
            color: {self.get_color()};
        """)
        
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
        
        for button_text in buttons:
            btn = self.create_button(button_text)
            button_layout.addWidget(btn)
        
        main_layout.addWidget(header_frame)
        main_layout.addWidget(content_frame)
        main_layout.addWidget(button_frame)
    
    def create_button(self, text):
        """Create styled button"""
        font_btn = QFont(self._font_family, FONT_SIZE_SM)
        font_btn.setWeight(QFont.Weight.Bold)

        button = QPushButton(text)
        button.setFont(font_btn)
        button.setMinimumWidth(100)
        
        if text in ["OK", "Yes", "Save", "Apply"]:
            button_type = "primary"
        elif text in ["No", "Cancel", "Close"]:
            button_type = "secondary"
        else:
            button_type = "secondary"
        
        if button_type == "primary":
            button.setStyleSheet("""
                QPushButton {
                    background-color: #0B7EC8;
                    color: white;
                    border: none;
                    padding: 10px 24px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #0968A3;
                }
                QPushButton:pressed {
                    background-color: #085A91;
                }
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
                QPushButton:hover {
                    background-color: #F0F9FF;
                }
                QPushButton:pressed {
                    background-color: #E0F2FE;
                }
            """)
        
        if text in ["Yes", "OK", "Save", "Apply"]:
            button.clicked.connect(lambda: self.accept_with_result(True))
        elif text in ["No", "Cancel", "Close"]:
            button.clicked.connect(lambda: self.accept_with_result(False))
        else:
            button.clicked.connect(self.accept)
        
        return button
    
    def get_icon(self):
        """Get icon based on message type"""
        icons = {
            "info": "ℹ️",
            "question": "❓",
            "warning": "⚠️",
            "error": "❌",
            "success": "✅"
        }
        return icons.get(self.msg_type, "ℹ️")
    
    def get_color(self):
        """Get color based on message type"""
        colors = {
            "info": "#0B7EC8",
            "question": "#F59E0B",
            "warning": "#F59E0B",
            "error": "#EF4444",
            "success": "#10B981"
        }
        return colors.get(self.msg_type, "#0B7EC8")
    
    def accept_with_result(self, result):
        """Accept dialog with specific result"""
        self.result_value = result
        self.accept()
    
    def fade_in_animation(self):
        """Fade in animation when dialog appears"""
        self.setWindowOpacity(0)
        
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(200)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()
    
    # Static methods for convenience
    @staticmethod
    def information(parent, title, message):
        """Show information message"""
        dialog = LightThemeMessageBox(parent, title, message, "info", ["OK"])
        dialog.exec_()
        return True
    
    @staticmethod
    def question(parent, title, message):
        """Show question dialog and return True/False"""
        dialog = LightThemeMessageBox(parent, title, message, "question", ["Yes", "No"])
        dialog.exec_()
        return dialog.result_value
    
    @staticmethod
    def warning(parent, title, message):
        """Show warning message"""
        dialog = LightThemeMessageBox(parent, title, message, "warning", ["OK"])
        dialog.exec_()
        return True
    
    @staticmethod
    def error(parent, title, message):
        """Show error message"""
        dialog = LightThemeMessageBox(parent, title, message, "error", ["OK"])
        dialog.exec_()
        return True
    
    @staticmethod
    def success(parent, title, message):
        """Show success message"""
        dialog = LightThemeMessageBox(parent, title, message, "success", ["OK"])
        dialog.exec_()
        return True
    
    @staticmethod
    def confirm(parent, title, message):
        """Show confirmation dialog with Yes/No buttons"""
        dialog = LightThemeMessageBox(parent, title, message, "question", ["Yes", "No"])
        dialog.exec_()
        return dialog.result_value
    
    @staticmethod
    def custom(parent, title, message, msg_type="info", buttons=None):
        """Show custom dialog with specified buttons"""
        if buttons is None:
            buttons = ["OK"]
        dialog = LightThemeMessageBox(parent, title, message, msg_type, buttons)
        dialog.exec_()
        return dialog.result_value
