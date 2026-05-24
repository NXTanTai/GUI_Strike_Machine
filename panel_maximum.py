"""
Panel Maximize Effect - PyQt5
Hiệu ứng phóng to panel khi click (Tile/Panel Zoom)
Dùng QPropertyAnimation để tạo chuyển động mượt
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QHBoxLayout, QGridLayout, QPushButton, QFrame
)
from PyQt5.QtCore import (
    Qt, QPropertyAnimation, QRect, QEasingCurve,
    QParallelAnimationGroup, pyqtProperty, QTimer
)
from PyQt5.QtGui import QColor, QFont, QPalette


# ─── Màu sắc cho từng panel ────────────────────────────────────────────────
PANEL_STYLES = [
    {"bg": "#1a1a2e", "accent": "#e94560", "icon": "📹", "title": "Camera 1",  "sub": "Sân trước"},
    {"bg": "#16213e", "accent": "#0f3460", "icon": "📡", "title": "Camera 2",  "sub": "Hành lang"},
    {"bg": "#0f3460", "accent": "#533483", "icon": "🎥", "title": "Camera 3",  "sub": "Sân sau"},
    {"bg": "#533483", "accent": "#e94560", "icon": "🔭", "title": "Camera 4",  "sub": "Cổng vào"},
]


class PanelWidget(QFrame):
    """Một panel có thể click để phóng to/thu nhỏ."""

    def __init__(self, index: int, style_info: dict, parent_grid=None):
        super().__init__()
        self.index = index
        self.style_info = style_info
        self.parent_grid = parent_grid  # tham chiếu đến GridManager
        self.is_maximized = False
        self._setup_ui()

    def _setup_ui(self):
        bg = self.style_info["bg"]
        accent = self.style_info["accent"]
        self.setStyleSheet(f"""
            PanelWidget {{
                background-color: {bg};
                border: 2px solid {accent};
                border-radius: 12px;
            }}
            PanelWidget:hover {{
                border: 2px solid #ffffff;
            }}
        """)
        self.setCursor(Qt.PointingHandCursor)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(8)

        # Icon + title row
        title_row = QHBoxLayout()
        icon_lbl = QLabel(self.style_info["icon"])
        icon_lbl.setFont(QFont("Segoe UI Emoji", 20))
        icon_lbl.setStyleSheet("background: transparent; border: none;")

        title_lbl = QLabel(self.style_info["title"])
        title_lbl.setFont(QFont("Segoe UI", 14, QFont.Bold))
        title_lbl.setStyleSheet(f"color: #ffffff; background: transparent; border: none;")

        title_row.addWidget(icon_lbl)
        title_row.addWidget(title_lbl)
        title_row.addStretch()

        # Sub label
        sub_lbl = QLabel(self.style_info["sub"])
        sub_lbl.setFont(QFont("Segoe UI", 10))
        sub_lbl.setStyleSheet("color: #aaaaaa; background: transparent; border: none;")

        # Status dot
        status = QLabel("● LIVE")
        status.setFont(QFont("Segoe UI", 9, QFont.Bold))
        status.setStyleSheet(f"color: {self.style_info['accent']}; background: transparent; border: none;")

        # Hint
        self.hint_lbl = QLabel("Click để phóng to")
        self.hint_lbl.setFont(QFont("Segoe UI", 8))
        self.hint_lbl.setStyleSheet("color: #666666; background: transparent; border: none;")
        self.hint_lbl.setAlignment(Qt.AlignCenter)

        layout.addLayout(title_row)
        layout.addWidget(sub_lbl)
        layout.addStretch()
        layout.addWidget(status)
        layout.addWidget(self.hint_lbl)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.parent_grid:
                self.parent_grid.toggle_panel(self.index)
        super().mousePressEvent(event)

    def set_hint(self, text: str):
        self.hint_lbl.setText(text)


class GridManager(QWidget):
    """
    Quản lý 4 panel trong grid 2x2.
    Khi click 1 panel → phóng to panel đó, ẩn 3 panel còn lại bằng animation.
    """

    ANIM_DURATION = 350  # ms

    def __init__(self):
        super().__init__()
        self.maximized_index = -1   # -1 = không panel nào đang phóng to
        self.panels: list[PanelWidget] = []
        self._setup_ui()

    def _setup_ui(self):
        self.setMinimumSize(700, 500)
        self.setStyleSheet("background-color: #0d0d1a;")

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)

        # ── Header ──────────────────────────────────────────────────
        header = QHBoxLayout()
        title = QLabel("🔒  Security Monitor")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setStyleSheet("color: #ffffff; background: transparent;")

        self.status_bar = QLabel("4 cameras online")
        self.status_bar.setFont(QFont("Segoe UI", 9))
        self.status_bar.setStyleSheet("color: #666666; background: transparent;")

        header.addWidget(title)
        header.addStretch()
        header.addWidget(self.status_bar)
        main_layout.addLayout(header)

        # ── Grid container ──────────────────────────────────────────
        # Dùng 1 QWidget làm container thực sự để tính toán geometry
        self.grid_container = QWidget()
        self.grid_container.setStyleSheet("background: transparent;")
        main_layout.addWidget(self.grid_container, stretch=1)

        # Tạo 4 panels — parent là grid_container (absolute positioning)
        for i, style_info in enumerate(PANEL_STYLES):
            panel = PanelWidget(i, style_info, parent_grid=self)
            panel.setParent(self.grid_container)
            self.panels.append(panel)

        # Layout sau khi widget được show
        QTimer.singleShot(0, self._initial_layout)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        QTimer.singleShot(0, self._relayout)

    def _initial_layout(self):
        self._relayout()
        for p in self.panels:
            p.show()

    def _relayout(self):
        """Tính lại vị trí panels theo trạng thái hiện tại (không animate)."""
        if self.maximized_index >= 0:
            self._set_geometry_maximized(self.maximized_index, animate=False)
        else:
            self._set_geometry_grid(animate=False)

    def _get_grid_rects(self) -> list[QRect]:
        """Trả về 4 QRect theo bố cục 2x2."""
        w = self.grid_container.width()
        h = self.grid_container.height()
        gap = 10
        pw = (w - gap) // 2
        ph = (h - gap) // 2
        return [
            QRect(0,        0,        pw, ph),
            QRect(pw + gap, 0,        pw, ph),
            QRect(0,        ph + gap, pw, ph),
            QRect(pw + gap, ph + gap, pw, ph),
        ]

    def _set_geometry_grid(self, animate: bool = True):
        """Đưa tất cả panels về bố cục 2x2."""
        rects = self._get_grid_rects()
        prev_idx = self.maximized_index
        full = QRect(0, 0, self.grid_container.width(), self.grid_container.height())
        for i, panel in enumerate(self.panels):
            panel.set_hint("Click để phóng to")
            if animate:
                if i == prev_idx:
                    # Panel đang phóng to → animate thu nhỏ từ full về grid
                    panel.show()
                    self._animate_panel(panel, full, rects[i])
                else:
                    # Panel bị ẩn → đặt sẵn đúng vị trí rồi show ngay (không animate)
                    panel.setGeometry(rects[i])
                    panel.show()
            else:
                panel.setGeometry(rects[i])
                panel.show()

    def _set_geometry_maximized(self, idx: int, animate: bool = True):
        """Phóng to panel idx, ẩn NGAY các panel còn lại."""
        full = QRect(0, 0, self.grid_container.width(), self.grid_container.height())
        rects = self._get_grid_rects()
        for i, panel in enumerate(self.panels):
            if i == idx:
                panel.show()
                panel.raise_()
                panel.set_hint("Click để thu nhỏ  ✕")
                if animate:
                    self._animate_panel(panel, rects[idx], full)
                else:
                    panel.setGeometry(full)
            else:
                # Ẩn ngay lập tức — không animate panel phụ khi phóng to
                panel.setGeometry(rects[i])
                panel.hide()

    def _animate_panel(self, panel: QWidget,
                       start: QRect, end: QRect,
                       on_finish=None):
        """Tạo QPropertyAnimation di chuyển + resize panel."""
        anim = QPropertyAnimation(panel, b"geometry")
        anim.setDuration(self.ANIM_DURATION)
        anim.setStartValue(start)
        anim.setEndValue(end)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        if on_finish:
            anim.finished.connect(on_finish)
        # Giữ reference để tránh bị GC thu hồi
        if not hasattr(self, '_anims'):
            self._anims = []
        self._anims.append(anim)
        anim.finished.connect(lambda a=anim: self._anims.remove(a) if a in self._anims else None)
        panel.raise_()
        anim.start()

    def toggle_panel(self, idx: int):
        """Click vào panel idx: phóng to hoặc thu nhỏ."""
        if self.maximized_index == idx:
            # Đang phóng to → thu nhỏ về grid
            self.maximized_index = -1
            self._set_geometry_grid(animate=True)
            self.status_bar.setText("4 cameras online")
        else:
            # Phóng to panel này
            self.maximized_index = idx
            self._set_geometry_maximized(idx, animate=True)
            title = PANEL_STYLES[idx]["title"]
            self.status_bar.setText(f"Đang xem: {title}  —  Click panel để thu nhỏ")


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Dark palette cho toàn app
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("#0d0d1a"))
    palette.setColor(QPalette.WindowText, QColor("#ffffff"))
    app.setPalette(palette)

    window = GridManager()
    window.setWindowTitle("Panel Maximize Demo")
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()