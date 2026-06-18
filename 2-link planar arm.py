"""
DEMO: Hiển thị cánh tay robot 2 bậc tự do (2-DOF) và điều khiển nó chuyển động
bằng cách gửi dữ liệu góc khớp vào hàm send_data().

Cách chạy:
    pip install matplotlib numpy
    python robot_arm_2dof.py

Cấu hình giả định: cánh tay phẳng 2 khâu, cả 2 khớp quay quanh trục Z
(giống ví dụ "2-link planar arm" chuẩn trong robotics).
"""

import time
import queue
import threading

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------- Thông số cánh tay ----------------
L1 = 1.0   # độ dài khâu 1 (từ gốc đến khớp khuỷu)
L2 = 0.8   # độ dài khâu 2 (từ khớp khuỷu đến đầu tay)

# Hàng đợi để nhận dữ liệu góc khớp mới từ bên ngoài (an toàn giữa các thread)
_data_queue = queue.Queue()


def forward_kinematics(theta1, theta2):
    """
    Tính toạ độ 3 điểm: gốc - khớp khuỷu - đầu tay, từ 2 góc khớp (radian).
    theta1: góc khớp gốc (so với trục X)
    theta2: góc khớp khuỷu (so với khâu 1)
    """
    p0 = np.array([0.0, 0.0, 0.0])
    p1 = p0 + np.array([L1 * np.cos(theta1), L1 * np.sin(theta1), 0.0])
    p2 = p1 + np.array([
        L2 * np.cos(theta1 + theta2),
        L2 * np.sin(theta1 + theta2),
        0.0,
    ])
    return p0, p1, p2


# ---------------- Thiết lập hình vẽ ----------------
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")

line, = ax.plot([], [], [], "o-", linewidth=5, markersize=12, color="royalblue")
label = ax.text2D(0.02, 0.95, "", transform=ax.transAxes, fontsize=11)

reach = L1 + L2 + 0.3
ax.set_xlim(-reach, reach)
ax.set_ylim(-reach, reach)
ax.set_zlim(-reach, reach)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Cánh tay robot 2 bậc tự do (2-DOF)")

_current_angles = [0.0, 0.0]  # theta1, theta2 hiện tại (radian)


def _update(frame):
    """Hàm này được FuncAnimation gọi liên tục để vẽ lại frame mới."""
    while not _data_queue.empty():
        _current_angles[0], _current_angles[1] = _data_queue.get()

    p0, p1, p2 = forward_kinematics(*_current_angles)
    xs, ys, zs = zip(p0, p1, p2)
    line.set_data(xs, ys)
    line.set_3d_properties(zs)
    label.set_text(
        f"θ1 = {np.degrees(_current_angles[0]):.1f}°   "
        f"θ2 = {np.degrees(_current_angles[1]):.1f}°"
    )
    return line, label


ani = FuncAnimation(fig, _update, interval=50, blit=False, cache_frame_data=False)


# ---------------- API để gửi dữ liệu vào ----------------
def send_data(theta1_deg, theta2_deg):
    """
    Gọi hàm này từ bất kỳ đâu (thread khác, callback nhận dữ liệu serial/socket/MQTT...)
    để cập nhật góc khớp mới (đơn vị: độ). Cánh tay sẽ tự vẽ lại theo dữ liệu này.

    Ví dụ: send_data(45, -30)
    """
    _data_queue.put((np.radians(theta1_deg), np.radians(theta2_deg)))


# ---------------- Demo: giả lập nguồn dữ liệu gửi vào liên tục ----------------
def _fake_data_source():
    """Thay hàm này bằng nguồn dữ liệu thật của bạn (serial, socket, MQTT, file, v.v.)."""
    t = 0.0
    while True:
        theta1 = 60 * np.sin(t)
        theta2 = 40 * np.cos(t * 1.5)
        send_data(theta1, theta2)
        t += 0.05
        time.sleep(0.05)

if __name__ == "__main__":
    threading.Thread(target=_fake_data_source, daemon=True).start()
    plt.show()