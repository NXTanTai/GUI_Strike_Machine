# pyside6-uic tech_link_theme.ui -o tech_link_theme.py
import sys
import random
import os
import re
import time 
import psutil
import platform
import subprocess
import logging
import logging.handlers
import sqlite3
import socket
import atexit
import snap7
from PySide6.QtCore import (Qt, QTimer, QMutex, 
                            QSettings, QDateTime, QCoreApplication,
                            QEvent, QUrl, QSharedMemory, 
                            QSystemSemaphore, QThread, QTranslator)
from PySide6.QtGui import QPalette, QColor, QPainter, QFont
from PySide6.QtWidgets import (
    QWidget, QGridLayout, QFormLayout, QPushButton, QHBoxLayout, QVBoxLayout, QHeaderView, 
    QComboBox, QCheckBox, QGroupBox, QLabel,QMainWindow, QApplication, QGraphicsProxyWidget
)
from PySide6.QtCharts import (
    QChart, QChartView,
    QLineSeries, QSplineSeries, QScatterSeries,
    QAreaSeries, QPieSeries,
    QStackedBarSeries, QBarSet,
    QValueAxis
)
from tech_link_theme import Ui_MainWindow
from Custom_Widgets import * #type: ignore
from spline_chart import SplineChartWidget
from Custom_Chart_Widgets import CustomChartWidget
from System_Data import syss
from Data_Simulator import DataSimulator

class StrikeMachine(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StrikeMachine()
    window.show()
    sys.exit(app.exec())