"""
DEMO: Cánh tay robot 2 bậc tự do (2-DOF) dạng khối 3D thật, dùng PyVista.
Gửi dữ liệu góc khớp vào hàm send_data() để điều khiển cánh tay chuyển động.

Cách chạy:
    pip install pyvista numpy
    python robot_arm_2dof_pyvista.py

Cấu hình giả định: cánh tay phẳng 2 khâu, cả 2 khớp quay quanh trục Z
(chuyển động trong mặt phẳng XY). Nếu robot thật của bạn có cấu hình khác
(ví dụ khớp gốc xoay ngang quanh Z + khớp vai nâng lên/xuống quanh Y để
chuyển động thật trong không gian 3D), báo mình để chỉnh lại ma trận xoay.
"""

import time
import queue
import threading

import numpy as np
import pyvista as pv
from vtkmodules.vtkCommonCore import vtkObject

# Tắt log warning/error nội bộ của VTK (ví dụ lỗi shader vô hại lúc đóng cửa sổ)
vtkObject.GlobalWarningDisplayOff()

# ---------------- Thông số cánh tay ----------------
L1 = 1.0     # độ dài khâu 1
L2 = 0.8     # độ dài khâu 2
RADIUS = 0.08  # bán kính khối trụ đại diện cho khâu

_data_queue = queue.Queue()
_current_angles = [0.0, 0.0]  # theta1, theta2 hiện tại (radian)


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
    """Ma trận 4x4: xoay quanh trục Z rồi tịnh tiến - dùng cho actor.user_matrix."""
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


# ---------------- Tạo khối hình học ở toạ độ "cục bộ" (chưa đặt vào vị trí cuối) ----------------
# Mỗi khâu được tạo dọc theo trục X, dài đúng L1/L2, sau đó sẽ xoay + tịnh tiến
# bằng actor.user_matrix mỗi khi có dữ liệu mới - không cần tạo lại mesh.
base_mesh = pv.Cylinder(center=(0, 0, -0.05), direction=(0, 0, 1), radius=0.18, height=0.1)
joint0_mesh = pv.Sphere(radius=0.12)
link1_mesh = pv.Cylinder(center=(L1 / 2, 0, 0), direction=(1, 0, 0), radius=RADIUS, height=L1)
joint1_mesh = pv.Sphere(radius=0.1)
link2_mesh = pv.Cylinder(center=(L2 / 2, 0, 0), direction=(1, 0, 0), radius=RADIUS * 0.85, height=L2)
end_effector_mesh = pv.Sphere(radius=0.08)

# ---------------- Thiết lập Plotter ----------------
plotter = pv.Plotter()
plotter.add_axes()
plotter.show_grid()
plotter.set_background("white")

plotter.add_mesh(base_mesh, color="dimgray")               # bệ đỡ, cố định
joint0_actor = plotter.add_mesh(joint0_mesh, color="orange")    # khớp gốc
link1_actor = plotter.add_mesh(link1_mesh, color="royalblue")   # khâu 1
joint1_actor = plotter.add_mesh(joint1_mesh, color="orange")    # khớp khuỷu
link2_actor = plotter.add_mesh(link2_mesh, color="seagreen")    # khâu 2
end_actor = plotter.add_mesh(end_effector_mesh, color="crimson")  # đầu tay

reach = L1 + L2 + 0.3
plotter.camera_position = [(reach * 1.6, -reach * 1.6, reach), (0, 0, 0), (0, 0, 1)]


def _apply_pose(theta1, theta2):
    """Áp ma trận transform mới cho từng khối dựa trên góc khớp hiện tại."""
    p0, p1, p2 = forward_kinematics(theta1, theta2)
    link1_actor.user_matrix = rotation_z_matrix(theta1)
    joint1_actor.user_matrix = translation_matrix(p1)
    link2_actor.user_matrix = rotation_z_matrix(theta1 + theta2, translation=p1)
    end_actor.user_matrix = translation_matrix(p2)


_apply_pose(0.0, 0.0)


# ---------------- API để gửi dữ liệu vào ----------------
def send_data(theta1_deg, theta2_deg):
    """
    Gọi hàm này từ bất kỳ đâu (thread khác, callback nhận dữ liệu serial/socket/MQTT...)
    để cập nhật góc khớp mới (đơn vị: độ). Cánh tay sẽ tự xoay theo dữ liệu này
    ở vòng lặp render bên dưới.

    Ví dụ: send_data(45, -30)
    """
    _data_queue.put((np.radians(theta1_deg), np.radians(theta2_deg)))


# ---------------- Demo: giả lập nguồn dữ liệu gửi vào liên tục ----------------
def _fake_data_source():
    """Thay hàm này bằng nguồn dữ liệu thật của bạn (serial, socket, MQTT, file, ROS...)."""
    t = 0.0
    while True:
        theta1 = 60 * np.sin(t)
        theta2 = 40 * np.cos(t * 1.5)
        send_data(theta1, theta2)
        t += 0.03
        time.sleep(0.03)


if __name__ == "__main__":
    threading.Thread(target=_fake_data_source, daemon=True).start()

    # interactive_update=True: cửa sổ vẫn cho xoay/zoom bằng chuột,
    # đồng thời vòng lặp dưới đây liên tục cập nhật theo dữ liệu mới.
    plotter.show(interactive_update=True, auto_close=False, title="Cánh tay robot 2 bậc tự do")
    while not plotter._closed:  # dừng ngay khi người dùng đóng cửa sổ, không render vào context đã huỷ
        while not _data_queue.empty():
            _current_angles[0], _current_angles[1] = _data_queue.get()
        _apply_pose(*_current_angles)
        try:
            plotter.update()
        except Exception:
            break
        time.sleep(0.03)