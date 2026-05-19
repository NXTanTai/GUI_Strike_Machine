import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates
import numpy as np
import random
import matplotlib.patheffects as pe

from datetime import datetime, timedelta

# ==========================================
# CONFIG
# ==========================================
window_seconds = 30

# ==========================================
# DATA
# ==========================================
x_data = []

T1 = []
T2 = []
T3 = []
P = []

# ==========================================
# FIGURE
# ==========================================
fig, ax1 = plt.subplots(figsize=(15, 7))

# ==========================================
# BACKGROUND
# ==========================================
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

ax1.imshow(
    gradient,
    aspect='auto',
    extent=[0, 1, 0, 1],
    transform=ax1.transAxes,
    cmap='Blues',
    alpha=0.25,
    zorder=0
)

fig.patch.set_facecolor('#d9e6ff')
ax1.set_facecolor('#f8f9fc')

# ==========================================
# SECOND AXIS
# ==========================================
ax2 = ax1.twinx()

# ==========================================
# LINES
# ==========================================
line1, = ax1.plot([], [], color='#00ffaa', linewidth=1.2, label='T1')
line2, = ax1.plot([], [], color='#ffcc00', linewidth=1.2, label='T2')
line3, = ax1.plot([], [], color='#ff4444', linewidth=1.2, label='T3')

line4, = ax2.plot([], [], color="#FFFFFF", linewidth=1.2, linestyle='--', label='Pressure')

# ==========================================
# GLOW EFFECT
# ==========================================
for line in [line1, line2, line3, line4]:
    line.set_path_effects([
        pe.Stroke(linewidth=3, foreground='white', alpha=0.2),
        pe.Normal()
    ])

# ==========================================
# TEXT STYLE
# ==========================================
bbox_style = dict(
    facecolor='black',
    alpha=0.6,
    edgecolor='none',
    boxstyle='round,pad=0.25'
)

txt1 = ax1.text(0, 0, '', color='#00ffaa',
                fontsize=10, fontweight='bold',
                bbox=bbox_style)

txt2 = ax1.text(0, 0, '', color='#ffcc00',
                fontsize=10, fontweight='bold',
                bbox=bbox_style)

txt3 = ax1.text(0, 0, '', color='#ff4444',
                fontsize=10, fontweight='bold',
                bbox=bbox_style)

txt4 = ax2.text(0, 0, '', color="#FFFFFF",
                fontsize=10, fontweight='bold',
                bbox=bbox_style)

# ==========================================
# GRID
# ==========================================
ax1.grid(
    True,
    linestyle='--',
    linewidth=0.6,
    alpha=0.6,
    color='gray'
)

# ==========================================
# BORDER
# ==========================================
for spine in ax1.spines.values():
    spine.set_linewidth(2)
    spine.set_color('#666666')

# ==========================================
# LABEL
# ==========================================
ax1.set_ylabel("Temperature (°C)", fontsize=12)
ax2.set_ylabel("Pressure (bar)", fontsize=12)

# ==========================================
# LIMIT
# ==========================================
ax1.set_ylim(0, 100)
ax2.set_ylim(0, 10)

# ==========================================
# DATETIME FORMAT
# ==========================================
ax1.xaxis.set_major_formatter(
    mdates.DateFormatter('%d-%m-%Y\n%H:%M:%S')
)

# ==========================================
# LEGEND
# ==========================================
lines = [line1, line2, line3, line4]
labels = [l.get_label() for l in lines]

ax1.legend(lines, labels, loc='upper left', ncol=4)

# ==========================================
# TITLE
# ==========================================
plt.title(
    "Realtime Temperature & Pressure SCADA",
    fontsize=18,
    fontweight='bold'
)

# ==========================================
# UPDATE
# ==========================================
def update(frame):

    now = datetime.now()

    # ======================================
    # ADD TIME
    # ======================================
    x_data.append(now)

    # ======================================
    # RANDOM DATA
    # ======================================
    T1.append(random.uniform(20, 50))
    T2.append(random.uniform(30, 60))
    T3.append(random.uniform(40, 80))

    P.append(random.uniform(1, 6))

    # ======================================
    # UPDATE LINE
    # ======================================
    line1.set_data(x_data, T1)
    line2.set_data(x_data, T2)
    line3.set_data(x_data, T3)

    line4.set_data(x_data, P)

    # ======================================
    # SCROLL WINDOW
    # ======================================
    left_time = now - timedelta(seconds=window_seconds)

    # sát mép phải
    right_time = now + timedelta(milliseconds=200)

    ax1.set_xlim(left_time, right_time)
    ax2.set_xlim(left_time, right_time)

    # ======================================
    # TEXT POSITION
    # ======================================
    text_x = now + timedelta(milliseconds=250)

    txt1.set_position((text_x, T1[-1]))
    txt1.set_text(f'{T1[-1]:.1f}°C')

    txt2.set_position((text_x, T2[-1]))
    txt2.set_text(f'{T2[-1]:.1f}°C')

    txt3.set_position((text_x, T3[-1]))
    txt3.set_text(f'{T3[-1]:.1f}°C')

    txt4.set_position((text_x, P[-1]))
    txt4.set_text(f'{P[-1]:.2f} bar')

    # ======================================
    # AUTO FORMAT
    # ======================================
    fig.autofmt_xdate()

    return (
        line1,
        line2,
        line3,
        line4,
        txt1,
        txt2,
        txt3,
        txt4
    )

# ==========================================
# RUN
# ==========================================
ani = FuncAnimation(
    fig,
    update,
    interval=1000,
    blit=False
)

plt.tight_layout()

plt.show()