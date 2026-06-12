import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLineEdit, QPushButton, QLabel, QFrame, QScrollArea
)
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QFont

CLIENT_ID     = "l7f810636265dc454c906aa1d02955a485"
CLIENT_SECRET = "661fea108d64429b939eefe6950d5557"

STATUS_MAP = {
    "DL": ("delivered", "Đã giao hàng"),
    "OD": ("transit",   "Đang giao hàng"),
    "IT": ("transit",   "Đang vận chuyển"),
    "DP": ("transit",   "Đã khởi hành"),
    "AR": ("transit",   "Đã đến trạm"),
    "PU": ("transit",   "Đã lấy hàng"),
    "PX": ("pending",   "Chờ lấy hàng"),
    "OC": ("pending",   "Đơn hàng đã tạo"),
}

STATUS_COLORS = {
    "transit":   {"bg": "#E6F1FB", "fg": "#0C447C"},
    "delivered": {"bg": "#EAF3DE", "fg": "#27500A"},
    "pending":   {"bg": "#FAEEDA", "fg": "#633806"},
}


def parse_fedex_response(raw: dict) -> dict:
    track = (
        raw.get("output", {}).get("completeTrackResults", [{}])[0].get("trackResults", [{}])[0]
    )

    status_detail = track.get("latestStatusDetail", {})
    code = status_detail.get("code", "")
    status_key, status_text = STATUS_MAP.get(code, ("pending", status_detail.get("description", "Không rõ")))

    def get_city(loc_key):
        try:
            addr = track[loc_key]["locationContactAndAddress"]["address"]
            city = addr.get("city", "")
            country = addr.get("countryCode", "")
            return f"{city}, {country}" if city else "—"
        except (KeyError, TypeError):
            return "—"

    origin = get_city("originLocation")
    dest   = get_city("destinationLocation")

    eta = "—"
    for d in track.get("dateAndTimes", []):
        if d.get("type") == "ESTIMATED_DELIVERY":
            eta = d.get("dateTime", "")[:10]
            break

    service = track.get("serviceDetail", {}).get("description", "FedEx")

    weight = "—"
    try:
        w = track["packageDetails"]["physicalPackagingType"]
        weight = w
    except (KeyError, TypeError):
        pass

    events = []
    for ev in track.get("scanEvents", []):
        desc = ev.get("eventDescription", "")
        date = ev.get("date", "")[:16].replace("T", " · ")
        loc  = ev.get("scanLocation", {}).get("city", "")
        meta = f"{date} · {loc}" if loc else date
        events.append((desc, meta, "done"))

    if events:
        events[0] = (events[0][0], events[0][1], "active")

    return {
        "status":      status_key,
        "status_text": status_text,
        "from":        origin,
        "to":          dest,
        "service":     service,
        "weight":      weight,
        "eta":         eta,
        "events":      events,
    }

class TrackWorker(QThread):
    result = Signal(dict)
    error  = Signal(str)

    def __init__(self, tracking_number: str):
        super().__init__()
        self.tracking_number = tracking_number.strip()

    def run(self):
        try:
            token_res = requests.post(
                "https://apis-sandbox.fedex.com/oauth/token",
                data={
                    "grant_type":    "client_credentials",
                    "client_id":     CLIENT_ID,
                    "client_secret": CLIENT_SECRET,
                },
                timeout=10
            )
            token_res.raise_for_status()
            token = token_res.json()["access_token"]

            res = requests.post(
                "https://apis-sandbox.fedex.com/track/v1/trackingnumbers",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type":  "application/json",
                    "X-locale":      "en_US",
                },
                json={
                    "trackingInfo": [{
                        "trackingNumberInfo": {
                            "trackingNumber": self.tracking_number
                        }
                    }],
                    "includeDetailedScans": True
                },
                timeout=10
            )
            res.raise_for_status()
            parsed = parse_fedex_response(res.json())
            self.result.emit(parsed)

        except requests.HTTPError as e:
            self.error.emit(f"HTTP {e.response.status_code}: {e.response.text[:200]}")
        except Exception as e:
            self.error.emit(str(e))

class FedExTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FedEx Tracker")
        self.setMinimumSize(520, 520)
        self._build_ui()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        title = QLabel("FedEx Shipment Tracker")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        layout.addWidget(title)

        row = QHBoxLayout()
        self.input = QLineEdit()
        self.input.setPlaceholderText("Nhập tracking number...")
        self.input.setFixedHeight(36)
        self.input.returnPressed.connect(self._track)

        self.btn = QPushButton("Tra cứu")
        self.btn.setFixedHeight(36)
        self.btn.clicked.connect(self._track)

        row.addWidget(self.input)
        row.addWidget(self.btn)
        layout.addLayout(row)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        self.result_widget = QWidget()
        self.result_layout = QVBoxLayout(self.result_widget)
        self.result_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll.setWidget(self.result_widget)
        layout.addWidget(scroll)

        self._show_placeholder()

    def _clear_result(self):
        while self.result_layout.count():
            item = self.result_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def _show_placeholder(self):
        lbl = QLabel("Nhập tracking number và nhấn Tra cứu")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl.setStyleSheet("color: gray; font-size: 14px; padding: 40px;")
        self.result_layout.addWidget(lbl)

    def _track(self):
        num = self.input.text().strip()
        if not num:
            return
        self.btn.setEnabled(False)
        self.btn.setText("Đang tìm...")
        self._clear_result()

        loading = QLabel("⏳ Đang kết nối FedEx API...")
        loading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        loading.setStyleSheet("color: gray; font-size: 13px; padding: 20px;")
        self.result_layout.addWidget(loading)

        self.worker = TrackWorker(num)
        self.worker.result.connect(self._on_success)
        self.worker.error.connect(self._on_error)
        self.worker.start()

    def _on_success(self, data: dict):
        import json
        print("=== FedEx Response ===")
        print(json.dumps(data, indent=2, ensure_ascii=False))
        print("=====================")
        self._clear_result()
        colors = STATUS_COLORS.get(data["status"], STATUS_COLORS["pending"])

        badge = QLabel(f"  {data['status_text']}  ")
        badge.setFixedHeight(28)
        badge.setStyleSheet(
            f"background: {colors['bg']}; color: {colors['fg']};"
            "border-radius: 6px; font-size: 13px; font-weight: bold; padding: 0 8px;"
        )
        self.result_layout.addWidget(badge)

        card = QFrame()
        card.setStyleSheet(
            "background: #f9f9f9; border: 1px solid #e0e0e0;"
            "border-radius: 10px; padding: 12px;"
        )
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(6)

        for label, value in [
            ("Từ",           data["from"]),
            ("Đến",          data["to"]),
            ("Dịch vụ",      data["service"]),
            ("Khối lượng",   data["weight"]),
            ("Dự kiến giao", data["eta"]),
        ]:
            rw = QWidget()
            rl = QHBoxLayout(rw)
            rl.setContentsMargins(0, 0, 0, 0)
            lbl = QLabel(f"{label}:")
            lbl.setStyleSheet("color: gray; font-size: 13px;")
            lbl.setFixedWidth(100)
            val = QLabel(value)
            val.setStyleSheet("font-size: 13px; font-weight: bold;")
            rl.addWidget(lbl)
            rl.addWidget(val)
            rl.addStretch()
            card_layout.addWidget(rw)

        self.result_layout.addWidget(card)

        if data["events"]:
            tl_title = QLabel("Lịch trình vận chuyển")
            tl_title.setStyleSheet("font-size: 13px; color: gray; margin-top: 8px;")
            self.result_layout.addWidget(tl_title)

            for event_text, meta, state in data["events"]:
                ef = QFrame()
                el = QHBoxLayout(ef)
                el.setContentsMargins(0, 0, 0, 0)
                el.setSpacing(10)

                dot = QLabel("●")
                dot_color = "#185FA5" if state == "active" else "#3B6D11"
                dot.setStyleSheet(f"color: {dot_color}; font-size: 10px;")
                dot.setFixedWidth(12)

                tc = QWidget()
                tl = QVBoxLayout(tc)
                tl.setContentsMargins(0, 0, 0, 0)
                tl.setSpacing(2)
                tl.addWidget(QLabel(event_text))
                meta_lbl = QLabel(meta)
                meta_lbl.setStyleSheet("font-size: 11px; color: gray;")
                tl.addWidget(meta_lbl)

                el.addWidget(dot, alignment=Qt.AlignmentFlag.AlignTop)
                el.addWidget(tc)
                self.result_layout.addWidget(ef)

        self.result_layout.addStretch()
        self._reset_btn()

    def _on_error(self, message: str):
        self._clear_result()
        lbl = QLabel(f"❌ {message}")
        lbl.setStyleSheet("color: #A32D2D; font-size: 13px; padding: 12px;")
        lbl.setWordWrap(True)
        lbl.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        lbl.setMinimumHeight(120)
        lbl.setMaximumWidth(460)
        self.result_layout.addWidget(lbl)
        self.result_layout.addStretch()
        self._reset_btn()

    def _reset_btn(self):
        self.btn.setEnabled(True)
        self.btn.setText("Tra cứu")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FedExTracker()
    window.show()
    sys.exit(app.exec())