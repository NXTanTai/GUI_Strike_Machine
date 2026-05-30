import sys
import os
from tech_link_theme import Ui_MainWindow
from Custom_Widgets import *  # type: ignore
from PySide6.QtWidgets import (QVBoxLayout, QHeaderView, QAbstractSpinBox,
                               QLabel, QMainWindow, QApplication, QLineEdit,
                               QFileDialog, QDialog, QTableWidget, QTableWidgetItem)
from PySide6.QtCore import QSettings, QEasingCurve, QTimer

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"
os.environ["QT_FONT_DPI"] = "96"

class StrikeMachine(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setup_slide_menu()
        QTimer.singleShot(500, lambda: print(
            "min:", self.ui.left_side_menu_widget.minimumHeight(),
            "max:", self.ui.left_side_menu_widget.maximumHeight(),
            "size:", self.ui.left_side_menu_widget.size(),
            "sizeHint:", self.ui.left_side_menu_widget.sizeHint(),
        ))

    def _setup_slide_menu(self):
        self.ui.left_side_menu_widget.customizeQCustomSlideMenu(
            defaultWidth = 70,
            defaultHeight = "parent",
            collapsedWidth = 70,
            collapsedHeight = "parent",
            expandedWidth = 175,
            expandedHeight = "parent",
            animationDuration = 200,
            animationEasingCurve = QEasingCurve.Linear,
            collapsingAnimationDuration = 200,
            collapsingAnimationEasingCurve = QEasingCurve.Linear,
            expandingAnimationDuration = 200,
            expandingAnimationEasingCurve = QEasingCurve.Linear,
        )
        self.ui.open_side_menu_btn.clicked.connect(
            self.ui.left_side_menu_widget.slideMenu
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StrikeMachine()
    window.show()
    sys.exit(app.exec())