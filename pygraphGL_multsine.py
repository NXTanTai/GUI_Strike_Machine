# -*- coding: utf-8 -*-
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys
import time


class Visualizer(object):
    def __init__(self):
        self.traces = dict()

        # Kiểm tra nếu QApplication đã tồn tại chưa
        self.app = QtWidgets.QApplication.instance()
        if self.app is None:
            self.app = QtWidgets.QApplication(sys.argv)

        self.w = gl.GLViewWidget()
        self.w.opts['distance'] = 40
        self.w.setWindowTitle('Animated 3D Sine Wave')
        self.w.setGeometry(100, 100, 1280, 720)  # tránh đặt ở 0,0
        self.w.show()
        self.w.raise_()  # đưa cửa sổ lên trên cùng

        # Thêm lưới tham chiếu để xác nhận OpenGL đang render
        grid = gl.GLGridItem()
        self.w.addItem(grid)

        self.phase = 0
        self.lines = 50
        self.points = 1000
        self.y = np.linspace(-10, 10, self.lines)
        self.x = np.linspace(-10, 10, self.points)

        for i, line in enumerate(self.y):
            y = np.array([line] * self.points)
            d = np.sqrt(self.x ** 2 + y ** 2)
            sine = 10 * np.sin(d + self.phase)
            pts = np.vstack([self.x, y, sine]).transpose()
            self.traces[i] = gl.GLLinePlotItem(
                pos=pts,
                color=pg.glColor((i, self.lines * 1.3)),
                width=(i + 1) / 10,
                antialias=True
            )
            self.w.addItem(self.traces[i])

    def start(self):
        self.app.exec()  # gọi trực tiếp, đơn giản hơn

    def set_plotdata(self, name, points, color, width):
        self.traces[name].setData(pos=points, color=color, width=width)

    def update(self):
        stime = time.time()
        for i, line in enumerate(self.y):
            y = np.array([line] * self.points)
            amp = 10 / (i + 1)
            phase = self.phase * (i + 1) - 10
            freq = self.x * (i + 1) / 10
            sine = amp * np.sin(freq - phase)
            pts = np.vstack([self.x, y, sine]).transpose()
            self.set_plotdata(
                name=i, points=pts,
                color=pg.glColor((i, self.lines * 1.3)),
                width=3
            )
        self.phase -= .0002
        elapsed = time.time() - stime
        if elapsed > 0:
            print('{:.0f} FPS'.format(1 / elapsed))

    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(10)
        self.start()


if __name__ == '__main__':
    v = Visualizer()
    v.animation()