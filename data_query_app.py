"""
data_query_app.py  –  Controller cho data_query.ui  (PySide6)
Yêu cầu : pip install PySide6
Chạy    : python data_query_app.py
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidgetItem, QHeaderView,
    QLineEdit, QPushButton, QTableWidget, QLabel
)
from PySide6.QtCore import Qt, QFile, QIODevice
from PySide6.QtUiTools import QUiLoader


# ─────────────────────────────────────────────
#  Dữ liệu mẫu  (No., Type, Name, Date)
# ─────────────────────────────────────────────
SAMPLE_DATA = [
    (1,  "Invoice",   "INV-2024-001",  "2024-01-05"),
    (2,  "Receipt",   "REC-2024-001",  "2024-01-08"),
    (3,  "Invoice",   "INV-2024-002",  "2024-01-15"),
    (4,  "Contract",  "CTR-2024-001",  "2024-01-20"),
    (5,  "Report",    "RPT-2024-Q1",   "2024-03-31"),
    (6,  "Invoice",   "INV-2024-003",  "2024-04-02"),
    (7,  "Receipt",   "REC-2024-002",  "2024-04-10"),
    (8,  "Contract",  "CTR-2024-002",  "2024-05-01"),
    (9,  "Report",    "RPT-2024-Q2",   "2024-06-30"),
    (10, "Invoice",   "INV-2024-004",  "2024-07-12"),
    (11, "Memo",      "MEM-2024-001",  "2024-07-18"),
    (12, "Receipt",   "REC-2024-003",  "2024-08-05"),
    (13, "Memo",      "MEM-2024-002",  "2024-08-22"),
    (14, "Contract",  "CTR-2024-003",  "2024-09-01"),
    (15, "Invoice",   "INV-2024-005",  "2024-09-14"),
]

class DataQueryWindow(QMainWindow):
    def __init__(self, ui_widget):
        super().__init__()

        # PySide6: QUiLoader trả về QWidget thông thường.
        # Nhúng vào QMainWindow làm centralWidget.
        self.setCentralWidget(ui_widget)
        self.setWindowTitle(ui_widget.windowTitle())
        self.resize(ui_widget.size())
        self.setStyleSheet(ui_widget.styleSheet())

        # Tham chiếu các widget con qua findChild
        self.lineEdit_search: QLineEdit   = ui_widget.findChild(QLineEdit,    "lineEdit_search")
        self.btn_clear:       QPushButton = ui_widget.findChild(QPushButton,  "btn_clear")
        self.tableWidget:     QTableWidget = ui_widget.findChild(QTableWidget, "tableWidget")
        self.label_info:      QLabel      = ui_widget.findChild(QLabel,       "label_info")

        self._setup_table()
        self._load_data(SAMPLE_DATA)
        self._connect_signals()

        # Ẩn nút clear lúc khởi động
        self.btn_clear.hide()

    # ── Cấu hình header bảng ───────────────────────────────────────
    def _setup_table(self):
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

    # ── Nạp dữ liệu vào bảng ───────────────────────────────────────
    def _load_data(self, records: list):
        table = self.tableWidget
        table.setSortingEnabled(False)  # Tắt sort khi insert để tránh lỗi thứ tự
        table.setRowCount(0)

        for row_idx, (no, rtype, name, date) in enumerate(records):
            table.insertRow(row_idx)
            values = [str(no), rtype, name, date]
            for col_idx, value in enumerate(values):
                item = QTableWidgetItem(value)
                if col_idx == 0:
                    item.setTextAlignment(Qt.AlignCenter)
                else:
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)
                table.setItem(row_idx, col_idx, item)

        table.setSortingEnabled(True)
        self._update_info(len(records), len(SAMPLE_DATA))

    # ── Kết nối tín hiệu ───────────────────────────────────────────
    def _connect_signals(self):
        self.lineEdit_search.textChanged.connect(self._on_search_changed)
        self.btn_clear.clicked.connect(self._on_clear_clicked)

    # ── Tìm kiếm real-time theo cột Type ──────────────────────────
    def _on_search_changed(self, keyword: str):
        keyword = keyword.strip()
        if keyword:
            self.btn_clear.show()
            filtered = [
                row for row in SAMPLE_DATA
                if keyword.lower() in row[1].lower()  # row[1] = Type
            ]
        else:
            self.btn_clear.hide()
            filtered = SAMPLE_DATA

        self._load_data(filtered)

    # ── Xoá ô tìm kiếm ────────────────────────────────────────────
    def _on_clear_clicked(self):
        self.lineEdit_search.clear()
        self.lineEdit_search.setFocus()

    # ── Cập nhật nhãn thông tin ────────────────────────────────────
    def _update_info(self, shown: int, total: int):
        if shown == total:
            self.label_info.setText(f"Showing all {total} records")
        else:
            self.label_info.setText(f"Found {shown} / {total} records")
        self.statusBar().showMessage(
            f"  {shown} record(s) displayed  •  Search by Type column"
        )


# ── Load file .ui bằng QUiLoader của PySide6 ──────────────────────
def load_ui(path: str):
    loader = QUiLoader()
    file = QFile(path)
    if not file.open(QIODevice.OpenModeFlag.ReadOnly):
        raise FileNotFoundError(f"Không mở được file UI: {path}")
    widget = loader.load(file)
    file.close()
    if widget is None:
        raise RuntimeError(f"QUiLoader không load được: {path}")
    return widget


# ── Entry point ────────────────────────────────────────────────────
def main():
    app = QApplication(sys.argv)
    ui_widget = load_ui("data_query.ui")
    window = DataQueryWindow(ui_widget)
    window.show()
    sys.exit(app.exec())   # PySide6 dùng exec() không phải exec_()


if __name__ == "__main__":
    main()