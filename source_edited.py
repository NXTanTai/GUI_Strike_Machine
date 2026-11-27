# pyside6-uic tech_link_theme_edited.ui -o tech_link_theme_edited_ui.py
# pyside6-rcc Icon.qrc -o Icon_rc.py
# pyside6-rcc icons.qrc -o icons_rc.py

# pyside6-lupdate tech_link_theme_edited.ui -ts tech_link_theme_en.ts
# pyside6-lupdate tech_link_theme_edited.ui -ts tech_link_theme_vn.ts
# pyside6-lupdate tech_link_theme_edited.ui -ts tech_link_theme_cn.ts

import sys
import os
import time 
import pandas as pd
import io
import msoffcrypto
import logging
import sqlite3
import queue
import threading
import subprocess
import tempfile
import psutil
import webbrowser
import json
import csv
from PySide6.QtCore import (
    Qt, QTimer, QObject, Slot,
    QTime, QSettings, QDateTime,
    QEvent, QThread, QEasingCurve, 
    QTranslator
)
from PySide6.QtGui import (
    QFont, 
    QPalette
)
from PySide6.QtWidgets import (
    QHeaderView, QAbstractSpinBox, QStyledItemDelegate,
    QMainWindow, QApplication, QLineEdit,
    QFileDialog, QTableWidget, QTableWidgetItem,
    QAbstractButton, QLabel
)
from typing import List, Optional, Tuple, Any
from pathlib import Path
from datetime import datetime
from tech_link_theme_edited_ui import Ui_MainWindow
from Custom_Widgets import * #type: ignore
from Custom_Chart_Widgets import CustomChartWidget
from message_box import LightThemeMessageBox as ltmessage
from console_window import ConsoleWindow
from password_dialog import *
from Data_Simulator import DataSimulator
from PLC_READ_MODULE import PLCRead, PLCReadBlock
from PLC_WRITE_MODULE import PLCWrite
from SERIAL_READ_MODULE import HYFWSerialRead
from export_excel_worker import ExportWorker
from db_layout_parser import parse_db_layout, DTYPE_SIZE
from LogFileHandler import MonthlyRotatingFileHandler

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"
os.environ["QT_FONT_DPI"] = "96" # 1024x768

BASE_DIR = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent

settings_path = str(BASE_DIR / "settings.ini")

def fmt_hms(sec: int) -> str:
    h, r = divmod(int(sec), 3600)
    return f"{h:02d}:{r // 60:02d}:{r % 60:02d}"

def fmt_hm(sec: int) -> str:
    h, r = divmod(int(sec), 3600)
    return f"{h} h {r // 60:02d} m"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS # type: ignore
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def install_clear_on_focus(widget):
    class FocusSelectFilter(QObject):
        def eventFilter(self, obj, event):
            if event.type() == QEvent.FocusIn:   # type: ignore
                if isinstance(widget, QAbstractSpinBox):
                    QTimer.singleShot(0, widget.lineEdit().selectAll)
                elif isinstance(widget, QLineEdit):
                    QTimer.singleShot(0, widget.selectAll)
            return False
 
    f = FocusSelectFilter(widget)
    widget.installEventFilter(f)

def get_exe_dir():
    """Lấy thư mục chứa file .exe (hoặc .py khi dev)"""
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent
    else:
        return Path(__file__).parent

SIMULATE = (get_exe_dir() / "simulate.txt").is_file()
PLC_SIM = (get_exe_dir() / "plcsim.txt").is_file()

EXCEL_PASSWORD = 'tl@12345'
PLC_STRING_MAX_CHARS = 254  # độ dài tối đa của tag STRING trong DB (Alarm_Info = String[254])

EXPECTED_ROW_NAMES = [
    "Cycle Setting",
    "Oil Start time",
    "Oil End time",
    "Air Filling time",
    "Air Holding time",
    "Air Bleeding time",
    "Pressure Setting",
    "Temperature Setting",
    "High Alarm Value",
    "Low Alarm Value",
    "Offset Front",
    "Offset Mid",
    "Offset End",
]

SPINBOX_PLC_MAP = {
    # ── Group A ───────────────────────────────────────────────────────────────
    "pressure_sv_a_5":  ("P1_PressureSetting",  None),
    "pressure_sv_a_6":  ("P1_Air_FillingTime",  "sec_to_msec"),
    "pressure_sv_a_7":  ("P1_Air_HoldingTime",  "sec_to_msec"),
    "pressure_sv_a_8":  ("P1_Air_ReleaseTime",  "sec_to_msec"),
    "pressure_sv_a_9":  ("P1_Oil_Start_Time",   "sec_to_msec"),
    "pressure_sv_a_10": ("P1_Oil_End_Time",      "sec_to_msec"),
    "pressure_sv_a_11": ("P1_CountTimes",        None),
 
    # ── Group B ───────────────────────────────────────────────────────────────
    "pressure_sv_b_5":  ("P2_PressureSetting",  None),
    "pressure_sv_b_6":  ("P2_Air_FillingTime",  "sec_to_msec"),
    "pressure_sv_b_7":  ("P2_Air_HoldingTime",  "sec_to_msec"),
    "pressure_sv_b_8":  ("P2_Air_ReleaseTime",  "sec_to_msec"),
    "pressure_sv_b_9":  ("P2_Oil_Start_Time",   "sec_to_msec"),
    "pressure_sv_b_10": ("P2_Oil_End_Time",      "sec_to_msec"),
    "pressure_sv_b_11": ("P2_CountTimes",        None),
 
    # ── Group C ───────────────────────────────────────────────────────────────
    "pressure_sv_c_5":  ("P3_PressureSetting",  None),
    "pressure_sv_c_6":  ("P3_Air_FillingTime",  "sec_to_msec"),
    "pressure_sv_c_7":  ("P3_Air_HoldingTime",  "sec_to_msec"),
    "pressure_sv_c_8":  ("P3_Air_ReleaseTime",  "sec_to_msec"),
    "pressure_sv_c_9":  ("P3_Oil_Start_Time",   "sec_to_msec"),
    "pressure_sv_c_10": ("P3_Oil_End_Time",      "sec_to_msec"),
    "pressure_sv_c_11": ("P3_CountTimes",        None),
 
    # ── Temperature SV ────────────────────────────────────────────────────────
    "t0_sv":            ("T0_TemperatureSetting", "fah_to_cel"),
 
    # ── High Alarm ────────────────────────────────────────────────────────────
    "t0_h_alm_value":   ("T0_TempLimitHIGH",    "fah_to_cel"),
    "at_h_alm_value":   ("P1_TempLimitHIGH",    "fah_to_cel"),
    "bt_h_alm_value":   ("P2_TempLimitHIGH",    "fah_to_cel"),
    "ct_h_alm_value":   ("P3_TempLimitHIGH",    "fah_to_cel"),
 
    # ── Low Alarm ─────────────────────────────────────────────────────────────
    "t0_l_alm_value":   ("T0_TempLimitLOW",     "fah_to_cel"),
    "at_l_alm_value":   ("P1_TempLimitLOW",     "fah_to_cel"),
    "bt_l_alm_value":   ("P2_TempLimitLOW",     "fah_to_cel"),
    "ct_l_alm_value":   ("P3_TempLimitLOW",     "fah_to_cel"),
 
    # ── Offset ────────────────────────────────────────────────────────────────
    "t0_offset_value":      ("T0_TempOffset",   "fah_to_cel"),
    "at_t1_offset_value":   ("P1_Temp1Offset",  "fah_to_cel"),
    "at_t2_offset_value":   ("P1_Temp2Offset",  "fah_to_cel"),
    "at_t3_offset_value":   ("P1_Temp3Offset",  "fah_to_cel"),
    "bt_t1_offset_value":   ("P2_Temp1Offset",  "fah_to_cel"),
    "bt_t2_offset_value":   ("P2_Temp2Offset",  "fah_to_cel"),
    "bt_t3_offset_value":   ("P2_Temp3Offset",  "fah_to_cel"),
    "ct_t1_offset_value":   ("P3_Temp1Offset",  "fah_to_cel"),
    "ct_t2_offset_value":   ("P3_Temp2Offset",  "fah_to_cel"),
    "ct_t3_offset_value":   ("P3_Temp3Offset",  "fah_to_cel"),

    # ── Tube (heater) limit ───────────────────────────────────────────────────
    "at_tube_sv":           ("P1_TempLimitHeater", "fah_to_cel"),
    "bt_tube_sv":           ("P2_TempLimitHeater", "fah_to_cel"),
    "ct_tube_sv":           ("P3_TempLimitHeater", "fah_to_cel"),
}

TEMP_SV_MIRROR = {
    "pressure_sv_a_1": ("P1_TemperatureSetting", "at_sv"),
    "pressure_sv_b_1": ("P2_TemperatureSetting", "bt_sv"),
    "pressure_sv_c_1": ("P3_TemperatureSetting", "ct_sv"),
}

TEMP_SV_REVERSE_MIRROR = {
    "at_sv": "pressure_sv_a_1",
    "bt_sv": "pressure_sv_b_1",
    "ct_sv": "pressure_sv_c_1",
}

CLEAR_GROUP_CONFIG = {
    "A": {"guard_widgets": ("refuel_btn_a","vacuum_btn_a","heat_btn_a"),
          "pressure_sv_obj": "pressure_a_sv_obj", "temp_sv_index": 1,
          "list_import": "list_for_import_a", "plc_prefix": "P1"},
    "B": {"guard_widgets": ("refuel_btn_b","vacuum_btn_b","heat_btn_b"),
          "pressure_sv_obj": "pressure_b_sv_obj", "temp_sv_index": 2,
          "list_import": "list_for_import_b", "plc_prefix": "P2"},
    "C": {"guard_widgets": ("refuel_btn_c","vacuum_btn_c","heat_btn_c"),
          "pressure_sv_obj": "pressure_c_sv_obj", "temp_sv_index": 3,
          "list_import": "list_for_import_c", "plc_prefix": "P3"},
}

CLEAR_GROUP_PLC_TAGS = (
    "CountTimes", "Oil_Start_Time", "Oil_End_Time", "Air_FillingTime",
    "Air_HoldingTime", "Air_ReleaseTime", "PressureSetting", "TemperatureSetting",
)

class SafePipeLogHandler(logging.Handler):
    def __init__(self, process, stdin_lock=None):
        super().__init__()
        self._process = process
        self._queue = queue.Queue(maxsize=500)
        self._broken = False
        self._stdin_lock = stdin_lock or threading.Lock()
        self._worker = threading.Thread(target=self._worker_thread, daemon=True)
        self._worker.start()

    def _worker_thread(self):
        while True:
            try:
                record = self._queue.get(timeout=0.5)
                if record is None:  # Stop signal
                    break
                if self._broken or not self._process or self._process.poll() is not None:
                    continue

                msg = self.format(record) + "\n"
                with self._stdin_lock:
                    self._process.stdin.write(msg)
                    self._process.stdin.flush()
            except queue.Empty:
                continue
            except Exception:
                self._broken = True

    def emit(self, record):
        try:
            if not self._broken:
                self._queue.put_nowait(record)
        except queue.Full:
            pass  # Bỏ qua nếu queue đầy

    def close(self):
        try:
            self._queue.put(None, timeout=0.5)  # Stop worker
            if self._worker.is_alive():
                self._worker.join(timeout=1)
        except:
            pass
        try:
            if self._process and self._process.stdin:
                self._process.stdin.close()
        except:
            pass
        super().close()

class BackgroundDelegate(QStyledItemDelegate):
    def paint(self, painter: QPainter, option, index):
        bg = index.data(Qt.BackgroundRole)  # type: ignore
        if bg:
            painter.fillRect(option.rect, bg)
            option.palette.setColor(QPalette.ColorRole.Base, bg)
        super().paint(painter, option, index)

ALARM_ERROR   = "Error"
ALARM_WARNING = "Warning"
ALARM_TYPE_COLORS = {
    ALARM_ERROR:   "#DC2626",
    ALARM_WARNING: "#D9C706",
}

class NotificationBadge(QLabel):
    """
    Badge đỏ hiển thị số lượng (kiểu chuông thông báo) ở góc trên bên phải icon của button.
    """
    def __init__(self, button: QAbstractButton, icon_left: int = 20):
        super().__init__(button)
        self._button    = button
        self._icon_left = icon_left  # padding-left của button (vị trí x của icon)
        self.setAlignment(Qt.AlignCenter)  # type: ignore
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setStyleSheet(
            "QLabel {"
            "  background-color: rgb(239, 68, 68);"
            "  color: white;"
            "  border-radius: 9px;"
            "  font-size: 10pt;"
            "  font-weight: bold;"
            "  padding: 0px 5px;"
            "}"
        )
        self.setFixedHeight(18)
        self.hide()
        button.installEventFilter(self)

    def set_count(self, count: int):
        if count <= 0:
            self.hide()
            return
        self.setText("99+" if count > 99 else str(count))
        self.setFixedWidth(max(18, self.sizeHint().width()))
        self._reposition()
        self.show()
        self.raise_()

    def _reposition(self):
        icon = self._button.iconSize()
        icon_top = (self._button.height() - icon.height()) // 2
        x = self._icon_left + icon.width() - self.width() // 2
        y = max(0, icon_top - self.height() // 2)
        self.move(x, y)

    def eventFilter(self, obj, event):
        if obj is self._button and event.type() == QEvent.Type.Resize:
            self._reposition()
        return super().eventFilter(obj, event)

class StrikeMachine(QMainWindow):
    _search_result_ready    = Signal(object)
    hide_loading            = Signal()
    show_loading            = Signal()

    def __init__(self, on_hide_loading=None, on_show_loading=None, info_system=None, plc_queue=None, parent=None, scale_factor: float = 1.0):
        super().__init__(parent)
        if on_hide_loading:
            self.hide_loading.connect(on_hide_loading)
        if on_show_loading:
            self.show_loading.connect(on_show_loading)
        self._info_system = info_system
        self._plc_queue = plc_queue
        self.app_settings = QSettings(
            settings_path,
            QSettings.Format.IniFormat
        )
        # self.logger.info("INIT SETTINGS:", self.app_settings.format())
        self._find_stk_mch_folder()
        self._init_logger()
        self.logger.info("----------------------------------------------------------------------------")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        self._scale_factor = scale_factor
        _BASE_W, _BASE_H = 1280, 960
        target_w = round(_BASE_W * scale_factor)
        target_h = round(_BASE_H * scale_factor)
        self.resize(target_w, target_h)
        self._scale_icons(scale_factor)
        self._scale_button_boxes(scale_factor)
        self._scale_fonts(scale_factor)

        self._init_app_data()
        self._init_db_layout_and_size()
        self._init_AI_actual_db()
        self._init_timer()
        self._init_group_object()
        self._init_list_unit()
        self._create_charts()
        self._init_history_database()
        self._init_alarm_database()
        self._init_table_list_history()
        self._paint_pv_obj("#E53935")
        self._paint_sv_obj("#43A047")
        self._setup_btn_signals()
        self._setup_plc_threads(SIMULATE)
        self._setup_serial_threads()
        self._translator = QTranslator()
        self._init_screen()

    def _scale_icons(self, factor: float = 0.8) -> None:
        """Scale iconSize của mọi QAbstractButton theo factor. Chạy 1 lần sau setupUi."""
        for btn in self.findChildren(QAbstractButton):
            size = btn.iconSize()
            if size.width() <= 0 or size.height() <= 0:
                continue
            new_w = max(1, round(size.width()  * factor))
            new_h = max(1, round(size.height() * factor))
            btn.setIconSize(QSize(new_w, new_h))

    def _scale_button_boxes(self, factor: float = 0.8) -> None:
        """
        Scale minimumSize/maximumSize của các nút có icon theo factor
        để khung nút co theo cùng tỉ lệ với icon
        """
        QWIDGETSIZE_MAX = 16777215

        def _scaled(v: int) -> int:
            if v <= 0 or v >= QWIDGETSIZE_MAX:
                return v
            return max(1, round(v * factor))

        for btn in self.findChildren(QAbstractButton):
            if btn.icon().isNull():
                continue
            min_size = btn.minimumSize()
            max_size = btn.maximumSize()
            btn.setMinimumSize(QSize(_scaled(min_size.width()), _scaled(min_size.height())))
            btn.setMaximumSize(QSize(_scaled(max_size.width()), _scaled(max_size.height())))

    def _scale_fonts(self, factor: float = 0.8) -> None:
        """
        Scale pointSize font của mọi widget theo factor
        Chạy 1 lần sau setupUi
        """
        for widget in self.findChildren(QWidget):
            f = widget.font()
            pt = f.pointSize()
            if pt <= 0:
                continue
            new_pt = max(1, round(pt * factor))
            if new_pt == pt:
                continue
            f.setPointSize(new_pt)
            widget.setFont(f)

    def _init_screen(self):
        self._set_style()
        self.ui.home_page_btn.click()
        self.ui.clear_history_search.hide()
        self._set_time_search_data_start_edit()
        self._set_time_search_data_end_edit()
        self._search_result_ready.connect(
            self._on_search_fetched,
            Qt.ConnectionType.QueuedConnection
        )
        self.ui.stacked_list_history_page.setCurrentIndex(0)

    def _set_style(self):
        self._i_o_group_1_style()
        self._i_o_group_2_style()
        self._i_o_group_3_style()
        self._i_o_group_4_style()
        self._back_page_widget_styles()
        
    def _i_o_group_1_style(self):
        self.ui.i_o_group_1.setStyleSheet("""
            QWidget{
                border: 2px solid #E5E5E5; 
                border-radius: 20px;
            }
            QGroupBox {
                border: 2px solid #E5E5E5;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #374151;
            }

            QLabel {
                color: #D12323;
                border: none;
            }

            QSpinBox {
                border: 1px solid #D1D5DB;
                border-radius: 6px;
                padding: 8px 12px;
                background-color: #F9FAFB;
            }
            QSpinBox:focus {
                border: 2px solid #0B7EC8;
                background-color: white;
            }

            QLineEdit {
                border: 1px solid #D1D5DB;
                border-radius: 6px;
                padding: 8px 12px;
                background-color: #F9FAFB;
            }
            QLineEdit:focus {
                border: 2px solid #0B7EC8;
                background-color: white;
            }
        """)

    def _i_o_group_2_style(self):
        self.ui.i_o_group_2.setStyleSheet("""
            QGroupBox {
                border: 2px solid #E5E5E5;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #374151;
            }

            QLabel {
                color: #D12323;
                border: none;
            }

            QSpinBox {
                border: 1px solid #D1D5DB;
                border-radius: 6px;
                padding: 8px 12px;
                background-color: #F9FAFB;
            }
            QSpinBox:focus {
                border: 2px solid #0B7EC8;
                background-color: white;
            }

            QLineEdit {
                border: 1px solid #D1D5DB;
                border-radius: 6px;
                padding: 8px 12px;
                background-color: #F9FAFB;
            }
            QLineEdit:focus {
                border: 2px solid #0B7EC8;
                background-color: white;
            }
            """)

    def _i_o_group_3_style(self):
        self.ui.i_o_group_3.setStyleSheet("""
            QGroupBox {
                border: 2px solid #E5E5E5;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #374151;
            }

            QLabel {
                border: none;
                color: #E6AC2E;
            }

            QDoubleSpinBox {
                border: 3px solid #E5E5E5; 
                border-radius: 10px;
                color: #10B981;
                background-color: white;
            }
            QLineEdit {
                border: 1px solid #D1D5DB;
                border-radius: 6px;
                padding: 8px 12px;
                background-color: #F9FAFB;
            }
            QLineEdit:focus {
                border: 2px solid #0B7EC8;
                background-color: white;
            }
            """)

    def _i_o_group_4_style(self):
        self.ui.i_o_group_4.setStyleSheet("""
            QGroupBox {
                border: 2px solid #E5E5E5;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #374151;
            }

            QLabel {
                border: none;
                color: #E6AC2E;
            }

            QDoubleSpinBox {
                border: 3px solid #E5E5E5; 
                border-radius: 10px;
                color: #10B981;
                background-color: white;
            }
            QLineEdit {
                border: 1px solid #D1D5DB;
                border-radius: 6px;
                padding: 8px 12px;
                background-color: #F9FAFB;
            }
            QLineEdit:focus {
                border: 2px solid #0B7EC8;
                background-color: white;
            }
            """)

    def _back_page_widget_styles(self):
        self.ui.back_page_widget.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #0B7EC8;
                border: 2px solid #0B7EC8;
                padding: 4px 4px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #F0F9FF;
            }
            QPushButton:pressed {
                background-color: #E0F2FE;
            }
        """)

    def _test_marquee_label(self):
        test_text = "Strike Machine System - Running Normally - No Error Detected"
        # test_text = "Hello Hello Hello"
        # self.ui.error_display.setText(test_text)
        # print(f"MarqueeLabel setText: '{self.ui.error_display.text()}' \nWidget visible: {self.ui.error_display.isVisible()} \nWidget size: {self.ui.error_display.size()}")
    
    def _init_AI_actual_db(self):
        self.ai_data_folder = Path(self.stk_mch_folder) / "AI_Training_Data"
        self.ai_data_folder.mkdir(parents=True, exist_ok=True)
        
        # self.fast_buffer = []      # Buffer cho tag nhanh (áp suất, ...)
        # self.slow_buffer = []      # Buffer cho tag chậm
        
        # self.fast_buffer_size = 30    # ~3 giây nếu 100ms
        # self.slow_buffer_size = 10    # ~10 giây nếu 1000ms

        self.data_buffer = []
        self.buffer_size = 10

        self.alarm_data_folder = Path(self.stk_mch_folder) / "Alarm_Log"
        self.alarm_data_folder.mkdir(parents=True, exist_ok=True)

        # Tự động xoá file cũ: lúc khởi động + mỗi 6 giờ (máy chạy liên tục nhiều ngày)
        self._cleanup_old_data_files()
        self._cleanup_timer = QTimer(self)
        self._cleanup_timer.setInterval(6 * 60 * 60 * 1000)
        self._cleanup_timer.timeout.connect(self._cleanup_old_data_files)
        self._cleanup_timer.start()

        # self.logger.info("Fast sampling (100ms) enabled for pressure & critical tags")

    # Thời gian lưu giữ (tháng)
    _AI_DATA_KEEP_MONTHS = 3
    _ALARM_KEEP_MONTHS   = 1

    @staticmethod
    def _months_ago(months: int) -> datetime:
        """Mốc 00:00 cách hôm nay `months` tháng (theo lịch, VD 31/05 - 3 tháng -> 28/02)"""
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        y, m = divmod(today.year * 12 + today.month - 1 - months, 12)
        m += 1
        last_day = (datetime(y + (m == 12), m % 12 + 1, 1) - datetime(y, m, 1)).days
        return today.replace(year=y, month=m, day=min(today.day, last_day))

    def _delete_old_files(self, folder: Path, prefix: str, keep_months: int) -> int:
        """Xoá file <prefix>YYYYMMDD.csv cũ hơn keep_months. Ngày lấy từ tên file,
        tên không đúng định dạng thì dùng thời gian sửa đổi của file."""
        cutoff = self._months_ago(keep_months)
        deleted = 0
        for f in folder.glob(f"{prefix}*.csv"):
            try:
                try:
                    file_date = datetime.strptime(f.stem[len(prefix):], "%Y%m%d")
                except ValueError:
                    file_date = datetime.fromtimestamp(f.stat().st_mtime)
                if file_date < cutoff:
                    f.unlink()
                    deleted += 1
            except Exception as e:
                if self.logger:
                    self.logger.warning("[Cleanup] Không xoá được %s: %s", f, e)
        if deleted and self.logger:
            self.logger.info("[Cleanup] Đã xoá %d file %s* cũ hơn %s trong %s",
                             deleted, prefix, cutoff.strftime("%Y-%m-%d"), folder)
        return deleted

    def _cleanup_old_data_files(self):
        """AI data giữ 3 tháng, alarm log giữ 1 tháng"""
        try:
            self._delete_old_files(self.ai_data_folder, "ai_", self._AI_DATA_KEEP_MONTHS)
            self._delete_old_files(self.alarm_data_folder, "alarm_", self._ALARM_KEEP_MONTHS)
        except Exception as e:
            if self.logger:
                self.logger.error("[Cleanup] Error: %s", e)

    def showEvent(self, event):# type: ignore
        super().showEvent(event)

    def _find_stk_mch_folder(self):
        # print("CURRENT SETTINGS:", self.app_settings.format())
        stk_mch_folder = Path(self.app_settings.value("stk_mch_folder", "C:\\SM_PRD", type=str)) # type: ignore

        if not stk_mch_folder.is_dir():
            self.hide_loading.emit()
            response = ltmessage.question(
                self,
                "Warning",
                "Data Folder not found! Create a new one?"
            )

            if response != ltmessage.Yes:
                self.show_loading.emit()
                return None

            parent_folder = QFileDialog.getExistingDirectory(
                self,
                "Select a Path for SM_PRD folder",
                str(stk_mch_folder.parent),
                QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks # type: ignore
            )

            self.show_loading.emit()
            if not parent_folder:
                return None

            stk_mch_folder = Path(parent_folder) / "SM_PRD"

            stk_mch_folder.mkdir(
                parents=True,
                exist_ok=True
            )

        # ALWAYS SAVE
        self.app_settings.setValue("stk_mch_folder", str(stk_mch_folder))
        self.app_settings.sync()

        self.stk_mch_folder = stk_mch_folder

    def _init_db_layout_and_size(self):
        stk_mch_file = Path(self.stk_mch_folder) / "DB_address"
        file_name = "DB Memory Address Default.xlsx"
        path = os.path.join(stk_mch_file, file_name)
        if not os.path.isfile(path):
            self.hide_loading.emit()
            file_str, _ = QFileDialog.getOpenFileName(
                self,
                "Select DB Address File",
                str(stk_mch_file),
                "Excel Files (*.xlsx *.xls)"
            )
            if not file_str:  # User cancel
                return
            path = Path(file_str)
        
        df = self._read_protected_excel(path, password=EXCEL_PASSWORD)
        if df is None:
            if self.logger:
                self.logger.error("[INIT]: Cannot read DB address file, app will not connect to PLC")
                self.show_loading.emit()
            return

        # Tự nhận diện vùng INPUT / ACTUAL (output) / ERROR (alarm) — hỗ trợ cả file có header (bản cũ)
        # và file chỉ có nhãn vùng Bit_Input / Input / Bit_Output / Output (bản mới)
        try:
            db_dict = parse_db_layout(df, string_max_chars=PLC_STRING_MAX_CHARS, logger=self.logger)
        except Exception as e:
            if self.logger:
                self.logger.error("[INIT]: Invalid DB address file (%s): %s", path, e)
            self.show_loading.emit()
            return

        # File mới không có header -> lấy IP / thời gian ghi đã dùng lần trước
        if db_dict["DB_FORMAT"] == "auto":
            db_dict["ip_plc"]     = self.app_settings.value("plc_ip", db_dict["ip_plc"], type=str)      # type: ignore
            db_dict["write_time"] = self.app_settings.value("plc_write_time", db_dict["write_time"], type=int)  # type: ignore
        else:
            self.app_settings.setValue("plc_ip", db_dict["ip_plc"])
            self.app_settings.setValue("plc_write_time", db_dict["write_time"])
            self.app_settings.sync()

        # Không đọc tag Spare + thu gọn vùng đọc theo tag thực dùng
        db_dict["DB_LAYOUT"] = [t for t in db_dict["DB_LAYOUT"] if not t[0].lower().startswith("spare")]
        self._shrink_read_regions(db_dict)

        if PLC_SIM:
            db_dict["ip_plc"] = "172.16.100.50"

        if self.logger:
            self.logger.info(
                "[INIT]: DB%d (%s) | INPUT [%d..%d) %d tags | ACTUAL [%d..%d) %d tags | ERROR [%d..%d) %d tags | total %d bytes",
                db_dict["db_name"], db_dict["DB_FORMAT"],
                db_dict["offsets_input"], db_dict["offsets_input"] + db_dict["input_size"], len(db_dict["DB_REGIONS"]["INPUT"]),
                db_dict["offsets_data"],  db_dict["offsets_data"]  + db_dict["data_size"],  len(db_dict["DB_REGIONS"]["ACTUAL"]),
                db_dict["offsets_error"], db_dict["offsets_error"] + db_dict["error_size"], len(db_dict["DB_REGIONS"]["ERROR"]),
                db_dict["DB_TOTAL_BYTES"],
            )

        self.db_dict = db_dict
        self._gui_update_connection_group(stk_mch_file)

    @staticmethod
    def _shrink_read_regions(db_dict: dict) -> None:
        """
        Tính lại [offset, size) từng vùng đọc CHỈ theo tag thực dùng (đã bỏ Spare).

        PLC PDU 240 → mỗi request tối đa 222 byte; vùng lớn hơn bị snap7 tách
        thành nhiều request. Bỏ byte Spare ở đầu/cuối vùng giúp vùng vừa 1
        request (VD INPUT 252 B → 212 B).
        Tag ACTUAL nằm SAU vùng ERROR (nếu có) → tách thành vùng ACTUAL_2.
        """
        def tag_end(dt: str, off: int) -> int:
            return off + (2 + PLC_STRING_MAX_CHARS if dt == "STRING" else DTYPE_SIZE.get(dt, 1))

        region_of = {n: rg for rg, names in db_dict["DB_REGIONS"].items() for n in names}
        spans: dict[str, list[tuple[int, int]]] = {}
        for n, dt, off, _ in db_dict["DB_LAYOUT"]:
            spans.setdefault(region_of.get(n), []).append((off, tag_end(dt, off)))

        def apply(k_off: str, k_size: str, sp: list[tuple[int, int]]) -> None:
            if sp:
                start = min(s for s, _ in sp)
                db_dict[k_off], db_dict[k_size] = start, max(e for _, e in sp) - start

        apply("offsets_input", "input_size", spans.get("INPUT", []))
        apply("offsets_error", "error_size", spans.get("ERROR", []))

        err_start = db_dict["offsets_error"]
        err_end   = err_start + db_dict["error_size"]
        actual    = spans.get("ACTUAL", [])
        has_error = bool(spans.get("ERROR"))
        main = [sp for sp in actual if not has_error or sp[0] < err_start]
        ext  = [sp for sp in actual if has_error and sp[0] >= err_end]
        apply("offsets_data", "data_size", main)

        db_dict["offsets_data_2"] = min(s for s, _ in ext) if ext else 0
        db_dict["data_size_2"]    = (max(e for _, e in ext) - db_dict["offsets_data_2"]) if ext else 0

    def _read_protected_excel(self, path, password=None, sheet_name=None):
        df_dict = None

        if password:
            try:
                with open(path, "rb") as f:
                    office_file = msoffcrypto.OfficeFile(f)
                    office_file.load_key(password=password)
                    decrypted = io.BytesIO()
                    office_file.decrypt(decrypted)
                df_dict = pd.read_excel(decrypted, sheet_name=None, header=None, engine='openpyxl')
            except Exception as e:
                if self.logger:
                    self.logger.warning("[EXCEL]: Encrypted read failed (%s), trying plain read...", e)

        if df_dict is None:
            try:
                df_dict = pd.read_excel(path, sheet_name=None, header=None, engine='openpyxl')
            except Exception as e:
                if self.logger:
                    self.logger.error("[EXCEL]: Cannot read file: %s", e)
                return None

        if sheet_name and sheet_name in df_dict:
            return df_dict[sheet_name]

        return next(iter(df_dict.values()))

    def _gui_update_connection_group(self, path_get):
        self.ui.plc_ip_address_edit.setText(self.db_dict["ip_plc"]) #type: ignore
        self.ui.db_file_path_edit.setText(str(path_get))
        # self.ui.db_number_input.setValue(self.db_dict["db_name"]) #type: ignore
        # self.ui.db_data_size_input.setValue(self.db_dict["DB_TOTAL_BYTES"]) #type: ignore
        self.ui.write_time_input.setValue(self.db_dict["write_time"]) #type: ignore

    def _init_logger(self):
        self.logger = logging.getLogger(__name__)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        log_dir = self.stk_mch_folder / "Strike Machine Log"
        os.makedirs(log_dir, exist_ok=True)

        file_handler = MonthlyRotatingFileHandler(
            base_log_dir=log_dir,
            prefix="TL_SM",
            maxBytes=5 * 1024 * 1024,
            backupCount=5,
            encoding='utf-8'
        )

        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

        if not getattr(sys, 'frozen', False):
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(file_formatter)
            self.logger.addHandler(stream_handler)

        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False  # tránh in trùng qua root logger

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonDblClick:
            double_click_actions = {
                self.ui.logo_btn        :self._on_logo_clicked,
                # self.ui.plc_io_btn      :self.i_o_page_btn,
                self.ui.cmd_btn         :self.cmd_btn,

                self.ui.reset_cycle_a_btn: lambda: self.reset_cycle_btn("A"),
                self.ui.reset_cycle_b_btn: lambda: self.reset_cycle_btn("B"),
                self.ui.reset_cycle_c_btn: lambda: self.reset_cycle_btn("C"),

                self.ui.clear_group_a: self.clear_group_a_btn,
                self.ui.clear_group_b: self.clear_group_b_btn,
                self.ui.clear_group_c: self.clear_group_c_btn,

            }
            if obj in double_click_actions:
                double_click_actions[obj]()
        return super().eventFilter(obj, event)

    def _init_app_data(self):
        self._app = QApplication.instance()
        self._lastpos = None
        self.ui.list_history.setItemDelegate(BackgroundDelegate(self.ui.list_history))
        self.ui.list_history_2.setItemDelegate(BackgroundDelegate(self.ui.list_history_2))
        self._last_history_time = 0.0
        self.db_dict = None
        self._COLOR_EVEN = QColor("#E2F1FD")
        self._COLOR_ODD  = QColor("#FFFFFF")

        self._pending_rows = []
        self._all_rows_cache = []
        self._table_display = 102
        self._search_table_display = 1000
        self._displayed_offset = 0
        self.history_db_path = None
        self.conn = None
        self.ai_sql_db = None
        self._history_batch_counter = 0
        self._ai_data_batch_counter = 0
        self._ai_warned_keys: set = set()
        self._db_offset = 0
        self._history_at_latest = True
        self._charts_paused = False
        self._search_keyword = ""
        self._search_offset = 0
        self._search_total = 0
        self._search_db_offset = 0
        self._loading_search_chunk = False
        self._search_scroll_connected = False
        self._exporting = False

        self._search_thread = None
        self._search_worker = None
        self._search_prepend = False

        self._current_unit = 0
        self._current_lang = "en"
        self._current_search_type = "name"

        self._original_data: list = []
        self._last_export_time = 0
        self.db_dict: Optional[dict] = None
        
        self.user = False
        self.worker_dict = {}
        self.thread_dict = {}
        self.all_data = {}
        self.actual_data = {}
        self.input_data = {}
        self.error_data = {}
        self.serial_data = {}
        self._data_lock = threading.Lock()
        
        self._last_i_o_group_3: list = [None] * 16
        self._last_i_o_group_4: list = [None] * 8
        self._last_group_a:     list = [None] * 9
        self._last_group_b:     list = [None] * 9
        self._last_group_c:     list = [None] * 9
        self._last_group_a_avg: float | None = None
        self._last_group_b_avg: float | None = None
        self._last_group_c_avg: float | None = None
        self._last_t0_pv:       float | None = None
        self._last_cycle:       list = [None] * 3
        self._last_at:          float | None = None
        self._last_bt:          float | None = None
        self._last_ct:          float | None = None
        self._last_itv:         list = [None] * 3

        self._last_cur_temp_a:         list = [None] * 3
        self._last_cur_temp_b:         list = [None] * 3
        self._last_cur_temp_c:         list = [None] * 3

        self._last_cur_pressure_a:         list = [None] * 5
        self._last_cur_pressure_b:         list = [None] * 5
        self._last_cur_pressure_c:         list = [None] * 5

        self._last_cur_cycle_a:         list = [None] * 4
        self._last_cur_cycle_b:         list = [None] * 4
        self._last_cur_cycle_c:         list = [None] * 4

        # Lệnh bấm nút đang chờ PLC xác nhận
        # key = tag name, value = {"value": bool, "t_sent": time.perf_counter(), "t_done": time ghi xong | None}
        self._pending_cmd = {}
        self._ai_expected_keys = [
            "datetime", "No.", "PLC Connection", "Serial Connection", "Bit_Alarm", 

            "V_A_HEATER_0", "V_B_HEATER_0", "V_C_HEATER_0",
            "I_A_HEATER_0", "I_B_HEATER_0", "I_C_HEATER_0",
            "total_active_power_kW_HEATER_0", "total_reactive_power_kvar_HEATER_0",
            "total_apparent_power_kVA_HEATER_0", "power_factor_HEATER_0", "frequency_Hz_HEATER_0",
            "T0_Current_Temp",

            "Out_Heat0", "Out_Fan1", "Out_Fan2",
            "Out_Heat1", "Out_Valve1_IN", "Out_Valve1_OUT", "Out_Valve1_OIL",
            "Out_Heat2", "Out_Valve2_IN", "Out_Valve2_OUT", "Out_Valve2_OIL",
            "Out_Heat3", "Out_Valve3_IN", "Out_Valve3_OUT", "Out_Valve3_OIL",

            "P1_Current_TempHeater", "P2_Current_TempHeater", "P3_Current_TempHeater",
            "P1_TempLimitHeater", "P2_TempLimitHeater", "P3_TempLimitHeater",

            "P1_Current_Air_FillingTime", "P1_Current_Air_HoldingTime", "P1_Current_Air_ReleaseTime",
            "P1_Current_Oil_End_Time", "P1_Current_Oil_Start_Time", "P1_Current_PressureHose",
            "P1_Current_PressureITV", "P1_Current_Temp1", "P1_Current_Temp2", "P1_Current_Temp3",
            "P1_Number_Test_Times",
            "P2_Current_Air_FillingTime", "P2_Current_Air_HoldingTime", "P2_Current_Air_ReleaseTime",
            "P2_Current_Oil_End_Time", "P2_Current_Oil_Start_Time", "P2_Current_PressureHose",
            "P2_Current_PressureITV", "P2_Current_Temp1", "P2_Current_Temp2", "P2_Current_Temp3",
            "P2_Number_Test_Times",
            "P3_Current_Air_FillingTime", "P3_Current_Air_HoldingTime", "P3_Current_Air_ReleaseTime",
            "P3_Current_Oil_End_Time", "P3_Current_Oil_Start_Time", "P3_Current_PressureHose",
            "P3_Current_PressureITV", "P3_Current_Temp1", "P3_Current_Temp2", "P3_Current_Temp3",
            "P3_Number_Test_Times",
            
            "P1_Air_FillingTime", "P1_Air_HoldingTime", "P1_Air_ReleaseTime", "P1_BitCountTimes",
            "P1_CountTimes", "P1_Oil_End_Time", "P1_Oil_Start_Time", "P1_PressureHoseOffset",
            "P1_PressureITVOffset", "P1_PressureSetting", "P1_Start_Heat", "P1_Start_Oil",
            "P1_Start_Pressure", "P1_Temp1Offset", "P1_Temp2Offset", "P1_Temp3Offset",
            "P1_TempLimitHIGH", "P1_TempLimitLOW", "P1_TemperatureSetting",
            "P2_Air_FillingTime", "P2_Air_HoldingTime", "P2_Air_ReleaseTime", "P2_BitCountTimes",
            "P2_CountTimes", "P2_Oil_End_Time", "P2_Oil_Start_Time", "P2_PressureHoseOffset",
            "P2_PressureITVOffset", "P2_PressureSetting", "P2_Start_Heat", "P2_Start_Oil",
            "P2_Start_Pressure", "P2_Temp1Offset", "P2_Temp2Offset", "P2_Temp3Offset",
            "P2_TempLimitHIGH", "P2_TempLimitLOW", "P2_TemperatureSetting",
            "P3_Air_FillingTime", "P3_Air_HoldingTime", "P3_Air_ReleaseTime", "P3_BitCountTimes",
            "P3_CountTimes", "P3_Oil_End_Time", "P3_Oil_Start_Time", "P3_PressureHoseOffset",
            "P3_PressureITVOffset", "P3_PressureSetting", "P3_Start_Heat", "P3_Start_Oil",
            "P3_Start_Pressure", "P3_Temp1Offset", "P3_Temp2Offset", "P3_Temp3Offset",
            "P3_TempLimitHIGH", "P3_TempLimitLOW", "P3_TemperatureSetting",
            "START", "STOP",
            "T0_Start_Heat", "T0_Stop_Heat", "T0_TempLimitHIGH", "T0_TempLimitLOW",
            "T0_TempOffset", "T0_TemperatureSetting",

            "Alarm_Info",
        ]

        self.init_signal = False

        self._alarm_active_rows = {}
        self._alarm_badge = NotificationBadge(self.ui.alarm_page_btn)
        self._alarm_row_limit = 200

        self.plc_read_worker = None
        self.plc_read_connection = False
        self.plc_read_thread = None
        self.plc_writer_worker = None
        self.plc_writer_connection = False
        self.plc_writer_thread = None
        self.serial_data_worker = None
        self.serial_data_thread = None
        self.serial_read_connection = False

        self.default_temp_room = 25.0

        self._sv_cycle_state("All", False)
        self._set_cycle_state("All")
        self._shutting_down = False
        self._button_flag()

    def _button_flag(self):
        self._start_flag = False
        self._stop_flag = False
        self._t0_heat_flag = False
        self._t0_stop_flag = False
        self._heating_a_flag = False
        self._heating_b_flag = False
        self._heating_c_flag = False    
        self._vacuum_a_flag = False
        self._vacuum_b_flag = False
        self._vacuum_c_flag = False
        self._oil_a_flag = False
        self._oil_b_flag = False
        self._oil_c_flag = False
        self._count_a_flag = False
        self._count_b_flag = False
        self._count_c_flag = False

    def _init_timer(self):
        self.all_timer = []

        self._last_group_update = 0.0
        self._last_actual_alarm = (None, None)
        self._alarm_err_seq = 0          # số lần đã nhận dữ liệu vùng ERROR
        self._alarm_pending = None       # (err_seq lúc Bit_Alarm bật, token) khi đang chờ Alarm_Info
        self._alarm_pending_token = 0

        self.data_table = QTimer(self)
        self.all_timer.append(self.data_table)
        self.data_table.setInterval(1000)
        self.data_table.timeout.connect(lambda: self._data_table(self._mapping_actual_data()))
        # self.data_table.start()

        # if self._plc_queue is not None:
        #     self.data_web_socket = QTimer(self)
        #     self.all_timer.append(self.data_web_socket)
        #     self.data_web_socket.setInterval(250)
        #     self.data_web_socket.timeout.connect(lambda: self._data_web_socket(self.all_data))
        #     self.data_web_socket.start()

        self.data_serial_timer = QTimer(self)
        self.all_timer.append(self.data_serial_timer)
        self.data_serial_timer.setInterval(200)
        self.data_serial_timer.timeout.connect(lambda: self._data_serial(self._mapping_serial_data()))

        # self.timer_stacked_pressure_page = QTimer(self)
        # self.all_timer.append(self.timer_stacked_pressure_page)
        
        self.chart_timer = QTimer(self)
        self.all_timer.append(self.chart_timer)
        self.chart_timer.setInterval(self.db_dict["data_read"] if self.db_dict else 200)
        self.chart_timer.timeout.connect(self._update_all_charts)
        self.chart_timer.timeout.connect(self._render_all_charts)
        self.chart_timer.start()
        
        self._history_flush_timer = QTimer(self)
        self.all_timer.append(self._history_flush_timer)
        self._history_flush_timer.setInterval(1000)
        self._history_flush_timer.timeout.connect(self._flush_history)
        self._history_flush_timer.start()


        # Đồng hồ & bộ đếm giờ tick 250 ms (chỉ vẽ lại khi số giây đổi).
        # Tick 1000 ms + sai số QTimer (~5-10%) làm số giây hiển thị bị nhảy
        # (VD 00:00:05 -> 00:00:07) vì có lúc 2 tick rơi vào 2 giây cách nhau.
        self._last_clock_s = None
        self.datetime_timer = QTimer(self)
        self.all_timer.append(self.datetime_timer)
        self.datetime_timer.timeout.connect(self.update_clock)
        self.datetime_timer.start(250)
        self.update_clock()

        self._init_run_time()
        self.run_time_timer = QTimer(self)
        self.all_timer.append(self.run_time_timer)
        self.run_time_timer.timeout.connect(self._update_run_time)
        self.run_time_timer.start(250)
        
        self.data_training_ai_timer = QTimer(self)
        self.all_timer.append(self.data_training_ai_timer)
        self.data_training_ai_timer.setInterval(1000)
        self.data_training_ai_timer.timeout.connect(lambda: self._data_AI(self.actual_data, self.serial_data, self.input_data, self.error_data))
        self.data_training_ai_timer.start()

    def _update_all_charts(self):
        self.update_chart_temp()
        self.update_chart_pressure()

    def _render_all_charts(self) -> None:
        """
        Render tuần tự 4 chart trong 1 lần gọi.
        """
        if self._charts_paused:
            return
        # t0 = time.perf_counter()

        self.chart_temp._render_frame()
        self.chart_pressure_a._render_frame()
        self.chart_pressure_b._render_frame()
        self.chart_pressure_c._render_frame()

        # elapsed_ms = (time.perf_counter() - t0) * 1000

        # if elapsed_ms > 80:
        #     self._chart_render_timer.setInterval(200)
        # elif elapsed_ms < 40 and self._chart_render_timer.interval() > 100:
        #     self._chart_render_timer.setInterval(100)

    def _init_group_object(self):
        """
        [0] = [2]
        [1] = [3]
        [2] = [4]
        [3] = [5]
        [4] = [6]
        [5] = [7]
        [6] = [8]
        [7] = [9]
        [8] = [10]
        [9] = [11]
        [10] = [12]
        """
        self.pressure_a_pv_obj = tuple(
            getattr(self.ui, f"pressure_pv_a_{i}") 
            for i in range(2, 13)
        )
 
        self.pressure_b_pv_obj = tuple(
            getattr(self.ui, f"pressure_pv_b_{i}") 
            for i in range(2, 13)
        )

        self.pressure_c_pv_obj = tuple(
            getattr(self.ui, f"pressure_pv_c_{i}") 
            for i in range(2, 13)
        )

        skip_value = frozenset({2, 3, 4})
        """
        [0] = 1
        [1] = 5
        [2] = 6
        [3] = 7
        [4] = 8
        [5] = 9
        [6] = 10
        [7] = 11
        """
        self.pressure_a_sv_obj = tuple(
            getattr(self.ui, f"pressure_sv_a_{i}") 
            for i in range(1, 12) if i not in skip_value
        )

        self.pressure_b_sv_obj = tuple(
            getattr(self.ui, f"pressure_sv_b_{i}") 
            for i in range(1, 12) if i not in skip_value
        )

        self.pressure_c_sv_obj = tuple(
            getattr(self.ui, f"pressure_sv_c_{i}") 
            for i in range(1, 12) if i not in skip_value
        )

        self.current_temp_a_pv_obj = (
            self.ui.pressure_pv_a_2,
            self.ui.pressure_pv_a_3,
            self.ui.pressure_pv_a_4
        )

        self.current_temp_b_pv_obj = (
            self.ui.pressure_pv_b_2,
            self.ui.pressure_pv_b_3,
            self.ui.pressure_pv_b_4
        )

        self.current_temp_c_pv_obj = (
            self.ui.pressure_pv_c_2,
            self.ui.pressure_pv_c_3,
            self.ui.pressure_pv_c_4
        )

        self.current_pressure_a_pv_obj = (
            self.ui.pressure_pv_a_5,
            self.ui.pressure_pv_a_6,
            self.ui.pressure_pv_a_7,
            self.ui.pressure_pv_a_8,
            self.ui.pressure_pv_a_12
        )

        self.current_pressure_b_pv_obj = (
            self.ui.pressure_pv_b_5,
            self.ui.pressure_pv_b_6,
            self.ui.pressure_pv_b_7,
            self.ui.pressure_pv_b_8,
            self.ui.pressure_pv_b_12
        )

        self.current_pressure_c_pv_obj = (
            self.ui.pressure_pv_c_5,
            self.ui.pressure_pv_c_6,
            self.ui.pressure_pv_c_7,
            self.ui.pressure_pv_c_8,
            self.ui.pressure_pv_c_12
        )

        self.current_cycle_a_pv_obj = (
            self.ui.pressure_pv_a_9,
            self.ui.pressure_pv_a_10,
            self.ui.pressure_pv_a_11,
            self.ui.cycle_a_displ_3,
        )

        self.current_cycle_b_pv_obj = (
            self.ui.pressure_pv_b_9,
            self.ui.pressure_pv_b_10,
            self.ui.pressure_pv_b_11,
            self.ui.cycle_b_displ_3,
        )

        self.current_cycle_c_pv_obj = (
            self.ui.pressure_pv_c_9,
            self.ui.pressure_pv_c_10,
            self.ui.pressure_pv_c_11,
            self.ui.cycle_c_displ_3,
        )

        self.temp_pv_obj = (
            self.ui.t0_pv,
            self.ui.at_pv,
            self.ui.bt_pv,
            self.ui.ct_pv
        )

        self.temp_sv_obj = (
            self.ui.t0_sv,
            self.ui.at_sv,
            self.ui.bt_sv,
            self.ui.ct_sv
        )

        self.temp_h_alm_obj = (
            self.ui.t0_h_alm_value,
            self.ui.at_h_alm_value,
            self.ui.bt_h_alm_value,
            self.ui.ct_h_alm_value
        )

        self.temp_l_alm_obj = (
            self.ui.t0_l_alm_value,
            self.ui.at_l_alm_value,
            self.ui.bt_l_alm_value,
            self.ui.ct_l_alm_value
        )

        self.tube_pv_obj = (self.ui.at_tube_pv, self.ui.bt_tube_pv, self.ui.ct_tube_pv)
        self.tube_sv_obj = (self.ui.at_tube_sv, self.ui.bt_tube_sv, self.ui.ct_tube_sv)

        self.temp_offset_obj = (
            self.ui.t0_offset_value,
            self.ui.at_t1_offset_value,
            self.ui.at_t2_offset_value,
            self.ui.at_t3_offset_value,
            self.ui.bt_t1_offset_value,
            self.ui.bt_t2_offset_value,
            self.ui.bt_t3_offset_value,
            self.ui.ct_t1_offset_value,
            self.ui.ct_t2_offset_value,
            self.ui.ct_t3_offset_value
        )

        self.list_for_import_a = (
            self.ui.pressure_sv_a_11,
            self.ui.pressure_sv_a_9,
            self.ui.pressure_sv_a_10,
            self.ui.pressure_sv_a_6,
            self.ui.pressure_sv_a_7,
            self.ui.pressure_sv_a_8,
            self.ui.pressure_sv_a_5,
            self.ui.pressure_sv_a_1,
            self.ui.at_h_alm_value,
            self.ui.at_l_alm_value,
            self.ui.at_t1_offset_value,
            self.ui.at_t2_offset_value,
            self.ui.at_t3_offset_value
        )
        self.list_for_import_b = (
            self.ui.pressure_sv_b_11,
            self.ui.pressure_sv_b_9,
            self.ui.pressure_sv_b_10,
            self.ui.pressure_sv_b_6,
            self.ui.pressure_sv_b_7,
            self.ui.pressure_sv_b_8,
            self.ui.pressure_sv_b_5,
            self.ui.pressure_sv_b_1,
            self.ui.bt_h_alm_value,
            self.ui.bt_l_alm_value,
            self.ui.bt_t1_offset_value,
            self.ui.bt_t2_offset_value,
            self.ui.bt_t3_offset_value
        )
        self.list_for_import_c = (
            self.ui.pressure_sv_c_11,
            self.ui.pressure_sv_c_9,
            self.ui.pressure_sv_c_10,
            self.ui.pressure_sv_c_6,
            self.ui.pressure_sv_c_7,
            self.ui.pressure_sv_c_8,
            self.ui.pressure_sv_c_5,
            self.ui.pressure_sv_c_1,
            self.ui.ct_h_alm_value,
            self.ui.ct_l_alm_value,
            self.ui.ct_t1_offset_value,
            self.ui.ct_t2_offset_value,
            self.ui.ct_t3_offset_value
        )
        self.list_for_import_t0 = (
            self.ui.t0_sv,
            self.ui.t0_h_alm_value,
            self.ui.t0_l_alm_value,
            self.ui.t0_offset_value
        )

        _sw = lambda i: getattr(self.ui, f"i_o_group_1_switch_{i}")
        # (tag PLC, switch) theo từng nhóm
        self.io_heat_obj  = tuple(zip(("Out_Heat0", "Out_Heat1", "Out_Heat2", "Out_Heat3"),
                                      (_sw(1), _sw(2), _sw(6), _sw(10))))
        # Valve: (tag IN, tag OUT, switch)
        # Tên tag đã qua normalize_name (db_layout_parser): '-' -> '_'
        self.io_valve_obj = (("Out_Valve1_IN", "Out_Valve1_OUT", _sw(3)),
                             ("Out_Valve2_IN", "Out_Valve2_OUT", _sw(7)),
                             ("Out_Valve3_IN", "Out_Valve3_OUT", _sw(11)))
        self.io_oil_obj   = tuple(zip(("Out_Valve1_OIL", "Out_Valve2_OIL", "Out_Valve3_OIL"),
                                      (_sw(4), _sw(8), _sw(12))))
        # Switch hiển thị trạng thái nút cycle A/B/C
        self.io_cycle_obj = ((self.ui.set_cycle_a_btn, _sw(5)),
                             (self.ui.set_cycle_b_btn, _sw(9)),
                             (self.ui.set_cycle_c_btn, _sw(13)))
        self.i_o_group_3_obj = (
            self.ui.t0_value,
            self.ui.t1_1_value,
            self.ui.t1_2_value,
            self.ui.t1_3_value,
            self.ui.t2_1_value,
            self.ui.t2_2_value,
            self.ui.t2_3_value,
            self.ui.t3_1_value,
            self.ui.t3_2_value,
            self.ui.t3_3_value,
            self.ui.p1_value,
            self.ui.p2_value,
            self.ui.p3_value,
            self.ui.fp1_value,
            self.ui.fp2_value,
            self.ui.fp3_value
        )
        self.i_o_group_4_obj = (
            self.ui.serial_data_1,
            self.ui.serial_data_2,
            self.ui.serial_data_3,
            self.ui.serial_data_4,
            self.ui.serial_data_5,
            self.ui.serial_data_6,
            self.ui.serial_data_7,
            self.ui.serial_data_8,
        )

    def _paint_pv_obj(self, color):
        for obj in self.pressure_a_pv_obj + self.pressure_b_pv_obj + self.pressure_c_pv_obj + self.temp_pv_obj + self.tube_pv_obj:
            obj.setStyleSheet(f"""
                QDoubleSpinBox {{
                    color: {color};}}
                QSpinBox {{
                    color: {color};}}""")
            
    def _paint_sv_obj(self, color):
        for obj in self.pressure_a_sv_obj + self.pressure_b_sv_obj + self.pressure_c_sv_obj\
              + self.temp_offset_obj + self.temp_h_alm_obj + self.temp_l_alm_obj + self.temp_sv_obj + self.tube_sv_obj:
            obj.setStyleSheet(f"""
                QDoubleSpinBox {{
                    color: {color};}}
                QDoubleSpinBox:hover {{
                    border: 2px solid {color};
                }}
                QSpinBox {{
                    color: {color};}}
                QSpinBox:hover {{
                    border: 2px solid {color};
                }}
            """)

    def _init_list_unit(self):
        self.cel_fah_change = [
            self.ui.stacked_cel_fah_press_a_1,
            self.ui.stacked_cel_fah_press_a_2,
            self.ui.stacked_cel_fah_press_a_3,
            self.ui.stacked_cel_fah_press_a_4,

            self.ui.stacked_cel_fah_press_b_1,
            self.ui.stacked_cel_fah_press_b_2,
            self.ui.stacked_cel_fah_press_b_3,
            self.ui.stacked_cel_fah_press_b_4,

            self.ui.stacked_cel_fah_press_c_1,
            self.ui.stacked_cel_fah_press_c_2,
            self.ui.stacked_cel_fah_press_c_3,
            self.ui.stacked_cel_fah_press_c_4,

            self.ui.stacked_cel_fah_temp_t0_1,
            self.ui.stacked_cel_fah_temp_t0_2,
            self.ui.stacked_cel_fah_temp_t0_3,
            self.ui.stacked_cel_fah_temp_t0_4,
            self.ui.stacked_cel_fah_temp_t0_5,

            self.ui.stacked_cel_fah_temp_a_1,
            self.ui.stacked_cel_fah_temp_a_2,
            self.ui.stacked_cel_fah_temp_a_3,
            self.ui.stacked_cel_fah_temp_a_4,
            self.ui.stacked_cel_fah_temp_a_5,
            self.ui.stacked_cel_fah_temp_a_6,
            self.ui.stacked_cel_fah_temp_a_7,
            self.ui.stacked_cel_fah_temp_a_8,
            self.ui.stacked_cel_fah_temp_a_9,

            self.ui.stacked_cel_fah_temp_b_1,
            self.ui.stacked_cel_fah_temp_b_2,
            self.ui.stacked_cel_fah_temp_b_3,
            self.ui.stacked_cel_fah_temp_b_4,
            self.ui.stacked_cel_fah_temp_b_5,
            self.ui.stacked_cel_fah_temp_b_6,
            self.ui.stacked_cel_fah_temp_b_7,
            self.ui.stacked_cel_fah_temp_b_8,
            self.ui.stacked_cel_fah_temp_b_9,

            self.ui.stacked_cel_fah_temp_c_1,
            self.ui.stacked_cel_fah_temp_c_2,
            self.ui.stacked_cel_fah_temp_c_3,
            self.ui.stacked_cel_fah_temp_c_4,
            self.ui.stacked_cel_fah_temp_c_5,
            self.ui.stacked_cel_fah_temp_c_6,
            self.ui.stacked_cel_fah_temp_c_7,
            self.ui.stacked_cel_fah_temp_c_8,
            self.ui.stacked_cel_fah_temp_c_9
        ]

    def _create_charts(self):
        font = QFont("Segoe UI", 15)
        font.setWeight(QFont.Weight.Bold)

        # Chart Nhiệt độ (Furnace)
        self.chart_temp = CustomChartWidget(
            title="Furnace",
            num_temp=2,
            num_pressure=0,
            temp_label="Temperature (°C)",
            pressure_label="",
            temp_range=(0, 50),
            pressure_range=(0, 0),
            max_seconds=30,
            chart_font=font
        )

        # Chart Group A
        self.chart_pressure_a = CustomChartWidget(
            title="Group A",
            num_temp=4,
            num_pressure=2,
            temp_label="Temperature (°C)",
            pressure_label="Pressure (bar)",
            temp_range=(0, 50),
            pressure_range=(0, 15),
            max_seconds=30,
            chart_font=font
        )

        # Chart Group B
        self.chart_pressure_b = CustomChartWidget(
            title="Group B",
            num_temp=4,
            num_pressure=2,
            temp_label="Temperature (°C)",
            pressure_label="Pressure (bar)",
            temp_range=(0, 50),
            pressure_range=(0, 15),
            max_seconds=30,
            chart_font=font
        )

        # Chart Group C
        self.chart_pressure_c = CustomChartWidget(
            title="Group C",
            num_temp=4,
            num_pressure=2,
            temp_label="Temperature (°C)",
            pressure_label="Pressure (bar)",
            temp_range=(0, 50),
            pressure_range=(0, 15),
            max_seconds=30,
            chart_font=font
        )

        self.chart_temp.btn_setting.clicked.connect(self.temperature_page_btn)
        self.chart_pressure_a.btn_setting.clicked.connect(self.ui.home_page_btn.click)
        self.chart_pressure_b.btn_setting.clicked.connect(self.ui.home_page_btn.click)
        self.chart_pressure_c.btn_setting.clicked.connect(self.ui.home_page_btn.click)

        self.ui.card_temperature.addWidget(self.chart_temp)
        self.ui.card_pressure_1.addWidget(self.chart_pressure_a)
        self.ui.card_pressure_2.addWidget(self.chart_pressure_b)
        self.ui.card_pressure_3.addWidget(self.chart_pressure_c)
        self._chart_frames = [
            self.ui.card_temperature.parentWidget(),   # frame chứa chart_temp
            self.ui.card_pressure_1.parentWidget(),    # frame chứa chart_pressure_a
            self.ui.card_pressure_2.parentWidget(),    # frame chứa chart_pressure_b
            self.ui.card_pressure_3.parentWidget(),    # frame chứa chart_pressure_c
        ]

        charts = [self.chart_temp, self.chart_pressure_a,
                self.chart_pressure_b, self.chart_pressure_c]

        for idx, chart in enumerate(charts):
            chart.clicked.connect(lambda i=idx: self._toggle_chart_frame(i))

        self._maximized_chart_idx = -1
        QTimer.singleShot(100, self._save_grid_rects)
        self._chart_layouts = [
            self.ui.card_temperature,
            self.ui.card_pressure_1,
            self.ui.card_pressure_2,
            self.ui.card_pressure_3,
        ]
        # self.chart_temp._render_timer.stop()
        # self.chart_pressure_a._render_timer.stop()
        # self.chart_pressure_b._render_timer.stop()
        # self.chart_pressure_c._render_timer.stop()

    def _save_grid_rects(self):
        rects = [f.geometry() for f in self._chart_frames]
        if all(r.width() > 0 and r.height() > 0 for r in rects):
            self._grid_rects = rects
            # print("Grid rects saved:", rects)
        else:
            QTimer.singleShot(100, self._save_grid_rects)
    
    def _toggle_chart_frame(self, idx: int):
        frames = self._chart_frames
        charts = [self.chart_temp, self.chart_pressure_a,
                self.chart_pressure_b, self.chart_pressure_c]
        grid = self.ui.gridLayout_2
        positions = {0: (0, 0), 1: (0, 1), 2: (1, 0), 3: (1, 1)}
        row, col = positions[idx]

        if self._maximized_chart_idx == idx:
            self._maximized_chart_idx = -1
            grid.setRowStretch(0, 1)
            grid.setRowStretch(1, 1)
            grid.setColumnStretch(0, 1)
            grid.setColumnStretch(1, 1)
            for i, f in enumerate(frames):
                if i != idx:
                    f.show()
        else:
            self._maximized_chart_idx = idx
            other_row = 1 if row == 0 else 0
            other_col = 1 if col == 0 else 0
            grid.setRowStretch(row, 100)
            grid.setRowStretch(other_row, 0)
            grid.setColumnStretch(col, 100)
            grid.setColumnStretch(other_col, 0)
            for i, f in enumerate(frames):
                if i != idx:
                    f.hide()
        
    ###########################################################################################
    #############################------ Button Function Setup ------###########################
    def _setup_btn_signals(self):
        # Duration = 1 ms → expand/collapse gần như tức thì (thư viện bỏ qua giá trị 0)
        self.ui.left_side_menu_widget.customizeQCustomSlideMenu(
            defaultWidth = 70,
            defaultHeight = "parent",
            collapsedWidth = 70,
            collapsedHeight = "parent",
            expandedWidth = 175,
            expandedHeight = "parent",
            animationDuration = 1,
            animationEasingCurve = QEasingCurve.Linear,  # type: ignore
            collapsingAnimationDuration = 1,
            collapsingAnimationEasingCurve = QEasingCurve.Linear,  # type: ignore
            expandingAnimationDuration = 1,
            expandingAnimationEasingCurve = QEasingCurve.Linear,  # type: ignore
        )
        self.ui.open_side_menu_btn.clicked.connect(self._on_menu_toggle)
        self.ui.logo_btn.installEventFilter(self)
        
        ### Left side menu button
        self.ui.home_page_btn.clicked.connect(self.pressure_page_btn)
        self.ui.chart_page_btn.clicked.connect(self.home_page_btn)
        self.ui.device_page_btn.clicked.connect(self.device_page_btn)
        self.ui.history_page_btn.clicked.connect(self.history_page_btn)
        self.ui.alarm_page_btn.clicked.connect(self.alarm_page_btn)

        self.ui.eng_language.clicked.connect(self.set_language_en)
        self.ui.vn_language.clicked.connect(self.set_language_vn)
        self.ui.cn_language.clicked.connect(self.set_language_cn)

        self.ui.next_group_page_btn.clicked.connect(self.next_previous_pressure_page)

        self.ui.back_connection_page_btn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.connection_page))
        self.ui.back_home_page_btn.clicked.connect(lambda: self.ui.home_page_btn.click())

        self.ui.temp_unit_selection_combox.currentIndexChanged.connect(lambda: QTimer.singleShot(50, self._set_cur_unit))

        # self.ui.plc_io_btn.installEventFilter(self)
        
        self.ui.plc_io_btn.clicked.connect(self.i_o_page_btn)
        self.ui.cmd_btn.installEventFilter(self)

        self.ui.new_data_btn.clicked.connect(self.new_data_btn)

        self.ui.start_stop_btn.clicked.connect(lambda: self.start_stop_btn("Start", self.ui.start_stop_btn))
        self.ui.stop_start_btn.clicked.connect(lambda: self.start_stop_btn("Stop", self.ui.stop_start_btn))

        self.ui.heat_btn_a.toggled.connect(lambda checked: self.heating_btn("A", checked, self.ui.heat_btn_a)) 
        self.ui.heat_btn_b.toggled.connect(lambda checked: self.heating_btn("B", checked, self.ui.heat_btn_b))
        self.ui.heat_btn_c.toggled.connect(lambda checked: self.heating_btn("C", checked, self.ui.heat_btn_c))
        self.ui.heat_on_btn_t0.clicked.connect(lambda: self.heating_btn_t0("T0_On", self.ui.heat_on_btn_t0))
        self.ui.heat_off_btn_t0.clicked.connect(lambda: self.heating_btn_t0("T0_Off", self.ui.heat_off_btn_t0))

        self.ui.vacuum_btn_a.toggled.connect(lambda checked: self.pumping_btn("A", checked, self.ui.vacuum_btn_a))
        self.ui.vacuum_btn_b.toggled.connect(lambda checked: self.pumping_btn("B", checked, self.ui.vacuum_btn_b))
        self.ui.vacuum_btn_c.toggled.connect(lambda checked: self.pumping_btn("C", checked, self.ui.vacuum_btn_c))

        # self.ui.refuel_btn_a.toggled.connect(lambda checked: self.fill_oil_btn("A", checked, self.ui.refuel_btn_a))
        # self.ui.refuel_btn_b.toggled.connect(lambda checked: self.fill_oil_btn("B", checked, self.ui.refuel_btn_b))
        # self.ui.refuel_btn_c.toggled.connect(lambda checked: self.fill_oil_btn("C", checked, self.ui.refuel_btn_c))

        self.ui.set_cycle_a_btn.toggled.connect(lambda checked: self.cycle_loop_btn("A", checked, self.ui.set_cycle_a_btn))
        self.ui.set_cycle_b_btn.toggled.connect(lambda checked: self.cycle_loop_btn("B", checked, self.ui.set_cycle_b_btn))
        self.ui.set_cycle_c_btn.toggled.connect(lambda checked: self.cycle_loop_btn("C", checked, self.ui.set_cycle_c_btn))

        self.ui.clear_data_btn.clicked.connect(self.clear_data_btn)

        self.ui.reset_cycle_a_btn.installEventFilter(self)
        self.ui.reset_cycle_b_btn.installEventFilter(self)
        self.ui.reset_cycle_c_btn.installEventFilter(self)
        
        self.ui.clear_group_a.installEventFilter(self)
        self.ui.clear_group_b.installEventFilter(self)
        self.ui.clear_group_c.installEventFilter(self)

        self.ui.search_data.textChanged.connect(self._on_search_changed)
        self.ui.select_group_name.currentTextChanged.connect(self._on_search_changed)
        self.ui.search_data_start_edit.dateTimeChanged.connect(self._on_search_changed)
        self.ui.search_data_end_edit.dateTimeChanged.connect(self._on_search_changed)
        self.ui.clear_history_search.clicked.connect(self._on_clear_clicked)
        self.ui.export_all_tables_to_excel_btn.clicked.connect(self.export_all_tables_to_excel_btn)
        self.ui.list_history_2.verticalScrollBar().valueChanged.connect(self._on_search_scroll)
        self.ui.stackedWidget_2.currentChanged.connect(self._on_main_page_changed)
        # Chart nằm ở menu_page → rời trang này thì dừng render (data vẫn append)
        self.ui.stackedWidget_2.currentChanged.connect(
            lambda i: setattr(self, "_charts_paused",
                              self.ui.stackedWidget_2.widget(i) is not self.ui.menu_page))

        # NOTE (refactor): Trước đây ở đây có 1 dict `spinbox_map` trỏ tới 47 hàm
        # on_*_changed riêng lẻ (~90 dòng lặp theo pattern group A/B/C). Toàn bộ
        # logic đó đã được thay bằng SPINBOX_PLC_MAP + _make_plc_handler(), xem
        # _setup_spinbox_handlers() bên dưới — kết quả đã được đối chiếu 1:1 với
        # 47 handler cũ (cùng PLC tag, cùng transform, cùng widget mirror).
        # install_clear_on_focus(self.ui.db_file_path_edit)
        # install_clear_on_focus(self.ui.plc_ip_address_edit)
        # install_clear_on_focus(self.ui.db_number_input)
        # install_clear_on_focus(self.ui.db_data_size_input)
        # install_clear_on_focus(self.ui.error_display)

        # protect_widgets_on_stacked(self.ui.stackedWidget_2, [
        #     (self.ui.db_file_path_edit,   None, None),
        #     (self.ui.plc_ip_address_edit, None, None),
        #     # (self.ui.db_number_input,     None, None),
        #     # (self.ui.db_data_size_input,  None, None),
        # ])

        self._setup_spinbox_handlers()

        # self.ui.error_display._speed = 50

    def _get_transform(self, key: str):
        if key == "sec_to_msec":
            return self.cal_sec_to_msec
        if key == "fah_to_cel":
            return self.cal_fah_to_cel
        return None
    
    def _make_plc_handler(self, widget_name: str, plc_key: str, transform_key):
        def handler(value):
            if not self.plc_writer_connection:
                return
            transform = self._get_transform(transform_key)
            v = transform(value) if transform else value
            self.plc_writer_worker.write_value.emit(plc_key, v)  # type: ignore
        return handler
    
    def _make_temp_sv_handler(self, widget_name: str, plc_key: str, mirror_widget: str):
        def handler(value):
            # Ghi PLC
            if self.plc_writer_connection:
                self.plc_writer_worker.write_value.emit(  # type: ignore
                    plc_key, self.cal_fah_to_cel(value)
                )
            # Đồng bộ sang widget kép (at_sv / bt_sv / ct_sv)
            mirror = getattr(self.ui, mirror_widget)
            mirror.blockSignals(True)
            mirror.setValue(value)
            mirror.blockSignals(False)
        return handler
    
    def _make_mirror_sv_handler(self, widget_name: str, target_widget: str):
        def handler(value):
            target = getattr(self.ui, target_widget)
            target.setValue(value)   # trigger pressure_sv_X_1 handler → ghi PLC
        return handler
    
    def _on_table_write_cycle_changed(self, value: float):
        """Đảm bảo table_write_cycle không nhỏ hơn read_time."""
        if (value * 1000) < self.ui.read_time_input.value():
            self.ui.table_write_cycle.setValue(
                float(self.ui.read_time_input.value()) / 1000
            )
    
    def _setup_spinbox_handlers(self):
        for widget_name, (plc_key, transform_key) in SPINBOX_PLC_MAP.items():
            spinbox = getattr(self.ui, widget_name)
            install_clear_on_focus(spinbox)
            spinbox.setKeyboardTracking(False)
            spinbox.valueChanged.connect(
                self._make_plc_handler(widget_name, plc_key, transform_key)
            )
    
        for widget_name, (plc_key, mirror_widget) in TEMP_SV_MIRROR.items():
            spinbox = getattr(self.ui, widget_name)
            install_clear_on_focus(spinbox)
            spinbox.setKeyboardTracking(False)
            spinbox.valueChanged.connect(
                self._make_temp_sv_handler(widget_name, plc_key, mirror_widget)
            )
    
        for widget_name, target_widget in TEMP_SV_REVERSE_MIRROR.items():
            spinbox = getattr(self.ui, widget_name)
            install_clear_on_focus(spinbox)
            spinbox.setKeyboardTracking(False)
            spinbox.valueChanged.connect(
                self._make_mirror_sv_handler(widget_name, target_widget)
            )
    
        self.ui.table_write_cycle.setKeyboardTracking(False)
        self.ui.table_write_cycle.valueChanged.connect(
            self._on_table_write_cycle_changed
        )

    def _init_history_database(self):
        """Khởi tạo SQLite Database - Không xóa bảng cũ"""
        db_folder = Path(self.stk_mch_folder) / "DB_address"
        db_folder.mkdir(parents=True, exist_ok=True)
        
        self.history_db_path = db_folder / "history.db"
        
        try:
            self.conn = sqlite3.connect(str(self.history_db_path), check_same_thread=False)
            self.conn.row_factory = sqlite3.Row
            self.conn.execute("PRAGMA journal_mode=WAL")
            self.conn.execute("PRAGMA synchronous=NORMAL")

            cursor = self.conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='history'")
            table_exists = cursor.fetchone() is not None

            if not table_exists:
                self.conn.execute('''
                    CREATE TABLE history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        "No." TEXT,
                        "Name." TEXT,
                        "Group." TEXT,
                        "Pressure SV." TEXT,
                        "Pressure." TEXT,
                        "Furnace SV." TEXT,
                        "T-Furnace." TEXT,
                        "Temperature SV." TEXT,
                        "Front." TEXT,
                        "Middle." TEXT,
                        "End." TEXT,
                        "Date." TEXT
                    )
                ''')
            for col_name in ["Pressure SV.", "Furnace SV.", "Temperature SV."]:
                try:
                    self.conn.execute(f'ALTER TABLE history ADD COLUMN "{col_name}" TEXT DEFAULT ""')
                    self.logger.info(f"Migrated: added column '{col_name}'")
                except Exception:
                    pass
            self.conn.commit()
            self.logger.info(f"SQLite DB ready: {self.history_db_path}")

            result = self.conn.execute(
                'SELECT MAX(CAST("No." AS INTEGER)) FROM history'
            ).fetchone()[0]
            self._history_batch_counter = result if result else 0

        except Exception as e:
            self.logger.error(f"SQLite init error: {e}")
            self.conn = None

    def _db_row_to_ui(self, row, stt: str) -> list:
        return [
            stt,
            str(row["Name."]         or ""),
            str(row["Group."]        or ""),
            str(row["Pressure."]     or ""),
            str(row["T-Furnace."]    or ""),
            str(row["Front."]        or ""),
            str(row["Middle."]       or ""),
            str(row["End."]          or ""),
            str(row["Date."]         or ""),
        ]
    
    def _init_table_list_history(self):
        """
        Tải dữ liệu từ database vào table list_history
        \n Chỉ load tối đa {self._table_display} dòng cuối để tránh lag khi có nhiều dữ liệu.
        """
        if not self.conn:
            return
        try:
            cursor = self.conn.cursor()

            total_db = self.conn.execute('SELECT COUNT(*) FROM history').fetchone()[0]

            cursor.execute(
                'SELECT * FROM history ORDER BY id DESC LIMIT ?',
                (self._table_display,)
            )
            rows = cursor.fetchall()
            rows.reverse()  # ASC lại

            self._all_rows_cache = []
            for idx, row in enumerate(rows):
                stt = row[1] if row[1] else str(total_db - len(rows) + idx + 1)
                formatted = self._db_row_to_ui(row, stt)
                self._all_rows_cache.append(formatted)

            self._db_offset = total_db - len(rows)
            self._displayed_start = 0
            self._history_at_latest = True

            self._render_chunk(0, len(self._all_rows_cache))

            self._apply_span(self.ui.list_history)

            self.ui.list_history.verticalScrollBar().valueChanged.connect(
                self._on_history_scroll
            )
            self.ui.list_history.scrollToBottom()
            self.logger.info(f"Total {total_db:,} records, showing last {self._table_display}")
            # self._resize_table_columns(self.ui.list_history)
            self._all_rows_cache.clear()

        except Exception as e:
            self.logger.error(f"Error loading history: {e}")

    def add_row_to_list_history(self, product_name, groups: list[dict]):
        """
        groups = [
            {"group": "Group A", ...},
            {"group": "Group B", ...},
            {"group": "Group C", ...},
        ]
        """
        try:
            if not hasattr(self, 'conn') or self.conn is None:
                return

            unit_suffix = "°F" if self._current_unit == 1 else "°C"
            def fmt(v):
                return f"{v:.1f}{unit_suffix}"

            today_date = datetime.now().strftime("%H:%M - %d/%m/%Y")

            sv_widget_map = {
                "a": (self.ui.pressure_sv_a_5, self.ui.t0_sv, self.ui.pressure_sv_a_1),
                "b": (self.ui.pressure_sv_b_5, self.ui.t0_sv, self.ui.pressure_sv_b_1),
                "c": (self.ui.pressure_sv_c_5, self.ui.t0_sv, self.ui.pressure_sv_c_1),
            }

            for g in groups:
                group_key = g["group"].replace("Group ", "").strip().lower()

                pressure_sv_widget, oven_sv_widget, temp_sv_widget = sv_widget_map.get(group_key, (None, None, None))

                pressure_sv_val = float(pressure_sv_widget.text()) if pressure_sv_widget else 0.0
                oven_sv_val     = float(oven_sv_widget.text())     if oven_sv_widget     else 0.0
                temp_sv_val     = float(temp_sv_widget.text())     if temp_sv_widget     else 0.0

                db_row = [
                    "",                              # [0]  batch_no
                    product_name,                    # [1]  Name.
                    g["group"],                      # [2]  Group.
                    f"{pressure_sv_val:.2f} bar",    # [3]  Pressure SV.
                    f"{g['pressure']:.2f} bar",      # [4]  Pressure.
                    fmt(self.for_display_temp(oven_sv_val)),                # [5]  Furnace SV.
                    fmt(self.for_display_temp(g["temp"])),                  # [6]  T-Furnace.
                    fmt(self.for_display_temp(temp_sv_val)),                # [7]  Temperature SV.
                    fmt(self.for_display_temp(g["front"])),                 # [8]  Front.
                    fmt(self.for_display_temp(g["mid"])),                   # [9]  Middle.
                    fmt(self.for_display_temp(g["end"])),                   # [10] End.
                    today_date                       # [11] Date.
                ]

                ui_row = [
                    db_row[0],   # No.
                    db_row[1],   # Name.
                    db_row[2],   # Group.
                    db_row[4],   # Pressure.
                    db_row[6],   # T-Furnace.
                    db_row[8],   # Front.
                    db_row[9],   # Middle.
                    db_row[10],  # End.
                    db_row[11],  # Date.
                ]

                self._pending_rows.append((db_row, ui_row))

            # Flush khi đủ 3 rows (1 batch = 3 groups)
            if len(self._pending_rows) >= 3:
                self._flush_history()

        except Exception as e:
            self.logger.error(f"[add_row_to_list_history] Error: {e}")

    def _flush_history(self):
        if not self._pending_rows or not self.conn:
            return

        batch = self._pending_rows[:3]
        self._pending_rows = self._pending_rows[3:]

        self._history_batch_counter += 1
        batch_no = str(self._history_batch_counter)

        db_rows = []
        ui_rows = []
        for db_row, ui_row in batch:
            db_row[0] = batch_no
            ui_row[0] = batch_no
            db_rows.append(db_row)
            ui_rows.append(ui_row)

        try:
            self.conn.executemany('''
                INSERT INTO history (
                    "No.", 
                    "Name.", 
                    "Group.",
                    "Pressure SV.", 
                    "Pressure.",
                    "Furnace SV.", 
                    "T-Furnace.", 
                    "Temperature SV.",
                    "Front.", 
                    "Middle.", 
                    "End.", 
                    "Date."
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', db_rows)
            self.conn.commit()
        except Exception as e:
            self.logger.error(f"[_flush_history][DB] {e}")

        # Đang xem dữ liệu cũ (cửa sổ đã trượt lên) -> không chèn vào table,
        # dữ liệu mới sẽ hiện khi kéo xuống cuối hoặc khi reset về dòng mới nhất
        if not getattr(self, '_history_at_latest', True):
            return

        table         = self.ui.list_history
        scrollbar     = table.verticalScrollBar()
        was_at_bottom = scrollbar.value() >= scrollbar.maximum() - 5

        table.setUpdatesEnabled(False)
        table.clearSpans()

        removed = 0
        for ui_row in ui_rows:
            row_pos = table.rowCount()
            table.insertRow(row_pos)
            for col, value in enumerate(ui_row):
                table.setItem(row_pos, col,
                    self._make_colored_item(str(value), self._history_batch_counter))

            if table.rowCount() > self._table_display:
                table.removeRow(0)
                removed += 1

        self._db_offset += removed

        table.setUpdatesEnabled(True)
        self._apply_span(self.ui.list_history)

        if was_at_bottom:
            table.scrollToBottom()

    def _apply_span(self, table):
        """
        Merge các row cùng No., Name., Date.
        """
        row_idx = 0
        while row_idx < table.rowCount():
            current_no = table.item(row_idx, 0).text() if table.item(row_idx, 0) else ""
            span = 1

            while (row_idx + span < table.rowCount() and
                table.item(row_idx + span, 0) and
                table.item(row_idx + span, 0).text() == current_no):
                span += 1

            if span > 1:
                for merge_col in [0, 1, 4, 8]:  # No., Name., Date.
                    table.setSpan(row_idx, merge_col, span, 1)

            row_idx += span

    def _render_chunk(self, start: int, end: int):
        chunk = self._all_rows_cache[start:end]
        if not chunk:
            return

        table = self.ui.list_history
        table.setUpdatesEnabled(False)
        self._insert_history_rows(table, table.rowCount(), chunk)
        table.setUpdatesEnabled(True)

    def _history_color_key(self, no: str, fallback: int) -> int:
        """Màu theo số No. của batch để màu không bị lệch khi cửa sổ trượt lên/xuống"""
        try:
            return int(no)
        except (TypeError, ValueError):
            return fallback

    def _insert_history_rows(self, table, start_row: int, rows: list):
        """Chèn các dòng đã format vào table bắt đầu từ start_row"""
        prev_no       = None
        batch_counter = 0
        for i, row_data in enumerate(rows):
            current_no = str(row_data[0]) if row_data[0] else ""
            if current_no != prev_no:
                batch_counter += 1
                prev_no = current_no
            color_key = self._history_color_key(current_no, batch_counter)

            row_pos = start_row + i
            table.insertRow(row_pos)
            for col, value in enumerate(row_data):
                table.setItem(row_pos, col,
                    self._make_colored_item(str(value), color_key))

    def _fetch_history_rows(self, offset: int, count: int) -> list:
        """Lấy count dòng (đã format cho UI) từ vị trí offset theo thứ tự id ASC"""
        if count <= 0 or not self.conn:
            return []
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT * FROM history ORDER BY id ASC LIMIT ? OFFSET ?',
            (count, offset)
        )
        result = []
        for idx, row in enumerate(cursor.fetchall()):
            stt = row[1] if row[1] else str(offset + idx + 1)
            result.append(self._db_row_to_ui(row, stt))
        return result

    def _history_scroll_step(self) -> int:
        """Số dòng trượt mỗi lần kéo (nửa cửa sổ, làm tròn theo batch 3 dòng)"""
        return max(3, (self._table_display // 2) // 3 * 3)

    def _make_colored_item(self, value: str, batch_counter: int) -> QTableWidgetItem:
        item = QTableWidgetItem(value)
        item.setTextAlignment(Qt.AlignCenter)  # type: ignore
        color = self._COLOR_EVEN if batch_counter % 2 == 0 else self._COLOR_ODD
        # print(f"batch={batch_counter}, color={color.name()}")
        item.setData(Qt.BackgroundRole, color)  # type: ignore
        return item

    def _on_history_scroll(self, value: int):
        sb = self.ui.list_history.verticalScrollBar()
        loading = getattr(self, '_loading_history_chunk', False)
        if value <= sb.minimum():
            if self._db_offset > 0 and not loading:
                self._loading_history_chunk = True
                QTimer.singleShot(1000, self._prepend_history_chunk)
        elif value >= sb.maximum() and not getattr(self, '_history_at_latest', True):
            if not loading:
                self._loading_history_chunk = True
                QTimer.singleShot(1000, self._append_history_chunk)

    def _prepend_history_chunk(self):
        """
        Kéo lên trên cùng: thêm các dòng cũ hơn vào đầu table và bỏ bớt
        dòng ở cuối để table luôn giữ đúng {self._table_display} dòng.
        """
        table = self.ui.list_history
        sb    = table.verticalScrollBar()
        try:
            if self._db_offset <= 0 or sb.value() > sb.minimum():
                return

            fetch_start = max(0, self._db_offset - self._history_scroll_step())
            new_chunk   = self._fetch_history_rows(fetch_start, self._db_offset - fetch_start)
            if not new_chunk:
                return

            try:
                sb.valueChanged.disconnect(self._on_history_scroll)
            except:
                pass

            table.setUpdatesEnabled(False)
            table.clearSpans()

            self._insert_history_rows(table, 0, new_chunk)
            self._db_offset = fetch_start

            overflow = table.rowCount() - self._table_display
            if overflow > 0:
                for _ in range(overflow):
                    table.removeRow(table.rowCount() - 1)
                self._history_at_latest = False

            self._apply_span(table)
            table.setUpdatesEnabled(True)

            table.scrollTo(
                table.model().index(len(new_chunk), 0),
                QTableWidget.ScrollHint.PositionAtTop
            )

            sb.valueChanged.connect(self._on_history_scroll)

        except Exception as e:
            self.logger.error(f"[_prepend_history_chunk] {e}")
        finally:
            self._loading_history_chunk = False

    def _append_history_chunk(self):
        """
        Kéo xuống cuối khi đang xem dữ liệu cũ: thêm các dòng mới hơn vào cuối
        table và bỏ bớt dòng ở đầu để table luôn giữ đúng {self._table_display} dòng.
        """
        table = self.ui.list_history
        sb    = table.verticalScrollBar()
        try:
            if getattr(self, '_history_at_latest', True) or sb.value() < sb.maximum():
                return

            step      = self._history_scroll_step()
            end       = self._db_offset + table.rowCount()
            new_chunk = self._fetch_history_rows(end, step)
            if len(new_chunk) < step:
                self._history_at_latest = True
            if not new_chunk:
                return

            try:
                sb.valueChanged.disconnect(self._on_history_scroll)
            except:
                pass

            table.setUpdatesEnabled(False)
            table.clearSpans()

            self._insert_history_rows(table, table.rowCount(), new_chunk)

            overflow = table.rowCount() - self._table_display
            if overflow > 0:
                for _ in range(overflow):
                    table.removeRow(0)
                self._db_offset += overflow

            self._apply_span(table)
            table.setUpdatesEnabled(True)

            table.scrollTo(
                table.model().index(table.rowCount() - len(new_chunk) - 1, 0),
                QTableWidget.ScrollHint.PositionAtBottom
            )

            sb.valueChanged.connect(self._on_history_scroll)

        except Exception as e:
            self.logger.error(f"[_append_history_chunk] {e}")
        finally:
            self._loading_history_chunk = False
            
    def _on_main_page_changed(self, index: int):
        """Rời khỏi history_page thì đưa list_history về {self._table_display} dòng mới nhất"""
        if self.ui.stackedWidget_2.widget(index) is not self.ui.history_page:
            self._reset_to_latest_table_display()
        elif self._history_at_latest:
            # Table bị ẩn lúc reset nên scrollbar có thể chưa đúng, cuộn lại khi hiện
            QTimer.singleShot(0, self.ui.list_history.scrollToBottom)

    def _reset_to_latest_table_display(self):
        table = self.ui.list_history
        sb = table.verticalScrollBar()

        if not self.conn:
            return
        if sb.value() >= sb.maximum() - 5 and getattr(self, '_history_at_latest', True):
            return

        try:
            sb.valueChanged.disconnect(self._on_history_scroll)
        except:
            pass

        total_db = self.conn.execute('SELECT COUNT(*) FROM history').fetchone()[0]  # type: ignore

        cursor = self.conn.cursor() # type: ignore
        cursor.execute(
            'SELECT * FROM history ORDER BY id DESC LIMIT ?',
            (self._table_display,)
        )
        rows = cursor.fetchall()
        rows.reverse()

        self._all_rows_cache = []
        for idx, row in enumerate(rows):
            stt = row[1] if row[1] else str(total_db - len(rows) + idx + 1)
            formatted = self._db_row_to_ui(row, stt)
            self._all_rows_cache.append(formatted)

        self._db_offset = total_db - len(rows)
        self._displayed_start = 0
        self._history_at_latest = True

        table.setUpdatesEnabled(False)
        table.clearSpans()
        table.setRowCount(0)
        self._render_chunk(0, len(self._all_rows_cache))
        table.setUpdatesEnabled(True)

        self._apply_span(table)
        table.scrollToBottom()

        sb.valueChanged.connect(self._on_history_scroll)


    def _on_search_changed(self, *args):
        """Hỗ trợ cả textbox và dateTimeChanged"""
        keyword = self.ui.search_data.text().strip().lower()
        group_parts = self.ui.select_group_name.currentText().strip()
        if not self.conn:
            return

        start_date = self.ui.search_data_start_edit.dateTime().toString("yyyy/MM/dd HH:mm")
        end_date = self.ui.search_data_end_edit.dateTime().toString("yyyy/MM/dd HH:mm")
        if not keyword and group_parts in ["All", "全部"] and start_date == end_date:
            self.ui.clear_history_search.hide()
            self.ui.stacked_list_history_page.setCurrentIndex(0)

            self._search_where_clause = ""
            self._search_params = ()
            return
            
        self.ui.clear_history_search.show()
        self.ui.stacked_list_history_page.setCurrentIndex(1)

        try:
            where_clauses = []
            params = []

            if keyword:
                where_clauses.append('LOWER("Name.") LIKE ?')
                params.append(f"%{keyword}%")

            if group_parts not in ["All", "全部"]:
                where_clauses.append('"Group." LIKE ?')
                params.append(f"%{group_parts}%")

            if start_date != end_date:
                where_clauses.append(""" 
                    (SUBSTR("Date.", 15, 4) || '/' || SUBSTR("Date.", 12, 2) || '/' || SUBSTR("Date.", 9, 2) || ' ' || SUBSTR("Date.", 1, 5)) 
                    BETWEEN ? AND ? 
                """)
                params.extend([start_date, end_date])

            where_clauses = [c for c in where_clauses if c.strip()]
            where_clause = " AND ".join(f"({c})" for c in where_clauses)
            self._search_where_clause = where_clause
            self._search_params = tuple(params)

            self._search_fetch_chunk(reset=True)

        except Exception as e:
            self.logger.error(f"Search error: {e}")
            import traceback
            self.logger.error(traceback.format_exc())
            # self._init_table_list_history()

    def _search_fetch_chunk(self, reset=False):
        if not hasattr(self, '_search_where_clause'):
            return

        where_clause = self._search_where_clause
        params = self._search_params
        limit = 1002

        if reset:
            self._search_db_offset = 0

        current_offset = self._search_db_offset
        is_reset = reset

        def _fetch():
            conn = None
            try:
                conn = sqlite3.connect(str(self.history_db_path), check_same_thread=False)
                conn.row_factory = sqlite3.Row

                total = conn.execute(
                    f'SELECT COUNT(*) FROM history WHERE {where_clause}', params
                ).fetchone()[0]

                if is_reset:
                    real_offset = max(0, total - limit)
                else:
                    real_offset = max(0, current_offset - limit)

                cursor = conn.cursor()
                cursor.execute(
                    f'SELECT * FROM history WHERE {where_clause} ORDER BY id ASC LIMIT ? OFFSET ?',
                    params + (limit, real_offset)
                )
                rows = cursor.fetchall()
                conn.close()
                self._search_result_ready.emit((total, real_offset, rows))
            except Exception as e:
                self.logger.error(f"_search_fetch_chunk fetch error: {e}")
                self._search_result_ready.emit((0, 0, []))
            finally:
                if conn:
                    conn.close()

        threading.Thread(target=_fetch, daemon=True).start()

    def _on_search_fetched(self, result):
        try:
            total, real_offset, rows = result

            self._search_db_offset = real_offset

            filtered = []
            for row in rows:
                stt = str(row[1]) if row[1] and str(row[1]).strip() else str(row[0])
                row_list = self._db_row_to_ui(row, stt)
                filtered.append(row_list)

            if getattr(self, '_search_prepend', False):
                self._prepend_search_data(filtered)
                self._search_prepend = False
            else:
                self._load_filtered_data(filtered)

        except Exception as e:
            self.logger.error(f"_on_search_fetched error: {e}")
        finally:
            self._loading_search_chunk = False

    def _prepend_search_data(self, new_chunk: list):
        table            = self.ui.list_history_2
        existing_batches = self._count_batches(table)
        prev_no          = None
        batch_counter    = existing_batches

        table.setUpdatesEnabled(False)
        
        for i, row_data in enumerate(new_chunk):
            current_no = str(row_data[0]) if row_data[0] else ""
            if current_no != prev_no:
                batch_counter += 1
                prev_no = current_no

            table.insertRow(i)
            for col, value in enumerate(row_data):
                table.setItem(i, col,
                    self._make_colored_item(str(value), batch_counter))

        table.setUpdatesEnabled(True)

        overflow = table.rowCount() - self._search_table_display
        if overflow > 0:
            for _ in range(overflow):
                table.removeRow(table.rowCount() - 1)

        self._apply_span(table)

        table.scrollTo(
            table.model().index(len(new_chunk), 0),
            QTableWidget.ScrollHint.PositionAtTop
        )

    def _count_batches(self, table) -> int:
        count = 0
        prev = None
        for row in range(table.rowCount()):
            item = table.item(row, 0)
            if item:
                val = item.text()
                if val != prev:
                    count += 1
                    prev = val
        return count

    def _on_search_scroll(self, value: int):
        sb = self.ui.list_history_2.verticalScrollBar()
        if value > sb.minimum() + 50:
            return
        if getattr(self, '_search_db_offset', 0) <= 0:
            return
        if getattr(self, '_loading_search_chunk', False):
            return

        self._loading_search_chunk = True
        self._search_prepend = True
        QTimer.singleShot(1000, self._search_fetch_chunk)
        
    def _load_filtered_data(self, filtered_data: list):
        table = self.ui.list_history_2
        table.setUpdatesEnabled(False)
        table.setRowCount(0)
        table.setRowCount(len(filtered_data))

        prev_no       = None
        batch_counter = 0

        for row_idx, row_data in enumerate(filtered_data):
            current_no = str(row_data[0]) if row_data[0] else ""
            if current_no != prev_no:
                batch_counter += 1
                prev_no = current_no

            for col, value in enumerate(row_data):
                table.setItem(row_idx, col,
                    self._make_colored_item(str(value), batch_counter))

        row_idx = 0
        while row_idx < table.rowCount():
            current_no = table.item(row_idx, 0).text() if table.item(row_idx, 0) else ""  # type: ignore
            span = 1
            while (row_idx + span < table.rowCount() and
                table.item(row_idx + span, 0) and
                table.item(row_idx + span, 0).text() == current_no):  # type: ignore
                span += 1
            if span > 1:
                for merge_col in [0, 1, 8]:
                    table.setSpan(row_idx, merge_col, span, 1)
            row_idx += span

        table.setUpdatesEnabled(True)
        table.scrollToBottom()
        self._resize_table_columns(table)

    def _resize_table_columns(self, table):
        if not table or table.columnCount() == 0:
            return
        
        screen = QApplication.primaryScreen().availableGeometry()
        is_maximized = (self.width() >= screen.width() - 50 and 
                        self.height() >= screen.height() - 50)

        header = table.horizontalHeader()
        last_col = table.columnCount() - 1
        # if is_maximized:
        #     header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        #     header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        #     header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        #     header.setSectionResizeMode(last_col, QHeaderView.ResizeMode.ResizeToContents)
        # else:
        for col in range(last_col):
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.ResizeToContents)

    def _on_clear_clicked(self):
        self.ui.search_data.clear()
        self.ui.select_group_name.setCurrentIndex(0)
        self._set_time_search_data_start_edit()
        self._set_time_search_data_end_edit()
        self.ui.search_data.setFocus()
        self.ui.list_history.scrollToBottom()

    def _set_time_search_data_start_edit(self):
        now = QDateTime.currentDateTime()
        rounded_time, extra_day = self.round_time(now.time())
        
        self.ui.search_data_start_edit.setDateTime(
            QDateTime(now.date().addDays(extra_day), rounded_time)
        )

    def _set_time_search_data_end_edit(self):
        now = QDateTime.currentDateTime()
        rounded_time, extra_day = self.round_time(now.time())
        
        self.ui.search_data_end_edit.setDateTime(
            QDateTime(now.date().addDays(extra_day), rounded_time)
        )

    def round_time(self, time: QTime):
        minute = time.minute()
        hour = time.hour()

        if minute <= 30:
            return QTime(hour, 30, 0), 0        # (time, ngày cộng thêm)
        else:
            next_hour = hour + 1
            if next_hour >= 24:
                return QTime(0, 0, 0), 1        # Qua ngày mới
            return QTime(next_hour, 0, 0), 0
        

    def _on_logo_clicked(self):
        webbrowser.open("https://www.techlinksilicones.com/")

    def _on_menu_toggle(self):
        self.ui.left_side_menu_widget.slideMenu()

    def home_page_btn(self):
        if self.user == True:
            self.user = False
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.menu_page)

    def pressure_page_btn(self):
        if self.user == True:
            self.user = False
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.temp_press_page)
        self.ui.stackedWidget.setCurrentWidget(self.ui.pressure_page)

    def temperature_page_btn(self):
        if self.user == True:
            self.user = False
        self.ui.home_page_btn.click()
        self.ui.stackedWidget.setCurrentWidget(self.ui.temperature_page)
        
    def device_page_btn(self):
        # self.user = False
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.device_page)
        self.connection_page_btn()

    def connection_page_btn(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.connection_page)
    
    def i_o_page_btn(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.i_o_page)
    
    def history_page_btn(self):
        if self.user == True:
            self.user = False
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.history_page)
        self._set_time_search_data_start_edit()
        self._set_time_search_data_end_edit()

    def alarm_page_btn(self):
        if self.user == True:
            self.user = False
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.alarm_page)

    def next_previous_pressure_page(self):
        index = self.ui.stackedWidget.currentIndex()
        if index == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
        elif index == 1:
            self.ui.stackedWidget.setCurrentIndex(0)

    def _setup_plc_threads(self, state: bool):
        if state:
            self.logger.info("PLC Thread set Off")
            return
        
        if not self.db_dict:
            self.hide_loading.emit()
            if self._current_lang == "en":
                title = "Error"
                content = "DB Layout not found! Cannot start PLC threads."
            elif self._current_lang == "cn":
                title = "错误"
                content = "未找到 DB 佈局！無法啟動 PLC 執行緒."
            elif self._current_lang == "vn":
                title = "Lỗi"
                content = "Không tìm thấy dữ liệu DB！Không thể khởi động PLC."
            ltmessage.error(self, title, content, self._current_lang) # type: ignore
            return

        QTimer.singleShot(100, self._start_write_plc_thread)

    def _start_write_plc_thread(self):
        if getattr(self, "_shutting_down", False):
            return

        if not self._setup_write_plc_thread(
                ip=self.db_dict["ip_plc"],
                db_number=self.db_dict["db_name"],
                db_layout=self.db_dict["DB_LAYOUT"],
                db_size=self.db_dict["DB_TOTAL_BYTES"],
                poll_ms=self.db_dict["write_time"],
                logger_parent=self.stk_mch_folder
            ):
            if self._current_lang == "en":  
                title = "Error"
                content = "Failed to connect to PLC! Try again later."
            elif self._current_lang == "cn":
                title = "错误"
                content = "无法连接 PLC！请稍后再试."
            elif self._current_lang == "vn":
                title = "Lỗi"
                content = "Không thể kết nối với PLC！Vui lòng thử lại sau."
            ltmessage.error(self, title, content, self._current_lang)  # type: ignore

        QTimer.singleShot(100, self._start_read_plc_thread)

    def _start_read_plc_thread(self):
        if getattr(self, "_shutting_down", False):
            return

        if not self._setup_read_plc_thread(
                ip=self.db_dict["ip_plc"],
                db_number=self.db_dict["db_name"],
                db_layout=self.db_dict["DB_LAYOUT"],
                regions=[
                    ("INPUT",  self.db_dict["offsets_input"], self.db_dict["input_size"], self.db_dict["input_read"]),
                    ("ACTUAL", self.db_dict["offsets_data"],  self.db_dict["data_size"],  self.db_dict["data_read"]),
                    ("ERROR",  self.db_dict["offsets_error"], self.db_dict["error_size"], self.db_dict["error_read"]),
                ] + ([("ACTUAL_2", self.db_dict["offsets_data_2"], self.db_dict["data_size_2"], self.db_dict["data_read"])]
                     if self.db_dict.get("data_size_2") else []),
                logger_parent=self.stk_mch_folder
            ):
            if self._current_lang == "en":
                title = "Error"
                content = "Failed to connect to PLC! Try again later."
            elif self._current_lang == "cn":
                title = "错误"
                content = "无法连接 PLC！请稍后再试."
            elif self._current_lang == "vn":
                title = "Lỗi"
                content = "Không thể kết nối với PLC！Vui lòng thử lại sau."
            ltmessage.error(self, title, content, self._current_lang) # type: ignore

    def _performance_communication(self, elapsed_time: float):
        """Cập nhật thời gian đọc PLC lên UI"""
        current_time = time.time()
        
        if not hasattr(self, '_last_ui_update_time'):
            self._last_ui_update_time = 0.0

        if current_time - self._last_ui_update_time >= 1.0:   # 1 giây
            try:
                self.ui.read_time_input.setValue(elapsed_time)  # type: ignore
                self._last_ui_update_time = current_time
            except Exception as e:
                self.logger.warning(f"Cannot update read_time_input: {e}")

    def _setup_read_plc_thread(
            self,
            regions: list[tuple[str, int, int, int]],
            ip: str = "172.16.100.100",
            db_number: Optional[int] = None,
            db_layout: Optional[list[tuple[str, str, int, Any]]] = None,
            logger_parent = None,
        ):
        try:
            if db_number is None:
                raise ValueError("DB number is not defined. Cannot start PLC read thread.")
            elif db_layout is None:
                raise ValueError("DB layout is not defined. Cannot start PLC read thread.")

            self.plc_read_thread = QThread()
            self.plc_read_worker = PLCReadBlock(
                regions=regions,
                name_module="BLOCK",
                ip=ip,
                db_number=db_number,
                db_layout=db_layout,
                string_max_chars=PLC_STRING_MAX_CHARS,
                logger_parent=logger_parent
            )
            self.plc_read_worker.moveToThread(self.plc_read_thread)

            self.plc_read_thread.started.connect(self.plc_read_worker.run)
            self.plc_read_worker.region_ready.connect(self._on_region_ready)
            self.plc_read_worker.init_data.connect(self._set_init_data)
            self.plc_read_worker.connected.connect(self._read_status_plc)
            self.plc_read_worker.elapsed_time.connect(self._performance_communication)
            self.plc_read_worker.error.connect(self._on_plc_read_error)
            self.plc_read_worker.disconnected.connect(self._on_plc_read_disconnected)
            self.plc_read_worker.finished.connect(self.plc_read_thread.quit)
            self.plc_read_worker.finished.connect(self.plc_read_worker.deleteLater)
            self.plc_read_thread.finished.connect(self.plc_read_thread.deleteLater)

            self.plc_read_thread.start()
            if not self.plc_read_thread.isRunning():
                raise Exception("plc_read_thread failed to start")
        except Exception as e:
            self.logger.info("PLC Reader gone wrong: %s", e)
            return False

        self.worker_dict["plc_read_worker"] = self.plc_read_worker
        return True

    def _on_region_ready(self, region: str, data: dict, read_ts: float):
        if region == "INPUT":
            self._data_input(data, read_ts)
        elif region == "ACTUAL":
            self._data_actual(data)
        elif region == "ERROR":
            self._data_error(data)
        elif region == "ACTUAL_2":
            with self._data_lock:
                self.actual_data.update(data)
            self._tube_data_filter(data)

    def _on_plc_read_error(self, message: str):
        self.logger.warning("PLC Read error: %s", message)
        self._raise_alarm("PLC Read", ALARM_ERROR, message)

    def _on_plc_read_disconnected(self):
        self.logger.warning("PLC Read disconnected")
        self._raise_alarm("PLC Read", ALARM_ERROR, "Mất kết nối PLC (Read)")

    def _data_get(self, data: dict):
        with self._data_lock:
            # print("Get: ", len(data))
            self.all_data.update(data)

    _GROUP_UPDATE_S = 0.5
    def _data_actual(self, data: dict):
        with self._data_lock:
            self.actual_data.update(data)
            snapshot = dict(self.actual_data)

        self._data_pressure(snapshot)

        # Tag alarm có thể nằm ở ACTUAL hoặc ERROR tuỳ file DB -> chỉ đánh giá lại khi giá trị ở ACTUAL đổi
        alarm_key = (snapshot.get('Bit_Alarm'), snapshot.get('Alarm_Info'))
        if alarm_key != self._last_actual_alarm:
            self._last_actual_alarm = alarm_key
            self._data_alarm()

        now = time.monotonic()
        if now - self._last_group_update >= self._GROUP_UPDATE_S:
            self._last_group_update = now
            self._data_temp(snapshot)
            self._data_cycle(snapshot)
            self._data_temp_group(snapshot)

            self._heat_data_filter(snapshot)
            self._valve_data_filter(snapshot)
            self._oil_data_filter(snapshot)
            self._tube_data_filter(snapshot)   # Px_Current_TempHeater (nay nằm trong vùng ACTUAL)
            self._cycle_btn_filter()

    def _data_input(self, data: dict, read_ts: float):
        with self._data_lock:
            self.input_data.update(data)
            snapshot = dict(self.input_data)
        self._detect_btn_obj(snapshot, read_ts)
        self._data_ready(snapshot)
        if not self.init_signal:
            self._is_start_checked(snapshot, read_ts)
            self._is_heat_t0_checked(snapshot, read_ts)

    def _data_error(self, data: dict):
        with self._data_lock:
            self.error_data.update(data)
        self._alarm_err_seq += 1
        self._data_alarm()

    def _mapping_actual_data(self):
        with self._data_lock:
            return dict(self.actual_data)

    def _mapping_input_data(self):
        with self._data_lock:
            return dict(self.input_data)

    def _mapping_error_data(self):
        with self._data_lock:
            return dict(self.error_data)

    def _mapping_serial_data(self):
        with self._data_lock:
            return dict(self.serial_data)

    def _setup_write_plc_thread(
            self, 
            ip: str = "172.16.100.100", 
            db_number: Optional[int] = None, 
            db_layout: Optional[List] = None, 
            db_size: Optional[int] = None, 
            poll_ms: int = 500,
            logger_parent = None
        ):
        try:
            if db_number is None:
                raise ValueError("DB number is not defined. Cannot start PLC write thread.")
            elif db_layout is None:
                raise ValueError("DB layout is not defined. Cannot start PLC write thread.")
            elif db_size is None:
                raise ValueError("DB size is not defined. Cannot start PLC write thread.")

            self.plc_writer_thread = QThread()
            self.plc_writer_worker = PLCWrite(
                ip=ip, 
                db_number=db_number, 
                db_layout=db_layout,
                db_size=db_size,
                write_ms=poll_ms,
                logger_parent=logger_parent
            )
            self.plc_writer_worker.moveToThread(self.plc_writer_thread)
            self.plc_writer_thread.started.connect(self.plc_writer_worker.run)
            self.plc_writer_worker.connected.connect(self._write_status_plc)
            self.plc_writer_worker.write_multi_done.connect(self.disable_btn)
            self.plc_writer_worker.write_multi_done.connect(self._on_write_multi_done)
            self.plc_writer_worker.write_multi_failed.connect(self._on_write_multi_failed)
            self.plc_writer_worker.write_bool_done.connect(self._on_write_bool_done)
            self.plc_writer_worker.write_bool_failed.connect(self._on_write_bool_failed)
            self.plc_writer_worker.error.connect(self._on_plc_write_error)
            self.plc_writer_worker.disconnected.connect(self._on_plc_write_disconnected)
            self.plc_writer_worker.finished.connect(self.plc_writer_thread.quit)
            self.plc_writer_worker.finished.connect(self.plc_writer_worker.deleteLater)
            self.plc_writer_thread.finished.connect(self.plc_writer_thread.deleteLater)

            self.plc_writer_thread.start()
            
        except Exception as e:
            self.logger.info("PLC Writer gone wrong:", e)
            return False
        self.thread_dict["plc_writer_thread"] = self.plc_writer_thread
        return True
    
    def _on_plc_write_error(self, message: str):
        # self.logger.warning("PLC Write error: %s", message)
        self._raise_alarm("PLC Write", ALARM_ERROR, message)

    def _on_plc_write_disconnected(self):
        # self.logger.warning("PLC Write disconnected")
        self._raise_alarm("PLC Write", ALARM_ERROR, "PLC disconnected")

    def _setup_serial_threads(self):
        self.serial_data_thread = QThread()
        self.serial_data_worker = HYFWSerialRead(
            name_module="HEATER_0",
            port_keyword="CH340",
            device_id=1,
            poll_ms=200,
            retry_ms=3000,
            scan_ms=1000,
            connect_timeout=5.0,
            logger_parent=self.stk_mch_folder
        )
        self.serial_data_worker.moveToThread(self.serial_data_thread)

        self.serial_data_thread.started.connect(self.serial_data_worker.run)
        self.serial_data_worker.data_ser.connect(self._data_port_com)
        self.serial_data_worker.finished.connect(self.serial_data_thread.quit)

        self.serial_data_worker.error.connect(self._on_serial_error)
        self.serial_data_worker.disconnected.connect(self._on_serial_disconnected)
        self.serial_data_worker.connected.connect(self._on_serial_connected)
        self.serial_data_worker.port_name.connect(self._serial_port_check)

        self.serial_data_thread.start()

    def _data_port_com(self, data: dict):
        with self._data_lock:
            self.serial_data.update(data)

    def _on_serial_error(self, message: str):
        self.logger.warning("Serial error: %s", message)
        self._raise_alarm("Serial", ALARM_WARNING, message)

    def _on_serial_connected(self, ok: bool):
        if self.serial_read_connection != ok:
            self.serial_read_connection = ok
        if ok:
            self._clear_alarm("Serial")
        elif "Serial" not in self._alarm_active_rows:
            # Giữ nguyên nội dung lỗi chi tiết từ _on_serial_error nếu đã có
            self._raise_alarm("Serial", ALARM_WARNING, "Port COM lost connection")

    def _on_serial_disconnected(self):
        self.logger.warning("Serial disconnected")
        self._raise_alarm("Serial", ALARM_WARNING, "Port COM lost connection")

    def _serial_port_check(self, is_name: str):
        if self.ui.port_display.text() != is_name:
            self.ui.port_display.setText(is_name)
        
    def _data_temp(self, data: dict):
        # def _t(label, fn):
            # t = time.perf_counter()
            # fn()
            # ms = (time.perf_counter() - t) * 1000
            # if ms > 1:
                # print(f"  [{label}] {ms:.1f}ms")
        try:
            # _t("i_o_group_3", lambda: 
            self._current_temp_display_P1([
                float(data.get('P1_Current_Temp1', 0.0)),
                float(data.get('P1_Current_Temp2', 0.0)),
                float(data.get('P1_Current_Temp3', 0.0)),
            ])
            self._current_temp_display_P2([
                float(data.get('P2_Current_Temp1', 0.0)),
                float(data.get('P2_Current_Temp2', 0.0)),
                float(data.get('P2_Current_Temp3', 0.0)),
            ])
            self._current_temp_display_P3([
                float(data.get('P3_Current_Temp1', 0.0)),
                float(data.get('P3_Current_Temp2', 0.0)),
                float(data.get('P3_Current_Temp3', 0.0)),
            ])
        except Exception as e:
            self._raise_alarm("Data Error", ALARM_WARNING, f"PLC Data Processing Error: {e}")

    def _data_AI(self, data_actual: dict, data_input: dict, data_error: dict, data_serial: dict):
        # print("AI Data:", data_actual, data_input, data_error, data_serial)
        if not any(isinstance(d, dict) and d for d in (data_actual, data_input, data_error, data_serial)):
            return

        try:
            self._ai_data_batch_counter += 1

            record = dict.fromkeys(self._ai_expected_keys)
            record["datetime"] = time.strftime("%H:%M:%S")
            record["No."] = str(self._ai_data_batch_counter)
            record["PLC Connection"] = int(bool(self.plc_read_connection))
            record["Serial Connection"] = int(bool(self.serial_read_connection))

            with self._data_lock:  
                for d in (data_actual, data_input, data_error, data_serial):
                    if not isinstance(d, dict) or not d:
                        continue

                    unknown_keys = d.keys() - record.keys() - self._ai_warned_keys
                    self._ai_warned_keys |= unknown_keys
                    if unknown_keys and self.logger:
                        self.logger.warning(f"[AI Training] Key chưa khai báo trong schema: {unknown_keys}")

                    # Bit BOOL ghi dạng 1/0 thay vì True/False
                    record.update({k: int(v) if isinstance(v, bool) else v
                                   for k, v in d.items() if k in record})

            self.data_buffer.append(record)

            if len(self.data_buffer) >= self.buffer_size:
                self._flush_buffer(self.data_buffer)
                self.data_buffer = []

        except Exception as e:
            if self.logger:
                self.logger.error(f"[AI Training] Error: {e}")

    def _flush_buffer(self, buffer: list):
        if not buffer:
            return

        date_str = time.strftime("%Y%m%d")
        if getattr(self, "_ai_csv_date", None) != date_str:
            # File trong ngày có header khác schema hiện tại -> ghi sang ai_YYYYMMDD_v2.csv, _v3...
            file_path = self.ai_data_folder / f"ai_{date_str}.csv"
            n = 1
            while file_path.exists():
                with open(file_path, newline='', encoding='utf-8') as f:
                    if next(csv.reader(f), None) == self._ai_expected_keys:
                        break
                n += 1
                file_path = self.ai_data_folder / f"ai_{date_str}_v{n}.csv"
            self._ai_csv_date, self._ai_csv_path = date_str, file_path
        file_path = self._ai_csv_path
        file_exists = file_path.exists()

        try:
            with open(file_path, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self._ai_expected_keys, extrasaction='ignore')
                if not file_exists:
                    writer.writeheader()
                writer.writerows(buffer)

        except Exception as e:
            self.logger.error(f"Flush error: {e}")

    def _data_pressure(self, data: dict):
        # def _t(label, fn):
            # t = time.perf_counter()
            # fn()
            # ms = (time.perf_counter() - t) * 1000
            # if ms > 1:
                # print(f"  [{label}] {ms:.1f}ms")
        try:
            self._current_pressure_display_P1([
                float(data.get('P1_Current_PressureHose', 0.00)),
                float(data.get('P1_Current_Air_FillingTime', 0)/1000),
                float(data.get('P1_Current_Air_HoldingTime', 0)/1000),
                float(data.get('P1_Current_Air_ReleaseTime', 0)/1000),
                float(data.get('P1_Current_PressureITV', 0.00)),
            ])
            self._current_pressure_display_P2([
                float(data.get('P2_Current_PressureHose', 0.00)),
                float(data.get('P2_Current_Air_FillingTime', 0)/1000),
                float(data.get('P2_Current_Air_HoldingTime', 0)/1000),
                float(data.get('P2_Current_Air_ReleaseTime', 0)/1000),
                float(data.get('P2_Current_PressureITV', 0.00)),
            ])
            self._current_pressure_display_P3([
                float(data.get('P3_Current_PressureHose', 0.00)),
                float(data.get('P3_Current_Air_FillingTime', 0)/1000),
                float(data.get('P3_Current_Air_HoldingTime', 0)/1000),
                float(data.get('P3_Current_Air_ReleaseTime', 0)/1000),
                float(data.get('P3_Current_PressureITV', 0.00)),
            ])
        except Exception as e:
            self._raise_alarm("Data Error", ALARM_WARNING, f"PLC Data Processing Error: {e}")

    def _data_cycle(self, data: dict):
        # def _t(label, fn):
            # t = time.perf_counter()
            # fn()
            # ms = (time.perf_counter() - t) * 1000
            # if ms > 1:
                # print(f"  [{label}] {ms:.1f}ms")
        try:
            # _t("group_a", lambda: 
            self._current_cycle_display_P1([
                float(data.get('P1_Current_Oil_Start_Time', 0)/1000),
                float(data.get('P1_Current_Oil_End_Time', 0)/1000),
                int(data.get('P1_Number_Test_Times', 0)),
                int(data.get('P1_Number_Test_Times', 0)),
            ])
            # )

            # _t("group_b", lambda: 
            self._current_cycle_display_P2([
                float(data.get('P2_Current_Oil_Start_Time', 0)/1000),
                float(data.get('P2_Current_Oil_End_Time', 0)/1000),
                int(data.get('P2_Number_Test_Times', 0)),
                int(data.get('P2_Number_Test_Times', 0)),
            ])
            # )

            # _t("group_c", lambda: 
            self._current_cycle_display_P3([
                float(data.get('P3_Current_Oil_Start_Time', 0)/1000),
                float(data.get('P3_Current_Oil_End_Time', 0)/1000),
                int(data.get('P3_Number_Test_Times', 0)),
                int(data.get('P3_Number_Test_Times', 0)),
            ])
            # )
        except Exception as e:
            self._raise_alarm("Data Error", ALARM_WARNING, f"PLC Data Processing Error: {e}")

    def _data_web_socket(self, data: dict):
        try:
            self._plc_queue.put_nowait(data) # type: ignore
        except Exception:
            pass

    def _data_ready(self, data: dict):
        # def _t(label, fn):
            # t = time.perf_counter()
            # fn()
            # ms = (time.perf_counter() - t) * 1000
            # if ms > 1:
                # print(f"  [{label}] {ms:.1f}ms")
        # print(data)
        try:
            if data == {}:
                return
            if self.init_signal:
                self._init_pressure_group_sv_obj([
                    int(data.get('P1_CountTimes', 0)),
                    float(data.get('P1_Oil_Start_Time', 0)/1000),
                    float(data.get('P1_Oil_End_Time', 0)/1000),
                    float(data.get('P1_Air_FillingTime', 0)/1000),
                    float(data.get('P1_Air_HoldingTime', 0)/1000),
                    float(data.get('P1_Air_ReleaseTime', 0)/1000),
                    float(data.get('P1_PressureSetting', 0.00)),
                    self.for_display_temp(float(data.get('P1_TemperatureSetting', 0.0))),
                    self.for_display_temp(float(data.get('P1_TempLimitHIGH', 0.0))),
                    self.for_display_temp(float(data.get('P1_TempLimitLOW', 0.0))),
                    self.for_display_temp(float(data.get('P1_Temp1Offset', 0.0))),
                    self.for_display_temp(float(data.get('P1_Temp2Offset', 0.0))),
                    self.for_display_temp(float(data.get('P1_Temp3Offset', 0.0)))
                ],
                [
                    int(data.get('P2_CountTimes', 0)),
                    float(data.get('P2_Oil_Start_Time', 0)/1000),
                    float(data.get('P2_Oil_End_Time', 0)/1000),
                    float(data.get('P2_Air_FillingTime', 0)/1000),
                    float(data.get('P2_Air_HoldingTime', 0)/1000),
                    float(data.get('P2_Air_ReleaseTime', 0)/1000),
                    float(data.get('P2_PressureSetting', 0.00)),
                    self.for_display_temp(float(data.get('P2_TemperatureSetting', 0.0))),
                    self.for_display_temp(float(data.get('P2_TempLimitHIGH', 0.0))),
                    self.for_display_temp(float(data.get('P2_TempLimitLOW', 0.0))),
                    self.for_display_temp(float(data.get('P2_Temp1Offset', 0.0))),
                    self.for_display_temp(float(data.get('P2_Temp2Offset', 0.0))),
                    self.for_display_temp(float(data.get('P2_Temp3Offset', 0.0)))
                ],
                [
                    int(data.get('P3_CountTimes', 0)),
                    float(data.get('P3_Oil_Start_Time', 0)/1000),
                    float(data.get('P3_Oil_End_Time', 0)/1000),
                    float(data.get('P3_Air_FillingTime', 0)/1000),
                    float(data.get('P3_Air_HoldingTime', 0)/1000),
                    float(data.get('P3_Air_ReleaseTime', 0)/1000),
                    float(data.get('P3_PressureSetting', 0.00)),
                    self.for_display_temp(float(data.get('P3_TemperatureSetting', 0.0))),
                    self.for_display_temp(float(data.get('P3_TempLimitHIGH', 0.0))),
                    self.for_display_temp(float(data.get('P3_TempLimitLOW', 0.0))),
                    self.for_display_temp(float(data.get('P3_Temp1Offset', 0.0))),
                    self.for_display_temp(float(data.get('P3_Temp2Offset', 0.0))),
                    self.for_display_temp(float(data.get('P3_Temp3Offset', 0.0)))
                ],
                [
                    self.for_display_temp(float(data.get('T0_TemperatureSetting', 0.0))),
                    self.for_display_temp(float(data.get('T0_TempLimitHIGH', 0.0))),
                    self.for_display_temp(float(data.get('T0_TempLimitLOW', 0.0))),
                    self.for_display_temp(float(data.get('T0_TempOffset', 0.0)))
                ])
                for tag, obj in zip(("P1_TempLimitHeater", "P2_TempLimitHeater", "P3_TempLimitHeater"),
                                    self.tube_sv_obj):
                    obj.blockSignals(True)
                    obj.setValue(self.for_display_temp(float(data.get(tag, 0.0))))
                    obj.blockSignals(False)
                self.init_signal = False
                return
            
        except Exception as e:
            self.logger.error("[Main]-[_data_ready]:PLC Data Processing Error: %s", e)

    def _data_temp_group(self, data: dict):
        # def _t(label, fn):
            # t = time.perf_counter()
            # fn()
            # ms = (time.perf_counter() - t) * 1000
            # if ms > 1:
                # print(f"  [{label}] {ms:.1f}ms")
        try:
            # _t("t0_data", lambda: 
            self._t0_data_filter([
                float(data.get('T0_Current_Temp', 0.0))
            ])
            # )
            # _t("at_data", lambda: 
            self._at_data_filter([
                float(data.get('P1_Current_Temp1', 0.0)),
                float(data.get('P1_Current_Temp2', 0.0)),
                float(data.get('P1_Current_Temp3', 0.0))
            ])
            # )

            # _t("bt_data", lambda: 
            self._bt_data_filter([
                float(data.get('P2_Current_Temp1', 0.0)),
                float(data.get('P2_Current_Temp2', 0.0)),
                float(data.get('P2_Current_Temp3', 0.0))
            ])
            # )

            # _t("ct_data", lambda: 
            self._ct_data_filter([
                float(data.get('P3_Current_Temp1', 0.0)),
                float(data.get('P3_Current_Temp2', 0.0)),
                float(data.get('P3_Current_Temp3', 0.0))
            ])
            # _t("i_o_group_3", lambda: 
            self._i_o_group_3_filter([
                float(data.get('T0_Current_Temp', 0.0)),
                float(data.get('P1_Current_Temp1', 0.0)),
                float(data.get('P1_Current_Temp2', 0.0)),
                float(data.get('P1_Current_Temp3', 0.0)),
                float(data.get('P2_Current_Temp1', 0.0)),
                float(data.get('P2_Current_Temp2', 0.0)),
                float(data.get('P2_Current_Temp3', 0.0)),
                float(data.get('P3_Current_Temp1', 0.0)),
                float(data.get('P3_Current_Temp2', 0.0)),
                float(data.get('P3_Current_Temp3', 0.0)),
                float(data.get('P1_Current_PressureHose', 0.00)),
                float(data.get('P2_Current_PressureHose', 0.00)),
                float(data.get('P3_Current_PressureHose', 0.00)),
                float(data.get('P1_Current_PressureITV', 0.0)),
                float(data.get('P2_Current_PressureITV', 0.0)),
                float(data.get('P3_Current_PressureITV', 0.0))
            ])
            # )
        except Exception as e:
            self.logger.error("[Main]-[_data_ready]:PLC Data Processing Error: %s", e)

    def _data_table(self, data: dict):
        # def _t(label, fn):
        #     t = time.perf_counter()
        #     try:
        #         fn()
        #     except Exception as e:
        #         self.logger.error(f"Error in {label}: {e}") if hasattr(self, 'logger') else print(f"Error in {label}: {e}")
        #     ms = (time.perf_counter() - t) * 1000
        #     if ms > 1.0:
        #         print(f"  [{label}] {ms:.1f}ms")

        # # if self.ui.start_stop_btn.isChecked() != 1:
        # #     return

        # # _t("_data_table", lambda: self._process_groups(data))
        self._process_groups(data)

    def _process_groups(self, data: dict):
        groups = []

        if self.ui.heat_btn_a.isChecked() or self.ui.vacuum_btn_a.isChecked():
            groups.append({
                "group": "Group A",
                "pressure": float(data.get('P1_Current_PressureHose', 0.0)),
                "temp":     float(data.get('T0_Current_Temp', 0.0)),
                "front":    float(data.get('P1_Current_Temp1', 0.0)),
                "mid":      float(data.get('P1_Current_Temp2', 0.0)),
                "end":      float(data.get('P1_Current_Temp3', 0.0))
            })

        if self.ui.heat_btn_b.isChecked() or self.ui.vacuum_btn_b.isChecked():
            groups.append({
                "group": "Group B",
                "pressure": float(data.get('P2_Current_PressureHose', 0.0)),
                "temp":     float(data.get('T0_Current_Temp', 0.0)),
                "front":    float(data.get('P2_Current_Temp1', 0.0)),
                "mid":      float(data.get('P2_Current_Temp2', 0.0)),
                "end":      float(data.get('P2_Current_Temp3', 0.0))
            })

        if self.ui.heat_btn_c.isChecked() or self.ui.vacuum_btn_c.isChecked():
            groups.append({
                "group": "Group C",
                "pressure": float(data.get('P3_Current_PressureHose', 0.0)),
                "temp":     float(data.get('T0_Current_Temp', 0.0)),
                "front":    float(data.get('P3_Current_Temp1', 0.0)),
                "mid":      float(data.get('P3_Current_Temp2', 0.0)),
                "end":      float(data.get('P3_Current_Temp3', 0.0))
            })

        if groups:
            self.add_row_to_list_history(self.ui.code_display.text(), groups)

    def _data_alarm(self, timeout_token=None):
        """Bit_Alarm + Alarm_Info. Thường Bit_Alarm ở vùng ACTUAL, Alarm_Info ở vùng ERROR,
        nhưng tuỳ nhãn vùng trong file DB mà tag có thể rơi vào vùng còn lại -> tìm ở cả 2.

        Bit_Alarm (ACTUAL, ~100 ms) thường về TRƯỚC Alarm_Info (ERROR, ~1500 ms). Nếu ghi
        alarm ngay lúc Bit_Alarm bật thì nội dung là "PLC Alarm" hoặc nội dung CŨ của lỗi
        trước, rồi khi Alarm_Info về lại sinh thêm 1 dòng → lịch sử bị dòng thừa/sai.
        → Khi Bit_Alarm vừa bật: chờ lần đọc vùng ERROR kế tiếp rồi mới ghi; quá thời gian
          chờ (error_read + 1 s) thì vẫn ghi với nội dung đang có để không bỏ sót lỗi."""
        def _get(tag, default):
            if tag in self.actual_data:
                return self.actual_data[tag]
            return self.error_data.get(tag, default)
        try:
            with self._data_lock:
                bit_alarm = bool(_get('Bit_Alarm', False))
                alarm_text = str(_get('Alarm_Info', '') or '').strip()
                info_in_actual = 'Alarm_Info' in self.actual_data

            if not bit_alarm:
                self._alarm_pending = None
                self._raise_alarm("PLC", ALARM_ERROR, "")
                return

            if "PLC" not in self._alarm_active_rows and not info_in_actual:
                if self._alarm_pending is None:
                    # Bit_Alarm vừa bật → bắt đầu chờ Alarm_Info mới
                    self._alarm_pending_token += 1
                    token = self._alarm_pending_token
                    self._alarm_pending = (self._alarm_err_seq, token)
                    db = getattr(self, "db_dict", None) or {}
                    wait_ms = int(db.get("error_read", 1500)) + 1000
                    QTimer.singleShot(wait_ms, self, lambda t=token: self._data_alarm(timeout_token=t))
                    return
                seq0, token = self._alarm_pending
                fresh = self._alarm_err_seq > seq0          # đã có lần đọc ERROR sau khi bit bật
                timed_out = timeout_token == token
                if not (fresh or timed_out):
                    return

            self._alarm_pending = None
            self._raise_alarm("PLC", ALARM_ERROR, alarm_text or "PLC Alarm")
        except Exception as e:
            self.logger.error("[Main]-[_data_alarm]:PLC Data Processing Error: %s", e)

    def _data_serial(self, data: dict):
        try:
            def _to_float(value, default=0.0):
                return default if value is None else float(value)
            self._serial_data_filter([
                _to_float(data.get('V_A_HEATER_0'), 0.0),
                _to_float(data.get('V_B_HEATER_0'), 0.0),
                _to_float(data.get('V_C_HEATER_0'), 0.0),
                _to_float(data.get('I_A_HEATER_0'), 0.0),
                _to_float(data.get('I_B_HEATER_0'), 0.0),
                _to_float(data.get('I_C_HEATER_0'), 0.0),
                _to_float(data.get('power_factor_HEATER_0'), 0.0),
                _to_float(data.get('frequency_Hz_HEATER_0'), 0.0),
            ])
        except Exception as e:
            self.logger.error("[Main]-[_data_serial]:Serial Data Processing Error: %s", e)

    def _set_init_data(self):
        self.init_signal = True
        
    def _detect_btn_obj(self, data: dict, read_ts: float):
        """
        Đồng bộ trạng thái nút theo PLC, gọi mỗi khi luồng PLC Read (input) có data mới.
        \n read_ts: time.perf_counter() lúc luồng đọc bắt đầu db_read gói data này
        """
        if self.init_signal:
            return
        sync_map = [
            (self.ui.heat_btn_a,      "P1_Start_Heat",     "_heating_a_flag"),
            (self.ui.vacuum_btn_a,    "P1_Start_Pressure", "_vacuum_a_flag"),
            (self.ui.refuel_btn_a,    "P1_Start_Oil",      "_oil_a_flag"),
            (self.ui.set_cycle_a_btn, "P1_BitCountTimes",  "_count_a_flag"),

            (self.ui.heat_btn_b,      "P2_Start_Heat",     "_heating_b_flag"),
            (self.ui.vacuum_btn_b,    "P2_Start_Pressure", "_vacuum_b_flag"),
            (self.ui.refuel_btn_b,    "P2_Start_Oil",      "_oil_b_flag"),
            (self.ui.set_cycle_b_btn, "P2_BitCountTimes",  "_count_b_flag"),

            (self.ui.heat_btn_c,      "P3_Start_Heat",     "_heating_c_flag"),
            (self.ui.vacuum_btn_c,    "P3_Start_Pressure", "_vacuum_c_flag"),
            (self.ui.refuel_btn_c,    "P3_Start_Oil",      "_oil_c_flag"),
            (self.ui.set_cycle_c_btn, "P3_BitCountTimes",  "_count_c_flag"),
        ]
        def on(tag):
            return bool(data.get(tag, False))
        for btn, tag, flag_name in sync_map:
            if self._should_ignore_status(tag, read_ts):
                continue
            plc_value = on(tag)
            if btn.isChecked() != plc_value:
                setattr(self, flag_name, True)
                btn.setChecked(plc_value)
                setattr(self, flag_name, False)
                # Đồng bộ theo PLC không gửi lệnh write
                self._pending_cmd.pop(tag, None)

    _PULSE_HOLD_MS = 200  # thời gian giữ mức True của lệnh xung STOP / T0_Stop_Heat

    def _is_start_checked(self, data: dict, read_ts: float):
        if self._should_ignore_status("START", read_ts):
            return
        if self.ui.start_stop_stacked.currentIndex() == 1 and not data.get("START", False):
            self.ui.stop_start_btn.click()
        elif self.ui.start_stop_stacked.currentIndex() == 0 and data.get("START", False):
            self.ui.start_stop_btn.click()

    def _is_heat_t0_checked(self, data: dict, read_ts: float):
        if self._should_ignore_status("T0_Start_Heat", read_ts):
            return
        if self.ui.heat_t0_stacked.currentIndex() == 1 and not data.get("T0_Start_Heat", False):
            self.ui.heat_off_btn_t0.click()
        elif self.ui.heat_t0_stacked.currentIndex() == 0 and data.get("T0_Start_Heat", False):
            self.ui.heat_on_btn_t0.click()

    _CMD_ACK_TIMEOUT = 10.0  # dự phòng khi không nhận được write_bool_done/failed

    def _mark_cmd(self, tag: str, value: bool):
        """Ghi nhận lệnh bấm nút vừa gửi xuống PLC, chờ PLC Write xác nhận"""
        if self.init_signal:
            return
        self._pending_cmd[tag] = {"value": bool(value), "t_sent": time.perf_counter(), "t_done": None}

    def _on_write_bool_done(self, name: str, value: bool, t_done: float):
        cmd = self._pending_cmd.get(name)
        if cmd is not None and cmd["value"] == value: # Bỏ qua xác nhận của lệnh cũ nếu đã toggle lại giá trị khác
            cmd["t_done"] = t_done

    def _on_write_multi_done(self, group: str, ok: bool):
        if ok:
            self._clear_alarm(f"PLC Save {group}")

    def _on_write_multi_failed(self, group: str, reason: str):
        self.logger.warning("[Main]-[write_multi]: Group %s save failed: %s", group, reason)
        self.disable_btn(group, True)
        self._raise_alarm(f"PLC Save {group}", ALARM_WARNING, f"Ghi thông số Group {group} xuống PLC thất bại")

    def _on_write_bool_failed(self, name: str, value: bool):
        cmd = self._pending_cmd.get(name)
        if cmd is not None and cmd["value"] == value:
            del self._pending_cmd[name]

    def _should_ignore_status(self, tag: str, read_ts: float) -> bool:
        """
        Bỏ qua trạng thái PLC của tag khi lệnh bấm nút chưa được xác nhận
        """
        cmd = self._pending_cmd.get(tag)
        if cmd is None:
            return False

        if cmd["t_done"] is None:
            if time.perf_counter() - cmd["t_sent"] < self._CMD_ACK_TIMEOUT:
                return True
            del self._pending_cmd[tag]
            return False

        if read_ts <= cmd["t_done"]:
            return True

        del self._pending_cmd[tag]
        return False

    def _init_pressure_group_sv_obj(self, list_init_a, list_init_b, list_init_c, list_init_t0):
        for i in range(len(self.list_for_import_a)):
            self.list_for_import_a[i].blockSignals(True)
            self.list_for_import_a[i].setValue(list_init_a[i])
            self.list_for_import_a[i].blockSignals(False)

            self.list_for_import_b[i].blockSignals(True)
            self.list_for_import_b[i].setValue(list_init_b[i])
            self.list_for_import_b[i].blockSignals(False)

            self.list_for_import_c[i].blockSignals(True)
            self.list_for_import_c[i].setValue(list_init_c[i])
            self.list_for_import_c[i].blockSignals(False)   

        for i in range(len(self.list_for_import_t0)):
            self.list_for_import_t0[i].blockSignals(True)
            self.list_for_import_t0[i].setValue(list_init_t0[i])
            self.list_for_import_t0[i].blockSignals(False)

        self._sync_temp_sv_mirror()

    def _sync_temp_sv_mirror(self):
        """Đồng bộ at_sv / bt_sv / ct_sv theo pressure_sv_X_1 (không phát signal)"""
        for widget_name, (_, mirror_widget) in TEMP_SV_MIRROR.items():
            mirror = getattr(self.ui, mirror_widget)
            mirror.blockSignals(True)
            mirror.setValue(getattr(self.ui, widget_name).value())
            mirror.blockSignals(False)

    def _unblock_import_widgets(self):
        for obj in self.list_for_import_a + self.list_for_import_b + self.list_for_import_c + self.list_for_import_t0:
            obj.blockSignals(False)
        for mirror_widget in TEMP_SV_REVERSE_MIRROR:
            getattr(self.ui, mirror_widget).blockSignals(False)

    def _read_status_plc(self, connected: bool):
        page = 0 if connected else 1
        if self.ui.sys_state_stacked_wid_40.currentIndex() != page:
            self.ui.sys_state_stacked_wid_40.setCurrentIndex(page)

        if connected == self.plc_read_connection:
            return

        self.plc_read_connection = connected
        if connected:
            self._clear_alarm("PLC Read")
            self.data_serial_timer.start()

    def _write_status_plc(self, connected: bool):
        page = 0 if connected else 1
        if self.ui.sys_state_stacked_wid_42.currentIndex() != page:
            self.ui.sys_state_stacked_wid_42.setCurrentIndex(page)

        if connected == self.plc_writer_connection:
            return
        self.plc_writer_connection = connected
        if connected:
            self._clear_alarm("PLC Write")

    def _data_group_filter(self, list_group_a_recv, list_group_b_recv, list_group_c_recv):
        groups_recv = [list_group_a_recv, list_group_b_recv, list_group_c_recv]
        if not all(isinstance(g, list) for g in groups_recv):
            return

        pv_avg = sum(g[1] for g in groups_recv) / 3

        group_ui_map = [
            ("pressure_pv_a", list_group_a_recv),
            ("pressure_pv_b", list_group_b_recv),
            ("pressure_pv_c", list_group_c_recv),
        ]

        for prefix, data in group_ui_map:
            getattr(self.ui, f"{prefix}_2").setValue(self.for_display_temp(data[2]))
            getattr(self.ui, f"{prefix}_3").setValue(self.for_display_temp(data[3]))
            getattr(self.ui, f"{prefix}_4").setValue(self.for_display_temp(data[4]))
            getattr(self.ui, f"{prefix}_5").setValue(data[0])
            getattr(self.ui, f"{prefix}_12").setValue(data[5])

        btn_map = [
            ("Group A", list_group_a_recv, "heat_btn_a", "vacuum_btn_a"),
            ("Group B", list_group_b_recv, "heat_btn_b", "vacuum_btn_b"),
            ("Group C", list_group_c_recv, "heat_btn_c", "vacuum_btn_c"),
        ]

        active_groups = [
            (label, data)
            for label, data, heat_btn, vacuum_btn in btn_map
            if getattr(self.ui, heat_btn).isChecked() or getattr(self.ui, vacuum_btn).isChecked()
        ]

        if not active_groups:
            return

        now = time.time()
        if now - self._last_history_time < self.ui.table_write_cycle.value():
            return

        self._last_history_time = now

        history_groups = [
            {
                "group": label,
                "pressure": data[0],
                "temp": self.for_display_temp(pv_avg),
                "front": self.for_display_temp(data[2]),
                "mid":   self.for_display_temp(data[3]),
                "end":   self.for_display_temp(data[4]),
            }
            for label, data in active_groups
        ]

        self.add_row_to_list_history(self.ui.code_display.text(), history_groups)

    def _t0_input_heat_filter(self, list_t0_input_recv):
        if not list_t0_input_recv[1]:
            self.ui.i_o_group_1_switch_1.setCurrentIndex(1)
            if list_t0_input_recv[0]:
                self.ui.i_o_group_1_switch_1.setCurrentIndex(0)

    @staticmethod
    def _apply_switch(pairs, data: dict):
        for tag, obj in pairs:
            obj.setCurrentIndex(int(bool(data.get(tag, False))))

    def _heat_data_filter(self, data: dict):
        """Out_Heat0..3 -> switch 1, 2, 6, 10"""
        self._apply_switch(self.io_heat_obj, data)

    def _valve_data_filter(self, data: dict):
        """Out_Valve1..3-IN/OUT -> switch 3, 7, 11
        0 (off): IN = OUT = False | 1 (on): IN = True | 2 (wait): OUT = True"""
        for tag_in, tag_out, obj in self.io_valve_obj:
            if data.get(tag_in, False):
                idx = 1
            elif data.get(tag_out, False):
                idx = 2
            else:
                idx = 0
            obj.setCurrentIndex(idx)

    def _oil_data_filter(self, data: dict):
        """Out_Valve1..3-OIL -> switch 4, 8, 12"""
        self._apply_switch(self.io_oil_obj, data)

    def _cycle_btn_filter(self):
        """Trạng thái nút cycle A/B/C -> switch 5, 9, 13"""
        for btn, obj in self.io_cycle_obj:
            obj.setCurrentIndex(int(btn.isChecked()))

    def _i_o_group_3_filter(self, values):
        for i, (obj, value) in enumerate(zip(self.i_o_group_3_obj, values)):
            v = round(value, 2)
            if v != self._last_i_o_group_3[i]:
                obj.setValue(value)
                self._last_i_o_group_3[i] = v

    def _serial_data_filter(self, values):
        for i, (obj, value) in enumerate(zip(self.i_o_group_4_obj, values)):
            v = round(value, 2)
            if v != self._last_i_o_group_4[i]:
                obj.setValue(value)
                self._last_i_o_group_4[i] = v

    def _group_a_data_filter(self, list_group_a_recv):
        try:
            for i, val_a in enumerate(list_group_a_recv):
                v = round(val_a if i >= 3 else self.for_display_temp(val_a), 2)
                self.pressure_a_pv_obj[i].setValue(v)
        except Exception as e:
            self.logger.error("A err: %s", e)

    def _group_b_data_filter(self, list_group_b_recv):
        try:
            for i, val_b in enumerate(list_group_b_recv):
                v = round(val_b if i >= 3 else self.for_display_temp(val_b), 2)
                self.pressure_b_pv_obj[i].setValue(v)
        except Exception as e:
            self.logger.error("B err: %s", e)

    def _group_c_data_filter(self, list_group_c_recv):
        try:
            for i, val_c in enumerate(list_group_c_recv):
                v = round(val_c if i >= 3 else self.for_display_temp(val_c), 2)
                self.pressure_c_pv_obj[i].setValue(v)
        except Exception as e:
            self.logger.error("C err: %s", e)

    def _t0_data_filter(self, list_group_t0_recv):
        v = round(self.for_display_temp(list_group_t0_recv[0]), 2)
        if v != self._last_t0_pv:
            self.temp_pv_obj[0].setValue(v)
            self._last_t0_pv = v

    def _current_temp_display_P1(self, list_temp_a_recv):
        try:
            for i, val_a in enumerate(list_temp_a_recv):
                if val_a != self._last_cur_temp_a[i]:
                    val_a = round(self.for_display_temp(val_a), 1)
                    self.current_temp_a_pv_obj[i].setValue(val_a)
                    self._last_cur_temp_a[i] = val_a
        except Exception as e:
            self.logger.error("A Temperature Display err: %s", e)

    def _current_temp_display_P2(self, list_temp_b_recv):
        try:
            for i, val_b in enumerate(list_temp_b_recv):
                if val_b != self._last_cur_temp_b[i]:
                    val_b = round(self.for_display_temp(val_b), 1)
                    self.current_temp_b_pv_obj[i].setValue(val_b)
                    self._last_cur_temp_b[i] = val_b
        except Exception as e:
            self.logger.error("B Temperature Display err: %s", e)

    def _current_temp_display_P3(self, list_temp_c_recv):
        try:
            for i, val_c in enumerate(list_temp_c_recv):
                if val_c != self._last_cur_temp_c[i]:
                    val_c = round(self.for_display_temp(val_c), 1)
                    self.current_temp_c_pv_obj[i].setValue(val_c)
                    self._last_cur_temp_c[i] = val_c
        except Exception as e:
            self.logger.error("C Temperature Display err: %s", e)

    def _current_pressure_display_P1(self, list_pressure_a_recv):
        try:
            for i, val_a in enumerate(list_pressure_a_recv):
                if val_a != self._last_cur_pressure_a[i]:
                    val_a = round(val_a, 2)
                    self.current_pressure_a_pv_obj[i].setValue(val_a)
                    self._last_cur_pressure_a[i] = val_a
        except Exception as e:
            self.logger.error("A Pressure Display err: %s", e)

    def _current_pressure_display_P2(self, list_pressure_b_recv):
        try:
            for i, val_b in enumerate(list_pressure_b_recv):
                if val_b != self._last_cur_pressure_b[i]:
                    val_b = round(val_b, 2)
                    self.current_pressure_b_pv_obj[i].setValue(val_b)
                    self._last_cur_pressure_b[i] = val_b
        except Exception as e:
            self.logger.error("B Pressure Display err: %s", e)

    def _current_pressure_display_P3(self, list_pressure_c_recv):
        try:
            for i, val_c in enumerate(list_pressure_c_recv):
                if val_c != self._last_cur_pressure_c[i]:
                    val_c = round(val_c, 2)
                    self.current_pressure_c_pv_obj[i].setValue(val_c)
                    self._last_cur_pressure_c[i] = val_c
        except Exception as e:
            self.logger.error("C Pressure Display err: %s", e)

    def _current_cycle_display_P1(self, list_cycle_a_recv):
        try:
            for i, val_a in enumerate(list_cycle_a_recv):
                if val_a != self._last_cur_cycle_a[i]:
                    val_a = round(val_a, 2)
                    self.current_cycle_a_pv_obj[i].setValue(val_a)
                    self._last_cur_cycle_a[i] = val_a
        except Exception as e:
            self.logger.error("A Cycle Display err: %s", e)

    def _current_cycle_display_P2(self, list_cycle_b_recv):
        try:
            for i, val_b in enumerate(list_cycle_b_recv):
                if val_b != self._last_cur_cycle_b[i]:
                    val_b = round(val_b, 2)
                    self.current_cycle_b_pv_obj[i].setValue(val_b)
                    self._last_cur_cycle_b[i] = val_b
        except Exception as e:
            self.logger.error("B Cycle Display err: %s", e)

    def _current_cycle_display_P3(self, list_cycle_c_recv):
        try:
            for i, val_c in enumerate(list_cycle_c_recv):
                if val_c != self._last_cur_cycle_c[i]:
                    val_c = round(val_c, 2)
                    self.current_cycle_c_pv_obj[i].setValue(val_c)
                    self._last_cur_cycle_c[i] = val_c
        except Exception as e:
            self.logger.error("C Cycle Display err: %s", e)

    def _set_cycle_time_unit(self, list_cycle_recv):
        for i, (displ_obj, val) in enumerate(zip(
            [self.ui.cycle_a_displ_3,  self.ui.cycle_b_displ_3,  self.ui.cycle_c_displ_3],
            list_cycle_recv
        )):
            if val != self._last_cycle[i]:
                displ_obj.setValue(val)
                self._last_cycle[i] = val

    def _at_data_filter(self, list_group_at_recv):
        v = round(self.for_display_temp(
            (list_group_at_recv[0]+list_group_at_recv[1]+list_group_at_recv[2])/3), 2)
        if v != self._last_at:
            self.ui.at_pv.setValue(v)
            self._last_at = v

    def _bt_data_filter(self, list_group_bt_recv):
        v = round(self.for_display_temp(
            (list_group_bt_recv[0]+list_group_bt_recv[1]+list_group_bt_recv[2])/3), 2)
        if v != self._last_bt:
            self.ui.bt_pv.setValue(v)
            self._last_bt = v

    def _tube_data_filter(self, data: dict):
        """Px_Current_TempHeater -> at/bt/ct_tube_pv"""
        for tag, obj in zip(("P1_Current_TempHeater", "P2_Current_TempHeater", "P3_Current_TempHeater"),
                            self.tube_pv_obj):
            if tag in data:
                obj.setValue(round(self.for_display_temp(float(data[tag])), 2))

    def _ct_data_filter(self, list_group_ct_recv):
        v = round(self.for_display_temp(
            (list_group_ct_recv[0]+list_group_ct_recv[1]+list_group_ct_recv[2])/3), 2)
        if v != self._last_ct:
            self.ui.ct_pv.setValue(v)
            self._last_ct = v

    # ── Lưu trữ alarm (SQLite: DB_address/alarm.db, cùng thư mục history.db) ──
    # Bảng list_alarm hiển thị LỊCH SỬ alarm: mới nhất ở trên cùng, cột No. là
    # số thứ tự của alarm (id trong DB, tăng dần theo thời điểm phát sinh),
    # KHÔNG phải số thứ tự hàng. Alarm hết lỗi vẫn giữ trong bảng (cột Type xám).
    _ALARM_RESOLVED_COLOR = "#94A3B8"

    def _init_alarm_database(self):
        db_folder = Path(self.stk_mch_folder) / "DB_address"
        db_folder.mkdir(parents=True, exist_ok=True)
        self.alarm_db_path = db_folder / "alarm.db"
        self.alarm_conn = None
        try:
            conn = sqlite3.connect(str(self.alarm_db_path), check_same_thread=False)
            conn.execute("PRAGMA journal_mode=WAL")
            conn.execute("PRAGMA synchronous=NORMAL")
            conn.execute("""
                CREATE TABLE IF NOT EXISTS alarm (
                    id         INTEGER PRIMARY KEY AUTOINCREMENT,
                    raised_at  TEXT NOT NULL,
                    source     TEXT NOT NULL,
                    type       TEXT NOT NULL,
                    content    TEXT NOT NULL,
                    cleared_at TEXT
                )
            """)
            # Alarm còn mở từ phiên chạy trước → đóng lại tại thời điểm khởi động
            # (nếu lỗi vẫn còn, PLC/worker sẽ báo lại thành alarm mới)
            conn.execute("UPDATE alarm SET cleared_at = ? WHERE cleared_at IS NULL",
                         (time.strftime("%Y-%m-%d %H:%M:%S"),))
            conn.commit()
            self.alarm_conn = conn
        except Exception as e:
            self.logger.error("[Alarm DB] Init error: %s", e)
        self._load_alarm_history()

    def _load_alarm_history(self):
        """Nạp lại bảng từ DB: _alarm_row_limit alarm mới nhất, mới nhất ở trên."""
        table = self.ui.list_alarm
        table.setUpdatesEnabled(False)
        try:
            table.setRowCount(0)
            if self.alarm_conn is None:
                return
            rows = self.alarm_conn.execute(
                "SELECT id, raised_at, source, type, content, cleared_at "
                "FROM alarm ORDER BY id DESC LIMIT ?", (self._alarm_row_limit,)
            ).fetchall()
            for r in rows:
                self._insert_alarm_row(table.rowCount(), *r)
        except Exception as e:
            self.logger.error("[Alarm DB] Load error: %s", e)
        finally:
            table.setUpdatesEnabled(True)

    def _insert_alarm_row(self, row: int, alarm_id, raised_at: str, source: str,
                          alarm_type: str, content: str, cleared_at=None):
        table = self.ui.list_alarm
        table.insertRow(row)

        no_item = QTableWidgetItem("-" if alarm_id is None else str(alarm_id))
        no_item.setData(Qt.ItemDataRole.UserRole, alarm_id)
        type_item = QTableWidgetItem(alarm_type)
        type_item.setForeground(QColor(ALARM_TYPE_COLORS.get(alarm_type, "#000000")))
        type_font = type_item.font()
        type_font.setBold(True)
        type_item.setFont(type_font)

        table.setItem(row, 0, no_item)                       # No.
        table.setItem(row, 1, QTableWidgetItem(source))      # Name.
        table.setItem(row, 2, type_item)                     # Type.
        table.setItem(row, 3, QTableWidgetItem(raised_at))   # Time.
        table.setItem(row, 4, QTableWidgetItem(content))     # Content

        if cleared_at:
            self._mark_alarm_row_resolved(row, cleared_at)

    def _mark_alarm_row_resolved(self, row: int, cleared_at: str):
        """Alarm đã hết lỗi: chỉ làm xám cột Type (các cột khác giữ màu bình thường)."""
        table = self.ui.list_alarm
        type_item = table.item(row, 2)
        if type_item is not None:
            type_item.setForeground(QColor(self._ALARM_RESOLVED_COLOR))
        for col in range(table.columnCount()):
            item = table.item(row, col)
            if item is not None:
                item.setToolTip(f"Resolved: {cleared_at}")

    def _find_alarm_row(self, alarm_id) -> int:
        table = self.ui.list_alarm
        for row in range(table.rowCount()):
            item = table.item(row, 0)
            if item is not None and item.data(Qt.ItemDataRole.UserRole) == alarm_id:
                return row
        return -1

    def _raise_alarm(self, source: str, alarm_type: str, content: str):
        if not content:
            self._clear_alarm(source)
            return

        active = self._alarm_active_rows.get(source)
        if active is not None:
            if active["content"] == content and active["type"] == alarm_type:
                return
            # Nội dung alarm thay đổi → đóng alarm cũ, ghi alarm mới
            self._clear_alarm(source)

        raised_at = time.strftime("%Y-%m-%d %H:%M:%S")
        alarm_id = None
        if self.alarm_conn is not None:
            try:
                cur = self.alarm_conn.execute(
                    "INSERT INTO alarm (raised_at, source, type, content) VALUES (?, ?, ?, ?)",
                    (raised_at, source, alarm_type, content),
                )
                self.alarm_conn.commit()
                alarm_id = cur.lastrowid
            except Exception as e:
                self.logger.error("[Alarm DB] Insert error: %s", e)

        table = self.ui.list_alarm
        self._insert_alarm_row(0, alarm_id, raised_at, source, alarm_type, content)
        while table.rowCount() > self._alarm_row_limit:
            table.removeRow(table.rowCount() - 1)

        self._alarm_active_rows[source] = {"id": alarm_id, "type": alarm_type, "content": content}
        self._flush_alarm_to_file(source, alarm_type, content, event="RAISE")
        self._update_alarm_badge()

    def _clear_alarm(self, source: str):
        active = self._alarm_active_rows.pop(source, None)
        if active is None:
            return
        cleared_at = time.strftime("%Y-%m-%d %H:%M:%S")
        if active["id"] is not None:
            if self.alarm_conn is not None:
                try:
                    self.alarm_conn.execute("UPDATE alarm SET cleared_at = ? WHERE id = ?",
                                            (cleared_at, active["id"]))
                    self.alarm_conn.commit()
                except Exception as e:
                    self.logger.error("[Alarm DB] Update error: %s", e)
            row = self._find_alarm_row(active["id"])
            if row >= 0:
                self._mark_alarm_row_resolved(row, cleared_at)
        self._flush_alarm_to_file(source, active["type"], "(resolved)", event="CLEAR")
        self._update_alarm_badge()

    def delete_alarm_history(self):
        """
        Xoá lịch sử alarm (cả DB lẫn bảng) — dùng cho nút "Xoá lỗi" (chưa gán, sẽ gán khi sửa UI):
            self.ui.<ten_nut>.clicked.connect(self.delete_alarm_history)

        - Hỏi xác nhận trước khi xoá.
        - Alarm ĐANG còn lỗi được giữ lại (nếu xoá, lỗi vẫn còn mà không thấy trên bảng).
        - Số thứ tự (No.) tiếp tục tăng, không đánh lại từ 1.
        """
        titles = {"en": "Delete Alarms", "cn": "删除报警", "vn": "Xoá lỗi"}
        texts = {
            "en": "Delete all resolved alarms?",
            "cn": "删除所有已解除的报警？",
            "vn": "Xoá toàn bộ lỗi đã hết?",
        }
        lang = self._current_lang if self._current_lang in titles else "en"
        if ltmessage.question(self, titles[lang], texts[lang], lang=lang) != ltmessage.Yes:  # type: ignore
            return

        if self.alarm_conn is not None:
            try:
                active_ids = [a["id"] for a in self._alarm_active_rows.values() if a["id"] is not None]
                if active_ids:
                    marks = ",".join("?" * len(active_ids))
                    self.alarm_conn.execute(f"DELETE FROM alarm WHERE id NOT IN ({marks})", active_ids)
                else:
                    self.alarm_conn.execute("DELETE FROM alarm")
                self.alarm_conn.commit()
                self.logger.info("[Alarm DB] Alarm history deleted (kept %d active)", len(active_ids))
            except Exception as e:
                self.logger.error("[Alarm DB] Delete error: %s", e)
        self._load_alarm_history()

    def _update_alarm_badge(self):
        """Badge chỉ đếm alarm đang active khác Warning (Warning vẫn hiện trong bảng + ghi file)"""
        count = sum(1 for a in self._alarm_active_rows.values() if a["type"] != ALARM_WARNING)
        self._alarm_badge.set_count(count)

    def _flush_alarm_to_file(self, source: str, alarm_type: str, content: str, event: str = "RAISE"):
        try:
            date_str = time.strftime("%Y%m%d")
            file_path = self.alarm_data_folder / f"alarm_{date_str}.csv"
            file_exists = file_path.exists()

            with open(file_path, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["datetime", "Source", "Type", "Event", "Content"])
                writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), source, alarm_type, event, content])

        except Exception as e:
            if self.logger:
                self.logger.error(f"[Alarm Log] Error: {e}")

    def heating_btn(self, channel: str, checked: bool, btn=None):
        if (not self.plc_writer_connection and not self.init_signal) or not self.ui.start_stop_stacked.currentIndex() == 1:
            if btn is not None:
                btn.blockSignals(True)
                btn.setChecked(False)
                btn.blockSignals(False)
            return

        tag_map = {
            "A":  "P1_Start_Heat",
            "B":  "P2_Start_Heat",
            "C":  "P3_Start_Heat",
        }
        tag = tag_map.get(channel)
        if not tag:
            return

        self._mark_cmd(tag, checked)

        if channel == "A":
            if not self.init_signal:
                if self._heating_a_flag:
                    self._heating_a_flag = False
                else:
                    self.plc_writer_worker.write_bool.emit("P1_Start_Heat", checked)
            self.disable_heat_group(channel, not checked)
            self.logger.info(f"[Main]-[heating_btn]: Group A Heating {'On' if checked else 'Off'}!")

        elif channel == "B":
            if not self.init_signal:
                if self._heating_b_flag:
                    self._heating_b_flag = False
                else:
                    self.plc_writer_worker.write_bool.emit("P2_Start_Heat", checked)
            self.disable_heat_group(channel, not checked)
            self.logger.info(f"[Main]-[heating_btn]: Group B Heating {'On' if checked else 'Off'}!")

        elif channel == "C":
            if not self.init_signal:
                if self._heating_c_flag:
                    self._heating_c_flag = False
                else:
                    self.plc_writer_worker.write_bool.emit("P3_Start_Heat", checked)
            self.disable_heat_group(channel, not checked)
            self.logger.info(f"[Main]-[heating_btn]: Group C Heating {'On' if checked else 'Off'}!")

        self._update_data_btns()

    def heating_btn_t0(self, channel: str, btn=None):
        if (not self.plc_writer_connection and not self.init_signal) or not self.ui.start_stop_stacked.currentIndex() == 1:
            return

        if channel == "T0_On":
            self._mark_cmd("T0_Start_Heat", True)
            self.plc_writer_worker.write_bool.emit("T0_Start_Heat", True)
            self.disable_heat_group(channel, False)
            self.logger.info("[Main]-[heating_btn]: T0 Heating On!")
            self.ui.heat_t0_stacked.setCurrentIndex(1)

        elif channel == "T0_Off":
            self._mark_cmd("T0_Start_Heat", False)
            self.plc_writer_worker.write_pulse.emit("T0_Stop_Heat", self._PULSE_HOLD_MS)
            self.plc_writer_worker.write_bool.emit("T0_Start_Heat", False)
            self.disable_heat_group(channel, True)
            self.logger.info("[Main]-[heating_btn]: T0 Heating Off!")
            self.ui.heat_t0_stacked.setCurrentIndex(0)

        self._update_data_btns()

    def pumping_btn(self, channel: str, checked: bool, btn=None):
        if (not self.plc_writer_connection and not self.init_signal) or not self.ui.start_stop_stacked.currentIndex() == 1:
            if btn is not None:
                btn.blockSignals(True)
                btn.setChecked(False)
                btn.blockSignals(False)
            return

        tag_map = {
            "A": "P1_Start_Pressure",
            "B": "P2_Start_Pressure",
            "C": "P3_Start_Pressure",
        }
        tag = tag_map.get(channel)
        if not tag:
            return

        self._mark_cmd(tag, checked)

        try:
            if not self.init_signal:
                if self._vacuum_a_flag and channel == "A":
                    self._vacuum_a_flag = False
                elif self._vacuum_b_flag and channel == "B":
                    self._vacuum_b_flag = False
                elif self._vacuum_c_flag and channel == "C":
                    self._vacuum_c_flag = False
                else:
                    self.plc_writer_worker.write_bool.emit(tag, checked) #type: ignore

            self.disable_pressure_group(channel, not checked)
            self._sv_cycle_state(channel, not checked)

            self.logger.info(
                f"[Main]-[pumping_btn]: Group {channel} Pressure {'On' if checked else 'Off'}!"
            )
        except Exception as e:
            self.logger.error(f"[Main]-[pumping_btn]: Error occurred - {str(e)}")
        finally:
            self._update_data_btns()

    def _any_plc_toggle_on(self) -> bool:
        """True nếu có bất kỳ nút bật/tắt PLC nào (trừ Start/Stop) đang ON"""
        toggle_btns = (
            self.ui.heat_btn_a, self.ui.heat_btn_b, self.ui.heat_btn_c,
            self.ui.vacuum_btn_a, self.ui.vacuum_btn_b, self.ui.vacuum_btn_c,
            self.ui.refuel_btn_a, self.ui.refuel_btn_b, self.ui.refuel_btn_c,
            self.ui.set_cycle_a_btn, self.ui.set_cycle_b_btn, self.ui.set_cycle_c_btn,
        )
        return any(b.isChecked() for b in toggle_btns) or self.ui.heat_t0_stacked.currentIndex() == 1

    def _update_data_btns(self):
        """Tạm ngắt new_data_btn & clear_data_btn khi có nút bật/tắt PLC đang ON"""
        enabled = not self._any_plc_toggle_on()
        self.ui.new_data_btn.setEnabled(enabled)
        self.ui.clear_data_btn.setEnabled(enabled)

    def fill_oil_btn(self, channel: str, checked: bool, btn=None):
        if (not self.plc_writer_connection and not self.init_signal) or not self.ui.start_stop_stacked.currentIndex() == 1:
            if btn is not None:
                btn.blockSignals(True)
                btn.setChecked(False)
                btn.blockSignals(False)
            return

        tag_map = {
            "A": "P1_Start_Oil",
            "B": "P2_Start_Oil",
            "C": "P3_Start_Oil",
        }
        tag = tag_map.get(channel)
        if not tag:
            return

        self._mark_cmd(tag, checked)

        try:
            if not self.init_signal:
                if self._oil_a_flag and channel == "A":
                    self._oil_a_flag = False
                elif self._oil_b_flag and channel == "B":
                    self._oil_b_flag = False
                elif self._oil_c_flag and channel == "C":
                    self._oil_c_flag = False
                else:
                    self.plc_writer_worker.write_bool.emit(tag, checked) #type: ignore

            self.disable_oil_group(channel, not checked)
            self._sv_cycle_state(channel, not checked)

            self.logger.info(
                f"[Main]-[fill_oil_btn]: Group {channel} Oil Filling {'On' if checked else 'Off'}!"
            )
        except Exception as e:
            self.logger.error(f"[Main]-[fill_oil_btn]: Error occurred - {str(e)}")
        finally:
            self._update_data_btns()

    def cycle_loop_btn(self, channel: str, checked: bool, btn=None):
        buttons_map = {
            "A": [self.ui.refuel_btn_a, self.ui.vacuum_btn_a],
            "B": [self.ui.refuel_btn_b, self.ui.vacuum_btn_b],
            "C": [self.ui.refuel_btn_c, self.ui.vacuum_btn_c],
        }

        if (not self.plc_writer_connection and not self.init_signal) or \
        any(b.isChecked() for b in buttons_map.get(channel, [])):
            if btn is not None:
                btn.blockSignals(True)
                btn.setChecked(False)
                btn.blockSignals(False)
            return

        tag_map = {
            "A": "P1_BitCountTimes",
            "B": "P2_BitCountTimes",
            "C": "P3_BitCountTimes",
        }
        tag = tag_map.get(channel)
        if not tag:
            return

        self._mark_cmd(tag, checked)

        try:
            if not self.init_signal:
                if self._count_a_flag and channel == "A":
                    self._count_a_flag = False
                elif self._count_b_flag and channel == "B":
                    self._count_b_flag = False
                elif self._count_c_flag and channel == "C":
                    self._count_c_flag = False
                else:
                    self.plc_writer_worker.write_bool.emit(tag, checked) #type: ignore
                if checked:
                    self.reset_cycle_btn(channel)

            self._sv_cycle_state(channel, checked)
            self._set_cycle_state(channel)

            self.logger.info(
                f"[Main]-[cycle_loop_btn]: Group {channel} Auto Repeat {'Off' if checked else 'On'}!"
            )
        except Exception as e:
            self.logger.error(f"[Main]-[cycle_loop_btn]: Error occurred - {str(e)}")
        finally:
            self._update_data_btns()

    def _sv_cycle_state(self, channel, status):
        if channel == "All":
            if self.ui.pressure_sv_a_11.isEnabled() != status:
                self.ui.pressure_sv_a_11.setEnabled(status)
            if self.ui.pressure_sv_b_11.isEnabled() != status:
                self.ui.pressure_sv_b_11.setEnabled(status)
            if self.ui.pressure_sv_c_11.isEnabled() != status:
                self.ui.pressure_sv_c_11.setEnabled(status)
        if channel == "A":
            if self.ui.pressure_sv_a_11.isEnabled() != status:
                self.ui.pressure_sv_a_11.setEnabled(status)
        if channel == "B":
            if self.ui.pressure_sv_b_11.isEnabled() != status:
                self.ui.pressure_sv_b_11.setEnabled(status)
        if channel == "C":
            if self.ui.pressure_sv_c_11.isEnabled() != status:
                self.ui.pressure_sv_c_11.setEnabled(status)

    def _set_cycle_state(self, channel):
        if channel == "All":
            self.ui.stacked_pressure_sv_a_11.setCurrentIndex(1) if self.ui.set_cycle_a_btn.isChecked() else self.ui.stacked_pressure_sv_a_11.setCurrentIndex(0)
            self.ui.stacked_pressure_sv_b_11.setCurrentIndex(1) if self.ui.set_cycle_b_btn.isChecked() else self.ui.stacked_pressure_sv_b_11.setCurrentIndex(0)
            self.ui.stacked_pressure_sv_c_11.setCurrentIndex(1) if self.ui.set_cycle_c_btn.isChecked() else self.ui.stacked_pressure_sv_c_11.setCurrentIndex(0)
        if channel == "A":
            self.ui.stacked_pressure_sv_a_11.setCurrentIndex(1) if self.ui.set_cycle_a_btn.isChecked() else self.ui.stacked_pressure_sv_a_11.setCurrentIndex(0)
        if channel == "B":
            self.ui.stacked_pressure_sv_b_11.setCurrentIndex(1) if self.ui.set_cycle_b_btn.isChecked() else self.ui.stacked_pressure_sv_b_11.setCurrentIndex(0)
        if channel == "C":
            self.ui.stacked_pressure_sv_c_11.setCurrentIndex(1) if self.ui.set_cycle_c_btn.isChecked() else self.ui.stacked_pressure_sv_c_11.setCurrentIndex(0)

    def start_stop_btn(self, channel: str, btn=None):
        try:            
            if not self.plc_writer_connection and not self.init_signal:
                if self._current_lang == "en":
                    title = "Error"
                    content = "PLC not connected!"
                elif self._current_lang == "cn":
                    title = "错误"
                    content = "PLC 未连接!"
                elif self._current_lang == "vn":
                    title = "Lỗi"
                    content = "PLC mất kết nối!"
                ltmessage.error(self, title, content, self._current_lang)  # type: ignore
                return
            
            if channel == "Start":
                self.ui.sys_state_stacked_wid_39.setCurrentIndex(1)
                self._mark_cmd("START", True)
                self.plc_writer_worker.write_bool.emit("START", True)   # type: ignore
                self.data_table.start()
                self.ui.start_stop_stacked.setCurrentIndex(1)
                self.logger.info("[Main]-[start_stop_btn]: System On")
            elif channel == "Stop":
                self.ui.sys_state_stacked_wid_39.setCurrentIndex(0)
                self._mark_cmd("START", False)
                self.plc_writer_worker.write_pulse.emit("STOP", self._PULSE_HOLD_MS)  # type: ignore
                self.plc_writer_worker.write_bool.emit("START", False)               # type: ignore
                QTimer.singleShot(150, self._set_off_oil_btn)
                QTimer.singleShot(150, self._set_off_vacuum_btn)
                QTimer.singleShot(150, self._set_off_heating_btn)
                self.data_table.stop()
                self.ui.start_stop_stacked.setCurrentIndex(0)
                self._update_data_btns()
                self.logger.info("[Main]-[start_stop_btn]: System Off")
        except Exception as e:
            self.logger.error(f"[Main]-[start_stop_btn]: Error occurred - {str(e)}")

    def _set_off_oil_btn(self):
        self.ui.refuel_btn_a.blockSignals(True)
        self.ui.refuel_btn_b.blockSignals(True)
        self.ui.refuel_btn_c.blockSignals(True)

        self.ui.refuel_btn_a.setChecked(False)
        self.disable_oil_group("A", True)   
        self.ui.refuel_btn_b.setChecked(False)
        self.disable_oil_group("B", True)   
        self.ui.refuel_btn_c.setChecked(False)
        self.disable_oil_group("C", True)
        self._sv_cycle_state("All", True)
        self._update_data_btns()

        self.ui.refuel_btn_a.blockSignals(False)
        self.ui.refuel_btn_b.blockSignals(False)
        self.ui.refuel_btn_c.blockSignals(False)

    def _set_off_vacuum_btn(self):
        self.ui.vacuum_btn_a.blockSignals(True)
        self.ui.vacuum_btn_b.blockSignals(True)
        self.ui.vacuum_btn_c.blockSignals(True)

        self.ui.vacuum_btn_a.setChecked(False)        
        self.disable_pressure_group("A", True)
        self.ui.vacuum_btn_b.setChecked(False)        
        self.disable_pressure_group("B", True)
        self.ui.vacuum_btn_c.setChecked(False)
        self.disable_pressure_group("C", True)
        self._sv_cycle_state("All", True)
        self._update_data_btns()

        self.ui.vacuum_btn_a.blockSignals(False)
        self.ui.vacuum_btn_b.blockSignals(False)
        self.ui.vacuum_btn_c.blockSignals(False)

    def _set_off_heating_btn(self):
        self.ui.heat_btn_a.blockSignals(True)
        self.ui.heat_btn_b.blockSignals(True)
        self.ui.heat_btn_c.blockSignals(True)
        self.ui.heat_on_btn_t0.blockSignals(True)
        self.ui.heat_off_btn_t0.blockSignals(True)

        self.ui.heat_btn_a.setChecked(False)        
        self.disable_heat_group("A", True)
        self.ui.heat_btn_b.setChecked(False)        
        self.disable_heat_group("B", True)
        self.ui.heat_btn_c.setChecked(False)        
        self.disable_heat_group("C", True)
        self.ui.heat_t0_stacked.setCurrentIndex(0)
        self.disable_heat_group("T0", True)
        self._update_data_btns()

        self.ui.heat_btn_a.blockSignals(False)
        self.ui.heat_btn_b.blockSignals(False)
        self.ui.heat_btn_c.blockSignals(False)
        self.ui.heat_on_btn_t0.blockSignals(False)
        self.ui.heat_off_btn_t0.blockSignals(False)

    def clear_data_btn(self):
        if self._any_plc_toggle_on():
            return

        if self._current_lang == "en":
            title = "Clear Data"
            content = "Set all SV to 0?"
        elif self._current_lang == "cn":
            title = "清除数据"
            content = "是否将所有 SV 设为 0?"
        elif self._current_lang == "vn":
            title = "Xoá dữ liệu"
            content = "Đặt toàn bộ SV về 0?"
        reply = ltmessage.question(
            self, title, content, self._current_lang # type: ignore
        )
        if reply == ltmessage.Yes:
            try:
                self.ui.code_display.setText("")
                for i in range(len(self.pressure_a_sv_obj)):
                    self.pressure_a_sv_obj[i].blockSignals(True)
                    self.pressure_b_sv_obj[i].blockSignals(True)
                    self.pressure_c_sv_obj[i].blockSignals(True)
                    
                    self.pressure_a_sv_obj[i].setValue(0) if i != 0 else self.pressure_a_sv_obj[i].setValue(self.for_display_temp(0))
                    self.pressure_b_sv_obj[i].setValue(0) if i != 0 else self.pressure_b_sv_obj[i].setValue(self.for_display_temp(0))
                    self.pressure_c_sv_obj[i].setValue(0) if i != 0 else self.pressure_c_sv_obj[i].setValue(self.for_display_temp(0))
                    
                    self.pressure_a_sv_obj[i].blockSignals(False)
                    self.pressure_b_sv_obj[i].blockSignals(False)
                    self.pressure_c_sv_obj[i].blockSignals(False)
                    
                for i in range(len(self.temp_sv_obj)):
                    self.temp_sv_obj[i].blockSignals(True)
                    self.temp_sv_obj[i].setValue(self.for_display_temp(0))
                    self.temp_sv_obj[i].blockSignals(False)
                for i in range(len(self.temp_h_alm_obj)):
                    self.temp_h_alm_obj[i].blockSignals(True)
                    self.temp_h_alm_obj[i].setValue(self.for_display_temp(0))
                    self.temp_h_alm_obj[i].blockSignals(False)

                for i in range(len(self.temp_l_alm_obj)):
                    self.temp_l_alm_obj[i].blockSignals(True)
                    self.temp_l_alm_obj[i].setValue(self.for_display_temp(0))
                    self.temp_l_alm_obj[i].blockSignals(False)
                for i in range(len(self.temp_offset_obj)):
                    self.temp_offset_obj[i].blockSignals(True)
                    self.temp_offset_obj[i].setValue(self.for_display_temp(0))
                    self.temp_offset_obj[i].blockSignals(False)
                items_a = [
                    self.plc_writer_worker.get_item("P1_CountTimes", self.list_for_import_a[0].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P1_Oil_Start_Time", self.list_for_import_a[1].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P1_Oil_End_Time", self.list_for_import_a[2].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P1_Air_FillingTime", self.list_for_import_a[3].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P1_Air_HoldingTime", self.list_for_import_a[4].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P1_Air_ReleaseTime", self.list_for_import_a[5].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P1_PressureSetting", self.list_for_import_a[6].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P1_TemperatureSetting", self.cal_fah_to_cel(self.list_for_import_a[7].value())),    # type: ignore
                    self.plc_writer_worker.get_item("P1_TempLimitHIGH", self.cal_fah_to_cel(self.list_for_import_a[8].value())), # type: ignore
                    self.plc_writer_worker.get_item("P1_TempLimitLOW", self.cal_fah_to_cel(self.list_for_import_a[9].value())),  # type: ignore
                    self.plc_writer_worker.get_item("P1_Temp1Offset", self.cal_fah_to_cel(self.list_for_import_a[10].value())),  # type: ignore
                    self.plc_writer_worker.get_item("P1_Temp2Offset", self.cal_fah_to_cel(self.list_for_import_a[11].value())),  # type: ignore
                    self.plc_writer_worker.get_item("P1_Temp3Offset", self.cal_fah_to_cel(self.list_for_import_a[12].value()))   # type: ignore
                ]
                items_b = [
                    self.plc_writer_worker.get_item("P2_CountTimes", self.list_for_import_b[0].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P2_Oil_Start_Time", self.list_for_import_b[1].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P2_Oil_End_Time", self.list_for_import_b[2].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P2_Air_FillingTime", self.list_for_import_b[3].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P2_Air_HoldingTime", self.list_for_import_b[4].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P2_Air_ReleaseTime", self.list_for_import_b[5].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P2_PressureSetting", self.list_for_import_b[6].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P2_TemperatureSetting", self.cal_fah_to_cel(self.list_for_import_b[7].value())),    # type: ignore
                    self.plc_writer_worker.get_item("P2_TempLimitHIGH", self.cal_fah_to_cel(self.list_for_import_b[8].value())), # type: ignore
                    self.plc_writer_worker.get_item("P2_TempLimitLOW", self.cal_fah_to_cel(self.list_for_import_b[9].value())),  # type: ignore
                    self.plc_writer_worker.get_item("P2_Temp1Offset", self.cal_fah_to_cel(self.list_for_import_b[10].value())),  # type: ignore
                    self.plc_writer_worker.get_item("P2_Temp2Offset", self.cal_fah_to_cel(self.list_for_import_b[11].value())),  # type: ignore
                    self.plc_writer_worker.get_item("P2_Temp3Offset", self.cal_fah_to_cel(self.list_for_import_b[12].value()))   # type: ignore
                ]
                items_c = [
                    self.plc_writer_worker.get_item("P3_CountTimes", self.list_for_import_c[0].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P3_Oil_Start_Time", self.list_for_import_c[1].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P3_Oil_End_Time", self.list_for_import_c[2].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P3_Air_FillingTime", self.list_for_import_c[3].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P3_Air_HoldingTime", self.list_for_import_c[4].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P3_Air_ReleaseTime", self.list_for_import_c[5].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P3_PressureSetting", self.list_for_import_c[6].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P3_TemperatureSetting", self.cal_fah_to_cel(self.list_for_import_c[7].value())),    # type: ignore
                    self.plc_writer_worker.get_item("P3_TempLimitHIGH", self.cal_fah_to_cel(self.list_for_import_c[8].value())), # type: ignore
                    self.plc_writer_worker.get_item("P3_TempLimitLOW", self.cal_fah_to_cel(self.list_for_import_c[9].value())),  # type: ignore
                    self.plc_writer_worker.get_item("P3_Temp1Offset", self.cal_fah_to_cel(self.list_for_import_c[10].value())),  # type: ignore
                    self.plc_writer_worker.get_item("P3_Temp2Offset", self.cal_fah_to_cel(self.list_for_import_c[11].value())),  # type: ignore
                    self.plc_writer_worker.get_item("P3_Temp3Offset", self.cal_fah_to_cel(self.list_for_import_c[12].value()))   # type: ignore
                ]
                items_t0 = [
                    self.plc_writer_worker.get_item("T0_TemperatureSetting", self.cal_fah_to_cel(self.list_for_import_t0[0].value())),   # type: ignore
                    self.plc_writer_worker.get_item("T0_TempLimitHIGH", self.cal_fah_to_cel(self.list_for_import_t0[1].value())),    # type: ignore
                    self.plc_writer_worker.get_item("T0_TempLimitLOW", self.cal_fah_to_cel(self.list_for_import_t0[2].value())), # type: ignore
                    self.plc_writer_worker.get_item("T0_TempOffset", self.cal_fah_to_cel(self.list_for_import_t0[3].value()))    # type: ignore
                ]
                self.plc_writer_worker.write_multi.emit(items_a, "A")   # type: ignore
                self.plc_writer_worker.write_multi.emit(items_b, "B")   # type: ignore
                self.plc_writer_worker.write_multi.emit(items_c, "C")   # type: ignore
                self.plc_writer_worker.write_multi.emit(items_t0, "T0") # type: ignore

                if self.plc_writer_connection:
                    if self.ui.set_cycle_a_btn.isChecked():
                        self.ui.set_cycle_a_btn.click()
                    if self.ui.set_cycle_b_btn.isChecked():
                        self.ui.set_cycle_b_btn.click()
                    if self.ui.set_cycle_c_btn.isChecked():
                        self.ui.set_cycle_c_btn.click()
                    self.disable_btn("A", False)
                    self.disable_btn("B", False)
                    self.disable_btn("C", False)
                    self.disable_btn("T0", False)
            except Exception as e:
                if self._current_lang == "en":
                    title = "Error"
                    content = f"Failed to clear data: {e}"
                elif self._current_lang == "cn":
                    title = "错误"
                    content = f"数据清除失败: {e}"
                elif self._current_lang == "vn":
                    title = "Lỗi"
                    content = f"Không thể xoá dữ liệu: {e}"
                ltmessage.error(self, title, content, self._current_lang) # type: ignore

    def _clear_group(self, channel: str):
        cfg = CLEAR_GROUP_CONFIG[channel]
        guard_widgets = [getattr(self.ui, name) for name in cfg["guard_widgets"]]
        if any(btn.isChecked() for btn in guard_widgets):
            return

        all_import_widgets = self.list_for_import_a + self.list_for_import_b + self.list_for_import_c
        try:
            for obj in all_import_widgets:
                obj.blockSignals(True)

            for widget in getattr(self, cfg["pressure_sv_obj"]):
                widget.blockSignals(True)
                widget.setValue(0)
                widget.blockSignals(False)

            temp_widget = self.temp_sv_obj[cfg["temp_sv_index"]]
            temp_widget.blockSignals(True)
            temp_widget.setValue(0)
            temp_widget.blockSignals(False)

            list_import = getattr(self, cfg["list_import"])
            prefix = cfg["plc_prefix"]
            items = [
                self.plc_writer_worker.get_item(f"{prefix}_{tag}", list_import[i].value())
                for i, tag in enumerate(CLEAR_GROUP_PLC_TAGS)
            ]
            self.plc_writer_worker.write_multi.emit(items, channel)

            for obj in all_import_widgets:
                obj.blockSignals(False)

            if self.plc_writer_connection:
                self.disable_btn(channel, False)
        except Exception as e:
            self.logger.error(f"Failed to clear {channel} data: {e}")
            for obj in all_import_widgets:
                obj.blockSignals(False)

    def clear_group_a_btn(self): self._clear_group("A")
    def clear_group_b_btn(self): self._clear_group("B")
    def clear_group_c_btn(self): self._clear_group("C")

    def reset_cycle_btn(self, channel):
        try:
            if channel == "A":
                self.plc_writer_worker.write_value.emit("P1_Number_Test_Times", 0) if self.plc_writer_connection else None #type: ignore
                if self.plc_writer_connection:
                    self.logger.info(f"[Main]-[reset_cycle_a_btn]: Total A Cycle: {self.ui.cycle_a_displ_3.value()}")
                else:
                    self.logger.info(f"[Main]-[reset_cycle_a_btn]: Cannot set Total A Cycle")
            if channel == "B":
                self.plc_writer_worker.write_value.emit("P2_Number_Test_Times", 0) if self.plc_writer_connection else None #type: ignore
                if self.plc_writer_connection:
                    self.logger.info(f"[Main]-[reset_cycle_b_btn]: Total B Cycle: {self.ui.cycle_b_displ_3.value()}")
                else:
                    self.logger.info(f"[Main]-[reset_cycle_b_btn]: Cannot set Total B Cycle")
            if channel == "C":
                self.plc_writer_worker.write_value.emit("P3_Number_Test_Times", 0) if self.plc_writer_connection else None #type: ignore
                if self.plc_writer_connection:
                    self.logger.info(f"[Main]-[reset_cycle_c_btn]: Total C Cycle: {self.ui.cycle_c_displ_3.value()}")
                else:
                    self.logger.info(f"[Main]-[reset_cycle_c_btn]: Cannot set Total C Cycle")
        except Exception as e:
            self.logger.error(f"[Main]-[reset_cycle_btn]: Error occurred - {str(e)}")

    def cmd_btn(self):
        try:
            if self._is_console_running():
                self._bring_console_to_front()
                return

            self._cleanup_console()

            flag_path = os.path.join(tempfile.gettempdir(), "sm_force_quit.flag")
            if os.path.exists(flag_path):
                os.remove(flag_path)

            if getattr(sys, 'frozen', False):
                cmd = [os.path.join(os.path.dirname(sys.executable), "cmd.exe")]
            else:
                pythonw = sys.executable.replace("python.exe", "pythonw.exe")
                cmd = [pythonw, "-u", os.path.join(os.path.dirname(__file__), "console_window.py")]

            creationflags = subprocess.CREATE_BREAKAWAY_FROM_JOB if os.name == 'nt' else 0

            self._console_process = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                creationflags=creationflags,
                start_new_session=True
            )
            self._console_stdin_lock = threading.Lock()
            self._attach_log_handler()   # gán log vào lần này
            self._start_console_query_reader()

            if not hasattr(self, '_watch_timer'):
                self._watch_timer = QTimer(self)
                self._watch_timer.timeout.connect(self._watch_console_process)
            self._watch_timer.start(500)

        except Exception as e:
            self.logger.error(f"[cmd_btn] Error: {e}", exc_info=True)

    def _attach_log_handler(self):
        self._pipe_handler = SafePipeLogHandler(
            self._console_process, stdin_lock=self._console_stdin_lock
            )
        fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self._pipe_handler.setFormatter(fmt)
        self.logger.addHandler(self._pipe_handler)

    def _start_console_query_reader(self):
        proc = self._console_process

        def _read_loop():
            try:
                if not proc.stdout:
                    return
                for raw_line in proc.stdout:
                    line = raw_line.rstrip("\n")
                    if not line:
                        continue
                    self._handle_console_query(line)
            except Exception:
                pass

        threading.Thread(target=_read_loop, daemon=True).start()

    def _handle_console_query(self, raw_line: str):
        prefix = "QUERY:"
        if not raw_line.startswith(prefix):
            return
            
        cmd = raw_line[len(prefix):].strip().lower()

        commands = {
            "getplcip": self._console_query_plc_ip,
        }

        handler = commands.get(cmd)
        if handler is None:
            self.logger.warning(f"[console-query] Unknown command: '{cmd}'")
            self._send_console_result(cmd, f"Unknown command: {cmd}")
            return

        try:
            result = handler()
            self._send_console_result(cmd, result)
        except Exception as e:
            error_msg = f"Error while handling '{cmd}': {e}"
            self._send_console_result(cmd, error_msg)
            self.logger.error(error_msg)

    def _send_console_result(self, cmd: str, text: str, level: str = "INFO"):
        if not hasattr(self, '_console_process') or self._console_process is None:
            return
        try:
            payload = {
                "cmd": cmd,
                "text": str(text),
                "level": level
            }
            self._console_process.stdin.write(f"RESULT:{json.dumps(payload, ensure_ascii=False)}\n")
            self._console_process.stdin.flush()
        except Exception as e:
            self.logger.error(f"Failed to send result to console: {e}")

    def _console_query_plc_ip(self):
        db = self.db_dict if isinstance(self.db_dict, dict) else {}
        ip = db.get("ip_plc", "N/A")
        self._send_console_result("getplcip", ip, "INFO")

    def _watch_console_process(self):
        if self._is_console_running():
            self._check_force_quit_flag()
            return
        self._cleanup_console()

    def _is_console_running(self):
        if not hasattr(self, '_console_process') or self._console_process is None:
            return False
        try:
            return self._console_process.poll() is None
        except:
            return False

    def _cleanup_console(self):
        if hasattr(self, '_watch_timer') and self._watch_timer:
            self._watch_timer.stop()

        if hasattr(self, '_pipe_handler') and self._pipe_handler:
            try:
                self.logger.removeHandler(self._pipe_handler)
                self._pipe_handler.close()
            except Exception:
                pass
            self._pipe_handler = None

        if hasattr(self, '_console_process') and self._console_process:
            try:
                if self._console_process.poll() is None:
                    self._console_process.kill()
            except:
                pass
            self._console_process = None

    def _bring_console_to_front(self):
        if not hasattr(self, '_console_process') or not self._console_process:
            return
        try:
            import ctypes
            from ctypes import wintypes

            user32 = ctypes.windll.user32
            target_pids = {self._console_process.pid}
            try:
                proc = psutil.Process(self._console_process.pid)
                for child in proc.children(recursive=True):
                    target_pids.add(child.pid)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

            WNDENUMPROC = ctypes.WINFUNCTYPE(
                wintypes.BOOL, wintypes.HWND, wintypes.LPARAM
            )

            hwnds = []

            def enum_callback(hwnd, _lparam):
                owner_pid = wintypes.DWORD(0)
                user32.GetWindowThreadProcessId(hwnd, ctypes.byref(owner_pid))
                if owner_pid.value in target_pids and user32.IsWindow(hwnd):
                    hwnds.append(hwnd)
                return True  # tiếp tục enumerate

            user32.EnumWindows(WNDENUMPROC(enum_callback), 0)

            if not hwnds:
                self.logger.warning(
                    "[cmd_btn] Console process is alive but its window "
                    "wasn't found yet (may still be initializing) - skip, "
                    "keep process running."
                )
                return

            hwnd = hwnds[0]
            user32.ShowWindow(hwnd, 9)   # SW_RESTORE
            user32.SetForegroundWindow(hwnd)
        except Exception as e:
            self.logger.warning(f"[cmd_btn] Cannot focus console: {e}")

    def _check_force_quit_flag(self):
        flag_path = os.path.join(tempfile.gettempdir(), "sm_force_quit.flag")
        if os.path.exists(flag_path):
            try:
                os.remove(flag_path)
            except Exception:
                pass
            self._cleanup_console()      # Thêm cleanup
            self._on_force_quit()

    @Slot()
    def _on_force_quit(self):
        self._cleanup()
        QApplication.instance().quit()

    def _validate_import_df(self, df) -> tuple[bool, str]:
        """
        Validate DataFrame from imported Excel file.
        Returns: (is_valid: bool, error_message: str)
        """
        errors = []

        if df.shape[1] < 5:
            return False, (
                f"File is missing columns!\n"
            )

        if df.shape[0] < 15:
            return False, (
                f"File is missing data rows!\n"
                f"Required at least 15 rows, current file only has {df.shape[0]} row(s)."
            )

        for i, expected_name in enumerate(EXPECTED_ROW_NAMES):
            row_idx = i + 2
            if row_idx >= df.shape[0]:
                errors.append(f"• Row {row_idx + 1}: Missing parameter '{expected_name}'.")
                continue
            cell_val = str(df.iloc[row_idx][0]).strip() if pd.notna(df.iloc[row_idx][0]) else ""
            if expected_name.lower() not in cell_val.lower():
                errors.append(
                    f"• Row {row_idx + 1}: Parameter name mismatch."
                )

        group_cols = {"Group A": 1, "Group B": 2, "Group C": 3}
        for row_idx in range(2, min(15, df.shape[0])):
            for group_name, col_idx in group_cols.items():
                cell = df.iloc[row_idx][col_idx]
                if pd.isna(cell):
                    continue
                try:
                    float(str(cell).strip())
                except ValueError:
                    pass

        for row_idx in range(9, 13):
            if row_idx >= df.shape[0]:
                break
            cell = df.iloc[row_idx][4]
            if pd.isna(cell):
                continue
            try:
                float(str(cell).strip())
            except ValueError:
                pass

        if errors:
            return False, "File format is invalid:\n\n" + "\n".join(errors)

        return True, ""

    def new_data_btn(self):
        if self._any_plc_toggle_on():
            return
        try:
            stk_mch_file = Path(self.stk_mch_folder)/ "Setting File"
            file_str, _ = QFileDialog.getOpenFileName(
                self,
                "Select Group Data File",
                str(stk_mch_file),
                "Excel Files (*.xlsx *.xls)"
            )
            if not file_str:
                return
            path = Path(file_str)

            try:
                df = pd.read_excel(path, sheet_name=0, header=None)
            except Exception as e:
                ltmessage.error(self, "Import Error", f"Cannot read file!\n\nError: {e}")
                return
            is_valid, error_msg = self._validate_import_df(df)
            if not is_valid:
                ltmessage.error(self, "Invalid File Format", error_msg)
                return

            self.ui.code_display.setText(str(df.iloc[0][0]).strip() if pd.notna(df.iloc[0][0]) else "")
            for i in range(2, len(df)):
                column = df.iloc[i]
                name_raw = str(column[0]).strip() if pd.notna(column[0]) else ""
                if name_raw == "" or name_raw.lower() == "nan":
                    break
                try:
                    if i > 8:
                        value_a_raw = str(column[1]).strip()
                        value_a = self.for_display_temp(float(value_a_raw))
                    else:
                        value_a_raw = str(column[1]).strip()
                        value_a = float(value_a_raw)
                except:
                    value_a = 0
                self.list_for_import_a[i-2].blockSignals(True)
                self.list_for_import_a[i-2].setValue(value_a)   # type: ignore
                
                try:
                    if i > 8:
                        value_b_raw = str(column[2]).strip()
                        value_b = self.for_display_temp(float(value_b_raw))
                    else:
                        value_b_raw = str(column[2]).strip()
                        value_b = float(value_b_raw)
                except:
                    value_b = 0
                self.list_for_import_b[i-2].blockSignals(True)
                self.list_for_import_b[i-2].setValue(value_b)   # type: ignore
                
                try:
                    if i > 8:
                        value_c_raw = str(column[3]).strip()
                        value_c = self.for_display_temp(float(value_c_raw))
                    else:
                        value_c_raw = str(column[3]).strip()
                        value_c = float(value_c_raw)
                except:
                    value_c = 0
                self.list_for_import_c[i-2].blockSignals(True)
                self.list_for_import_c[i-2].setValue(value_c)   # type: ignore

                if i >= 9  and i <=12:
                    try:
                        value_t0_raw = str(column[4]).strip()
                        value_t0 = self.for_display_temp(float(value_t0_raw))
                    except:
                        value_t0 = 0
                    self.list_for_import_t0[i-9].blockSignals(True)
                    self.list_for_import_t0[i-9].setValue(value_t0)

            self.ui.at_sv.blockSignals(True)
            self.ui.at_sv.setValue(self.ui.pressure_sv_a_1.value())
            self.ui.bt_sv.blockSignals(True)
            self.ui.bt_sv.setValue(self.ui.pressure_sv_b_1.value())
            self.ui.ct_sv.blockSignals(True)
            self.ui.ct_sv.setValue(self.ui.pressure_sv_c_1.value())
            items_a = [
                self.plc_writer_worker.get_item("P1_CountTimes", self.list_for_import_a[0].value()),                                    # type: ignore
                self.plc_writer_worker.get_item("P1_Oil_Start_Time", (self.cal_sec_to_msec(self.list_for_import_a[1].value()))),        # type: ignore
                self.plc_writer_worker.get_item("P1_Oil_End_Time", (self.cal_sec_to_msec(self.list_for_import_a[2].value()))),          # type: ignore
                self.plc_writer_worker.get_item("P1_Air_FillingTime", (self.cal_sec_to_msec(self.list_for_import_a[3].value()))),       # type: ignore
                self.plc_writer_worker.get_item("P1_Air_HoldingTime", (self.cal_sec_to_msec(self.list_for_import_a[4].value()))),       # type: ignore
                self.plc_writer_worker.get_item("P1_Air_ReleaseTime", (self.cal_sec_to_msec(self.list_for_import_a[5].value()))),       # type: ignore
                self.plc_writer_worker.get_item("P1_PressureSetting", self.list_for_import_a[6].value()),                               # type: ignore
                self.plc_writer_worker.get_item("P1_TemperatureSetting", self.cal_fah_to_cel(self.list_for_import_a[7].value())),                            # type: ignore
                self.plc_writer_worker.get_item("P1_TempLimitHIGH", self.cal_fah_to_cel(self.list_for_import_a[8].value())),                                 # type: ignore
                self.plc_writer_worker.get_item("P1_TempLimitLOW", self.cal_fah_to_cel(self.list_for_import_a[9].value())),                                  # type: ignore
                self.plc_writer_worker.get_item("P1_Temp1Offset", self.cal_fah_to_cel(self.list_for_import_a[10].value())),                                  # type: ignore
                self.plc_writer_worker.get_item("P1_Temp2Offset", self.cal_fah_to_cel(self.list_for_import_a[11].value())),                                  # type: ignore
                self.plc_writer_worker.get_item("P1_Temp3Offset", self.cal_fah_to_cel(self.list_for_import_a[12].value()))                                   # type: ignore
            ]
            items_b = [
                self.plc_writer_worker.get_item("P2_CountTimes", self.list_for_import_b[0].value()),                                    # type: ignore
                self.plc_writer_worker.get_item("P2_Oil_Start_Time", (self.cal_sec_to_msec(self.list_for_import_b[1].value()))),        # type: ignore
                self.plc_writer_worker.get_item("P2_Oil_End_Time", (self.cal_sec_to_msec(self.list_for_import_b[2].value()))),          # type: ignore
                self.plc_writer_worker.get_item("P2_Air_FillingTime", (self.cal_sec_to_msec(self.list_for_import_b[3].value()))),       # type: ignore
                self.plc_writer_worker.get_item("P2_Air_HoldingTime", (self.cal_sec_to_msec(self.list_for_import_b[4].value()))),       # type: ignore
                self.plc_writer_worker.get_item("P2_Air_ReleaseTime", (self.cal_sec_to_msec(self.list_for_import_b[5].value()))),       # type: ignore
                self.plc_writer_worker.get_item("P2_PressureSetting", self.list_for_import_b[6].value()),                               # type: ignore
                self.plc_writer_worker.get_item("P2_TemperatureSetting", self.cal_fah_to_cel(self.list_for_import_b[7].value())),                            # type: ignore
                self.plc_writer_worker.get_item("P2_TempLimitHIGH", self.cal_fah_to_cel(self.list_for_import_b[8].value())),                                 # type: ignore
                self.plc_writer_worker.get_item("P2_TempLimitLOW", self.cal_fah_to_cel(self.list_for_import_b[9].value())),                                  # type: ignore
                self.plc_writer_worker.get_item("P2_Temp1Offset", self.cal_fah_to_cel(self.list_for_import_b[10].value())),                                  # type: ignore
                self.plc_writer_worker.get_item("P2_Temp2Offset", self.cal_fah_to_cel(self.list_for_import_b[11].value())),                                  # type: ignore
                self.plc_writer_worker.get_item("P2_Temp3Offset", self.cal_fah_to_cel(self.list_for_import_b[12].value()))                                   # type: ignore
            ]
            items_c = [
                self.plc_writer_worker.get_item("P3_CountTimes", self.list_for_import_c[0].value()),                                    # type: ignore
                self.plc_writer_worker.get_item("P3_Oil_Start_Time", (self.cal_sec_to_msec(self.list_for_import_c[1].value()))),        # type: ignore
                self.plc_writer_worker.get_item("P3_Oil_End_Time", (self.cal_sec_to_msec(self.list_for_import_c[2].value()))),          # type: ignore
                self.plc_writer_worker.get_item("P3_Air_FillingTime", (self.cal_sec_to_msec(self.list_for_import_c[3].value()))),       # type: ignore
                self.plc_writer_worker.get_item("P3_Air_HoldingTime", (self.cal_sec_to_msec(self.list_for_import_c[4].value()))),       # type: ignore
                self.plc_writer_worker.get_item("P3_Air_ReleaseTime", (self.cal_sec_to_msec(self.list_for_import_c[5].value()))),       # type: ignore
                self.plc_writer_worker.get_item("P3_PressureSetting", self.list_for_import_c[6].value()),                               # type: ignore
                self.plc_writer_worker.get_item("P3_TemperatureSetting", self.cal_fah_to_cel(self.list_for_import_c[7].value())),                            # type: ignore
                self.plc_writer_worker.get_item("P3_TempLimitHIGH", self.cal_fah_to_cel(self.list_for_import_c[8].value())),                                 # type: ignore
                self.plc_writer_worker.get_item("P3_TempLimitLOW", self.cal_fah_to_cel(self.list_for_import_c[9].value())),                                  # type: ignore
                self.plc_writer_worker.get_item("P3_Temp1Offset", self.cal_fah_to_cel(self.list_for_import_c[10].value())),                                  # type: ignore
                self.plc_writer_worker.get_item("P3_Temp2Offset", self.cal_fah_to_cel(self.list_for_import_c[11].value())),                                  # type: ignore
                self.plc_writer_worker.get_item("P3_Temp3Offset", self.cal_fah_to_cel(self.list_for_import_c[12].value()))                                   # type: ignore
            ]
            items_t0 = [
                self.plc_writer_worker.get_item("T0_TemperatureSetting", self.cal_fah_to_cel(self.list_for_import_t0[0].value())),                           # type: ignore
                self.plc_writer_worker.get_item("T0_TempLimitHIGH", self.cal_fah_to_cel(self.list_for_import_t0[1].value())),                                # type: ignore
                self.plc_writer_worker.get_item("T0_TempLimitLOW", self.cal_fah_to_cel(self.list_for_import_t0[2].value())),                                 # type: ignore
                self.plc_writer_worker.get_item("T0_TempOffset", self.cal_fah_to_cel(self.list_for_import_t0[3].value()))                                    # type: ignore
            ]
            self.plc_writer_worker.write_multi.emit(items_a, "A")                                                                       # type: ignore
            self.plc_writer_worker.write_multi.emit(items_b, "B")                                                                       # type: ignore
            self.plc_writer_worker.write_multi.emit(items_c, "C")                                                                       # type: ignore
            self.plc_writer_worker.write_multi.emit(items_t0, "T0")                                                                     # type: ignore
            
            self._unblock_import_widgets()

            self.disable_btn("A", False)
            self.disable_btn("B", False)
            self.disable_btn("C", False)
            self.disable_btn("T0", False)
        except Exception as e:
            # Mở lại signal, tránh các ô SV bị khoá vĩnh viễn (mất đồng bộ + không ghi PLC)
            self._unblock_import_widgets()
            self.logger.error(f"[Main]-[new_data_btn]: Error occurred - {str(e)}")

    def set_language_en(self):
        self._app.removeTranslator(self._translator)    # type: ignore
        self._current_lang = "en"

    def set_language_cn(self):
        self._app.removeTranslator(self._translator)    # type: ignore
        self._translator.load(resource_path("tech_link_theme_cn.qm"))
        self._app.installTranslator(self._translator)   # type: ignore
        self._current_lang = "cn"

    def set_language_vn(self):
        self._app.removeTranslator(self._translator)    # type: ignore
        self._translator.load(resource_path("tech_link_theme_vn.qm"))
        self._app.installTranslator(self._translator)   # type: ignore
        self._current_lang = "vn"
        
    def changeEvent(self, event):
        super().changeEvent(event)
        if event.type() == QEvent.Type.LanguageChange:
            ip_text = self.ui.plc_ip_address_edit.text()
            db_text = self.ui.db_file_path_edit.text()
            self.ui.retranslateUi(self)
            charts = [self.chart_temp, self.chart_pressure_a,
                        self.chart_pressure_b, self.chart_pressure_c]
            if self._current_lang == "cn":
                self.ui.plc_ip_address_edit.setPlaceholderText("请输入IP地址: 172.16.100.***")
                self.ui.db_file_path_edit.setPlaceholderText("输入路径文件夹")
                
                charts[0].btn_setting.setText("烤箱")
                charts[0].plot.setLabel("left", "温度 (°C)") if self._current_unit == 0 else charts[0].plot.setLabel("left", "温度 (°F)")
                
                charts[1].btn_setting.setText("A组")
                charts[1].plot.setLabel("left", "温度 (°C)") if self._current_unit == 0 else charts[1].plot.setLabel("left", "温度 (°F)")
                charts[1].plot.plotItem.axes["right"]["item"].setLabel("压力 (bar)")    # type: ignore
                
                charts[2].btn_setting.setText("B组")
                charts[2].plot.setLabel("left", "温度 (°C)") if self._current_unit == 0 else charts[2].plot.setLabel("left", "温度 (°F)")
                charts[2].plot.plotItem.axes["right"]["item"].setLabel("压力 (bar)")    # type: ignore
                
                charts[3].btn_setting.setText("C组")
                charts[3].plot.setLabel("left", "温度 (°C)") if self._current_unit == 0 else charts[3].plot.setLabel("left", "温度 (°F)")
                charts[3].plot.plotItem.axes["right"]["item"].setLabel("压力 (bar)")    # type: ignore

                self.ui.start_stop_btn.setText("开始") if not self.ui.start_stop_stacked.currentIndex() == 1 else self.ui.start_stop_btn.setText("停止")

            elif self._current_lang == "vn":
                self.ui.plc_ip_address_edit.setPlaceholderText("Vui lòng nhập địa chỉ IP: 172.16.100.***")
                self.ui.db_file_path_edit.setPlaceholderText("Nhập đường dẫn thư mục")
                
                charts[0].btn_setting.setText("Lò sấy")
                charts[0].plot.setLabel("left", "Nhiệt độ (°C)") if self._current_unit == 0 else charts[0].plot.setLabel("left", "Nhiệt độ (°F)")
                
                charts[1].btn_setting.setText("Nhóm A")
                charts[1].plot.setLabel("left", "Nhiệt độ (°C)") if self._current_unit == 0 else charts[1].plot.setLabel("left", "Nhiệt độ (°F)")
                charts[1].plot.plotItem.axes["right"]["item"].setLabel("Áp suất (bar)")    # type: ignore
                
                charts[2].btn_setting.setText("Nhóm B")
                charts[2].plot.setLabel("left", "Nhiệt độ (°C)") if self._current_unit == 0 else charts[2].plot.setLabel("left", "Nhiệt độ (°F)")
                charts[2].plot.plotItem.axes["right"]["item"].setLabel("Áp suất (bar)")    # type: ignore
                
                charts[3].btn_setting.setText("Nhóm C")
                charts[3].plot.setLabel("left", "Nhiệt độ (°C)") if self._current_unit == 0 else charts[3].plot.setLabel("left", "Nhiệt độ (°F)")
                charts[3].plot.plotItem.axes["right"]["item"].setLabel("Áp suất (bar)")    # type: ignore

                self.ui.start_stop_btn.setText("Bật") if not self.ui.start_stop_stacked.currentIndex() == 1 else self.ui.start_stop_btn.setText("Tắt")

            elif self._current_lang == "en":
                self.ui.plc_ip_address_edit.setPlaceholderText("Enter IP Address: 172.16.100.***")
                self.ui.db_file_path_edit.setPlaceholderText("Enter Path Folder")
                
                charts[0].btn_setting.setText("Furnace")
                charts[0].plot.setLabel("left", "Temperature (°C)") if self._current_unit == 0 else charts[0].plot.setLabel("left", "Temperature (°F)")
                
                charts[1].btn_setting.setText("Group A")
                charts[1].plot.setLabel("left", "Temperature (°C)") if self._current_unit == 0 else charts[1].plot.setLabel("left", "Temperature (°F)")
                charts[1].plot.plotItem.axes["right"]["item"].setLabel("Pressure (bar)")    # type: ignore
                
                charts[2].btn_setting.setText("Group B")
                charts[2].plot.setLabel("left", "Temperature (°C)") if self._current_unit == 0 else charts[2].plot.setLabel("left", "Temperature (°F)")
                charts[2].plot.plotItem.axes["right"]["item"].setLabel("Pressure (bar)")    # type: ignore
                
                charts[3].btn_setting.setText("Group C")
                charts[3].plot.setLabel("left", "Temperature (°C)") if self._current_unit == 0 else charts[3].plot.setLabel("left", "Temperature (°F)")
                charts[3].plot.plotItem.axes["right"]["item"].setLabel("Pressure (bar)")    # type: ignore
                
                self.ui.start_stop_btn.setText("Start") if not self.ui.start_stop_stacked.currentIndex() == 1 else self.ui.start_stop_btn.setText("Stop")
            self.ui.plc_ip_address_edit.setText(ip_text)
            self.ui.db_file_path_edit.setText(db_text)
            
    def _set_cur_unit(self):
        index = self.ui.temp_unit_selection_combox.currentIndex()
        for i in range(len(self.cel_fah_change)):
            self.cel_fah_change[i].setCurrentIndex(index)
        self._current_unit = index
        self._set_sv_widget_pressure_obj()
        self._set_sv_widget_temperature_obj()
        self._set_chart_unit()

    def _set_sv_widget_pressure_obj(self):
        self.pressure_a_sv_obj[0].blockSignals(True)
        self.pressure_a_sv_obj[0].setValue(self.convert_cel_fah(self.pressure_a_sv_obj[0].value()))
        self.pressure_a_sv_obj[0].blockSignals(False)
        self.pressure_b_sv_obj[0].blockSignals(True)
        self.pressure_b_sv_obj[0].setValue(self.convert_cel_fah(self.pressure_b_sv_obj[0].value()))
        self.pressure_b_sv_obj[0].blockSignals(False)
        self.pressure_c_sv_obj[0].blockSignals(True)
        self.pressure_c_sv_obj[0].setValue(self.convert_cel_fah(self.pressure_c_sv_obj[0].value()))
        self.pressure_c_sv_obj[0].blockSignals(False)

    def _set_sv_widget_temperature_obj(self):
        for i in range(4):
            self.temp_sv_obj[i].blockSignals(True)
            self.temp_sv_obj[i].setValue(self.convert_cel_fah(self.temp_sv_obj[i].value()))         # type: ignore
            self.temp_sv_obj[i].blockSignals(False)

            self.temp_h_alm_obj[i].blockSignals(True)
            self.temp_h_alm_obj[i].setValue(self.convert_cel_fah(self.temp_h_alm_obj[i].value()))   # type: ignore
            self.temp_h_alm_obj[i].blockSignals(False)

            self.temp_l_alm_obj[i].blockSignals(True)
            self.temp_l_alm_obj[i].setValue(self.convert_cel_fah(self.temp_l_alm_obj[i].value()))   # type: ignore
            self.temp_l_alm_obj[i].blockSignals(False)

        for i in range(len(self.temp_offset_obj)):
            self.temp_offset_obj[i].blockSignals(True)
            self.temp_offset_obj[i].setValue(self.convert_cel_fah(self.temp_offset_obj[i].value())) # type: ignore
            self.temp_offset_obj[i].blockSignals(False)

        for obj in self.tube_sv_obj + self.tube_pv_obj:
            obj.blockSignals(True)
            obj.setValue(self.convert_cel_fah(obj.value()))   # type: ignore
            obj.blockSignals(False)

    def _set_chart_unit(self):
        if self._current_unit not in (0, 1):
            return
        unit = "°C" if self._current_unit == 0 else "°F"
        name = "Temperature" if self._current_lang == "en" else "温度"
        for chart in (self.chart_temp, self.chart_pressure_a,
                      self.chart_pressure_b, self.chart_pressure_c):
            chart.set_temp_label(f"{name} ({unit})", unit=unit)
    
    def for_display_temp(self, celsius):
        if self._current_unit == 1:
            return celsius * 9/5 + 32
        return celsius

    def convert_cel_fah(self, temp):
        if self._current_unit == 1:
            return temp * 9/5 + 32
        elif self._current_unit == 0:
            return (temp - 32) * 5/9

    def cal_fah_to_cel(self, temp):
        if self._current_unit == 1:
            return (temp - 32) * 5/9
        return temp
    
    def cal_sec_to_msec(self, time_sec):
        return time_sec * 1000

    def apply_group_to_ui(self, group_dict: dict, widgets: list):
        for widget, value in zip(widgets, group_dict.values()):
            widget.blockSignals(True)
            try:
                if hasattr(widget, 'setValue'):
                    widget.setValue(float(value))
            finally:
                widget.blockSignals(False)
                
    def update_chart_temp(self):
        self.chart_temp.append_data([
            self.ui.t0_sv.value(),
            self.ui.t0_pv.value()
        ])

    def update_chart_pressure(self):
        ui = self.ui
        for grp, chart in (("a", self.chart_pressure_a),
                           ("b", self.chart_pressure_b),
                           ("c", self.chart_pressure_c)):
            chart.append_data(
                [getattr(ui, f"pressure_sv_{grp}_1").value(),
                 getattr(ui, f"pressure_pv_{grp}_2").value(),
                 getattr(ui, f"pressure_pv_{grp}_3").value(),
                 getattr(ui, f"pressure_pv_{grp}_4").value()],
                [getattr(ui, f"pressure_sv_{grp}_5").value(),
                 getattr(ui, f"pressure_pv_{grp}_5").value()],
            )

    def update_clock(self):
        now = QDateTime.currentDateTime()
        sec = now.toSecsSinceEpoch()
        if sec != self._last_clock_s:          # chỉ vẽ lại khi sang giây mới
            self._last_clock_s = sec
            self.ui.date_displ.setDateTime(now)

    # ---------------- Run time / Heat up time ----------------
    _RUN_TIME_SAVE_S = 60      # chu kỳ lưu Total Run Time vào settings.ini
    _HEAT_UP_TOL_C = 1.0       # coi như đạt nhiệt khi PV >= SV - sai số (°C)

    def _init_run_time(self):
        """Khởi tạo bộ đếm thời gian chạy máy và thời gian gia nhiệt."""
        self._total_run_s = self.app_settings.value("total_run_time_s", 0, type=int)  # type: ignore
        self._run_start = None          # time.monotonic() lúc nhấn Start, None khi đang Stop
        self._since_start_s = 0
        self._last_run_save = time.monotonic()
        # T0 (Heat Up Time chung), A, B, C: [mốc bắt đầu gia nhiệt, đã đạt nhiệt, số giây hiển thị]
        self._heat_up = {k: [None, False, 0] for k in ("T0", "A", "B", "C")}
        self.ui.total_run_time_val.setText(fmt_hm(self._total_run_s))

    def _save_run_time(self):
        total = self._total_run_s
        if self._run_start is not None:
            total += int(time.monotonic() - self._run_start)
        self.app_settings.setValue("total_run_time_s", total)
        self._last_run_save = time.monotonic()

    def _update_run_time(self):
        try:
            now = time.monotonic()
            running = self.ui.start_stop_stacked.currentIndex() == 1

            # Cur.Run Time: đếm từ lúc Start, giữ nguyên giá trị khi Stop
            if running and self._run_start is None:
                self._run_start = now
            elif not running and self._run_start is not None:
                self._total_run_s += int(now - self._run_start)
                self._run_start = None
                self._save_run_time()
            if self._run_start is not None:
                self._since_start_s = int(now - self._run_start)
                if now - self._last_run_save >= self._RUN_TIME_SAVE_S:
                    self._save_run_time()

            def _set(widget, text):             # tick 250 ms -> chỉ setText khi chữ đổi
                if widget.text() != text:
                    widget.setText(text)

            total_s = self._total_run_s + (self._since_start_s if self._run_start is not None else 0)
            _set(self.ui.total_run_time_val, fmt_hm(total_s))
            _set(self.ui.since_start_time_val, fmt_hms(self._since_start_s))

            # Heat Up Time: đếm từ lúc bật gia nhiệt đến khi nhiệt độ PV đạt Temp Setting
            with self._data_lock:
                actual = dict(self.actual_data)
                inp = dict(self.input_data)

            def _f(tag):
                v = actual.get(tag, inp.get(tag))
                return None if v is None else float(v)

            groups = (
                ("T0", self.ui.heat_t0_stacked.currentIndex() == 1, ("T0_Current_Temp",),
                 "T0_TemperatureSetting", self.ui.heat_up_time_val),
                ("A", self.ui.heat_btn_a.isChecked(), ("P1_Current_Temp1", "P1_Current_Temp2", "P1_Current_Temp3"),
                 "P1_TemperatureSetting", self.ui.a_heat_up_time_val),
                ("B", self.ui.heat_btn_b.isChecked(), ("P2_Current_Temp1", "P2_Current_Temp2", "P2_Current_Temp3"),
                 "P2_TemperatureSetting", self.ui.b_heat_up_time_val),
                ("C", self.ui.heat_btn_c.isChecked(), ("P3_Current_Temp1", "P3_Current_Temp2", "P3_Current_Temp3"),
                 "P3_TemperatureSetting", self.ui.c_heat_up_time_val),
            )
            for key, heating, pv_tags, sv_tag, widget in groups:
                state = self._heat_up[key]
                if not heating:
                    state[0] = None             # tắt gia nhiệt -> giữ giá trị cuối, lần bật sau đếm lại
                else:
                    if state[0] is None:
                        state[0], state[1], state[2] = now, False, 0
                    if not state[1]:
                        state[2] = int(now - state[0])
                        pvs = [_f(t) for t in pv_tags]
                        sv = _f(sv_tag)
                        if sv and sv > 0 and all(p is not None for p in pvs) \
                                and min(pvs) >= sv - self._HEAT_UP_TOL_C:  # type: ignore
                            state[1] = True     # đã đạt nhiệt -> dừng đếm
                _set(widget, fmt_hms(state[2]))
        except Exception as e:
            self.logger.error(f"[Main]-[_update_run_time]: Error occurred - {str(e)}")

    def disable_oil_group(self, channel, status):
        """
        Enable or disable UI controls during system operation.
        \nBật hoặc tắt các điều khiển UI trong quá trình hoạt động của máy.
        """
        if channel == "A":
            for i in range(5, 7):
                self.pressure_a_sv_obj[i].setEnabled(status)
            return

        elif channel == "B":
            for i in range(5, 7):
                self.pressure_b_sv_obj[i].setEnabled(status)
            return

        elif channel == "C":
            for i in range(5, 7):
                self.pressure_c_sv_obj[i].setEnabled(status)
            return

    def disable_pressure_group(self, channel, status):
        """
        Enable or disable UI controls during system operation.
        \nBật hoặc tắt các điều khiển UI trong quá trình hoạt động của máy.
        """
        if channel == "A":
            self.ui.set_cycle_a_btn.setEnabled(status)
            for i in range(1, 5):
                self.pressure_a_sv_obj[i].setEnabled(status)
            return

        elif channel == "B":
            self.ui.set_cycle_b_btn.setEnabled(status)
            for i in range(1, 5):
                self.pressure_b_sv_obj[i].setEnabled(status)
            return

        elif channel == "C":
            self.ui.set_cycle_c_btn.setEnabled(status)
            for i in range(1, 5):
                self.pressure_c_sv_obj[i].setEnabled(status)
            return

    def disable_heat_group(self, channel, status):
        """
        Enable or disable UI controls during system operation.
        \nBật hoặc tắt các điều khiển UI trong quá trình hoạt động của máy.
        """
        if channel == "A":  
            self.pressure_a_sv_obj[0].setEnabled(status)
            for i in [1]:
                self.temp_sv_obj[i].setEnabled(status)
                self.temp_h_alm_obj[i].setEnabled(status)
                self.temp_l_alm_obj[i].setEnabled(status)
            for i in range(1,4):
                self.temp_offset_obj[i].setEnabled(status)
            return

        elif channel == "B":
            self.pressure_b_sv_obj[0].setEnabled(status)
            for i in [2]:
                self.temp_sv_obj[i].setEnabled(status)
                self.temp_h_alm_obj[i].setEnabled(status)
                self.temp_l_alm_obj[i].setEnabled(status)
            for i in range(4,7):
                self.temp_offset_obj[i].setEnabled(status)
            return

        elif channel == "C":
            self.pressure_c_sv_obj[0].setEnabled(status)
            for i in [3]:
                self.temp_sv_obj[i].setEnabled(status)
                self.temp_h_alm_obj[i].setEnabled(status)
                self.temp_l_alm_obj[i].setEnabled(status)
            for i in range(7,10):
                self.temp_offset_obj[i].setEnabled(status)
            return

        elif channel in ("T0", "T0_On", "T0_Off"):
            for i in [0]:
                self.temp_sv_obj[i].setEnabled(status)
                self.temp_h_alm_obj[i].setEnabled(status)
                self.temp_l_alm_obj[i].setEnabled(status)
                self.temp_offset_obj[i].setEnabled(status)
            return

    def disable_btn(self, channel, status):
        # print(channel, status)
        if channel == "A":  
            self.ui.refuel_btn_a.setEnabled(status)
            self.ui.vacuum_btn_a.setEnabled(status)
            self.ui.heat_btn_a.setEnabled(status)
            return

        elif channel == "B":
            self.ui.refuel_btn_b.setEnabled(status)
            self.ui.vacuum_btn_b.setEnabled(status)
            self.ui.heat_btn_b.setEnabled(status)
            return

        elif channel == "C":
            self.ui.refuel_btn_c.setEnabled(status)
            self.ui.vacuum_btn_c.setEnabled(status)
            self.ui.heat_btn_c.setEnabled(status)
            return
        
        elif channel in ("T0", "T0_On", "T0_Off"):
            self.ui.heat_on_btn_t0.setEnabled(status)
            self.ui.heat_off_btn_t0.setEnabled(status)

    def export_all_tables_to_excel_btn(self):
        current_date = datetime.now().strftime("%d-%m-%Y")
        if self._current_lang == "cn":
            name = self.ui.search_data.text().strip() or "历史记录"
            group = "组"
        elif self._current_lang == "vn":
            name = self.ui.search_data.text().strip() or "Lịch sử"
            group = "Nhóm"
        else:
            name = self.ui.search_data.text().strip() or "History"
            group = "Group"
        default_filename_done = f"{name} - {group} {self.ui.select_group_name.currentText()} {current_date}"
        list_history_folder = Path(self.stk_mch_folder) / "Excel"
        list_history_folder.mkdir(parents=True, exist_ok=True)  
        filename_done = list_history_folder / f"{default_filename_done}.xlsx"
        if self.ui.stacked_list_history_page.currentIndex() == 0:
            if self._current_lang == "en":
                title = "Export All File"
                content = "This might take a while. Do you want to continue?"
            elif self._current_lang == "cn":
                title = "导出全部文件"
                content = "这可能需要一段时间. 是否继续?"
            elif self._current_lang == "vn":
                title = "Xuất toàn bộ lịch sử"
                content = "Việc này sẽ mất một lúc. Tiếp tục?"
            reply = ltmessage.question(
                self, title, content, lang=self._current_lang  # type: ignore
            )
            if reply == ltmessage.Yes:
                pass
            else:
                return
        self.export_table_to_excel(str(filename_done))

    def export_table_to_excel(self, default_filename: str = "export"):
        if getattr(self, '_exporting', False):
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Excel File", default_filename, "Excel Files (*.xlsx)"
        )
        if not file_path:
            return
        if not file_path.endswith(".xlsx"):
            file_path += ".xlsx"

        self._exporting = True
        # if self._current_lang == "en":
        #     text_disp = "Exporting... Please wait."
        # elif self._current_lang == "cn":
        #     text_disp = "导出中... 请等待."
        # elif self._current_lang == "vn":
        #     text_disp = "Đang tạo file..."
        # self.ui.error_display.setText(text_disp) # type: ignore
        self._export_thread = QThread()
        if self.ui.stacked_list_history_page.currentIndex() == 0:
            self._export_worker = ExportWorker(
                self.history_db_path,  # type: ignore
                file_path,
                lang=self._current_lang,
            )
        elif self.ui.stacked_list_history_page.currentIndex() == 1:
            self._export_worker = ExportWorker(
                db_path=self.history_db_path,   # type: ignore
                file_path=file_path,
                name=self.ui.search_data.text(),
                group=self.ui.select_group_name.currentText(),
                start_date=self.ui.search_data_start_edit.dateTime().toString("yyyy/MM/dd HH:mm"),
                end_date=self.ui.search_data_end_edit.dateTime().toString("yyyy/MM/dd HH:mm"),
                lang=self._current_lang,
            )
        self._export_worker.moveToThread(self._export_thread)

        self._export_thread.started.connect(self._export_worker.run)
        self._export_worker.finished.connect(self._on_export_done)
        self._export_worker.finished.connect(self._export_thread.quit)
        self._export_worker.finished.connect(self._export_worker.deleteLater)
        self._export_thread.finished.connect(self._export_thread.deleteLater)

        self._export_thread.start()
        self.ui.export_all_tables_to_excel_btn.setEnabled(False)

    def _on_export_done(self, file_path: str, error: str):
        self._exporting = False
        # self.ui.error_display.setText("")
        if error:
            if self._current_lang == "en":
                title = "Error"
                content = f"Export failed:\n{error}"
            elif self._current_lang == "cn":
                title = "错误"
                content = f"导出失败:\n{error}"
            elif self._current_lang == "vn":
                title = "Lỗi"
                content = f"Xuất file lỗi:\n{error}"
            ltmessage.error(self, title, content, lang=self._current_lang) # type: ignore
        else:
            if self._current_lang == "en":
                title = "Export Success"
                content = f"Go to Save Folder?"
            elif self._current_lang == "cn":
                title = "导出成功"
                content = "是否前往保存文件夹？"
            elif self._current_lang == "vn":
                title = "Xuất dữ liệu thành công"
                content = "Chuyển đến thư mục lưu trữ?"
            reply = ltmessage.custom(
                self, title, content, # type: ignore
                msg_type="success", lang=self._current_lang
            )
            if reply == ltmessage.Yes:
                folder = str(Path(file_path.split("|")[0]).parent)
                os.startfile(folder)
            else:
                pass
        self.ui.export_all_tables_to_excel_btn.setEnabled(True)

    def resizeEvent(self, event): # type: ignore
        super().resizeEvent(event)
        if hasattr(self, '_maximized_chart_idx') and self._maximized_chart_idx == -1:
            QTimer.singleShot(50, self._save_grid_rects)
            
    def closeEvent(self, event):
        self._shutting_down = True
        if self._current_lang == "en":
            title = "Exit Confirmation"
            content = "Are you sure you want to exit?"
        elif self._current_lang == "cn":
            title = "退出确认"
            content = "您确定要退出吗？"
        elif self._current_lang == "vn":
            title = "Xác nhận thoát"
            content = "Bạn có chắc chắn muốn thoát không?"
        reply = ltmessage.question(
            self, title, content, lang=self._current_lang # type: ignore
        )

        if reply == ltmessage.Yes:
            self.logger.info("Application is closing...")
            try:
                self._cleanup()
            except Exception as e:
                pass
            event.accept()
        else:
            event.ignore()
        
    def _cleanup(self):
        try:
            self._save_run_time()
        except Exception:
            pass
        try:
            if getattr(self, "alarm_conn", None) is not None:
                self.alarm_conn.close()
                self.alarm_conn = None
        except Exception:
            pass
        for timer in getattr(self, 'all_timer', []):
            if timer.isActive():
                timer.stop()
            timer.deleteLater()
        self.all_timer.clear()
        self.hide()
        workers = [
            getattr(self, 'plc_read_worker', None),
            getattr(self, 'plc_read_data_worker', None),
            getattr(self, 'plc_read_input_worker', None),
            getattr(self, 'plc_read_error_worker', None),
            getattr(self, 'plc_writer_worker', None),
            getattr(self, 'serial_data_worker', None),
        ]
        for worker in workers:
            if worker:
                try:
                    worker.stop()
                except:
                    pass

        threads = [
            getattr(self, 'plc_read_thread', None),
            getattr(self, 'plc_read_data_thread', None),
            getattr(self, 'plc_read_input_thread', None),
            getattr(self, 'plc_read_error_thread', None),
            getattr(self, 'plc_writer_thread', None),
            getattr(self, 'serial_data_thread', None),
        ]
        for thread in threads:
            if thread and thread.isRunning():
                try:
                    thread.wait()
                except:
                    pass