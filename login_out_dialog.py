"""
Modern Login Dialog Module
===========================
Dialog hiện đại để đăng nhập với username và password.

Usage:
    from modern_login_dialog import ModernLoginDialog
    
    dialog = ModernLoginDialog(parent)
    if dialog.exec_():
        data = dialog.get_data()
        print(data)  # {'username': '...', 'password': '...'}
"""

from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QLineEdit, QCheckBox, QComboBox)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QFont, QPixmap
from icons import *

class ModernLoginDialog(QDialog):
    """
    Dialog hiện đại để đăng nhập.
    
    Có 2 trường input:
    - Username (text)
    - Password (password)
    """
    
    def __init__(self, parent=None, title="Login"):
        super().__init__(parent)
        
        # Variables for dragging
        self.dragging = False
        self.drag_position = None
        
        # Setup dialog
        self.setWindowTitle(title)
        self.setModal(True)
        self.setFixedWidth(450)
        self.setFixedHeight(600)
        
        # Remove default window frame
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        
        # Apply modern styling
        self.setStyleSheet("""
            QDialog {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #F8FAFC, stop:1 #E2E8F0);
                border: 2px solid #0B7EC8;
                border-radius: 12px;
            }
        """)
        
        self.setup_ui(title)
        
        # Animation
        self.fade_in_animation()
        
    def setup_ui(self, title):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Determine dialog type
        is_logout = title.lower() == "logout"
        
        # Header
        header_frame = QFrame()
        header_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
        """)
        
        # Enable dragging on header
        header_frame.mousePressEvent = self.header_mouse_press
        header_frame.mouseMoveEvent = self.header_mouse_move
        header_frame.mouseReleaseEvent = self.header_mouse_release
        header_frame.setCursor(Qt.SizeAllCursor)
        
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(20, 15, 20, 15)
        
        icon_label = QLabel()
        pixmap = QPixmap(":/newPrefix/Logo_Cty_2.png")
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon_label.setPixmap(scaled_pixmap)
        else:
            # Different emoji based on dialog type
            icon_label.setText("🔓" if is_logout else "🔐")
            icon_label.setStyleSheet("font-size: 28px;")
        
        title_label = QLabel("Logout" if is_logout else "Login")
        title_label.setStyleSheet("""
            font-size: 18px;
            font-weight: 600;
            color: #1E293B;
            margin-left: 10px;
            border: none;
        """)
        
        # Close button
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
        
        # Content area
        content_frame = QFrame()
        content_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: none;
            }
        """)
        
        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(40, 30, 40, 20)
        content_layout.setSpacing(20)
        
        if is_logout:
            # LOGOUT UI
            self.setup_logout_ui(content_layout)
        else:
            # LOGIN UI
            # self.setup_login_ui(content_layout)
            self.setup_ask_password_ui(content_layout)
        
        # Button area
        button_frame = QFrame()
        button_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
                border-top: 1px solid #E5E5E5;
            }
        """)
        
        button_layout = QVBoxLayout(button_frame)
        button_layout.setContentsMargins(40, 20, 40, 20)
        button_layout.setSpacing(10)
        
        if is_logout:
            self.setup_logout_buttons(button_layout)
        else:
            self.setup_login_buttons(button_layout)
        
        # Assemble dialog
        main_layout.addWidget(header_frame)
        main_layout.addWidget(content_frame, 1)
        main_layout.addWidget(button_frame)

    def setup_login_ui(self, content_layout):
        """Setup UI for Login dialog"""
        # Welcome text
        welcome_label = QLabel("Packing System")
        welcome_label.setStyleSheet("""
            font-size: 24px;
            font-weight: 700;
            color: #1E293B;
            border: none;
        """)
        welcome_label.setAlignment(Qt.AlignCenter)
        
        subtitle_label = QLabel("Please enter your credentials to continue")
        subtitle_label.setStyleSheet("""
            font-size: 13px;
            color: #64748B;
            border: none;
            margin-bottom: 5px;
        """)
        subtitle_label.setAlignment(Qt.AlignCenter)
        
        content_layout.addWidget(welcome_label)
        content_layout.addWidget(subtitle_label)
        content_layout.addSpacing(10)
        
        self.inputs = {}
        
        username_group = self.create_username_input_group(
            "Username",
            "username",
            "Enter your username",
            icon="👤",
            dropdown_options=["user", "staff", "admin"]
        )
        content_layout.addWidget(username_group)
        
        password_group = self.create_input_group(
            "Password",
            "password",
            "Enter your password",
            icon="🔒",
            is_password=True
        )
        content_layout.addWidget(password_group)
        
        self.validation_label = QLabel("ℹ️ Fill in all fields")
        self.validation_label.setStyleSheet("""
            font-size: 16px;
            color: #64748B;
            font-style: italic;
            border: none;
        """)
        self.validation_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(self.validation_label)

    def setup_ask_password_ui(self, content_layout):
        """Setup UI for Login dialog"""
        # Welcome text
        welcome_label = QLabel("Data Access")
        welcome_label.setStyleSheet("""
            font-size: 24px;
            font-weight: 700;
            color: #1E293B;
            border: none;
        """)
        welcome_label.setAlignment(Qt.AlignCenter)
        
        subtitle_label = QLabel("Enter password to continue")
        subtitle_label.setStyleSheet("""
            font-size: 13px;
            color: #64748B;
            border: none;
            margin-bottom: 5px;
        """)
        subtitle_label.setAlignment(Qt.AlignCenter)
        
        content_layout.addWidget(welcome_label)
        content_layout.addWidget(subtitle_label)
        content_layout.addSpacing(10)
        
        self.inputs = {}
        
        # username_group = self.create_username_input_group(
        #     "Username",
        #     "username",
        #     "Enter your username",
        #     icon="👤",
        #     dropdown_options=["user", "staff", "admin"]
        # )
        # content_layout.addWidget(username_group)
        
        password_group = self.create_input_group(
            "Password",
            "password",
            "Enter your password",
            icon="🔒",
            is_password=True
        )
        content_layout.addWidget(password_group)
        
        self.validation_label = QLabel("ℹ️ Fill in all fields")
        self.validation_label.setStyleSheet("""
            font-size: 16px;
            color: #64748B;
            font-style: italic;
            border: none;
        """)
        self.validation_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(self.validation_label)

    def setup_logout_ui(self, content_layout):
        """Setup UI for Logout dialog"""
        # Icon
        icon_label = QLabel("👋")
        icon_label.setStyleSheet("font-size: 64px;")
        icon_label.setAlignment(Qt.AlignCenter)
        
        # Main message
        message_label = QLabel("Are you sure you want to logout?")
        message_label.setStyleSheet("""
            font-size: 20px;
            font-weight: 700;
            color: #1E293B;
            border: none;
        """)
        message_label.setAlignment(Qt.AlignCenter)
        
        # Subtitle
        subtitle_label = QLabel("You will need to login again to access the system")
        subtitle_label.setStyleSheet("""
            font-size: 15px;
            color: #64748B;
            border: none;
        """)
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setWordWrap(True)
        
        content_layout.addStretch()
        content_layout.addWidget(icon_label)
        content_layout.addSpacing(20)
        content_layout.addWidget(message_label)
        content_layout.addSpacing(10)
        content_layout.addWidget(subtitle_label)
        content_layout.addStretch()

    def setup_login_buttons(self, button_layout):
        """Setup buttons for Login dialog"""
        # Login button
        self.login_btn = QPushButton("🔓 Login")
        self.login_btn.setMinimumHeight(45)
        self.login_btn.setStyleSheet("""
            QPushButton {
                background-color: #0B7EC8;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 8px;
                font-size: 15px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #0968A3;
            }
            QPushButton:pressed {
                background-color: #085A91;
            }
            QPushButton:disabled {
                background-color: #94A3B8;
                color: #CBD5E1;
            }
        """)
        self.login_btn.clicked.connect(self.validate_and_accept)
        self.login_btn.setEnabled(False)
        
        # Cancel button
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setMinimumHeight(40)
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #64748B;
                border: 1px solid #E5E5E5;
                padding: 10px 24px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #F8FAFC;
                border: 1px solid #CBD5E1;
            }
            QPushButton:pressed {
                background-color: #F1F5F9;
            }
        """)
        cancel_btn.clicked.connect(self.reject)
        cancel_btn.setAutoDefault(False)
        cancel_btn.setDefault(False)
        
        button_layout.addWidget(self.login_btn)
        button_layout.addWidget(cancel_btn)

        self.login_btn.setDefault(True)
        self.login_btn.setAutoDefault(True)

    def setup_logout_buttons(self, button_layout):
        """Setup buttons for Logout dialog"""
        # Logout button
        logout_btn = QPushButton("🚪 Logout")
        logout_btn.setMinimumHeight(45)
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #EF4444;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 8px;
                font-size: 15px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #DC2626;
            }
            QPushButton:pressed {
                background-color: #B91C1C;
            }
        """)
        logout_btn.clicked.connect(self.accept)
        
        # Cancel button
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setMinimumHeight(40)
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #64748B;
                border: 1px solid #E5E5E5;
                padding: 10px 24px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #F8FAFC;
                border: 1px solid #CBD5E1;
            }
            QPushButton:pressed {
                background-color: #F1F5F9;
            }
        """)
        cancel_btn.clicked.connect(self.reject)
        
        button_layout.addWidget(logout_btn)
        button_layout.addWidget(cancel_btn)

    def create_input_group(self, label_text, field_name, placeholder, icon="", is_password=False):
        """Create a styled input group"""
        group = QFrame()
        group.setStyleSheet("""
            QFrame {
                background-color: transparent;
                border: none;
            }
        """)
        
        layout = QVBoxLayout(group)
        layout.setSpacing(8)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Label with icon
        label_layout = QHBoxLayout()
        
        if icon:
            icon_label = QLabel(icon)
            icon_label.setStyleSheet("font-size: 16px;")
            label_layout.addWidget(icon_label)
        
        label = QLabel(label_text)
        label.setStyleSheet("""
            font-size: 13px;
            font-weight: 600;
            color: #374151;
            border: none;
        """)
        label_layout.addWidget(label)
        label_layout.addStretch()
        
        # Input field
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        input_field.setMinimumHeight(45)
        
        if is_password:
            input_field.setEchoMode(QLineEdit.Password)
        
        input_field.setStyleSheet("""
            QLineEdit {
                border: 2px solid #E5E5E5;
                border-radius: 8px;
                padding: 12px 16px;
                font-size: 16px;
                background-color: #F8FAFC;
            }
            QLineEdit:focus {
                border: 2px solid #0B7EC8;
                background-color: white;
            }
            QLineEdit:hover {
                border: 2px solid #CBD5E1;
                background-color: white;
            }
        """)
        
        # Connect change event for validation
        input_field.textChanged.connect(self.check_validation)
        input_field.returnPressed.connect(self.validate_and_accept)
        # Store reference
        self.inputs[field_name] = input_field
        
        layout.addLayout(label_layout)
        layout.addWidget(input_field)
        
        return group
    
    def create_username_input_group(self, label_text, field_name, placeholder, icon="", dropdown_options=None):
        """Create a styled input group"""
        group = QFrame()
        group.setStyleSheet("""
            QFrame {
                background-color: transparent;
                border: none;
            }
        """)
        
        layout = QVBoxLayout(group)
        layout.setSpacing(8)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Label with icon
        label_layout = QHBoxLayout()
        
        if icon:
            icon_label = QLabel(icon)
            icon_label.setStyleSheet("font-size: 16px;")
            label_layout.addWidget(icon_label)
        
        label = QLabel(label_text)
        label.setStyleSheet("""
            font-size: 13px;
            font-weight: 600;
            color: #374151;
            border: none;
        """)
        label_layout.addWidget(label)
        label_layout.addStretch()
        
        # Editable ComboBox
        combo_box = QComboBox()
        combo_box.setEditable(True)
        combo_box.setMinimumHeight(45)
        
        # Add items: empty first, then user, staff, admin
        combo_box.addItem("")  # Empty option for manual input
        if dropdown_options:
            combo_box.addItems(dropdown_options)
        
        # Set placeholder text
        combo_box.lineEdit().setPlaceholderText(placeholder)
        
        combo_box.setStyleSheet("""
            QComboBox {
                border: 2px solid #E5E5E5;
                border-radius: 8px;
                padding: 12px 16px;
                padding-right: 35px;
                font-size: 16px;
                background-color: #F8FAFC;
            }
            QComboBox:focus {
                border: 2px solid #0B7EC8;
                background-color: white;
            }
            QComboBox:hover {
                border: 2px solid #CBD5E1;
                background-color: white;
            }
            QComboBox::drop-down {
                border: none;
                width: 30px;
                subcontrol-origin: padding;
                subcontrol-position: center right;
                padding-right: 5px;
            }

            QComboBox QAbstractItemView {
                border: 2px solid #0B7EC8;
                border-radius: 8px;
                background-color: white;
                selection-background-color: #0B7EC8;
                selection-color: white;
                padding: 5px;
                outline: none;
            }
            QComboBox QAbstractItemView::item {
                min-height: 45px;
                height: 45px;
                padding-left: 10px;
                padding-top: 5px;
                padding-bottom: 5px;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #E0F2FE;
                color: #0B7EC8;
            }
        """)
        
        # Connect change event for validation
        combo_box.currentTextChanged.connect(self.check_validation)
        combo_box.lineEdit().returnPressed.connect(self.validate_and_accept)
        # combo_box.view().setMinimumHeight(200)
        # Store reference
        self.inputs[field_name] = combo_box
        
        layout.addLayout(label_layout)
        layout.addWidget(combo_box)
        
        return group

    def check_validation(self):
        """Check if all fields are valid"""
        username = self.inputs['username'].currentText().strip()
        password = self.inputs['password'].text().strip()
        
        if username and password:
            self.validation_label.setText("✅ Ready to login")
            self.validation_label.setStyleSheet("""
                font-size: 14px;
                color: #10B981;
                font-weight: 500;
                border: none;
            """)
            self.login_btn.setEnabled(True)
        else:
            missing = []
            if not username:
                missing.append("username")
            if not password:
                missing.append("password")
            
            self.validation_label.setText(f"⚠️ Please enter {' and '.join(missing)}")
            self.validation_label.setStyleSheet("""
                font-size: 14px;
                color: #F59E0B;
                font-style: italic;
                border: none;
            """)
            self.login_btn.setEnabled(False)

    def validate_and_accept(self):
        """Validate data before accepting"""
        username = self.inputs['username'].currentText().strip()
        password = self.inputs['password'].text().strip()
        
        if not username or not password:
            self.validation_label.setText("❌ All fields are required!")
            self.validation_label.setStyleSheet("""
                font-size: 14px;
                color: #EF4444;
                font-weight: 600;
                border: none;
            """)
            if not username:
                self.inputs['username'].setFocus()
            else:
                self.inputs['password'].setFocus()
            return
        
        self.accept()


    def check_pass_only(self):
        """Check if all fields are valid"""
        password = self.inputs['password'].text().strip()
        
        if password:
            self.validation_label.setText("✅ Ready to login")
            self.validation_label.setStyleSheet("""
                font-size: 14px;
                color: #10B981;
                font-weight: 500;
                border: none;
            """)
            self.login_btn.setEnabled(True)
        else:
            missing = []
            if not password:
                missing.append("password")
            
            self.validation_label.setText(f"⚠️ Please enter {' and '.join(missing)}")
            self.validation_label.setStyleSheet("""
                font-size: 14px;
                color: #F59E0B;
                font-style: italic;
                border: none;
            """)
            self.login_btn.setEnabled(False)

    def validate_and_accept_pass_only(self):
        """Validate data before accepting"""
        password = self.inputs['password'].text().strip()
        
        if not password:
            self.validation_label.setText("❌ All fields are required!")
            self.validation_label.setStyleSheet("""
                font-size: 14px;
                color: #EF4444;
                font-weight: 600;
                border: none;
            """)
            if not password:
                self.inputs['password'].setFocus()
            return
        
        self.accept()

    def get_data(self):
        """Get all input data as dictionary"""
        return {
            'username': self.inputs['username'].currentText().strip(),
            'password': self.inputs['password'].text().strip()
        }

    def get_password(self):
        """Get all input data as dictionary"""
        return {
            'password': self.inputs['password'].text().strip()
        }

    def log_out(self):
        return True

    def fade_in_animation(self):
        """Fade in animation when dialog appears"""
        self.setWindowOpacity(0)
        
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(200)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()

    def header_mouse_press(self, event):
        """Handle mouse press on header for dragging"""
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def header_mouse_move(self, event):
        """Handle mouse move for dragging"""
        if self.dragging and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def header_mouse_release(self, event):
        """Handle mouse release to stop dragging"""
        if event.button() == Qt.LeftButton:
            self.dragging = False
            event.accept()
    
    @staticmethod
    def get_login_data(parent=None, title = "login"):
        """
        Static method để hiển thị dialog và lấy dữ liệu
        
        Usage:
            data = ModernLoginDialog.get_login_data(self)
            if data:
                print(f"Username: {data['username']}")
                print(f"Password: {data['password']}")
                print(f"Remember: {data['remember']}")
        """
        dialog = ModernLoginDialog(parent, title)
        result = dialog.exec_()
        
        if result == QDialog.Accepted:
            return dialog.get_data()
        return None
    
    @staticmethod
    def get_asking_data(parent=None, title = "asking"):
        """
        Static method để hiển thị dialog và lấy dữ liệu
        
        Usage:
            data = ModernLoginDialog.get_login_data(self)
            if data:
                print(f"Username: {data['username']}")
                print(f"Password: {data['password']}")
                print(f"Remember: {data['remember']}")
        """
        dialog = ModernLoginDialog(parent, title)
        result = dialog.exec_()
        
        if result == QDialog.Accepted:
            return dialog.get_data()
        return None

    @staticmethod
    def get_logout_data(parent=None, title = "logout"):
        """
        Static method để hiển thị dialog và lấy dữ liệu
        
        Usage:
            data = ModernLoginDialog.get_logout_data(self)
            if data:
                log out
        """
        dialog = ModernLoginDialog(parent, title)
        result = dialog.exec_()
        
        if result == QDialog.Accepted:
            return dialog.log_out()
        return None
