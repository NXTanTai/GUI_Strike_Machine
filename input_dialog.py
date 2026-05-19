"""
Modern Input Dialog Module
===========================
Dialog hiện đại để nhập thông số sản phẩm với 10 trường dữ liệu.

Usage:
    from modern_input_dialog import ModernInputDialog
    
    dialog = ModernInputDialog(parent)
    if dialog.exec_():
        data = dialog.get_data()
        print(data)  # {'name': '...', 'width': ..., 'thick': ..., ...}
"""

from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QLineEdit, QGridLayout,
                             QScrollArea, QWidget)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QFont, QDoubleValidator, QIntValidator


class ModernInputDialog(QDialog):
    """
    Dialog hiện đại để nhập thông số sản phẩm.
    
    Có 10 trường input:
    - Name Product (text)
    - Product Width (number)
    - Product Thick (number)
    - Gap Length (number)
    - Scale I/O (number)
    - Scale O/I (number)
    - Conveyor Spd (number)
    """
    
    def __init__(self, parent=None, title="Product Configuration", type = "product", initial_data=None):
        super().__init__(parent)
        self.initial_data = initial_data or {}
        self.type_object = type
        # Variables for dragging
        self.dragging = False
        self.drag_position = None
        
        # Setup dialog
        self.setWindowTitle(title)
        self.setModal(True)
        self.setMinimumWidth(800)
        self.setMinimumHeight(650)
        
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
        self.load_initial_data()
        
        # Animation
        self.fade_in_animation()
    
    def setup_ui(self, title):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Header
        header_frame = QFrame()
        header_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                
            }
        """)
        # border-bottom: 1px solid #E5E5E5;
        # Enable dragging on header
        header_frame.mousePressEvent = self.header_mouse_press
        header_frame.mouseMoveEvent = self.header_mouse_move
        header_frame.mouseReleaseEvent = self.header_mouse_release
        # Change cursor on header
        header_frame.setCursor(Qt.SizeAllCursor)
        
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(20, 15, 20, 15)
        
        # Icon and title
        icon_label = QLabel("📝")
        icon_label.setStyleSheet("font-size: 28px; color: #0B7EC8;")
        
        title_label = QLabel(title)
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
        
        # Content area with scroll
        content_frame = QFrame()
        content_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: none;
            }
        """)
        
        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(20, 20, 20, 20)
        
        # Scroll area for inputs
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background-color: #F1F5F9;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background-color: #CBD5E1;
                border-radius: 5px;
                min-height: 30px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #94A3B8;
            }
        """)
        
        # Input container
        input_widget = QWidget()
        input_layout = QVBoxLayout(input_widget)
        input_layout.setSpacing(10)
        
        # Store input fields
        self.inputs = {}
        if self.type_object == "product":
            # Product Name Input
            name_group = self.create_input_group(
                "Name Product",
                "name",
                "Enter product name",
                input_type="text",
                icon="📦"
            )
            input_layout.addWidget(name_group)
            
            # Separator
            separator1 = QFrame()
            separator1.setFrameShape(QFrame.HLine)
            separator1.setStyleSheet("background-color: #E5E5E5; max-height: 1px;")
            input_layout.addWidget(separator1)
            
            # Parameters section
            params_title = QLabel("📏 Product Parameters")
            params_title.setStyleSheet("""
                font-size: 16px;
                font-weight: 600;
                color: #1E293B;
                margin-top: 10px;
                border: none;
                margin-bottom: 5px;
            """)
            input_layout.addWidget(params_title)
            
            # Grid layout for parameter inputs
            grid_layout = QGridLayout()
            grid_layout.setSpacing(10)
            grid_layout.setContentsMargins(0, 10, 0, 10)
            
            # Define parameters with their details
            parameters = [
                ("Product Width", "width", "Enter product width", "📐"),
                ("Product Thick", "thick", "Enter product thickness", "📏"),
                ("Gap Length", "gap_length", "Enter gap length", "↔️"),
                ("Scale I/O", "scale_io", "Enter scale I/O", "⚖️"),
                ("Scale O/I", "scale_oi", "Enter scale O/I", "⚖️"),
                ("Conveyor Spd", "conveyor_spd", "Enter conveyor speed", "🔄")
            ]
        elif self.type_object == "box":
            # Product Name Input
            name_group = self.create_input_group(
                "Name Box",
                "name",
                "Enter box name",
                input_type="text",
                icon="📦"
            )
            input_layout.addWidget(name_group)
            
            # Separator
            separator1 = QFrame()
            separator1.setFrameShape(QFrame.HLine)
            separator1.setStyleSheet("background-color: #E5E5E5; max-height: 1px;")
            input_layout.addWidget(separator1)
            
            # Parameters section
            params_title = QLabel("📏 Box Parameters")
            params_title.setStyleSheet("""
                font-size: 16px;
                font-weight: 600;
                color: #1E293B;
                margin-top: 10px;
                border: none;
                margin-bottom: 5px;
            """)
            input_layout.addWidget(params_title)
            
            # Grid layout for parameter inputs
            grid_layout = QGridLayout()
            grid_layout.setSpacing(10)
            grid_layout.setContentsMargins(0, 10, 0, 10)
            
            # Define parameters with their details
            parameters = [
                ("Box length", "length", "Enter box length", "📐"),
                ("Box Width", "width", "Enter box width", "📐"),
                ("Box Height", "height", "Enter box height", "📐"),
            ]
        
        # Create parameter inputs in grid (3x3)
        for i, (label, field_name, placeholder, icon) in enumerate(parameters):
            param_group = self.create_input_group(
                label,
                field_name,
                placeholder,
                input_type="number",
                icon=icon
            )
            row = i // 3
            col = i % 3
            grid_layout.addWidget(param_group, row, col)
        
        input_layout.addLayout(grid_layout)
        input_layout.addStretch()
        
        scroll_area.setWidget(input_widget)
        content_layout.addWidget(scroll_area)
        
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
        
        button_layout = QHBoxLayout(button_frame)
        button_layout.setContentsMargins(20, 15, 20, 15)
        button_layout.setSpacing(10)
        
        # Validation info
        self.validation_label = QLabel("ℹ️ Fill in all required fields")
        self.validation_label.setStyleSheet("""
            font-size: 12px;
            color: #64748B;
            font-style: italic;
        """)
        
        button_layout.addWidget(self.validation_label)
        button_layout.addStretch()
        
        # Cancel button
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setMinimumWidth(100)
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #0B7EC8;
                border: 1px solid #0B7EC8;
                padding: 10px 24px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #F0F9FF;
            }
            QPushButton:pressed {
                background-color: #E0F2FE;
            }
        """)
        cancel_btn.clicked.connect(self.reject)
        cancel_btn.setDefault(False)
        cancel_btn.setAutoDefault(False)
        
        # Save button
        self.save_btn = QPushButton("💾 Save")
        self.save_btn.setMinimumWidth(120)
        self.save_btn.setStyleSheet("""
            QPushButton {
                background-color: #0B7EC8;
                color: white;
                border: none;
                padding: 10px 24px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: 500;
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
        self.save_btn.clicked.connect(self.validate_and_accept)
        self.save_btn.setDefault(True)
        self.save_btn.setAutoDefault(True)
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(self.save_btn)
        
        # Assemble dialog
        main_layout.addWidget(header_frame)
        main_layout.addWidget(content_frame, 1)  # Content takes most space
        main_layout.addWidget(button_frame)


    
    def create_input_group(self, label_text, field_name, placeholder, input_type="text", icon=""):
        """Create a styled input group"""
        group = QFrame()
        group.setStyleSheet("""
            QFrame {
                background-color: #F8FAFC;
                border: 1px solid #E5E5E5;
                border-radius: 8px;
                padding: 12px;
            }
        """)
        
        layout = QVBoxLayout(group)
        layout.setSpacing(8)
        layout.setContentsMargins(12, 12, 12, 12)
        
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
        input_field.setStyleSheet("""
            QLineEdit {
                border: 1px solid #D1D5DB;
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
                background-color: white;
            }
            QLineEdit:focus {
                border: 2px solid #0B7EC8;
                background-color: white;
            }
            QLineEdit:hover {
                border: 1px solid #0B7EC8;
            }
        """)
        
        # Set validator based on input type
        if input_type == "number":
            validator = QDoubleValidator(0.0, 999.99, 2)
            validator.setNotation(QDoubleValidator.StandardNotation)
            input_field.setValidator(validator)
            input_field.setText("0.00")
        
        # Connect change event for validation
        input_field.textChanged.connect(self.check_validation)
        
        # Store reference
        self.inputs[field_name] = input_field
        
        layout.addLayout(label_layout)
        layout.addWidget(input_field)
        
        return group
    
    def check_validation(self):
        """Check if all fields are valid"""
        name = self.inputs['name'].text().strip()
        
        if name:
            self.validation_label.setText("✅ Ready to save")
            self.validation_label.setStyleSheet("""
                font-size: 12px;
                color: #10B981;
                font-weight: 500;
            """)
            self.save_btn.setEnabled(True)
        else:
            if self.type_object == "product":
                self.validation_label.setText("⚠️ Product name is required")
            elif self.type_object == "box":
                self.validation_label.setText("⚠️ Box name is required")
                
            self.validation_label.setStyleSheet("""
                font-size: 12px;
                color: #F59E0B;
                font-style: italic;
            """)
            self.save_btn.setEnabled(False)
    
    def validate_and_accept(self):
        """Validate data before accepting"""
        name = self.inputs['name'].text().strip()
        
        if not name:
            if self.type_object =="product":
                self.validation_label.setText("❌ Product name cannot be empty!")
            elif self.type_object == "box":
                self.validation_label.setText("❌ Box name cannot be empty!")
            self.validation_label.setStyleSheet("""
                font-size: 12px;
                color: #EF4444;
                font-weight: 600;
            """)
            self.inputs['name'].setFocus()
            return
        
        self.accept()
    
    def load_initial_data(self):
        """Load initial data into fields"""
        if self.initial_data:
            for field_name, value in self.initial_data.items():
                if field_name in self.inputs:
                    self.inputs[field_name].setText(str(value))
        self.check_validation()
    
    def get_data(self):
        """Get all input data as dictionary"""
        data = {}
        data['name'] = self.inputs['name'].text().strip()
        
        # Get all numeric parameters
        if self.type_object =="product":
            numeric_fields = [
                'width', 'thick', 'gap_length', 
                'scale_io', 'scale_oi', 'conveyor_spd'
            ]
        elif self.type_object =="box":
            numeric_fields = [
                'length', 'width', 'height'
            ]
        
        for field_name in numeric_fields:
            try:
                value = float(self.inputs[field_name].text() or 0)
                data[field_name] = value
            except ValueError:
                data[field_name] = 0.0
        
        return data
    
    def fade_in_animation(self):
        """Fade in animation when dialog appears"""
        self.setWindowOpacity(0)
        
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(200)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()
    
    # Dragging functionality
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
    def get_type_data(parent=None, title="Product Configuration", type = "product", initial_data=None):
        """
        Static method để hiển thị dialog và lấy dữ liệu
        
        Usage:
            data = ModernInputDialog.get_type_data(self, "Add Product")
            if data:
                print(data)
        """
        dialog = ModernInputDialog(parent, title, type, initial_data)
        result = dialog.exec_()
        
        if result == QDialog.Accepted:
            return dialog.get_data()
        return None

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            # Nếu focus đang ở một input field
            if isinstance(self.focusWidget(), QLineEdit):
                self.validate_and_accept()
                event.accept()
                return
        elif event.key() == Qt.Key_Escape:
            self.reject()
            event.accept()
            return
        
        super().keyPressEvent(event)