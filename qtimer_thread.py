import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox
from PySide6.QtCore import Slot, QMetaObject, QObject, Qt, QTimer, QThread, Q_ARG


class Worker(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.work)

    def start(self):
        self.timer.start(1000)

    def work(self):
        print("Hello World...")

    def stop(self):
        self.timer.stop()
        
    @Slot(int)
    def set_interval(self, interval):
        self.timer.setInterval(interval)
