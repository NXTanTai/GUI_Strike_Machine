"""
Modern Login Dialog Module
===========================
Dialog hiện đại để đăng nhập với password only.

Usage:
    from modern_login_dialog import ModernLoginDialog
    
    # Password-only dialog
    data = ModernLoginDialog.get_asking_data(parent)
    if data:
        print(data)  # {'password': '...'}

    # Full login (username + password)
    data = ModernLoginDialog.get_login_data(parent)
    if data:
        print(data)  # {'username': '...', 'password': '...'}

    # Logout confirmation
    result = ModernLoginDialog.get_logout_data(parent)
    if result:
        # proceed with logout
        pass
"""

from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel,QDoubleSpinBox,
                               QPushButton, QFrame, QLineEdit, QComboBox, QSpinBox)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPixmap
from icons import *

PASSWORD = "tl@12345"

class ModernLoginDialog(QDialog):
    """
    Dialog hiện đại để đăng nhập.

    Modes (controlled by `title` parameter):
    - "login"   → username (ComboBox) + password
    - "logout"  → confirmation screen
    - anything else → password only ("Data Access")
    """

    def __init__(self, parent=None, title="Login"):
        super().__init__(parent)

        self.dragging = False
        self.drag_position = None

        self.setWindowTitle(title)
        self.setModal(True)
        self.setFixedWidth(450)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)

        self.setStyleSheet("""
            QDialog {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #F8FAFC, stop:1 #E2E8F0);
                border: 2px solid #0B7EC8;
                border-radius: 12px;
            }
        """)

        self._mode = title.lower()  # "login" | "logout" | anything else → password-only
        self.inputs = {}

        self.setup_ui(title)
        self.fade_in_animation()

    # ------------------------------------------------------------------ #
    #  UI assembly                                                         #
    # ------------------------------------------------------------------ #

    def setup_ui(self, title):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        is_logout = self._mode == "logout"

        # ── Header ──────────────────────────────────────────────────────
        header_frame = QFrame()
        header_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
        """)
        header_frame.mousePressEvent   = self.header_mouse_press
        header_frame.mouseMoveEvent    = self.header_mouse_move
        header_frame.mouseReleaseEvent = self.header_mouse_release
        header_frame.setCursor(Qt.SizeAllCursor)

        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(20, 15, 20, 15)

        icon_label = QLabel()
        pixmap = QPixmap(":/newPrefix/Logo_Cty_2.png")
        if not pixmap.isNull():
            scaled = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon_label.setPixmap(scaled)
        else:
            icon_label.setText("🔓" if is_logout else "🔐")
            icon_label.setStyleSheet("font-size: 28px;")

        title_label = QLabel("Logout" if is_logout else title.title())
        title_label.setStyleSheet("""
            font-size: 18px;
            font-weight: 600;
            color: #1E293B;
            margin-left: 10px;
            border: none;
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
            QPushButton:hover { background-color: #F1F5F9; color: #1E293B; }
            QPushButton:pressed { background-color: #E2E8F0; }
        """)
        close_btn.clicked.connect(self.reject)

        header_layout.addWidget(icon_label)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(close_btn)

        # ── Content ─────────────────────────────────────────────────────
        content_frame = QFrame()
        content_frame.setStyleSheet("QFrame { background-color: white; border: none; }")

        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(40, 30, 40, 20)
        content_layout.setSpacing(20)

        if is_logout:
            self.setFixedHeight(420)
            self._setup_logout_ui(content_layout)
        elif self._mode == "login":
            self.setFixedHeight(600)
            self._setup_login_ui(content_layout)
        else:
            self.setFixedHeight(480)
            self._setup_password_only_ui(content_layout)

        # ── Buttons ─────────────────────────────────────────────────────
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
            self._setup_logout_buttons(button_layout)
        else:
            self._setup_login_buttons(button_layout)

        main_layout.addWidget(header_frame)
        main_layout.addWidget(content_frame, 1)
        main_layout.addWidget(button_frame)

    # ------------------------------------------------------------------ #
    #  Content panels                                                      #
    # ------------------------------------------------------------------ #

    def _setup_login_ui(self, layout):
        """Username (ComboBox) + Password."""
        self._add_header_labels(layout, "Packing System", "Please enter your credentials to continue")
        layout.addSpacing(10)

        layout.addWidget(self._create_username_group(
            "Username", "username", "Enter your username",
            icon="👤", dropdown_options=["user", "staff", "admin"]
        ))
        layout.addWidget(self._create_password_group())
        layout.addWidget(self._make_validation_label())

    def _setup_password_only_ui(self, layout):
        """Password only – no username field."""
        self._add_header_labels(layout, "Data Access", "Enter password to continue")
        layout.addSpacing(10)

        layout.addWidget(self._create_password_group())
        layout.addWidget(self._make_validation_label())

    def _setup_logout_ui(self, layout):
        icon_label = QLabel("👋")
        icon_label.setStyleSheet("font-size: 64px;")
        icon_label.setAlignment(Qt.AlignCenter)

        msg = QLabel("Are you sure you want to logout?")
        msg.setStyleSheet("font-size: 20px; font-weight: 700; color: #1E293B; border: none;")
        msg.setAlignment(Qt.AlignCenter)

        sub = QLabel("You will need to login again to access the system")
        sub.setStyleSheet("font-size: 15px; color: #64748B; border: none;")
        sub.setAlignment(Qt.AlignCenter)
        sub.setWordWrap(True)

        layout.addStretch()
        layout.addWidget(icon_label)
        layout.addSpacing(20)
        layout.addWidget(msg)
        layout.addSpacing(10)
        layout.addWidget(sub)
        layout.addStretch()

    # ------------------------------------------------------------------ #
    #  Button panels                                                       #
    # ------------------------------------------------------------------ #

    def _setup_login_buttons(self, layout):
        self.login_btn = QPushButton("🔓 Login")
        self.login_btn.setMinimumHeight(45)
        self.login_btn.setStyleSheet("""
            QPushButton {
                background-color: #0B7EC8; color: white; border: none;
                padding: 12px 24px; border-radius: 8px;
                font-size: 15px; font-weight: 600;
            }
            QPushButton:hover   { background-color: #0968A3; }
            QPushButton:pressed { background-color: #085A91; }
            QPushButton:disabled { background-color: #94A3B8; color: #CBD5E1; }
        """)
        self.login_btn.clicked.connect(self._validate_and_accept)
        self.login_btn.setEnabled(False)
        self.login_btn.setDefault(True)
        self.login_btn.setAutoDefault(True)

        cancel_btn = self._make_cancel_button()

        layout.addWidget(self.login_btn)
        layout.addWidget(cancel_btn)

    def _setup_logout_buttons(self, layout):
        logout_btn = QPushButton("🚪 Logout")
        logout_btn.setMinimumHeight(45)
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #EF4444; color: white; border: none;
                padding: 12px 24px; border-radius: 8px;
                font-size: 15px; font-weight: 600;
            }
            QPushButton:hover   { background-color: #DC2626; }
            QPushButton:pressed { background-color: #B91C1C; }
        """)
        logout_btn.clicked.connect(self.accept)

        layout.addWidget(logout_btn)
        layout.addWidget(self._make_cancel_button())

    # ------------------------------------------------------------------ #
    #  Widget helpers                                                      #
    # ------------------------------------------------------------------ #

    def _add_header_labels(self, layout, title_text, subtitle_text):
        title = QLabel(title_text)
        title.setStyleSheet("font-size: 24px; font-weight: 700; color: #1E293B; border: none;")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel(subtitle_text)
        subtitle.setStyleSheet("font-size: 13px; color: #64748B; border: none; margin-bottom: 5px;")
        subtitle.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(subtitle)

    def _make_validation_label(self):
        self.validation_label = QLabel("ℹ️ Fill in all fields")
        self.validation_label.setStyleSheet("""
            font-size: 16px; color: #64748B;
            font-style: italic; border: none;
        """)
        self.validation_label.setAlignment(Qt.AlignCenter)
        return self.validation_label

    def _make_cancel_button(self):
        btn = QPushButton("Cancel")
        btn.setMinimumHeight(40)
        btn.setStyleSheet("""
            QPushButton {
                background-color: white; color: #64748B;
                border: 1px solid #E5E5E5; padding: 10px 24px;
                border-radius: 8px; font-size: 14px; font-weight: 500;
            }
            QPushButton:hover   { background-color: #F8FAFC; border: 1px solid #CBD5E1; }
            QPushButton:pressed { background-color: #F1F5F9; }
        """)
        btn.clicked.connect(self.reject)
        btn.setAutoDefault(False)
        btn.setDefault(False)
        return btn

    # ── Input group: password ──────────────────────────────────────────

    def _create_password_group(self):
        group = QFrame()
        group.setStyleSheet("QFrame { background-color: transparent; border: none; }")
        layout = QVBoxLayout(group)
        layout.setSpacing(8)
        layout.setContentsMargins(0, 0, 0, 0)

        # Label row
        lbl_row = QHBoxLayout()
        lbl_row.addWidget(QLabel("🔒"))
        label = QLabel("Password")
        label.setStyleSheet("font-size: 13px; font-weight: 600; color: #374151; border: none;")
        lbl_row.addWidget(label)
        lbl_row.addStretch()

        # Input
        field = QLineEdit()
        field.setPlaceholderText("Enter your password")
        field.setMinimumHeight(45)
        field.setEchoMode(QLineEdit.Password)
        field.setStyleSheet("""
            QLineEdit {
                border: 2px solid #E5E5E5; border-radius: 8px;
                padding: 12px 16px; font-size: 16px; background-color: #F8FAFC;
            }
            QLineEdit:focus { border: 2px solid #0B7EC8; background-color: white; }
            QLineEdit:hover { border: 2px solid #CBD5E1; background-color: white; }
        """)
        field.textChanged.connect(self._check_validation)
        field.returnPressed.connect(self._validate_and_accept)
        self.inputs["password"] = field

        layout.addLayout(lbl_row)
        layout.addWidget(field)
        return group

    # ── Input group: username ComboBox ────────────────────────────────

    def _create_username_group(self, label_text, field_name, placeholder,
                                icon="", dropdown_options=None):
        group = QFrame()
        group.setStyleSheet("QFrame { background-color: transparent; border: none; }")
        layout = QVBoxLayout(group)
        layout.setSpacing(8)
        layout.setContentsMargins(0, 0, 0, 0)

        lbl_row = QHBoxLayout()
        if icon:
            lbl_row.addWidget(QLabel(icon))
        label = QLabel(label_text)
        label.setStyleSheet("font-size: 13px; font-weight: 600; color: #374151; border: none;")
        lbl_row.addWidget(label)
        lbl_row.addStretch()

        combo = QComboBox()
        combo.setEditable(True)
        combo.setMinimumHeight(45)
        combo.addItem("")
        if dropdown_options:
            combo.addItems(dropdown_options)
        combo.lineEdit().setPlaceholderText(placeholder)
        combo.setStyleSheet("""
            QComboBox {
                border: 2px solid #E5E5E5; border-radius: 8px;
                padding: 12px 16px; padding-right: 35px;
                font-size: 16px; background-color: #F8FAFC;
            }
            QComboBox:focus { border: 2px solid #0B7EC8; background-color: white; }
            QComboBox:hover { border: 2px solid #CBD5E1; background-color: white; }
            QComboBox::drop-down { border: none; width: 30px; }
            QComboBox QAbstractItemView {
                border: 2px solid #0B7EC8; border-radius: 8px;
                background-color: white;
                selection-background-color: #0B7EC8; selection-color: white;
                padding: 5px; outline: none;
            }
            QComboBox QAbstractItemView::item {
                min-height: 45px; padding-left: 10px;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #E0F2FE; color: #0B7EC8;
            }
        """)
        combo.currentTextChanged.connect(self._check_validation)
        combo.lineEdit().returnPressed.connect(self._validate_and_accept)
        self.inputs[field_name] = combo

        layout.addLayout(lbl_row)
        layout.addWidget(combo)
        return group

    # ------------------------------------------------------------------ #
    #  Validation                                                          #
    # ------------------------------------------------------------------ #

    def _check_validation(self):
        """Enable/disable login button based on required fields."""
        password = self.inputs["password"].text().strip()

        if self._mode == "login":
            username = self.inputs.get("username")
            username = username.currentText().strip() if username else ""
            ready = bool(username and password)
            missing = (["username"] if not username else []) + (["password"] if not password else [])
        else:
            ready = bool(password)
            missing = [] if password else ["password"]

        if ready:
            self.validation_label.setText("✅ Ready to login")
            self.validation_label.setStyleSheet(
                "font-size: 14px; color: #10B981; font-weight: 500; border: none;")
            self.login_btn.setEnabled(True)
        else:
            self.validation_label.setText(f"⚠️ Please enter {' and '.join(missing)}")
            self.validation_label.setStyleSheet(
                "font-size: 14px; color: #F59E0B; font-style: italic; border: none;")
            self.login_btn.setEnabled(False)

    def _validate_and_accept(self):
        """Final validation before closing the dialog."""
        password = self.inputs["password"].text().strip()

        if self._mode == "login":
            username_widget = self.inputs.get("username")
            username = username_widget.currentText().strip() if username_widget else ""
            if not username or not password:
                self.validation_label.setText("❌ All fields are required!")
                self.validation_label.setStyleSheet(
                    "font-size: 14px; color: #EF4444; font-weight: 600; border: none;")
                if not username:
                    self.inputs["username"].setFocus()
                else:
                    self.inputs["password"].setFocus()
                return
        else:
            if not password:
                self.validation_label.setText("❌ Password is required!")
                self.validation_label.setStyleSheet(
                    "font-size: 14px; color: #EF4444; font-weight: 600; border: none;")
                self.inputs["password"].setFocus()
                return

        self.accept()

    # ------------------------------------------------------------------ #
    #  Data getters                                                        #
    # ------------------------------------------------------------------ #

    def get_password(self) -> dict:
        """Return {'password': '...'}."""
        return {"password": self.inputs["password"].text().strip()}

    def get_data(self) -> dict:
        """Return {'username': '...', 'password': '...'} for full login mode."""
        result = {"password": self.inputs["password"].text().strip()}
        if "username" in self.inputs:
            result["username"] = self.inputs["username"].currentText().strip()
        return result

    @staticmethod
    def _log_out():
        return True

    # ------------------------------------------------------------------ #
    #  Animation & dragging                                                #
    # ------------------------------------------------------------------ #

    def fade_in_animation(self):
        self.setWindowOpacity(0)
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(200)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()

    def header_mouse_press(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def header_mouse_move(self, event):
        if self.dragging and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def header_mouse_release(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            event.accept()

    # ------------------------------------------------------------------ #
    #  Static factory methods                                              #
    # ------------------------------------------------------------------ #

    @staticmethod
    def get_login_data(parent=None, title="Login") -> dict | None:
        """
        Show full login dialog (username + password).
        Returns {'username': ..., 'password': ...} or None on cancel.
        """
        dialog = ModernLoginDialog(parent, title)
        if dialog.exec_() == QDialog.Accepted:
            return dialog.get_data()
        return None

    @staticmethod
    def get_asking_data(parent=None, title="Access") -> dict | None:
        """
        Show password-only dialog.
        Returns {'password': ...} or None on cancel.
        """
        dialog = ModernLoginDialog(parent, title)
        if dialog.exec_() == QDialog.Accepted:
            return dialog.get_password()
        return None

    @staticmethod
    def get_logout_data(parent=None, title="Logout") -> bool | None:
        """
        Show logout confirmation dialog.
        Returns True on confirm, None on cancel.
        """
        dialog = ModernLoginDialog(parent, title)
        if dialog.exec_() == QDialog.Accepted:
            return ModernLoginDialog._log_out()
        return None
    
class PasswordProtectedMixin:
    def init_protection(self, field_name: str, on_unlocked=None):
        self._field_name = field_name
        self._on_unlocked = on_unlocked
        self._locked = True
        self._apply_locked_state()
 
    def _apply_locked_state(self):
        if isinstance(self, QLineEdit):
            self.setReadOnly(True)
        elif isinstance(self, (QSpinBox, QDoubleSpinBox)):
            self.setReadOnly(True)
            self.setButtonSymbols(QSpinBox.NoButtons)
            self._install_spinbox_filter()
 
    def _install_spinbox_filter(self):
        """Dùng QTimer để đảm bảo lineEdit() đã sẵn sàng."""
        from PySide6.QtCore import QTimer
        def _do_install():
            internal = self.lineEdit()
            if internal:
                internal.installEventFilter(self)
        QTimer.singleShot(0, _do_install)
 
    def _apply_unlocked_state(self):
        if isinstance(self, QLineEdit):
            self.setReadOnly(False)
        elif isinstance(self, (QSpinBox, QDoubleSpinBox)):
            self.setReadOnly(False)
            internal = self.lineEdit()
            if internal:
                internal.removeEventFilter(self)
 
    def eventFilter(self, obj, event):
        """Bắt click trên internal line edit của SpinBox khi đang khoá."""
        from PySide6.QtCore import QEvent
        if self._locked and event.type() in (QEvent.MouseButtonPress, QEvent.MouseButtonDblClick):
            self._ask_password()
            return True
        return super().eventFilter(obj, event)
 
    def mousePressEvent(self, event):
        if self._locked and isinstance(self, QLineEdit):
            self._ask_password()
        else:
            super().mousePressEvent(event)
 
    def _ask_password(self):
        # Nếu có group và group đã unlock → mở thẳng, không hỏi lại
        group = getattr(self, "_group", None)
        if group and group.is_unlocked():
            self._locked = False
            self._apply_unlocked_state()
            return
 
        data = ModernLoginDialog.get_asking_data(
            parent=self.window(),
            title=f"Access – PLC Data"
        )
        if data is None:
            return
        if data.get("password", "") == PASSWORD:
            self._unlock()
        else:
            self._ask_password()
 
    def _unlock(self):
        group = getattr(self, "_group", None)
        if group:
            group.unlock_all()  # mở khoá toàn nhóm
        else:
            self._locked = False
            self._apply_unlocked_state()
        self.setFocus()
        if callable(self._on_unlocked):
            self._on_unlocked(self)
 
    def _lock(self):
        self._locked = True
        self._apply_locked_state()

# ──────────────────────────────────────────────
class ProtectionGroup:
    """
    Nhóm widget dùng chung password session.
    Hỏi password 1 lần → tất cả đều mở khoá.
    Chuyển trang → reset toàn bộ nhóm.
    """
    def __init__(self):
        self._widgets = []
        self._unlocked = False  # trạng thái chung của cả nhóm
 
    def add(self, widget):
        self._widgets.append(widget)
        widget._group = self
 
    def is_unlocked(self):
        return self._unlocked
 
    def unlock_all(self):
        self._unlocked = True
        for w in self._widgets:
            w._locked = False
            w._apply_unlocked_state()
 
    def lock_all(self):
        self._unlocked = False
        for w in self._widgets:
            w._locked = True
            w._apply_locked_state()
 
# ──────────────────────────────────────────────
#  3 widget classes
# ──────────────────────────────────────────────
class ProtectedLineEdit(PasswordProtectedMixin, QLineEdit):
    def __init__(self, field_name: str, on_unlocked=None, parent=None):
        super().__init__(parent)
        self.init_protection(field_name, on_unlocked)
 
 
class ProtectedSpinBox(PasswordProtectedMixin, QSpinBox):
    def __init__(self, field_name: str, on_unlocked=None, parent=None):
        super().__init__(parent)
        self.init_protection(field_name, on_unlocked)
 
 
class ProtectedDoubleSpinBox(PasswordProtectedMixin, QDoubleSpinBox):
    def __init__(self, field_name: str, on_unlocked=None, parent=None):
        super().__init__(parent)
        self.init_protection(field_name, on_unlocked)
 
 
# ──────────────────────────────────────────────
#  Hàm patch widget có sẵn từ Designer
# ──────────────────────────────────────────────
def protect_widget(widget, field_name: str = None, on_unlocked=None):
    if widget is None:
        import warnings
        warnings.warn(f"protect_widget: widget is None (field_name={field_name!r}), skipping.", stacklevel=2)
        return
    """
    Gán PasswordProtectedMixin vào widget có sẵn (từ Qt Designer).
    Hỗ trợ: QLineEdit, QSpinBox, QDoubleSpinBox.
 
    Ví dụ:
        protect_widget(self.ui.db_file_path_edit,   "DB File Path",  self.connect_db)
        protect_widget(self.ui.plc_ip_address_edit, "PLC IP",        self.connect_plc)
        protect_widget(self.ui.db_number_input,     "DB Number",     self.connect_db_number)
        protect_widget(self.ui.db_data_size_input,  "DB Data Size",  self.connect_db_size)
    """
    # Chèn Mixin vào __class__ của instance (hot-patch)
    original_class = widget.__class__
    # Tạo class mới kế thừa Mixin + class gốc, không copy method thủ công
    # để Pylance và MRO đều hoạt động đúng
    if not issubclass(original_class, PasswordProtectedMixin):
        new_class = type(
            f"Protected{original_class.__name__}",
            (PasswordProtectedMixin, original_class),
            {}          # để trống → Python MRO tự resolve method từ Mixin
        )
        widget.__class__ = new_class
    widget.init_protection(field_name or widget.objectName() or "Field", on_unlocked)
 
 
def protect_widgets_on_stacked(stacked_widget, widgets_config: list):
    """
    Patch nhiều widget và tự động reset khoá khi chuyển trang QStackedWidget.
 
    widgets_config: list of tuple (widget, field_name, on_unlocked)
 
    Ví dụ:
        protect_widgets_on_stacked(self.ui.stackedWidget, [
            (self.ui.db_file_path_edit,   None, self.connect_db),
            (self.ui.plc_ip_address_edit, None, self.connect_plc),
            (self.ui.db_number_input,     None, self.connect_db_number),
            (self.ui.db_data_size_input,  None, self.connect_db_size),
        ])
    """
    group = ProtectionGroup()
    protected = []
    for widget, field_name, on_unlocked in widgets_config:
        if widget is None:
            continue
        protect_widget(widget, field_name, on_unlocked)
        group.add(widget)
        protected.append(widget)
 
    # Lấy page chứa widget (dùng widget đầu tiên để tìm)
    def _find_page(w):
        parent = w.parent()
        while parent is not None:
            if parent.parent() is stacked_widget:
                return parent
            parent = parent.parent()
        return None
 
    home_page = _find_page(protected[0]) if protected else None
 
    def _on_page_changed(index):
        current_page = stacked_widget.widget(index)
        if current_page is not home_page:
            group.lock_all()  # chuyển trang → reset toàn nhóm
 
    stacked_widget.currentChanged.connect(_on_page_changed)