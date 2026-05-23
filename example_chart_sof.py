# Source - https://stackoverflow.com/q/78419328
# Posted by Piotr Herbut, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-22, License - CC BY-SA 4.0

"""Minimal reproducible example 1"""

import sys
import logging
from time import time_ns
import numpy as np
import paho.mqtt.client as mqtt
from PySide6.QtCore import QObject, QThread, QTimer, QCoreApplication, Qt, QMutex, QMutexLocker
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea,
)
from PySide6.QtGui import QGuiApplication
from pyqtgraph import GraphicsLayoutWidget, QtWidgets, mkPen, setConfigOptions, intColor

F_ACQ = 250
NUM_CHANNELS = 16
WINDOW = 60
NUM_SENSORS = 12
NS_TO_S = 1e-9
TRACES_PER_PLOT = 2
GRAPH_HEIGHT = 200
MARGIN = 1.05

MQTT_BROKER = "localhost"
MQTT_PORT = 1883

PLOT_START_TOPIC = "v1/command/plot_start"
PLOT_STOP_TOPIC = "v1/command/plot_stop"
PLOT_DATA_TOPIC = "v1/plot_data"

class CircularBuffer:
    """1D circular buffer"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = np.zeros(capacity, dtype=float)
        self.head = 0

    def append(self, value):
        """Append new element to buffer"""
        self.buffer[self.head] = value
        self.head = (self.head + 1) % self.capacity

    def get(self):
        """Roll buffer and return"""
        return np.roll(self.buffer, -self.head)


class CircularBuffer2D:
    """2D Circular buffer"""

    def __init__(self, n_rows, capacity):
        self.capacity = capacity
        self.n_rows = n_rows
        self.buffer = np.zeros((n_rows, capacity), dtype=float)
        self.head = 0

    def append(self, values):
        """Append new element to buffer"""
        self.buffer[:, self.head] = values
        self.head = (self.head + 1) % self.capacity

    def get(self):
        """Roll buffer and return"""
        return np.roll(self.buffer, -self.head, axis=1)


class CircPacketArray:  # pylint: disable=too-few-public-methods
    """Circular data packet"""

    def __init__(self, f_acq=100, window=60, num_channels=24):
        self._buffer_size = window * f_acq
        self.packet = {
            "time": CircularBuffer(capacity=self._buffer_size),
            "sensors": CircularBuffer2D(n_rows=NUM_SENSORS, capacity=self._buffer_size),
            "channels": CircularBuffer2D(n_rows=num_channels, capacity=self._buffer_size),
        }
        self.start_time = time_ns()

    def add(self, packet):
        """Add new corti packet and dispatch it per channel"""
        self.packet["time"].append(calc_time(packet[0], self.start_time))
        self.packet["sensors"].append(packet[1:13])
        self.packet["channels"].append(packet[13:])


def calc_time(data, start_time):
    """Calc elapsed time in [s]"""
    return (data - start_time) * NS_TO_S


class ScrollChart(QWidget):
    """Scroll chart"""

    def __init__(self, mutex, plot_packet):
        super().__init__()

        setConfigOptions(antialias=False, useOpenGL=False)

        self.mutex = mutex
        self.plot_packet = plot_packet

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_plot)

        self.init_ui(num_channels=NUM_CHANNELS)

        self.counter = 0
        self.start_time = 0

    def init_ui(self, num_channels):
        """Inititalize UI"""
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        layout.addWidget(self.scroll_area)

        num_channel_plots = int(np.ceil(num_channels / TRACES_PER_PLOT))
        num_sensor_plots = int(np.ceil(NUM_SENSORS / 3))

        canvas = GraphicsLayoutWidget()
        canvas.setFixedHeight((num_channel_plots + num_sensor_plots) * GRAPH_HEIGHT * MARGIN)
        canvas.setAntialiasing(False)
        canvas.setOptimizationFlag(QtWidgets.QGraphicsView.DontAdjustForAntialiasing)
        canvas.scene().setItemIndexMethod(QtWidgets.QGraphicsScene.NoIndex)
        canvas.ci.layout.setRowSpacing(0, 0)

        self.plots = []

        for idx in range(num_channel_plots):
            plot = canvas.addPlot(row=idx, col=0, rowspan=1, colspan=1, skipFiniteCheck=True)
            plot.setFixedHeight(GRAPH_HEIGHT)
            plot.setAutoVisible(x=False, y=False)

            self.plots.append(plot)

        self.channels = []

        for idx in range(num_channels):
            plot_idx = idx // TRACES_PER_PLOT
            self.channels.append(
                self.plots[plot_idx].plot(
                    pen=mkPen(intColor(idx, num_channels), width=1),
                    connect="auto",
                    name=idx,
                )
            )

        self.sensors = []
        for idx in range(num_sensor_plots):

            plot = canvas.addPlot(
                row=num_channel_plots + idx,
                col=0,
                rowspan=1,
                colspan=1,
                skipFiniteCheck=True,
            )

            plot.setFixedHeight(GRAPH_HEIGHT)
            plot.setAutoVisible(x=False, y=False)

            self.plots.append(plot)

        self.sensors = []
        for idx in range(NUM_SENSORS):
            plot_idx = idx // 3

            self.sensors.append(
                self.plots[num_channel_plots + plot_idx].plot(
                    pen=mkPen(
                        intColor(idx, NUM_SENSORS),
                        width=1,
                    ),
                    connect="auto",
                    name=idx,
                )
            )

        for plot in self.channels + self.sensors:
            view_box = plot.getViewBox()
            view_box.setYRange(0, 5.0, padding=0)
            view_box.setMouseEnabled(x=False, y=False)

        # Add QLabel for debug
        self.debug_info = QLabel("FPS: -")
        layout.addWidget(self.debug_info)

        self.scroll_area.setWidget(canvas)

    def start_timer(self):
        """start timer"""
        self.timer.start(100)

    def refresh_plot(self):
        """Refresh plot"""
        self.plot()
        self.update_status()

    def plot(self):
        """Plot graph"""
        #with QMutexLocker(self.mutex):
        dataset = self.plot_packet.packet

        t_data = dataset["time"].get()
        channels = dataset["channels"].get()
        sensors = dataset["sensors"].get()

        for idx, pen in enumerate(self.channels):
            pen.setData(x=t_data, y=channels[idx], _callSync="off", clear=True)

        for idx, pen in enumerate(self.sensors):
            pen.setData(x=t_data, y=sensors[idx], _callSync="off", clear=True)

    def update_status(self):
        """Display debug info"""
        if self.counter == 0:
            now = time_ns()
            elapsed_time = (now - self.start_time) * NS_TO_S
            self.start_time = now

            debug_text = f"FPS: {10/elapsed_time:2f}"
            logging.info(debug_text)
            self.debug_info.setText(debug_text)

        self.counter = (self.counter + 1) % 10


class MainScreen(QMainWindow):
    """Top level container"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MRE 1: Plotting only")

        width, height = QGuiApplication.instance().primaryScreen().size().toTuple()
        self.setGeometry(0, 0, width, height)

        self.plot_buffer = CircPacketArray(f_acq=F_ACQ, num_channels=NUM_CHANNELS, window=WINDOW)
        self.mutex = QMutex()
        self.worker = Worker(self.mutex, self.plot_buffer)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.run)

        self.chart = ScrollChart(self.mutex, self.plot_buffer)
        self.setCentralWidget(self.chart)
        self.chart.start_timer()
        self.worker_thread.start()


class Worker(QObject):
    """Communicator class"""

    def __init__(self, mutex, plot_buffer):
        super().__init__()
        self.mutex = mutex
        self.plot_buffer = plot_buffer
        self.client = mqtt.Client(protocol=mqtt.MQTTv5)
        self.client.connect(MQTT_BROKER, MQTT_PORT)
        self.client.message_callback_add(PLOT_DATA_TOPIC, self.on_plot_data)
        self.client.loop_start()

    def run(self):
        """Run communication thread"""
        logging.error("Worker running")
        self.plot_start()

    def on_plot_data(self, client, userdata, message):  # pylint: disable=unused-argument
        """Plot data callback"""
        data = np.frombuffer(message.payload)
        #with QMutexLocker(self.mutex):
        self.plot_buffer.add(data)

    def plot_start(self):
        """Request data for plotting"""
        self.client.subscribe(PLOT_DATA_TOPIC)
        self.client.publish(PLOT_START_TOPIC, "", qos=1)

    def plot_stop(self):
        """Stop data"""
        self.client.publish(PLOT_STOP_TOPIC, "", qos=1)
        self.client.unsubscribe(PLOT_DATA_TOPIC)


def run():
    """Run Qt app."""
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts, True)
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

    app = QApplication(sys.argv)
    window = MainScreen()
    window.show()

    app.exec()


if __name__ == "__main__":
    run()
