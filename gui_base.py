# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from Custom_Widgets.Widgets import *

class gui_base(QMainWindow):
    def __init__(self):
        super(gui_base, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        loadJsonStyle(self, self.ui)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = gui_base()
    window.show()
    sys.exit(app.exec_())
