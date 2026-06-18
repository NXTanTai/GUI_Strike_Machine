"""
DEMO: App desktop (PySide6 + PyVista) hiển thị cánh tay robot 2 bậc tự do (2-DOF),
có thanh trượt điều khiển thủ công và API send_data() để nhận dữ liệu từ bên ngoài
(cảm biến, socket, serial...) một cách AN TOÀN với luồng GUI của Qt.
"""

import time
import threading
import numpy as np
import pyvista as pv
from pyvistaqt import QtInteractor
from PySide6.QtCore import QObject, Signal, Qt, QTimer
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QSlider, QLabel, QGroupBox, QPushButton,
)
from vtkmodules.vtkCommonCore import vtkObject

vtkObject.GlobalWarningDisplayOff()  # tắt log warning/error nội bộ của VTK (vô hại lúc đóng app)

# ---------------- Thông số cánh tay ----------------
L1 = 1.0       # độ dài khâu 1
L2 = 0.8       # độ dài khâu 2
RADIUS = 0.08  # bán kính khối trụ đại diện cho khâu

def forward_kinematics(theta1, theta2):
    """Tính toạ độ gốc - khớp khuỷu - đầu tay từ 2 góc khớp (radian)."""
    p0 = np.array([0.0, 0.0, 0.0])
    p1 = p0 + np.array([L1 * np.cos(theta1), L1 * np.sin(theta1), 0.0])
    p2 = p1 + np.array([
        L2 * np.cos(theta1 + theta2),
        L2 * np.sin(theta1 + theta2),
        0.0,
    ])
    return p0, p1, p2

def rotation_z_matrix(angle, translation=(0.0, 0.0, 0.0)):
    c, s = np.cos(angle), np.sin(angle)
    m = np.eye(4)
    m[0, 0], m[0, 1] = c, -s
    m[1, 0], m[1, 1] = s, c
    m[0, 3], m[1, 3], m[2, 3] = translation
    return m

def translation_matrix(t):
    m = np.eye(4)
    m[0, 3], m[1, 3], m[2, 3] = t
    return m


# ==================== Widget hiển thị 3D (nhúng PyVista vào Qt) ====================
class RobotArmView(QtInteractor):
    """QtInteractor = Plotter của PyVista nhưng là một QWidget thật, nhúng được vào layout Qt."""

    def __init__(self, parent=None):
        super().__init__(parent)

        base_mesh = pv.Cylinder(center=(0, 0, -0.05), direction=(0, 0, 1), radius=0.18, height=0.1)
        joint0_mesh = pv.Sphere(radius=0.12)
        link1_mesh = pv.Cylinder(center=(L1 / 2, 0, 0), direction=(1, 0, 0), radius=RADIUS, height=L1)
        joint1_mesh = pv.Sphere(radius=0.1)
        link2_mesh = pv.Cylinder(center=(L2 / 2, 0, 0), direction=(1, 0, 0), radius=RADIUS * 0.85, height=L2)
        end_effector_mesh = pv.Sphere(radius=0.08)

        self.add_mesh(base_mesh, color="dimgray")
        self.joint0_actor = self.add_mesh(joint0_mesh, color="orange")
        self.link1_actor = self.add_mesh(link1_mesh, color="royalblue")
        self.joint1_actor = self.add_mesh(joint1_mesh, color="orange")
        self.link2_actor = self.add_mesh(link2_mesh, color="seagreen")
        self.end_actor = self.add_mesh(end_effector_mesh, color="crimson")

        self.add_axes()
        self.show_grid()

        reach = L1 + L2 + 0.3
        self.camera_position = [(reach * 1.6, -reach * 1.6, reach), (0, 0, 0), (0, 0, 1)]

        self.apply_pose(0.0, 0.0)
        self.render_timer = QTimer(self)
        self.render_timer.timeout.connect(self.render)
        self.render_timer.start(16)   # ~60 FPS

    def apply_pose(self, theta1, theta2):
        """theta1, theta2: radian. Chỉ cập nhật ma trận transform, không vẽ lại mesh."""
        p0, p1, p2 = forward_kinematics(theta1, theta2)
        self.link1_actor.user_matrix = rotation_z_matrix(theta1)
        self.joint1_actor.user_matrix = translation_matrix(p1)
        self.link2_actor.user_matrix = rotation_z_matrix(theta1 + theta2, translation=p1)
        self.end_actor.user_matrix = translation_matrix(p2)
        # self.render()


# ==================== Cầu nối dữ liệu thread-safe ====================
class DataBridge(QObject):
    """
    Nhận góc khớp mới từ BẤT KỲ thread nào (cảm biến, socket, serial, MQTT...)
    rồi chuyển an toàn sang thread chính của Qt thông qua signal/slot - đây là
    cách chuẩn để cập nhật GUI từ thread khác trong Qt, tránh crash/lỗi do
    đụng tài nguyên GUI từ ngoài thread chính.
    """
    new_angles = Signal(float, float)  # theta1_deg, theta2_deg


bridge = DataBridge()

def send_data(theta1_deg, theta2_deg):
    """Gọi hàm này từ bất kỳ đâu (thread khác, callback nhận dữ liệu...) để cập nhật cánh tay."""
    bridge.new_angles.emit(theta1_deg, theta2_deg)


# ==================== Cửa sổ chính ====================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cánh tay robot 2 bậc tự do")
        self.resize(1100, 700)

        central = QWidget()
        layout = QHBoxLayout(central)
        self.setCentralWidget(central)

        # --- Khung nhìn 3D ---
        self.view = RobotArmView(self)
        layout.addWidget(self.view, stretch=4)

        # --- Bảng điều khiển ---
        panel = QGroupBox("Điều khiển")
        panel.setFixedWidth(260)
        panel_layout = QVBoxLayout(panel)

        self.label_t1 = QLabel("Theta 1: 0°")
        self.slider_t1 = QSlider(Qt.Horizontal)
        self.slider_t1.setRange(-180, 180)
        self.slider_t1.valueChanged.connect(self._on_slider_changed)

        self.label_t2 = QLabel("Theta 2: 0°")
        self.slider_t2 = QSlider(Qt.Horizontal)
        self.slider_t2.setRange(-180, 180)
        self.slider_t2.valueChanged.connect(self._on_slider_changed)

        btn_reset = QPushButton("Reset về 0°")
        btn_reset.clicked.connect(lambda: send_data(0, 0))

        panel_layout.addWidget(self.label_t1)
        panel_layout.addWidget(self.slider_t1)
        panel_layout.addWidget(self.label_t2)
        panel_layout.addWidget(self.slider_t2)
        panel_layout.addStretch()
        panel_layout.addWidget(btn_reset)

        layout.addWidget(panel)

        # Lắng nghe dữ liệu gửi từ bên ngoài qua send_data()
        bridge.new_angles.connect(self._on_external_data)

    def _on_slider_changed(self, _value):
        """Người dùng tự kéo slider để test thủ công."""
        t1_deg = self.slider_t1.value()
        t2_deg = self.slider_t2.value()
        self.label_t1.setText(f"Theta 1: {t1_deg}°")
        self.label_t2.setText(f"Theta 2: {t2_deg}°")
        self.view.apply_pose(np.radians(t1_deg), np.radians(t2_deg))

    def _on_external_data(self, theta1_deg, theta2_deg):
        """Slot này luôn được Qt chạy trên thread chính, nên cập nhật GUI ở đây an toàn."""
        self.slider_t1.blockSignals(True)
        self.slider_t2.blockSignals(True)
        self.slider_t1.setValue(int(round(theta1_deg)))
        self.slider_t2.setValue(int(round(theta2_deg)))
        self.slider_t1.blockSignals(False)
        self.slider_t2.blockSignals(False)

        self.label_t1.setText(f"Theta 1: {theta1_deg:.1f}°")
        self.label_t2.setText(f"Theta 2: {theta2_deg:.1f}°")
        self.view.apply_pose(np.radians(theta1_deg), np.radians(theta2_deg))
        # self.add_text(
        #     f"{self.iren.GetDesiredUpdateRate()}",
        #     position="upper_left"
        # )

    def closeEvent(self, event):
        self.view.close()
        super().closeEvent(event)


# ==================== Demo: giả lập nguồn dữ liệu gửi vào liên tục ====================
def _fake_data_source():
    """Thay hàm này bằng nguồn dữ liệu thật của bạn (serial, socket, MQTT, file, ROS...)."""
    t = 0.0
    while True:
        send_data(60 * np.sin(t), 40 * np.cos(t * 1.5))
        t += 0.005
        time.sleep(0.005)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()

    threading.Thread(target=_fake_data_source, daemon=True).start()

    app.exec()