# pyside6-uic tech_link_theme.ui -o tech_link_theme.py
# pyside6-rcc Icon.qrc -o Icon_rc.py
# pyside6-rcc icons.qrc -o icons_rc.py

# pyside6-lupdate tech_link_theme.ui -ts tech_link_theme_en.ts
# pyside6-lupdate tech_link_theme.ui -ts tech_link_theme_cn.ts

import sys
import os
import time 
import pandas as pd
import io
import msoffcrypto
import logging
import sqlite3
import threading
import webbrowser
from PySide6.QtCore import (Qt, QTimer, QObject, 
                            QTime, QSettings, QDateTime,
                            QEvent, QThread, QEasingCurve, 
                            QTranslator)
from PySide6.QtGui import QFont, QFontDatabase, QPalette
from PySide6.QtWidgets import (QHeaderView, QAbstractSpinBox, QStyledItemDelegate,
                               QMainWindow, QApplication, QLineEdit,
                               QFileDialog, QTableWidget, QTableWidgetItem)
from typing import List, Optional, Tuple, Any
from pathlib import Path
from datetime import datetime
from tech_link_theme import Ui_MainWindow
from Custom_Widgets import * #type: ignore
from Custom_Chart_Widgets import CustomChartWidget
from message_box import LightThemeMessageBox as ltmessage
from password_dialog import *
from Data_Simulator import DataSimulator
from query_plc_thread_V2 import PLCRead
from write_plc_thread_V2 import PLCWrite
from export_excel_worker import ExportWorker

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"
os.environ["QT_FONT_DPI"] = "96"

BASE_DIR = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent

settings_path = str(BASE_DIR / "settings.ini")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS # type: ignore
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def install_clear_on_focus(widget):
    class FocusSelectFilter(QObject):
        def eventFilter(self, obj, event):
            if event.type() == QEvent.FocusIn:
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

class BackgroundDelegate(QStyledItemDelegate):
    def paint(self, painter: QPainter, option, index):
        bg = index.data(Qt.BackgroundRole)  # type: ignore
        if bg:
            painter.fillRect(option.rect, bg)
            option.palette.setColor(QPalette.ColorRole.Base, bg)
        super().paint(painter, option, index)

class StrikeMachine(QMainWindow):
    _request_scroll_reset   = Signal()
    _search_result_ready    = Signal(object)
    hide_loading            = Signal()
    show_loading            = Signal()

    def __init__(self, on_hide_loading=None, on_show_loading=None, parent=None):
        super().__init__(parent)
        if on_hide_loading:
            self.hide_loading.connect(on_hide_loading)
        if on_show_loading:
            self.show_loading.connect(on_show_loading)
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
        self._init_app_data()
        self._init_db_layout_and_size()
        self._init_timer()
        self._init_group_object()
        self._init_list_unit()
        self._create_charts()
        self._init_history_database()
        self._init_table_list_history()
        # self._setup_table()
        self._paint_pv_obj("#E53935")
        self._paint_sv_obj("#43A047")
        self._setup_btn_signals()
        self._setup_plc_threads(SIMULATE)
        self._translator = QTranslator()
        self.ui.home_page_btn.click()
        self.ui.clear_history_search.hide()
        self._set_time_search_data_start_edit()
        self._set_time_search_data_end_edit()
        self._search_result_ready.connect(
            self._on_search_fetched,
            Qt.ConnectionType.QueuedConnection
        )
        self.ui.stacked_list_history_page.setCurrentIndex(0)
        # QTimer.singleShot(2500, self._test_marquee_label)

    def _test_marquee_label(self):
        test_text = "Strike Machine System - Running Normally - No Error Detected"
        # test_text = "Hello Hello Hello"
        self.ui.error_display.setText(test_text)
        print(f"MarqueeLabel setText: '{self.ui.error_display.text()}'")
        print(f"Widget visible: {self.ui.error_display.isVisible()}")
        print(f"Widget size: {self.ui.error_display.size()}")

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
        
        df = self._read_protected_excel(path, password='tl@12345')
        if df is None:
            if self.logger:
                self.logger.error("[INIT]: Cannot read DB address file, app will not connect to PLC")
                self.show_loading.emit()
            return

        db_layout: List[Tuple[str, str, int, Any]] = []
        max_byte = 0
        
        for i in range(5, len(df)):
            row = df.iloc[i]
            # Cột B: Name
            name_raw = str(row[1]).strip() if pd.notna(row[1]) else ""
            if name_raw == "" or name_raw.lower() == "nan":
                break
                
            # Chuẩn hóa tên
            name = name_raw.replace(" ", "_").replace("-", "_")
            
            # Cột C: Type
            data_type = str(row[2]).strip().upper() if pd.notna(row[2]) else ""
            
            # Cột D: Address
            try:
                addr_str = str(row[3]).strip()

                if '.' in addr_str:
                    parts = addr_str.split('.')
                    byte_addr = int(float(parts[0]))
                    bit_from_addr = int(parts[1])  # lấy bit từ cột D luôn
                else:
                    byte_addr = int(float(addr_str))
                    bit_from_addr = 0

            except:
                byte_addr = 0
                bit_from_addr = 0

            if byte_addr > max_byte:
                max_byte = byte_addr

            # Xử lý Bit cho BOOL
            bit: Any = None
            if data_type == "BOOL":
                bit = bit_from_addr  # ← lấy từ addr_str, không đọc row[4] nữa

            db_layout.append((name, data_type, byte_addr, bit))
        
        last_item = db_layout[-1] if db_layout else None
        if last_item and last_item[1] == "STRING":
            string_start = last_item[2]
            db_total_bytes = string_start + 256
        else:
            db_total_bytes = max_byte + 4
        
        self.db_dict =  {
            "ip_plc": str(df.iloc[0, 1]).strip(),
            "read_time": int(str(df.iloc[1, 1]).strip()), # iloc[collumn, row]
            "write_time": int(str(df.iloc[2, 1]).strip()), 
            "db_name": int(str(df.iloc[3, 0]).strip().replace("DB", "")),
            "DB_LAYOUT": db_layout,
            "DB_TOTAL_BYTES": db_total_bytes
        }
        # self.logger.info(f"{self.db_dict}")
        self._gui_update_connection_group(stk_mch_file)

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
                return None  # ← return None, KHÔNG raise → app không bị tắt

        if sheet_name and sheet_name in df_dict:
            return df_dict[sheet_name]

        return next(iter(df_dict.values()))

    def _gui_update_connection_group(self, path_get):
        self.ui.plc_ip_address_edit.setText(self.db_dict["ip_plc"]) #type: ignore
        self.ui.db_file_path_edit.setText(str(path_get))
        self.ui.db_number_input.setValue(self.db_dict["db_name"]) #type: ignore
        self.ui.db_data_size_input.setValue(self.db_dict["DB_TOTAL_BYTES"]) #type: ignore
        self.ui.read_time_input.setValue(self.db_dict["read_time"]) #type: ignore
        self.ui.write_time_input.setValue(self.db_dict["write_time"]) #type: ignore

    def _init_logger(self):
        self.logger = logging.getLogger(__name__)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        # Tạo thư mục log nếu chưa có
        log_dir = self.stk_mch_folder/"Strike Machine Log"
        os.makedirs(log_dir, exist_ok=True)
        log_date = datetime.now().strftime("%d_%m_%Y")
        log_filename = os.path.join(log_dir, f'TL_SM_{log_date}.log')

        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        file_handler = logging.handlers.RotatingFileHandler( # type: ignore
            log_filename,
            maxBytes=5 * 1024 * 1024,
            backupCount=5,
            encoding='utf-8'
        )

        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        stream_handler.setFormatter(stream_formatter)
        self.logger.addHandler(stream_handler)

        # log_handler = QPlainTextEditLogger(self)
        # gui_formatter = logging.Formatter(
        #             '%(asctime)s - %(levelname)s - %(message)s'
        #         )
        # log_handler.setFormatter(gui_formatter)
        # self.logger.addHandler(log_handler)

        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonDblClick:
            double_click_actions = {
                self.ui.logo_btn        :self._on_logo_clicked,
                self.ui.plc_io_btn    : self.i_o_page_btn,
                self.ui.clear_group_a: self.clear_group_a_btn,
                self.ui.clear_group_b: self.clear_group_b_btn,
                self.ui.clear_group_c: self.clear_group_c_btn,
                self.ui.reset_cycle_a_btn: self.reset_cycle_a_btn("A"),
                self.ui.reset_cycle_b_btn: self.reset_cycle_a_btn("B"),
                self.ui.reset_cycle_c_btn: self.reset_cycle_a_btn("C"),
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
        self._displayed_offset = 0
        self.history_db_path = None
        self.conn = None
        self._history_batch_counter = 0
        self._db_offset = 0
        self._search_keyword = ""
        self._search_offset = 0
        self._search_cache = []
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
        
        self._last_i_o_group_3: list = [None] * 16
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

        self.init_signal = False

        self.plc_read_worker = None
        self.plc_read_connection = False
        self.plc_read_thread = None
        self.plc_writer_worker = None
        self.plc_writer_connection = False
        self.plc_writer_thread = None

        self.default_temp_room = 25.0
        
    def _init_timer(self):
        self.all_timer = []

        self.timer_alarm = QTimer()
        self.all_timer.append(self.timer_alarm)

        self.timer_stacked_pressure_page = QTimer()
        self.all_timer.append(self.timer_stacked_pressure_page)
        
        self.chart_timer = QTimer()
        self.all_timer.append(self.chart_timer)
        self.chart_timer.timeout.connect(self._update_all_charts)
        if self.db_dict is not None: # type: ignore
            self.chart_timer.setInterval(self.db_dict["read_time"]) # type: ignore
        else:
            self.chart_timer.setInterval(200)
        self.chart_timer.start()
        
        self._history_flush_timer = QTimer(self)
        self.all_timer.append(self._history_flush_timer)
        self._history_flush_timer.setInterval(1000)
        self._history_flush_timer.timeout.connect(self._flush_history)
        self._history_flush_timer.start()

        self._scroll_reset_timer = QTimer(self)
        self.all_timer.append(self._scroll_reset_timer)
        self._scroll_reset_timer.setSingleShot(True)
        self._scroll_reset_timer.timeout.connect(self._reset_to_latest_table_display)
        self._request_scroll_reset.connect(self._do_reset_scroll_timer, Qt.ConnectionType.QueuedConnection)

        self.date_time_timer = QTimer(self)
        self.all_timer.append(self.date_time_timer)
        self.date_time_timer.timeout.connect(self.update_clock)
        self.date_time_timer.start(1000)
        self.update_clock()

    def _update_all_charts(self):
        self.update_chart_temp()
        self.update_chart_pressure_a()
        self.update_chart_pressure_b()
        self.update_chart_pressure_c()

    def _init_group_object(self):
        # self.pressure_state_obj = []
        # for i in range(10):
        #     obj = getattr(self.ui, f"pressure_sv_a_{i}")
        #     self.pressure_state_obj.append(obj)
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

        self.io_group_1_switch_obj = tuple(
            getattr(self.ui, f"i_o_group_1_switch_{i}") for i in range(1, 14)
        )
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

    def _paint_pv_obj(self, color):
        for obj in self.pressure_a_pv_obj + self.pressure_b_pv_obj + self.pressure_c_pv_obj + self.temp_pv_obj:
            obj.setStyleSheet(f"""
                QDoubleSpinBox {{
                    color: {color};}}
                QSpinBox {{
                    color: {color};}}""")
            
    def _paint_sv_obj(self, color):
        for obj in self.pressure_a_sv_obj + self.pressure_b_sv_obj + self.pressure_c_sv_obj + self.temp_offset_obj + self.temp_h_alm_obj + self.temp_l_alm_obj + self.temp_sv_obj:
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

            self.ui.stacked_cel_fah_temp_b_1,
            self.ui.stacked_cel_fah_temp_b_2,
            self.ui.stacked_cel_fah_temp_b_3,
            self.ui.stacked_cel_fah_temp_b_4,
            self.ui.stacked_cel_fah_temp_b_5,
            self.ui.stacked_cel_fah_temp_b_6,
            self.ui.stacked_cel_fah_temp_b_7,

            self.ui.stacked_cel_fah_temp_c_1,
            self.ui.stacked_cel_fah_temp_c_2,
            self.ui.stacked_cel_fah_temp_c_3,
            self.ui.stacked_cel_fah_temp_c_4,
            self.ui.stacked_cel_fah_temp_c_5,
            self.ui.stacked_cel_fah_temp_c_6,
            self.ui.stacked_cel_fah_temp_c_7
        ]

    def _create_charts(self):
        font = QFont("Segoe UI", 17)
        font.setWeight(QFont.Weight.Bold)

        # Chart Nhiệt độ (Oven)
        self.chart_temp = CustomChartWidget(
            title="Oven",
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

        # Kết nối nút tiêu đề
        self.chart_temp.btn_setting.clicked.connect(self.temperature_page_btn)
        self.chart_pressure_a.btn_setting.clicked.connect(self.ui.home_page_btn.click)
        self.chart_pressure_b.btn_setting.clicked.connect(self.ui.home_page_btn.click)
        self.chart_pressure_c.btn_setting.clicked.connect(self.ui.home_page_btn.click)

        # Thêm vào layout
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

    def _save_grid_rects(self):
        rects = [f.geometry() for f in self._chart_frames]
        if all(r.width() > 0 and r.height() > 0 for r in rects):
            self._grid_rects = rects
            # print("Grid rects saved:", rects)  # xoá sau khi debug xong
        else:
            QTimer.singleShot(100, self._save_grid_rects)
    
    def _toggle_chart_frame(self, idx: int):
        frames = self._chart_frames
        charts = [self.chart_temp, self.chart_pressure_a,
                self.chart_pressure_b, self.chart_pressure_c]
        grid = self.ui.gridLayout_2

        # idx → (row, col) trong grid 2x2
        positions = {0: (0, 0), 1: (0, 1), 2: (1, 0), 3: (1, 1)}
        row, col = positions[idx]

        if self._maximized_chart_idx == idx:
            # ── Thu nhỏ ───────────────────────────────────────────────────────
            self._maximized_chart_idx = -1

            # Trả stretch về đều
            grid.setRowStretch(0, 1)
            grid.setRowStretch(1, 1)
            grid.setColumnStretch(0, 1)
            grid.setColumnStretch(1, 1)

            # Hiện lại 3 frame còn lại
            for i, f in enumerate(frames):
                if i != idx:
                    f.show()

            # Bật lại render timer cho tất cả
            for c in charts:
                c._render_timer.start()

        else:
            # ── Phóng to ──────────────────────────────────────────────────────
            self._maximized_chart_idx = idx

            other_row = 1 if row == 0 else 0
            other_col = 1 if col == 0 else 0

            grid.setRowStretch(row,       100)
            grid.setRowStretch(other_row, 0)
            grid.setColumnStretch(col,       100)
            grid.setColumnStretch(other_col, 0)

            # Ẩn 3 frame còn lại + tắt render timer
            for i, f in enumerate(frames):
                if i != idx:
                    f.hide()
                    charts[i]._render_timer.stop()
        
    ###########################################################################################
    #############################------ Button Function Setup ------###########################
    def _setup_btn_signals(self):
        self.ui.left_side_menu_widget.customizeQCustomSlideMenu(
            defaultWidth = 70,
            defaultHeight = "parent",
            collapsedWidth = 70,
            collapsedHeight = "parent",
            expandedWidth = 175,
            expandedHeight = "parent",
            animationDuration = 200,
            animationEasingCurve = QEasingCurve.Linear,  # type: ignore
            collapsingAnimationDuration = 200,
            collapsingAnimationEasingCurve = QEasingCurve.Linear,  # type: ignore
            expandingAnimationDuration = 200,
            expandingAnimationEasingCurve = QEasingCurve.Linear,  # type: ignore
        )
        self.ui.open_side_menu_btn.clicked.connect(self._on_menu_toggle)
        self.ui.logo_btn.installEventFilter(self)
        
        ### Left side menu button
        self.ui.home_page_btn.clicked.connect(self.pressure_page_btn)
        self.ui.chart_page_btn.clicked.connect(self.home_page_btn)
        self.ui.device_page_btn.clicked.connect(self.device_page_btn)
        self.ui.history_page_btn.clicked.connect(self.history_page_btn)

        self.ui.eng_language.clicked.connect(self.set_language_en)
        self.ui.cn_language.clicked.connect(self.set_language_cn)

        self.ui.next_group_page_btn.clicked.connect(self.next_previous_pressure_page)

        self.ui.back_connection_page_btn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.connection_page))
        self.ui.back_home_page_btn.clicked.connect(lambda: self.ui.home_page_btn.click())

        self.ui.temp_unit_selection_combox.currentIndexChanged.connect(lambda: QTimer.singleShot(50, self._set_cur_unit))

        self.ui.plc_io_btn.installEventFilter(self)

        self.ui.new_data_btn.clicked.connect(self.new_data_btn)

        if SIMULATE:
            self.ui.heat_btn_a.toggled.connect(lambda checked: self.simu_heat_btn("A", checked)) 
            self.ui.heat_btn_b.toggled.connect(lambda checked: self.simu_heat_btn("B", checked))
            self.ui.heat_btn_c.toggled.connect(lambda checked: self.simu_heat_btn("C", checked))

            self.ui.vacuum_btn_a.toggled.connect(lambda checked: self.simu_pressure_btn("A", checked))
            self.ui.vacuum_btn_b.toggled.connect(lambda checked: self.simu_pressure_btn("B", checked))
            self.ui.vacuum_btn_c.toggled.connect(lambda checked: self.simu_pressure_btn("C", checked))

            # self.ui.refuel_btn_a.toggled.connect(lambda checked: self.simu_oil_btn("A", checked))
            # self.ui.refuel_btn_b.toggled.connect(lambda checked: self.simu_oil_btn("B", checked))
            # self.ui.refuel_btn_c.toggled.connect(lambda checked: self.simu_oil_btn("C", checked))
        else:
            self.ui.start_btn.clicked.connect(lambda: self.start_stop_btn(self.ui.start_btn))
            self.ui.stop_btn.clicked.connect(lambda: self.start_stop_btn(self.ui.stop_btn))

            self.ui.heat_btn_a.toggled.connect(lambda checked: self.heating_btn("A", checked, self.ui.heat_btn_a)) 
            self.ui.heat_btn_b.toggled.connect(lambda checked: self.heating_btn("B", checked, self.ui.heat_btn_b))
            self.ui.heat_btn_c.toggled.connect(lambda checked: self.heating_btn("C", checked, self.ui.heat_btn_c))
            self.ui.heat_btn_t0.toggled.connect(lambda checked: self.heating_btn("T0", checked, self.ui.heat_btn_t0))

            self.ui.vacuum_btn_a.toggled.connect(lambda checked: self.pumping_btn("A", checked, self.ui.vacuum_btn_a))
            self.ui.vacuum_btn_b.toggled.connect(lambda checked: self.pumping_btn("B", checked, self.ui.vacuum_btn_b))
            self.ui.vacuum_btn_c.toggled.connect(lambda checked: self.pumping_btn("C", checked, self.ui.vacuum_btn_c))

            self.ui.refuel_btn_a.toggled.connect(lambda checked: self.fill_oil_btn("A", checked, self.ui.refuel_btn_a))
            self.ui.refuel_btn_b.toggled.connect(lambda checked: self.fill_oil_btn("B", checked, self.ui.refuel_btn_b))
            self.ui.refuel_btn_c.toggled.connect(lambda checked: self.fill_oil_btn("C", checked, self.ui.refuel_btn_c))

            self.ui.set_cycle_a_btn.toggled.connect(lambda checked: self.cycle_loop_btn("A", checked, self.ui.set_cycle_a_btn))
            self.ui.set_cycle_b_btn.toggled.connect(lambda checked: self.cycle_loop_btn("B", checked, self.ui.set_cycle_b_btn))
            self.ui.set_cycle_c_btn.toggled.connect(lambda checked: self.cycle_loop_btn("C", checked, self.ui.set_cycle_c_btn))

            self.ui.clear_data_btn.clicked.connect(self.clear_data_btn)
            
            self.ui.clear_group_a.installEventFilter(self)
            self.ui.clear_group_b.installEventFilter(self)
            self.ui.clear_group_c.installEventFilter(self)

            self.ui.reset_cycle_a_btn.clicked.connect(lambda: self.plc_writer_worker.write_value.emit("P1_Number_Test_Times", 0) if self.plc_writer_connection else None) #type: ignore
            self.ui.reset_cycle_b_btn.clicked.connect(lambda: self.plc_writer_worker.write_value.emit("P2_Number_Test_Times", 0) if self.plc_writer_connection else None) #type: ignore
            self.ui.reset_cycle_c_btn.clicked.connect(lambda: self.plc_writer_worker.write_value.emit("P3_Number_Test_Times", 0) if self.plc_writer_connection else None) #type: ignore

        self.ui.search_data.textChanged.connect(self._on_search_changed)
        self.ui.select_group_name.currentTextChanged.connect(self._on_search_changed)
        self.ui.search_data_start_edit.dateTimeChanged.connect(self._on_search_changed)
        self.ui.search_data_end_edit.dateTimeChanged.connect(self._on_search_changed)
        self.ui.clear_history_search.clicked.connect(self._on_clear_clicked)
        self.ui.export_all_tables_to_excel_btn.clicked.connect(self.export_all_tables_to_excel_btn)
        self.ui.list_history_2.verticalScrollBar().valueChanged.connect(self._on_search_scroll)

        spinbox_map = {
            "pressure_sv_a_1": self.on_pressure_sv_a_1_changed,
            "pressure_sv_a_5": self.on_pressure_sv_a_5_changed,
            "pressure_sv_a_6": self.on_pressure_sv_a_6_changed,
            "pressure_sv_a_7": self.on_pressure_sv_a_7_changed,
            "pressure_sv_a_8": self.on_pressure_sv_a_8_changed,
            "pressure_sv_a_9": self.on_pressure_sv_a_9_changed,
            "pressure_sv_a_10": self.on_pressure_sv_a_10_changed,
            "pressure_sv_a_11": self.on_cycle_a_displ_2_changed,

            "pressure_sv_b_1": self.on_pressure_sv_b_1_changed,
            "pressure_sv_b_5": self.on_pressure_sv_b_5_changed,
            "pressure_sv_b_6": self.on_pressure_sv_b_6_changed,
            "pressure_sv_b_7": self.on_pressure_sv_b_7_changed,
            "pressure_sv_b_8": self.on_pressure_sv_b_8_changed,
            "pressure_sv_b_9": self.on_pressure_sv_b_9_changed,
            "pressure_sv_b_10": self.on_pressure_sv_b_10_changed,
            "pressure_sv_b_11": self.on_cycle_b_displ_2_changed,

            "pressure_sv_c_1": self.on_pressure_sv_c_1_changed,
            "pressure_sv_c_5": self.on_pressure_sv_c_5_changed,
            "pressure_sv_c_6": self.on_pressure_sv_c_6_changed,
            "pressure_sv_c_7": self.on_pressure_sv_c_7_changed,
            "pressure_sv_c_8": self.on_pressure_sv_c_8_changed,
            "pressure_sv_c_9": self.on_pressure_sv_c_9_changed,
            "pressure_sv_c_10": self.on_pressure_sv_c_10_changed,
            "pressure_sv_c_11": self.on_cycle_c_displ_2_changed,

            "t0_sv": self.on_t0_sv_changed,
            "at_sv": self.on_at_sv_changed,
            "bt_sv": self.on_bt_sv_changed,
            "ct_sv": self.on_ct_sv_changed,

            "t0_h_alm_value": self.on_t0_h_alm_value_changed,
            "at_h_alm_value": self.on_at_h_alm_value_changed,
            "bt_h_alm_value": self.on_bt_h_alm_value_changed,
            "ct_h_alm_value": self.on_ct_h_alm_value_changed,

            "t0_l_alm_value": self.on_t0_l_alm_value_changed,
            "at_l_alm_value": self.on_at_l_alm_value_changed,
            "bt_l_alm_value": self.on_bt_l_alm_value_changed,
            "ct_l_alm_value": self.on_ct_l_alm_value_changed,

            "t0_offset_value": self.on_t0_offset_value_changed,
            "at_t1_offset_value": self.on_at_t1_offset_value_changed,
            "at_t2_offset_value": self.on_at_t2_offset_value_changed,
            "at_t3_offset_value": self.on_at_t3_offset_value_changed,
            "bt_t1_offset_value": self.on_bt_t1_offset_value_changed,
            "bt_t2_offset_value": self.on_bt_t2_offset_value_changed,
            "bt_t3_offset_value": self.on_bt_t3_offset_value_changed,
            "ct_t1_offset_value": self.on_ct_t1_offset_value_changed,
            "ct_t2_offset_value": self.on_ct_t2_offset_value_changed,
            "ct_t3_offset_value": self.on_ct_t3_offset_value_changed,

            "table_write_cycle": self.on_table_write_cycle_value_changed,

        }

        install_clear_on_focus(self.ui.db_file_path_edit)
        install_clear_on_focus(self.ui.plc_ip_address_edit)
        install_clear_on_focus(self.ui.db_number_input)
        install_clear_on_focus(self.ui.db_data_size_input)
        install_clear_on_focus(self.ui.error_display)

        protect_widgets_on_stacked(self.ui.stackedWidget_2, [
            (self.ui.db_file_path_edit,   None, None),
            (self.ui.plc_ip_address_edit, None, None),
            (self.ui.db_number_input,     None, None),
            (self.ui.db_data_size_input,  None, None)
        ])

        for name, handler in spinbox_map.items():
            spinbox = getattr(self.ui, name)
            install_clear_on_focus(spinbox)
            spinbox.setKeyboardTracking(False)
            spinbox.valueChanged.connect(handler)

        self.ui.error_display._speed = 50

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
                        "Temperature SV." TEXT,
                        "T-Oven." TEXT,
                        "Front." TEXT,
                        "Middle." TEXT,
                        "End." TEXT,
                        "Date." TEXT
                    )
                ''')
            for col_name in ["Pressure SV.", "Temperature SV."]:
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
            str(row["T-Oven."]       or ""),
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

            self._render_chunk(0, len(self._all_rows_cache))

            self._apply_span(self.ui.list_history)

            self.ui.list_history.verticalScrollBar().valueChanged.connect(
                self._on_history_scroll
            )
            self.ui.list_history.scrollToBottom()
            self.logger.info(f"Total {total_db:,} records, showing last {self._table_display}")
            self._resize_table_columns(self.ui.list_history)

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
                "a": (self.ui.pressure_sv_a_5, self.ui.pressure_sv_a_1),
                "b": (self.ui.pressure_sv_b_5, self.ui.pressure_sv_b_1),
                "c": (self.ui.pressure_sv_c_5, self.ui.pressure_sv_c_1),
            }

            for g in groups:
                group_key = g["group"].replace("Group ", "").strip().lower()  # "Group A" -> "a"
                
                pressure_sv_widget, temp_sv_widget = sv_widget_map.get(group_key, (None, None))
                
                pressure_sv_val = float(pressure_sv_widget.text()) if pressure_sv_widget else 0.0
                temp_sv_val     = float(temp_sv_widget.text())     if temp_sv_widget     else 0.0

                db_row = [
                    "",                         # [0] batch_no - gán sau
                    product_name,               # [1]
                    g["group"],                 # [2]
                    f"{pressure_sv_val:.2f} bar",  # [3] Pressure SV.
                    f"{g['pressure']:.2f} bar", # [4] Pressure.
                    fmt(temp_sv_val),           # [5] Temperature SV.
                    fmt(g["temp"]),             # [6] T-Oven.
                    fmt(g["front"]),            # [7] Front.
                    fmt(g["mid"]),              # [8] Middle.
                    fmt(g["end"]),              # [9] End.
                    today_date                  # [10] Date.
                ]

                ui_row = [
                    db_row[0],   # No.
                    db_row[1],   # Name.
                    db_row[2],   # Group.
                    db_row[4],   # Pressure.      <- db index 4
                    db_row[6],   # T-Oven.        <- db index 6
                    db_row[7],   # Front.
                    db_row[8],   # Middle.
                    db_row[9],   # End.
                    db_row[10],  # Date.
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
                    "No.", "Name.", "Group.",
                    "Pressure SV.", "Pressure.",
                    "Temperature SV.", "T-Oven.",
                    "Front.", "Middle.", "End.", "Date."
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', db_rows)
            self.conn.commit()
        except Exception as e:
            self.logger.error(f"[_flush_history][DB] {e}")

        table         = self.ui.list_history
        scrollbar     = table.verticalScrollBar()
        was_at_bottom = scrollbar.value() >= scrollbar.maximum() - 5

        table.setUpdatesEnabled(False)

        for ui_row in ui_rows:
            row_pos = table.rowCount()
            table.insertRow(row_pos)
            for col, value in enumerate(ui_row):
                table.setItem(row_pos, col,
                    self._make_colored_item(str(value), self._history_batch_counter))

            if table.rowCount() > self._table_display:
                table.removeRow(0)

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

        table            = self.ui.list_history
        existing_batches = self._count_batches(table)
        prev_no          = None
        batch_counter    = existing_batches

        table.setUpdatesEnabled(False)

        for row_data in chunk:
            current_no = str(row_data[0]) if row_data[0] else ""
            if current_no != prev_no:
                batch_counter += 1
                prev_no = current_no

            row_pos = table.rowCount()
            table.insertRow(row_pos)
            for col, value in enumerate(row_data):
                table.setItem(row_pos, col,
                    self._make_colored_item(str(value), batch_counter))

        table.setUpdatesEnabled(True)

    def _make_colored_item(self, value: str, batch_counter: int) -> QTableWidgetItem:
        item = QTableWidgetItem(value)
        item.setTextAlignment(Qt.AlignCenter)  # type: ignore
        color = self._COLOR_EVEN if batch_counter % 2 == 0 else self._COLOR_ODD
        # print(f"batch={batch_counter}, color={color.name()}")
        item.setData(Qt.BackgroundRole, color)  # type: ignore
        return item

    def _on_history_scroll(self, value: int):
        sb = self.ui.list_history.verticalScrollBar()
        if value <= sb.minimum() + 50:
            if self._db_offset <= 0:
                pass
            elif not getattr(self, '_loading_history_chunk', False):
                self._loading_history_chunk = True
                QTimer.singleShot(1000, self._prepend_history_chunk)

        self._request_scroll_reset.emit()

    def _prepend_history_chunk(self):
        try:
            if self._db_offset <= 0:
                return

            table = self.ui.list_history
            sb    = table.verticalScrollBar()

            if sb.value() > sb.minimum() + 50:
                return

            try:
                sb.valueChanged.disconnect(self._on_history_scroll)
            except:
                pass

            fetch_start = max(0, self._db_offset - self._table_display)
            fetch_count = self._db_offset - fetch_start

            cursor = self.conn.cursor()  # type: ignore
            cursor.execute(
                'SELECT * FROM history ORDER BY id ASC LIMIT ? OFFSET ?',
                (fetch_count, fetch_start)
            )
            rows = cursor.fetchall()

            new_chunk = []
            for idx, row in enumerate(rows):
                stt = row[1] if row[1] else str(fetch_start + idx + 1)
                formatted = self._db_row_to_ui(row, stt)
                new_chunk.append(formatted)

            if not new_chunk:
                return

            self._db_offset      = fetch_start
            self._all_rows_cache = new_chunk + self._all_rows_cache

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
            self._apply_span(table)

            table.scrollTo(
                table.model().index(len(new_chunk), 0),
                QTableWidget.ScrollHint.PositionAtTop
            )

            sb.valueChanged.connect(self._on_history_scroll)

        finally:
            self._loading_history_chunk = False
            
    def _reset_scroll_timer(self):
        """Mỗi lần scroll đều reset timer — sau 10s không scroll thì về {self._table_display} dòng cuối"""
        if not hasattr(self, '_scroll_reset_timer'):
            self._scroll_reset_timer = QTimer(self)
            self._scroll_reset_timer.setSingleShot(True)
            self._scroll_reset_timer.timeout.connect(self._reset_to_latest_table_display)

        self._scroll_reset_timer.stop()
        self._scroll_reset_timer.start(5000)  # 5s

    def _reset_to_latest_table_display(self):
        table = self.ui.list_history
        sb = table.verticalScrollBar()

        if sb.value() >= sb.maximum() - 5:
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

        table.setUpdatesEnabled(False)
        table.setRowCount(0)
        self._render_chunk(0, len(self._all_rows_cache))
        table.setUpdatesEnabled(True)

        self._apply_span(table)
        table.scrollToBottom()

        sb.valueChanged.connect(self._on_history_scroll)

    def _do_reset_scroll_timer(self):
        self._scroll_reset_timer.stop()
        self._scroll_reset_timer.start(10000)

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
        self._apply_span(table)

        table.scrollTo(
            table.model().index(len(new_chunk), 0),
            QTableWidget.ScrollHint.PositionAtTop
        )

    def _count_batches(self, table) -> int:
        seen = set()
        for row in range(table.rowCount()):
            item = table.item(row, 0)
            if item:
                seen.add(item.text())
        return len(seen)

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
        if is_maximized:
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(last_col, QHeaderView.ResizeMode.ResizeToContents)
        else:
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
        
    # ── Group A ──────────────────────────────────────────
    def on_pressure_sv_a_1_changed(self, value: float): 
        if self.plc_writer_connection:
            self.plc_writer_worker.write_value.emit("P1_TemperatureSetting", self.cal_fah_to_cel(value)) #type: ignore
        else: 
            pass
        self.ui.at_sv.blockSignals(True)
        self.ui.at_sv.setValue(value)
        self.ui.at_sv.blockSignals(False)

    def on_pressure_sv_a_5_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_PressureSetting", value) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_a_6_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_Air_FillingTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_a_7_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_Air_HoldingTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_a_8_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_Air_ReleaseTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_a_9_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_Oil_Start_Time", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_a_10_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_Oil_End_Time", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore

    # ── Group B ──────────────────────────────────────────
    def on_pressure_sv_b_1_changed(self, value: float): 
        if self.plc_writer_connection:
            self.plc_writer_worker.write_value.emit("P2_TemperatureSetting", self.cal_fah_to_cel(value)) #type: ignore
        else: 
            pass
        self.ui.bt_sv.blockSignals(True)
        self.ui.bt_sv.setValue(value)
        self.ui.bt_sv.blockSignals(False)

    def on_pressure_sv_b_5_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_PressureSetting", value) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_b_6_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_Air_FillingTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_b_7_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_Air_HoldingTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_b_8_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_Air_ReleaseTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_b_9_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_Oil_Start_Time", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_b_10_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_Oil_End_Time", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore

    # ── Group C ──────────────────────────────────────────
    def on_pressure_sv_c_1_changed(self, value: float): 
        if self.plc_writer_connection:
            self.plc_writer_worker.write_value.emit("P3_TemperatureSetting", self.cal_fah_to_cel(value)) #type: ignore
        else: 
            pass
        self.ui.ct_sv.blockSignals(True)
        self.ui.ct_sv.setValue(value)
        self.ui.ct_sv.blockSignals(False)

    def on_pressure_sv_c_5_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_PressureSetting", value) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_c_6_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_Air_FillingTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_c_7_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_Air_HoldingTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_c_8_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_Air_ReleaseTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_c_9_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_Oil_Start_Time", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_c_10_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_Oil_End_Time", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore

    # ── Cycle ──────────────────────────────────────────
    def on_cycle_a_displ_2_changed(self, value: int): self.plc_writer_worker.write_value.emit("P1_CountTimes", value) if self.plc_writer_connection else None #type: ignore
    def on_cycle_b_displ_2_changed(self, value: int): self.plc_writer_worker.write_value.emit("P2_CountTimes", value) if self.plc_writer_connection else None #type: ignore
    def on_cycle_c_displ_2_changed(self, value: int): self.plc_writer_worker.write_value.emit("P3_CountTimes", value) if self.plc_writer_connection else None #type: ignore

    # ── Temperature Modify ──────────────────────────────────────────
    def on_t0_sv_changed(self, value: float): self.plc_writer_worker.write_value.emit("T0_TemperatureSetting", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_at_sv_changed(self, value: float): self.ui.pressure_sv_a_1.setValue(value)
    def on_bt_sv_changed(self, value: float): self.ui.pressure_sv_b_1.setValue(value)
    def on_ct_sv_changed(self, value: float): self.ui.pressure_sv_c_1.setValue(value)

    def on_t0_h_alm_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("T0_TempLimitHIGH", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_at_h_alm_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_TempLimitHIGH", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_bt_h_alm_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_TempLimitHIGH", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_ct_h_alm_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_TempLimitHIGH", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore

    def on_t0_l_alm_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("T0_TempLimitLOW", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_at_l_alm_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_TempLimitLOW", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_bt_l_alm_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_TempLimitLOW", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_ct_l_alm_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_TempLimitLOW", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore

    def on_t0_offset_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("T0_TempOffset", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_at_t1_offset_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_Temp1Offset", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_at_t2_offset_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_Temp2Offset", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_at_t3_offset_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_Temp3Offset", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_bt_t1_offset_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_Temp1Offset", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_bt_t2_offset_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_Temp2Offset", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_bt_t3_offset_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_Temp3Offset", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_ct_t1_offset_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_Temp1Offset", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_ct_t2_offset_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_Temp2Offset", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_ct_t3_offset_value_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_Temp3Offset", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_table_write_cycle_value_changed(self, value: float): self.ui.table_write_cycle.setValue(float(self.ui.read_time_input.value())/1000) if (value*1000) < self.ui.read_time_input.value() else None #type: ignore

    def _on_logo_clicked(self):
        webbrowser.open("https://www.techlinksilicones.com/")

    def _on_menu_toggle(self):
        if self.ui.stackedWidget_2.currentIndex() == 0:
            self._pause_charts()
            self.ui.left_side_menu_widget.slideMenu()
            QTimer.singleShot(220, self._resume_charts)
        else:
            self.ui.left_side_menu_widget.slideMenu()

    def _pause_charts(self): 
        self.chart_temp._render_timer.stop()
        self.chart_pressure_a._render_timer.stop()
        self.chart_pressure_b._render_timer.stop()
        self.chart_pressure_c._render_timer.stop()

    def _resume_charts(self):
        self.chart_temp._render_timer.start()
        self.chart_pressure_a._render_timer.start()
        self.chart_pressure_b._render_timer.start()
        self.chart_pressure_c._render_timer.start()

    def home_page_btn(self):
        self.user = False
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.menu_page)

    def pressure_page_btn(self):
        self.user = False
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.temp_press_page)
        self.ui.stackedWidget.setCurrentWidget(self.ui.pressure_page)

    def temperature_page_btn(self):
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
        self.user = False
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.history_page)

    # def (self):
    
    def next_previous_pressure_page(self):
        index = self.ui.stackedWidget.currentIndex()
        if index == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
        elif index == 1:
            self.ui.stackedWidget.setCurrentIndex(0)

    def _setup_plc_threads(self, state: bool):
        if state:
            self.logger.info("PLC Thread set Off")
            self.setup_simulate_threads()
            return
        
        if not self.db_dict:
            self.hide_loading.emit()
            ltmessage.error(self, "Error", "DB Layout not found! Cannot start PLC threads.")
            return 

        if not self._setup_write_plc_thread(
            ip=self.db_dict["ip_plc"],
            db_number=self.db_dict["db_name"],
            db_layout=self.db_dict["DB_LAYOUT"],
            db_size=self.db_dict["DB_TOTAL_BYTES"],
            poll_ms=self.db_dict["write_time"],
            logger=self.logger
        ):
            ltmessage.error(self, "Error", "Failed to connect to PLC! Try again later.")

        time.sleep(0.2)

        if not self._setup_read_plc_thread(
            ip=self.db_dict["ip_plc"],
            db_number=self.db_dict["db_name"],
            db_layout=self.db_dict["DB_LAYOUT"],
            db_size=self.db_dict["DB_TOTAL_BYTES"],
            poll_ms=self.db_dict["read_time"],
            logger=self.logger
        ):
            ltmessage.error(self, "Error", "Failed to connect to PLC! Try again later.")

    def setup_simulate_threads(self):
        try:
            simulate_thread = DataSimulator()
            simulate_thread.db_data_convert.connect(self._data_group_filter)
            simulate_thread.start()
            self.thread_dict["data_simulator"] = simulate_thread

            if not simulate_thread.isRunning():
                raise Exception("DataSimulator thread failed to start")

            time.sleep(0.1)

        except Exception as e:
            return 

    def _setup_read_plc_thread(
            self, 
            ip: str = "172.16.100.100", 
            db_number: Optional[int] = None, 
            db_layout: Optional[list[tuple[str, str, int, Any]]] = None, 
            db_size: Optional[int] = None, 
            poll_ms: int = 500,
            logger: Optional[logging.Logger] = None
            ):
        try:
            if db_number is None:
                raise ValueError("DB number is not defined. Cannot start PLC read thread.")
            elif db_layout is None:
                raise ValueError("DB layout is not defined. Cannot start PLC read thread.")
            elif db_size is None:
                raise ValueError("DB size is not defined. Cannot start PLC read thread.")
            
            self.plc_read_thread = QThread()
            self.plc_read_worker = PLCRead(
                ip=ip,
                db_number=db_number,
                db_layout=db_layout,
                db_size=db_size,
                poll_ms=poll_ms,
                logger=logger
            )
            self.plc_read_worker.moveToThread(self.plc_read_thread)

            self.plc_read_thread.started.connect(self.plc_read_worker.run)
            self.plc_read_worker.data_ready.connect(self._data_ready)
            self.plc_read_worker.connected.connect(self._read_status_plc)
            self.plc_read_worker.init_data.connect(self._set_system_data)
            
            self.plc_read_worker.finished.connect(self.plc_read_thread.quit)
            self.plc_read_worker.finished.connect(self.plc_read_worker.deleteLater)
            self.plc_read_thread.finished.connect(self.plc_read_thread.deleteLater)

            self.plc_read_thread.start()
            if not self.plc_read_thread.isRunning():
                raise Exception("plc_read_thread failed to start")
        except Exception as e:
            self.logger.info("PLC Reader gone wrong:", e)
            return False
        
        self.worker_dict["plc_read_worker"] = self.plc_read_worker
        return True

    def _setup_write_plc_thread(
            self, 
            ip: str = "172.100.16.100", 
            db_number: Optional[int] = None, 
            db_layout: Optional[List] = None, 
            db_size: Optional[int] = None, 
            poll_ms: int = 500,
            logger: Optional[logging.Logger] = None
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
                logger=logger
            )
            self.plc_writer_worker.moveToThread(self.plc_writer_thread)
            self.plc_writer_thread.started.connect(self.plc_writer_worker.run)
            self.plc_writer_worker.connected.connect(self._write_status_plc)
            self.plc_writer_worker.write_multi_done.connect(self.disable_btn)

            self.plc_writer_worker.finished.connect(self.plc_writer_thread.quit)
            self.plc_writer_worker.finished.connect(self.plc_writer_worker.deleteLater)
            self.plc_writer_thread.finished.connect(self.plc_writer_thread.deleteLater)

            self.plc_writer_thread.start()
            
        except Exception as e:
            self.logger.info("PLC Writer gone wrong:", e)
            return False
        self.thread_dict["plc_writer_thread"] = self.plc_writer_thread
        return True
    
    def _data_ready(self, data: dict):
        # def _t(label, fn):
            # t = time.perf_counter()
            # fn()
            # ms = (time.perf_counter() - t) * 1000
            # if ms > 1:
                # print(f"  [{label}] {ms:.1f}ms")
        try:
            if self.init_signal:
                self.logger.info("[Main]-[_data_ready]: Getting PLC State")
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
                    float(data.get('P2_TemperatureSetting', 0.0)),
                    float(data.get('P2_TempLimitHIGH', 0.0)),
                    float(data.get('P2_TempLimitLOW', 0.0)),
                    float(data.get('P2_Temp1Offset', 0.0)),
                    float(data.get('P2_Temp2Offset', 0.0)),
                    float(data.get('P2_Temp3Offset', 0.0))
                ],
                [
                    int(data.get('P3_CountTimes', 0)),
                    float(data.get('P3_Oil_Start_Time', 0)/1000),
                    float(data.get('P3_Oil_End_Time', 0)/1000),
                    float(data.get('P3_Air_FillingTime', 0)/1000),
                    float(data.get('P3_Air_HoldingTime', 0)/1000),
                    float(data.get('P3_Air_ReleaseTime', 0)/1000),
                    float(data.get('P3_PressureSetting', 0.00)),
                    float(data.get('P3_TemperatureSetting', 0.0)),
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
                print("Init Value Done")
                
                self._init_button_obj([
                    bool(data.get('START', False)),
                    bool(data.get('STOP', False)),
                    bool(data.get('T0_Start_Heat', False)),
                    bool(data.get('T0_Stop_Heat', False)),
                    bool(data.get('P1_Start_Heat', False)),
                    bool(data.get('P1_Start_Pressure', False)),
                    bool(data.get('P1_Start_Oil', False)),
                    bool(data.get('P1_BitCountTimes', False)),
                    bool(data.get('P2_Start_Heat', False)),
                    bool(data.get('P2_Start_Pressure', False)),
                    bool(data.get('P2_Start_Oil', False)),
                    bool(data.get('P2_BitCountTimes', False)),
                    bool(data.get('P3_Start_Heat', False)),
                    bool(data.get('P3_Start_Pressure', False)),
                    bool(data.get('P3_Start_Oil', False)),
                    bool(data.get('P3_BitCountTimes', False)),
                ])
                print("Init Button Done")
                self.init_signal = False

            now = time.time()
            if now - self._last_history_time >= self.ui.table_write_cycle.value():
                self._last_history_time = now

                groups = []
                if bool(data.get('P1_Start_Heat')) or bool(data.get('P1_Start_Pressure')):
                    groups.append({
                        "group": "Group A",
                        "pressure": float(data.get('P1_Current_PressureHose', 0.0)),
                        "temp": float(data.get('T0_Current_Temp', 0.0)),
                        "front": float(data.get('P1_Current_Temp1', 0.0)),
                        "mid": float(data.get('P1_Current_Temp2', 0.0)),
                        "end": float(data.get('P1_Current_Temp3', 0.0))
                    })
                if bool(data.get('P2_Start_Heat')) or bool(data.get('P2_Start_Pressure')):
                    groups.append({
                        "group": "Group B",
                        "pressure": float(data.get('P2_Current_PressureHose', 0.0)),
                        "temp": float(data.get('T0_Current_Temp', 0.0)),
                        "front": float(data.get('P2_Current_Temp1', 0.0)),
                        "mid": float(data.get('P2_Current_Temp2', 0.0)),
                        "end": float(data.get('P2_Current_Temp3', 0.0))
                    })
                if bool(data.get('P3_Start_Heat')) or bool(data.get('P3_Start_Pressure')):
                    groups.append({
                        "group": "Group C",
                        "pressure": float(data.get('P3_Current_PressureHose', 0.0)),
                        "temp": float(data.get('T0_Current_Temp', 0.0)),
                        "front": float(data.get('P3_Current_Temp1', 0.0)),
                        "mid": float(data.get('P3_Current_Temp2', 0.0)),
                        "end": float(data.get('P3_Current_Temp3', 0.0))
                    })

                if groups:
                    self.add_row_to_list_history(self.ui.code_display.text(), groups)

            # _t("t0_input_heat", lambda: 
            self._t0_input_heat_filter([
                bool(data.get('T0_Start_Heat', False)),
                bool(data.get('T0_Stop_Heat', False))
            ])
            # )

            # _t("input_data", lambda: 
            self._input_data_filter([
                bool(data.get('P1_Start_Heat', False)),
                bool(data.get('P1_Start_Pressure', False)),
                bool(data.get('P1_Start_Oil', False)),
                bool(data.get('P1_BitCountTimes', False)),
                bool(data.get('P2_Start_Heat', False)),
                bool(data.get('P2_Start_Pressure', False)),
                bool(data.get('P2_Start_Oil', False)),
                bool(data.get('P2_BitCountTimes', False)),
                bool(data.get('P3_Start_Heat', False)),
                bool(data.get('P3_Start_Pressure', False)),
                bool(data.get('P3_Start_Oil', False)),
                bool(data.get('P3_BitCountTimes', False)),
            ])
            # )

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

            # _t("t0_data", lambda: 
            self._t0_data_filter([
                float(data.get('T0_TemperatureSetting', 0.0)),
                float(data.get('T0_Current_Temp', 0.0))
            ])
            # )

            # _t("group_a", lambda: 
            self._group_a_data_filter([
                float(data.get('P1_Current_Temp1', 0.0)),
                float(data.get('P1_Current_Temp2', 0.0)),
                float(data.get('P1_Current_Temp3', 0.0)),
                float(data.get('P1_Current_PressureHose', 0.00)),
                float(data.get('P1_Current_Air_FillingTime', 0)/1000),
                float(data.get('P1_Current_Air_HoldingTime', 0)/1000),
                float(data.get('P1_Current_Air_ReleaseTime', 0)/1000),
                float(data.get('P1_Current_Oil_Start_Time', 0)/1000),
                float(data.get('P1_Current_Oil_End_Time', 0)/1000),
                int(data.get('P1_Number_Test_Times', 0)),
                float(data.get('P1_Current_PressureITV', 0.0))
            ])
            # )

            # _t("group_b", lambda: 
            self._group_b_data_filter([
                float(data.get('P2_Current_Temp1', 0.0)),
                float(data.get('P2_Current_Temp2', 0.0)),
                float(data.get('P2_Current_Temp3', 0.0)),
                float(data.get('P2_Current_PressureHose', 0.00)),
                float(data.get('P2_Current_Air_FillingTime', 0)/1000),
                float(data.get('P2_Current_Air_HoldingTime', 0)/1000),
                float(data.get('P2_Current_Air_ReleaseTime', 0)/1000),
                float(data.get('P2_Current_Oil_Start_Time', 0)/1000),
                float(data.get('P2_Current_Oil_End_Time', 0)/1000),
                int(data.get('P2_Number_Test_Times', 0)),
                float(data.get('P2_Current_PressureITV', 0.0))
            ])
            # )

            # _t("group_c", lambda: 
            self._group_c_data_filter([
                float(data.get('P3_Current_Temp1', 0.0)),
                float(data.get('P3_Current_Temp2', 0.0)),
                float(data.get('P3_Current_Temp3', 0.0)),
                float(data.get('P3_Current_PressureHose', 0.00)),
                float(data.get('P3_Current_Air_FillingTime', 0)/1000),
                float(data.get('P3_Current_Air_HoldingTime', 0)/1000),
                float(data.get('P3_Current_Air_ReleaseTime', 0)/1000),
                float(data.get('P3_Current_Oil_Start_Time', 0)/1000),
                float(data.get('P3_Current_Oil_End_Time', 0)/1000),
                int(data.get('P3_Number_Test_Times', 0)),
                float(data.get('P3_Current_PressureITV', 0.0))
            ])
            # )

            # _t("cycle_time", lambda: 
            self._set_cycle_time_unit([
                int(data.get('P1_Number_Test_Times', 0)),
                int(data.get('P2_Number_Test_Times', 0)),
                int(data.get('P3_Number_Test_Times', 0))
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
            # )

            # _t("alarm", lambda: 
            self._alarm_data_filter([
                bool(data.get('Bit_Alarm', False)),
                str(data.get('Alarm_Info', ""))
            ])
            # )
        except Exception as e:
            self.logger.error("[Main]-[_data_ready]:PLC Data Processing Error: %s", e)
            
    def _set_system_data(self):
        self.init_signal = True
        
    def _init_button_obj(self, list_bool):
        self.logger.info("[Main]-[_init_button_obj]: CHECKING PLC BOOL")
        if not list_bool[1]:
            self.ui.sys_state_stacked_wid_39.setCurrentIndex(0)
            if list_bool[0]:
                self.logger.info("[Main]-[_init_button_obj]: START BOOL: 1")
                self.ui.sys_state_stacked_wid_39.setCurrentIndex(1)
                self.ui.start_stop_stacked.setCurrentIndex(1)

        if not list_bool[3]:
            if list_bool[2]:
                self.logger.info("[Main]-[_init_button_obj]: HEAT T0 BOOL: 1")
                self.ui.heat_btn_t0.click() if not self.ui.heat_btn_t0.isChecked() else None

        if list_bool[4]:
            self.logger.info("[Main]-[_init_button_obj]: HEAT A BOOL: 1")
            self.ui.heat_btn_a.click() if not self.ui.heat_btn_a.isChecked() else None
        if list_bool[5]:
            self.logger.info("[Main]-[_init_button_obj]: PRESSURE A BOOL: 1")
            self.ui.vacuum_btn_a.click() if not self.ui.vacuum_btn_a.isChecked() else None
        if list_bool[6]:
            self.logger.info("[Main]-[_init_button_obj]: OIL A BOOL: 1")
            self.ui.refuel_btn_a.click() if not self.ui.refuel_btn_a.isChecked() else None
        if list_bool[7]:
            self.logger.info("[Main]-[_init_button_obj]: CYCLE A BOOL: 1")
            self.ui.set_cycle_a_btn.click() if not self.ui.set_cycle_a_btn.isChecked() else None

        if list_bool[8]:
            self.logger.info("[Main]-[_init_button_obj]: HEAT B BOOL: 1")
            self.ui.heat_btn_b.click() if not self.ui.heat_btn_b.isChecked() else None
        if list_bool[9]:
            self.logger.info("[Main]-[_init_button_obj]: PRESSURE B BOOL: 1")
            self.ui.vacuum_btn_b.click() if not self.ui.vacuum_btn_b.isChecked() else None
        if list_bool[10]:
            self.logger.info("[Main]-[_init_button_obj]: OIL B BOOL: 1")
            self.ui.refuel_btn_b.click() if not self.ui.refuel_btn_b.isChecked() else None
        if list_bool[11]:
            self.logger.info("[Main]-[_init_button_obj]: CYCLE B BOOL: 1")
            self.ui.set_cycle_b_btn.click() if not self.ui.set_cycle_b_btn.isChecked() else None

        if list_bool[12]:
            self.logger.info("[Main]-[_init_button_obj]: HEAT C BOOL: 1")
            self.ui.heat_btn_c.click() if not self.ui.heat_btn_c.isChecked() else None
        if list_bool[13]:
            self.logger.info("[Main]-[_init_button_obj]: PRESSURE C BOOL: 1")
            self.ui.vacuum_btn_c.click() if not self.ui.vacuum_btn_c.isChecked() else None
        if list_bool[14]:
            self.logger.info("[Main]-[_init_button_obj]: OIL C BOOL: 1")
            self.ui.refuel_btn_c.click() if not self.ui.refuel_btn_c.isChecked() else None
        if list_bool[15]:
            self.logger.info("[Main]-[_init_button_obj]: CYCLE C BOOL: 1")
            self.ui.set_cycle_c_btn.click() if not self.ui.set_cycle_c_btn.isChecked() else None

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

    def _read_status_plc(self, connected: bool):
        if connected:
            self.ui.sys_state_stacked_wid_40.setCurrentIndex(0)
        else:
            self.ui.sys_state_stacked_wid_40.setCurrentIndex(1)
        self.plc_read_connection = connected

    def _write_status_plc(self, connected: bool):
        if connected:
            self.ui.sys_state_stacked_wid_42.setCurrentIndex(0)
        else:
            self.ui.sys_state_stacked_wid_42.setCurrentIndex(1)
        self.plc_writer_connection = connected
            
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

    def _input_data_filter(self, list_input_recv):
        # button_map = [
        #     (self.ui.heat_btn_a,    0,  "HEAT A"),
        #     (self.ui.vacuum_btn_a,  1,  "PRESSURE A"),
        #     (self.ui.refuel_btn_a,  2,  "OIL A"),
        #     (self.ui.set_cycle_a_btn, 3, "CYCLE A"),

        #     (self.ui.heat_btn_b,    4,  "HEAT B"),
        #     (self.ui.vacuum_btn_b,  5,  "PRESSURE B"),
        #     (self.ui.refuel_btn_b,  6, "OIL B"),
        #     (self.ui.set_cycle_b_btn, 7, "CYCLE B"),

        #     (self.ui.heat_btn_c,    8, "HEAT C"),
        #     (self.ui.vacuum_btn_c,  9, "PRESSURE C"),
        #     (self.ui.refuel_btn_c,  10, "OIL C"),
        #     (self.ui.set_cycle_c_btn, 11, "CYCLE C"),
        # ]

        # for btn, idx, label in button_map:
        #     new_val = list_input_recv[idx]
        #     if btn.isChecked() != new_val:
        #         self.logger.info(f"[Main]-[_button_changed]: {label} BOOL: {not new_val} -> {new_val}")
        #         btn.blockSignals(True)
        #         btn.setChecked(new_val)
        #         btn.blockSignals(False)
        for obj, value in zip(self.io_group_1_switch_obj, list_input_recv):
            obj.setCurrentIndex(value)

    def _i_o_group_3_filter(self, values):
        for i, (obj, value) in enumerate(zip(self.i_o_group_3_obj, values)):
            v = round(value, 2)
            if v != self._last_i_o_group_3[i]:
                obj.setValue(value)
                self._last_i_o_group_3[i] = v

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
        v = round(self.for_display_temp(list_group_t0_recv[1]), 2)
        if v != self._last_t0_pv:
            self.temp_pv_obj[0].setValue(v)
            self._last_t0_pv = v

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

    def _ct_data_filter(self, list_group_ct_recv):
        v = round(self.for_display_temp(
            (list_group_ct_recv[0]+list_group_ct_recv[1]+list_group_ct_recv[2])/3), 2)
        if v != self._last_ct:
            self.ui.ct_pv.setValue(v)
            self._last_ct = v

    def _alarm_data_filter(self, alarm_recv):
        if alarm_recv[0]:
            self.ui.error_display.setText(alarm_recv[1]) if self.ui.error_display.text() != alarm_recv[1] else None
            # print(alarm_recv[1])

    def simu_heat_btn(self, channel: str, checked: bool):
        simulator = self.thread_dict.get("data_simulator")
        if simulator is None:
            return
        
        if checked:
            if channel == "A":
                sv_obj = self.ui.pressure_sv_a_1
            if channel == "B":
                sv_obj = self.ui.pressure_sv_b_1
            if channel == "C":
                sv_obj = self.ui.pressure_sv_c_1
            temp_sv = max(sv_obj.value(), self.default_temp_room)  # type: ignore
            simulator.set_heat_active(channel, temp_sv)  # type: ignore
        else:
            simulator.set_heat_active(channel, 25.0)

    def simu_pressure_btn(self, channel: str, checked: bool):
        simulator = self.thread_dict.get("data_simulator")
        if simulator is None:
            return

        if checked:
            if channel == "A":
                sv_obj = self.ui.pressure_sv_a_5
            if channel == "B":
                sv_obj = self.ui.pressure_sv_b_5
            if channel == "C":
                sv_obj = self.ui.pressure_sv_c_5
            pressure_itv_sv = sv_obj.value()  # type: ignore
            pressure_sv = sv_obj.value()  # type: ignore
            simulator.set_pressure_active(channel, pressure_sv, pressure_itv_sv)  # type: ignore
        else:
            simulator.set_pressure_active(channel, 0.0, 0.0)
            
    def heating_btn(self, channel: str, checked: bool, btn=None):
        if not self.plc_writer_connection and not self.init_signal:
            ltmessage.error(self, "Error", "PLC Writer not connected!")
            if btn is not None:
                btn.blockSignals(True)   # Chặn signal để tránh gọi đệ quy
                btn.setChecked(False)
                btn.blockSignals(False)
            return
        else:
            if channel == "A":
                if checked:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P1_Start_Heat", True)   # type: ignore
                    self.disable_heat_group(channel, False)
                    self.logger.info("[Main]-[heating_btn]: Group A Heating On!")
                    # ltmessage.information(self, "Heating", "Group A Heating On!")
                else:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P1_Start_Heat", False)  # type: ignore
                    self.disable_heat_group(channel, True)
                    self.logger.info("[Main]-[heating_btn]: Group A Heating Off!")
                return
            if channel == "B":
                if checked:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P2_Start_Heat", True)   # type: ignore
                    self.disable_heat_group(channel, False)
                    self.logger.info("[Main]-[heating_btn]: Group B Heating On!")
                    # ltmessage.information(self, "Heating", "Group B Heating On!")
                else:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P2_Start_Heat", False)  # type: ignore
                    self.disable_heat_group(channel, True)
                    self.logger.info("[Main]-[heating_btn]: Group B Heating Off!")
                return
            if channel == "C":
                if checked:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P3_Start_Heat", True)   # type: ignore
                    self.disable_heat_group(channel, False)
                    self.logger.info("[Main]-[heating_btn]: Group C Heating On!")
                    # ltmessage.information(self, "Heating", "Group C Heating On!")
                else:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P3_Start_Heat", False)  # type: ignore
                    self.disable_heat_group(channel, True)
                    self.logger.info("[Main]-[heating_btn]: Group C Heating Off!")
                return
            if channel == "T0":
                if checked:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("T0_Start_Heat", True)   # type: ignore
                    self.disable_heat_group(channel, False)
                    self.logger.info("[Main]-[heating_btn]: T0 Heating On!")
                    # ltmessage.information(self, "Heating", "T0 Heating On!")
                else:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("T0_Stop_Heat", True)    # type: ignore
                        QTimer.singleShot(100,  lambda: self.plc_writer_worker.write_bool.emit("T0_Start_Heat", False)) # type: ignore
                        QTimer.singleShot(200,  lambda: self.plc_writer_worker.write_bool.emit("T0_Stop_Heat", False))  # type: ignore
                    self.disable_heat_group(channel, True)
                    self.logger.info("[Main]-[heating_btn]: T0 Heating Off!")
                return

    def pumping_btn(self, channel: str, checked: bool, btn=None):
        if not self.plc_writer_connection and not self.init_signal:
            ltmessage.error(self, "Error", "PLC Writer not connected!")
            if btn is not None:
                btn.blockSignals(True)   # Chặn signal để tránh gọi đệ quy
                btn.setChecked(False)
                btn.blockSignals(False)
            return
        else:
            if channel == "A":
                if checked:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P1_Start_Pressure", True)   # type: ignore
                    self.disable_pressure_group(channel, False)
                    self.logger.info("[Main]-[pumping_btn]: Group A Pressure On!")
                    # ltmessage.information(self, "Pumping", "Group A Pressure On!")
                else:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P1_Start_Pressure", False)  # type: ignore
                    self.disable_pressure_group(channel, True)
                    self.logger.info("[Main]-[pumping_btn]: Group A Pressure Off!")

            elif channel == "B":
                if checked:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P2_Start_Pressure", True)   # type: ignore
                    self.disable_pressure_group(channel, False)
                    self.logger.info("[Main]-[pumping_btn]: Group B Pressure On!")
                    # ltmessage.information(self, "Pumping", "Group B Pressure On!")
                else:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P2_Start_Pressure", False)  # type: ignore
                    self.disable_pressure_group(channel, True)
                    self.logger.info("[Main]-[pumping_btn]: Group B Pressure Off!")

            elif channel == "C":
                if checked:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P3_Start_Pressure", True)   # type: ignore
                    self.disable_pressure_group(channel, False)
                    self.logger.info("[Main]-[pumping_btn]: Group C Pressure On!")
                    # ltmessage.information(self, "Pumping", "Group C Pressure On!")
                else:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P3_Start_Pressure", False)  # type: ignore
                    self.disable_pressure_group(channel, True)
                    self.logger.info("[Main]-[pumping_btn]: Group C Pressure Off!")
            return

    def fill_oil_btn(self, channel: str, checked: bool, btn=None):
        if not self.plc_writer_connection and not self.init_signal:
            ltmessage.error(self, "Error", "PLC Writer not connected!")
            if btn is not None:
                btn.blockSignals(True)   # Chặn signal để tránh gọi đệ quy
                btn.setChecked(False)
                btn.blockSignals(False)
            return
        else:
            if channel == "A":
                if checked:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P1_Start_Oil", True)    # type: ignore
                    self.disable_oil_group(channel, False)
                    self.logger.info("[Main]-[fill_oil_btn]: Group A Oil Filling On!")
                    # ltmessage.information(self, "Oil Fill", "Group A Oil Filling On!")
                else:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P1_Start_Oil", False)   # type: ignore
                    self.disable_oil_group(channel, True)
                    self.logger.info("[Main]-[fill_oil_btn]: Group A Oil Filling Off!")

            if channel == "B":
                if checked:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P2_Start_Oil", True)    # type: ignore
                    self.disable_oil_group(channel, False)
                    self.logger.info("[Main]-[fill_oil_btn]: Group B Oil Filling On!")
                    # ltmessage.information(self, "Oil Fill", "Group B Oil Filling On!")
                else:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P2_Start_Oil", False)   # type: ignore
                    self.disable_oil_group(channel, True)
                    self.logger.info("[Main]-[fill_oil_btn]: Group B Oil Filling Off!")

            if channel == "C":
                if checked:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P3_Start_Oil", True)    # type: ignore
                    self.disable_oil_group(channel, False)
                    self.logger.info("[Main]-[fill_oil_btn]: Group C Oil Filling On!")
                    # ltmessage.information(self, "Oil Fill", "Group C Oil Filling On!")
                else:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P3_Start_Oil", False)   # type: ignore
                    self.disable_oil_group(channel, True)
                    self.logger.info("[Main]-[fill_oil_btn]: Group C Oil Filling Off!")

    def cycle_loop_btn(self, channel: str, checked: bool, btn=None):
        if not self.plc_writer_connection and not self.init_signal:
            ltmessage.error(self, "Error", "PLC Writer not connected!")
            if btn is not None:
                btn.blockSignals(True)   # Chặn signal để tránh gọi đệ quy
                btn.setChecked(False)
                btn.blockSignals(False)
            return
        else:
            if channel == "A":
                if checked:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P1_BitCountTimes", True)    # type: ignore
                    self.ui.pressure_sv_a_11.setEnabled(False)
                    self.logger.info("[Main]-[cycle_loop_btn]: Group A Auto Repeat Off!")
                    # ltmessage.information(self, "Set Cycle A", "Group A Auto Repeat!")
                else:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P1_BitCountTimes", False)   # type: ignore
                    self.ui.pressure_sv_a_11.setEnabled(True)
                    self.logger.info("[Main]-[cycle_loop_btn]: Group A Auto Repeat On!")
                return
            if channel == "B":
                if checked:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P2_BitCountTimes", True)    # type: ignore
                    self.ui.pressure_sv_b_11.setEnabled(False)
                    self.logger.info("[Main]-[cycle_loop_btn]: Group B Auto Repeat Off!")
                    # ltmessage.information(self, "Set Cycle B", "Group B Auto Repeat!")
                else:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P2_BitCountTimes", False)   # type: ignore
                    self.ui.pressure_sv_b_11.setEnabled(True)
                    self.logger.info("[Main]-[cycle_loop_btn]: Group B Auto Repeat On!")
                return
            if channel == "C":
                if checked:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P3_BitCountTimes", True)    # type: ignore
                    self.ui.pressure_sv_c_11.setEnabled(False)
                    self.logger.info("[Main]-[cycle_loop_btn]: Group C Auto Repeat Off!")
                    # ltmessage.information(self, "Set Cycle C", "Group C Auto Repeat!")
                else:
                    if not self.init_signal:
                        self.plc_writer_worker.write_bool.emit("P3_BitCountTimes", False)   # type: ignore
                    self.ui.pressure_sv_c_11.setEnabled(True)
                    self.logger.info("[Main]-[cycle_loop_btn]: Group C Auto Repeat On!")
                return

    def start_stop_btn(self, btn=None):
        if not self.plc_writer_connection and not self.init_signal:
            ltmessage.error(self, "Error", "PLC Writer not connected!")
            if btn is not None:
                btn.blockSignals(True)   # Chặn signal để tránh gọi đệ quy
                btn.setChecked(False)
                btn.blockSignals(False)
            return
        if self.ui.start_stop_stacked.currentIndex() == 0:
            self.ui.sys_state_stacked_wid_39.setCurrentIndex(1)
            self.ui.start_stop_stacked.setCurrentIndex(1)
            self.plc_writer_worker.write_bool.emit("START", True)   # type: ignore
            self.logger.info("[Main]-[start_stop_btn]: System On")
            # QTimer.singleShot(250, lambda: self.plc_writer_worker.write_bool.emit("START", False))
            # ltmessage.information(self, "Strike Machine", "System On!")
        elif self.ui.start_stop_stacked.currentIndex() == 1:
            self.ui.sys_state_stacked_wid_39.setCurrentIndex(0)
            self.ui.start_stop_stacked.setCurrentIndex(0)
            self.plc_writer_worker.write_bool.emit("STOP", True)    # type: ignore
            QTimer.singleShot(100, lambda: self.plc_writer_worker.write_bool.emit("START", False))  # type: ignore
            QTimer.singleShot(200, lambda: self.plc_writer_worker.write_bool.emit("STOP", False))   # type: ignore
            QTimer.singleShot(250, self._set_off_oil_btn)
            QTimer.singleShot(250, self._set_off_vacuum_btn)
            QTimer.singleShot(250, self._set_off_heating_btn)
            self.logger.info("[Main]-[start_stop_btn]: System Off")

    def _set_off_oil_btn(self):
        self.ui.refuel_btn_a.blockSignals(True)
        self.ui.refuel_btn_b.blockSignals(True)
        self.ui.refuel_btn_c.blockSignals(True)

        self.ui.refuel_btn_a.setChecked(False)
        self.ui.refuel_btn_b.setChecked(False)
        self.ui.refuel_btn_c.setChecked(False)

        self.ui.refuel_btn_a.blockSignals(True)
        self.ui.refuel_btn_b.blockSignals(True)
        self.ui.refuel_btn_c.blockSignals(True)

    def _set_off_vacuum_btn(self):
        self.ui.vacuum_btn_a.blockSignals(True)
        self.ui.vacuum_btn_b.blockSignals(True)
        self.ui.vacuum_btn_c.blockSignals(True)

        self.ui.vacuum_btn_a.setChecked(False)
        self.ui.vacuum_btn_b.setChecked(False)
        self.ui.vacuum_btn_c.setChecked(False)

        self.ui.vacuum_btn_a.blockSignals(False)
        self.ui.vacuum_btn_b.blockSignals(False)
        self.ui.vacuum_btn_c.blockSignals(False)

    def _set_off_heating_btn(self):
        self.ui.heat_btn_a.blockSignals(True)
        self.ui.heat_btn_b.blockSignals(True)
        self.ui.heat_btn_c.blockSignals(True)
        self.ui.heat_btn_t0.blockSignals(True)

        self.ui.heat_btn_a.setChecked(False)
        self.ui.heat_btn_b.setChecked(False)
        self.ui.heat_btn_c.setChecked(False)
        self.ui.heat_btn_t0.setChecked(False)

        self.ui.heat_btn_a.blockSignals(False)
        self.ui.heat_btn_b.blockSignals(False)
        self.ui.heat_btn_c.blockSignals(False)
        self.ui.heat_btn_t0.blockSignals(False)

    def clear_group_a_btn(self):
        try:
            for i in range(len(self.pressure_a_sv_obj)):
                self.pressure_a_sv_obj[i].blockSignals(False)
                self.pressure_a_sv_obj[i].setValue(0)
                self.pressure_a_sv_obj[i].blockSignals(True)
            for i in range(0):
                self.temp_sv_obj[i].blockSignals(False)
                self.temp_sv_obj[i].setValue(0)
                self.temp_sv_obj[i].blockSignals(True)
            items_a = [
                self.plc_writer_worker.get_item("P1_CountTimes", self.list_for_import_a[0].value()),        # type: ignore
                self.plc_writer_worker.get_item("P1_Oil_Start_Time", self.list_for_import_a[1].value()),    # type: ignore
                self.plc_writer_worker.get_item("P1_Oil_End_Time", self.list_for_import_a[2].value()),      # type: ignore
                self.plc_writer_worker.get_item("P1_Air_FillingTime", self.list_for_import_a[3].value()),   # type: ignore
                self.plc_writer_worker.get_item("P1_Air_HoldingTime", self.list_for_import_a[4].value()),   # type: ignore
                self.plc_writer_worker.get_item("P1_Air_ReleaseTime", self.list_for_import_a[5].value()),   # type: ignore
                self.plc_writer_worker.get_item("P1_PressureSetting", self.list_for_import_a[6].value()),   # type: ignore
                self.plc_writer_worker.get_item("P1_TemperatureSetting", self.list_for_import_a[7].value()) # type: ignore
            ]
            self.plc_writer_worker.write_multi.emit(items_a, "A")   # type: ignore
            if self.plc_writer_connection:
                self.disable_btn("A", False)
        except Exception as e:
            self.logger.error(f"Failed to clear A data: {e}")

    def clear_group_b_btn(self):
        try:
            for i in range(len(self.pressure_b_sv_obj)):
                self.pressure_b_sv_obj[i].blockSignals(False)
                self.pressure_b_sv_obj[i].setValue(0)
                self.pressure_b_sv_obj[i].blockSignals(True)
            for i in range(1):
                self.temp_sv_obj[i].blockSignals(False)
                self.temp_sv_obj[i].setValue(0)
                self.temp_sv_obj[i].blockSignals(True)
            items_b = [
                    self.plc_writer_worker.get_item("P2_CountTimes", self.list_for_import_b[0].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P2_Oil_Start_Time", self.list_for_import_b[1].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P2_Oil_End_Time", self.list_for_import_b[2].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P2_Air_FillingTime", self.list_for_import_b[3].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P2_Air_HoldingTime", self.list_for_import_b[4].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P2_Air_ReleaseTime", self.list_for_import_b[5].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P2_PressureSetting", self.list_for_import_b[6].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P2_TemperatureSetting", self.list_for_import_b[7].value()) # type: ignore
                ]
            self.plc_writer_worker.write_multi.emit(items_b, "B")   # type: ignore
            if self.plc_writer_connection:
                self.disable_btn("B", False)
        except Exception as e:
            self.logger.error(f"Failed to clear B data: {e}")

    def clear_group_c_btn(self):
        try:
            for i in range(len(self.pressure_c_sv_obj)):
                self.pressure_c_sv_obj[i].blockSignals(False)
                self.pressure_c_sv_obj[i].setValue(0)
                self.pressure_c_sv_obj[i].blockSignals(True)
            for i in range(2):
                self.temp_sv_obj[i].blockSignals(False)
                self.temp_sv_obj[i].setValue(0)
                self.temp_sv_obj[i].blockSignals(True)
            items_c = [
                    self.plc_writer_worker.get_item("P3_CountTimes", self.list_for_import_c[0].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P3_Oil_Start_Time", self.list_for_import_c[1].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P3_Oil_End_Time", self.list_for_import_c[2].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P3_Air_FillingTime", self.list_for_import_c[3].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P3_Air_HoldingTime", self.list_for_import_c[4].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P3_Air_ReleaseTime", self.list_for_import_c[5].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P3_PressureSetting", self.list_for_import_c[6].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P3_TemperatureSetting", self.list_for_import_c[7].value()) # type: ignore
                ]
            self.plc_writer_worker.write_multi.emit(items_c, "C")   # type: ignore
            if self.plc_writer_connection:
                self.disable_btn("C", False)
        except Exception as e:
            self.logger.error(f"Failed to clear C data: {e}")

    def clear_data_btn(self):
        reply = ltmessage.question(
            self, "Clear Data", "Set all SV to 0?"
        )
        if reply == ltmessage.Yes:
            try:
                self.ui.code_display.setText("")
                for i in range(len(self.pressure_a_sv_obj)):
                    self.pressure_a_sv_obj[i].blockSignals(False)
                    self.pressure_b_sv_obj[i].blockSignals(False)
                    self.pressure_c_sv_obj[i].blockSignals(False)                    
                    self.pressure_a_sv_obj[i].setValue(0)
                    self.pressure_b_sv_obj[i].setValue(0)
                    self.pressure_c_sv_obj[i].setValue(0)
                    self.pressure_a_sv_obj[i].blockSignals(True)
                    self.pressure_b_sv_obj[i].blockSignals(True)
                    self.pressure_c_sv_obj[i].blockSignals(True)       
                for i in range(len(self.temp_sv_obj)):
                    self.temp_sv_obj[i].blockSignals(False)
                    self.temp_sv_obj[i].setValue(0)
                    self.temp_sv_obj[i].blockSignals(True)
                for i in range(len(self.temp_h_alm_obj)):
                    self.temp_h_alm_obj[i].blockSignals(False)
                    self.temp_h_alm_obj[i].setValue(0)
                    self.temp_h_alm_obj[i].blockSignals(True)

                for i in range(len(self.temp_l_alm_obj)):
                    self.temp_l_alm_obj[i].blockSignals(False)
                    self.temp_l_alm_obj[i].setValue(0)
                    self.temp_l_alm_obj[i].blockSignals(True)
                for i in range(len(self.temp_offset_obj)):
                    self.temp_offset_obj[i].blockSignals(False)
                    self.temp_offset_obj[i].setValue(0)
                    self.temp_offset_obj[i].blockSignals(True)
                items_a = [
                    self.plc_writer_worker.get_item("P1_CountTimes", self.list_for_import_a[0].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P1_Oil_Start_Time", self.list_for_import_a[1].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P1_Oil_End_Time", self.list_for_import_a[2].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P1_Air_FillingTime", self.list_for_import_a[3].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P1_Air_HoldingTime", self.list_for_import_a[4].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P1_Air_ReleaseTime", self.list_for_import_a[5].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P1_PressureSetting", self.list_for_import_a[6].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P1_TemperatureSetting", self.list_for_import_a[7].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P1_TempLimitHIGH", self.list_for_import_a[8].value()), # type: ignore
                    self.plc_writer_worker.get_item("P1_TempLimitLOW", self.list_for_import_a[9].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P1_Temp1Offset", self.list_for_import_a[10].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P1_Temp2Offset", self.list_for_import_a[11].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P1_Temp3Offset", self.list_for_import_a[12].value())   # type: ignore
                ]
                items_b = [
                    self.plc_writer_worker.get_item("P2_CountTimes", self.list_for_import_b[0].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P2_Oil_Start_Time", self.list_for_import_b[1].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P2_Oil_End_Time", self.list_for_import_b[2].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P2_Air_FillingTime", self.list_for_import_b[3].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P2_Air_HoldingTime", self.list_for_import_b[4].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P2_Air_ReleaseTime", self.list_for_import_b[5].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P2_PressureSetting", self.list_for_import_b[6].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P2_TemperatureSetting", self.list_for_import_b[7].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P2_TempLimitHIGH", self.list_for_import_b[8].value()), # type: ignore
                    self.plc_writer_worker.get_item("P2_TempLimitLOW", self.list_for_import_b[9].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P2_Temp1Offset", self.list_for_import_b[10].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P2_Temp2Offset", self.list_for_import_b[11].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P2_Temp3Offset", self.list_for_import_b[12].value())   # type: ignore
                ]
                items_c = [
                    self.plc_writer_worker.get_item("P3_CountTimes", self.list_for_import_c[0].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P3_Oil_Start_Time", self.list_for_import_c[1].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P3_Oil_End_Time", self.list_for_import_c[2].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P3_Air_FillingTime", self.list_for_import_c[3].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P3_Air_HoldingTime", self.list_for_import_c[4].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P3_Air_ReleaseTime", self.list_for_import_c[5].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P3_PressureSetting", self.list_for_import_c[6].value()),   # type: ignore
                    self.plc_writer_worker.get_item("P3_TemperatureSetting", self.list_for_import_c[7].value()),    # type: ignore
                    self.plc_writer_worker.get_item("P3_TempLimitHIGH", self.list_for_import_c[8].value()), # type: ignore
                    self.plc_writer_worker.get_item("P3_TempLimitLOW", self.list_for_import_c[9].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P3_Temp1Offset", self.list_for_import_c[10].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P3_Temp2Offset", self.list_for_import_c[11].value()),  # type: ignore
                    self.plc_writer_worker.get_item("P3_Temp3Offset", self.list_for_import_c[12].value())   # type: ignore
                ]
                items_t0 = [
                    self.plc_writer_worker.get_item("T0_TemperatureSetting", self.list_for_import_t0[0].value()),   # type: ignore
                    self.plc_writer_worker.get_item("T0_TempLimitHIGH", self.list_for_import_t0[1].value()),    # type: ignore
                    self.plc_writer_worker.get_item("T0_TempLimitLOW", self.list_for_import_t0[2].value()), # type: ignore
                    self.plc_writer_worker.get_item("T0_TempOffset", self.list_for_import_t0[3].value())    # type: ignore
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
                ltmessage.error(self, "Error", f"Failed to clear data: {e}")

    def reset_cycle_a_btn(self, channel):
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

    def new_data_btn(self):
        stk_mch_file = Path(self.stk_mch_folder)/ "Setting File" 
        # print("Default path for data file:", stk_mch_file)s
        file_str, _ = QFileDialog.getOpenFileName(
            self,
            "Select Group Data File",
            str(stk_mch_file),
            "Excel Files (*.xlsx *.xls)"
        )
        if not file_str:  # User cancel
            return
        path = Path(file_str)

        df = pd.read_excel(path, sheet_name='Sheet1', header=None)
        self.ui.code_display.setText(str(df.iloc[0][0]).strip() if pd.notna(df.iloc[0][0]) else "")
        for i in range(2, len(df)): # Bắt đầu từ hàng 3
            column = df.iloc[i]
            name_raw = str(column[0]).strip() if pd.notna(column[0]) else ""
            if name_raw == "" or name_raw.lower() == "nan":
                break
            # Cột B: Group A
            try:
                value_a_raw = str(column[1]).strip()
                value_a = float(value_a_raw)
            except:
                value_a = 0
            self.list_for_import_a[i-2].blockSignals(True)
            self.list_for_import_a[i-2].setValue(value_a)   # type: ignore
            
            # Cột C: Group B
            try:
                value_b_raw = str(column[2]).strip()
                value_b = float(value_b_raw)
            except:
                value_b = 0
            self.list_for_import_b[i-2].blockSignals(True)
            self.list_for_import_b[i-2].setValue(value_b)   # type: ignore
            
            # Cột D: Group C
            try:
                value_c_raw = str(column[3]).strip()
                value_c = float(value_c_raw)
            except:
                value_c = 0
            self.list_for_import_c[i-2].blockSignals(True)
            self.list_for_import_c[i-2].setValue(value_c)   # type: ignore

            if i >= 9  and i <=12:
                # Cột E: Group T0
                try:
                    value_t0_raw = str(column[4]).strip()
                    value_t0 = float(value_t0_raw)
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
            self.plc_writer_worker.get_item("P1_CountTimes", self.list_for_import_a[0].value()),    # type: ignore
            self.plc_writer_worker.get_item("P1_Oil_Start_Time", (self.cal_sec_to_msec(self.list_for_import_a[1].value()))), # type: ignore
            self.plc_writer_worker.get_item("P1_Oil_End_Time", (self.cal_sec_to_msec(self.list_for_import_a[2].value()))),   # type: ignore
            self.plc_writer_worker.get_item("P1_Air_FillingTime", (self.cal_sec_to_msec(self.list_for_import_a[3].value()))),    # type: ignore
            self.plc_writer_worker.get_item("P1_Air_HoldingTime", (self.cal_sec_to_msec(self.list_for_import_a[4].value()))),    # type: ignore
            self.plc_writer_worker.get_item("P1_Air_ReleaseTime", (self.cal_sec_to_msec(self.list_for_import_a[5].value()))),    # type: ignore
            self.plc_writer_worker.get_item("P1_PressureSetting", self.list_for_import_a[6].value()),   # type: ignore
            self.plc_writer_worker.get_item("P1_TemperatureSetting", self.list_for_import_a[7].value()),    # type: ignore
            self.plc_writer_worker.get_item("P1_TempLimitHIGH", self.list_for_import_a[8].value()), # type: ignore
            self.plc_writer_worker.get_item("P1_TempLimitLOW", self.list_for_import_a[9].value()),  # type: ignore
            self.plc_writer_worker.get_item("P1_Temp1Offset", self.list_for_import_a[10].value()),  # type: ignore
            self.plc_writer_worker.get_item("P1_Temp2Offset", self.list_for_import_a[11].value()),  # type: ignore
            self.plc_writer_worker.get_item("P1_Temp3Offset", self.list_for_import_a[12].value())   # type: ignore
        ]
        items_b = [
            self.plc_writer_worker.get_item("P2_CountTimes", self.list_for_import_b[0].value()),    # type: ignore
            self.plc_writer_worker.get_item("P2_Oil_Start_Time", (self.cal_sec_to_msec(self.list_for_import_b[1].value()))), # type: ignore
            self.plc_writer_worker.get_item("P2_Oil_End_Time", (self.cal_sec_to_msec(self.list_for_import_b[2].value()))),   # type: ignore
            self.plc_writer_worker.get_item("P2_Air_FillingTime", (self.cal_sec_to_msec(self.list_for_import_b[3].value()))),    # type: ignore
            self.plc_writer_worker.get_item("P2_Air_HoldingTime", (self.cal_sec_to_msec(self.list_for_import_b[4].value()))),    # type: ignore
            self.plc_writer_worker.get_item("P2_Air_ReleaseTime", (self.cal_sec_to_msec(self.list_for_import_b[5].value()))),    # type: ignore
            self.plc_writer_worker.get_item("P2_PressureSetting", self.list_for_import_b[6].value()),   # type: ignore
            self.plc_writer_worker.get_item("P2_TemperatureSetting", self.list_for_import_b[7].value()),    # type: ignore
            self.plc_writer_worker.get_item("P2_TempLimitHIGH", self.list_for_import_b[8].value()), # type: ignore
            self.plc_writer_worker.get_item("P2_TempLimitLOW", self.list_for_import_b[9].value()),  # type: ignore
            self.plc_writer_worker.get_item("P2_Temp1Offset", self.list_for_import_b[10].value()),  # type: ignore
            self.plc_writer_worker.get_item("P2_Temp2Offset", self.list_for_import_b[11].value()),  # type: ignore
            self.plc_writer_worker.get_item("P2_Temp3Offset", self.list_for_import_b[12].value())   # type: ignore
        ]
        items_c = [
            self.plc_writer_worker.get_item("P3_CountTimes", self.list_for_import_c[0].value()),                                # type: ignore
            self.plc_writer_worker.get_item("P3_Oil_Start_Time", (self.cal_sec_to_msec(self.list_for_import_c[1].value()))),    # type: ignore
            self.plc_writer_worker.get_item("P3_Oil_End_Time", (self.cal_sec_to_msec(self.list_for_import_c[2].value()))),      # type: ignore
            self.plc_writer_worker.get_item("P3_Air_FillingTime", (self.cal_sec_to_msec(self.list_for_import_c[3].value()))),   # type: ignore
            self.plc_writer_worker.get_item("P3_Air_HoldingTime", (self.cal_sec_to_msec(self.list_for_import_c[4].value()))),   # type: ignore
            self.plc_writer_worker.get_item("P3_Air_ReleaseTime", (self.cal_sec_to_msec(self.list_for_import_c[5].value()))),   # type: ignore
            self.plc_writer_worker.get_item("P3_PressureSetting", self.list_for_import_c[6].value()),   # type: ignore
            self.plc_writer_worker.get_item("P3_TemperatureSetting", self.list_for_import_c[7].value()),    # type: ignore
            self.plc_writer_worker.get_item("P3_TempLimitHIGH", self.list_for_import_c[8].value()), # type: ignore
            self.plc_writer_worker.get_item("P3_TempLimitLOW", self.list_for_import_c[9].value()),  # type: ignore
            self.plc_writer_worker.get_item("P3_Temp1Offset", self.list_for_import_c[10].value()),  # type: ignore
            self.plc_writer_worker.get_item("P3_Temp2Offset", self.list_for_import_c[11].value()),  # type: ignore
            self.plc_writer_worker.get_item("P3_Temp3Offset", self.list_for_import_c[12].value())   # type: ignore
        ]
        items_t0 = [
            self.plc_writer_worker.get_item("T0_TemperatureSetting", self.list_for_import_t0[0].value()),   # type: ignore
            self.plc_writer_worker.get_item("T0_TempLimitHIGH", self.list_for_import_t0[1].value()),    # type: ignore
            self.plc_writer_worker.get_item("T0_TempLimitLOW", self.list_for_import_t0[2].value()), # type: ignore
            self.plc_writer_worker.get_item("T0_TempOffset", self.list_for_import_t0[3].value())    # type: ignore
        ]
        self.plc_writer_worker.write_multi.emit(items_a, "A")   # type: ignore
        self.plc_writer_worker.write_multi.emit(items_b, "B")   # type: ignore
        self.plc_writer_worker.write_multi.emit(items_c, "C")   # type: ignore
        self.plc_writer_worker.write_multi.emit(items_t0, "T0") # type: ignore
        
        for i in range(len(self.list_for_import_a)):
            self.list_for_import_a[i].blockSignals(False)
            self.list_for_import_b[i].blockSignals(False)
            self.list_for_import_c[i].blockSignals(False)
        for i in range(len(self.list_for_import_t0)):
            self.list_for_import_t0[i].blockSignals(False)
        
        self.ui.at_sv.blockSignals(False)
        self.ui.bt_sv.blockSignals(False)
        self.ui.ct_sv.blockSignals(False)
        if self.plc_writer_connection:
            if not self.ui.set_cycle_a_btn.isChecked():
                self.ui.set_cycle_a_btn.click()
            if not self.ui.set_cycle_b_btn.isChecked():
                self.ui.set_cycle_b_btn.click()
            if not self.ui.set_cycle_c_btn.isChecked():
                self.ui.set_cycle_c_btn.click()
            self.disable_btn("A", False)
            self.disable_btn("B", False)
            self.disable_btn("C", False)
            self.disable_btn("T0", False)

    def set_language_en(self):
        self._app.removeTranslator(self._translator)    # type: ignore
        self._current_lang = "en"

    def set_language_cn(self):
        self._app.removeTranslator(self._translator)    # type: ignore
        self._translator.load(resource_path("tech_link_theme_cn.qm"))
        self._app.installTranslator(self._translator)   # type: ignore
        self._current_lang = "cn"
        
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

            elif self._current_lang == "en":
                self.ui.plc_ip_address_edit.setPlaceholderText("Enter IP Address: 172.16.100.***")
                self.ui.db_file_path_edit.setPlaceholderText("Enter Path Folder")
                
                charts[0].btn_setting.setText("Oven")
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

    def _set_chart_unit(self):
        if self._current_unit == 0:
            self.chart_temp.set_temp_label("Temperature (°C)", unit="°C") if self._current_lang == "en" else self.chart_temp.set_temp_label("温度 (°C)", unit="°C")
            self.chart_pressure_a.set_temp_label("Temperature (°C)", unit="°C") if self._current_lang == "en" else self.chart_pressure_a.set_temp_label("温度 (°C)", unit="°C")
            self.chart_pressure_b.set_temp_label("Temperature (°C)", unit="°C") if self._current_lang == "en" else self.chart_pressure_b.set_temp_label("温度 (°C)", unit="°C")
            self.chart_pressure_c.set_temp_label("Temperature (°C)", unit="°C") if self._current_lang == "en" else self.chart_pressure_c.set_temp_label("温度 (°C)", unit="°C")

        elif self._current_unit == 1:
            self.chart_temp.set_temp_label("Temperature (°F)", unit="°F") if self._current_lang == "en" else self.chart_temp.set_temp_label("温度 (°F)", unit="°F")
            self.chart_pressure_a.set_temp_label("Temperature (°F)", unit="°F") if self._current_lang == "en" else self.chart_pressure_a.set_temp_label("温度 (°F)", unit="°F")
            self.chart_pressure_b.set_temp_label("Temperature (°F)", unit="°F") if self._current_lang == "en" else self.chart_pressure_b.set_temp_label("温度 (°F)", unit="°F")
            self.chart_pressure_c.set_temp_label("Temperature (°F)", unit="°F") if self._current_lang == "en" else self.chart_pressure_c.set_temp_label("温度 (°F)", unit="°F")
    
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

    def update_chart_pressure_a(self):
        group_a_values = [self.ui.pressure_sv_a_1.value(),
                        self.ui.pressure_pv_a_2.value(),
                        self.ui.pressure_pv_a_3.value(),
                        self.ui.pressure_pv_a_4.value()]
        group_a_press_values = [self.ui.pressure_sv_a_5.value(),
                                self.ui.pressure_pv_a_5.value()]
        self.chart_pressure_a.append_data(group_a_values, group_a_press_values)

    def update_chart_pressure_b(self):
        group_b_values = [self.ui.pressure_sv_b_1.value(),
                        self.ui.pressure_pv_b_2.value(),
                        self.ui.pressure_pv_b_3.value(),
                        self.ui.pressure_pv_b_4.value()]
        group_b_press_values = [self.ui.pressure_sv_b_5.value(),
                                self.ui.pressure_pv_b_5.value()]
        self.chart_pressure_b.append_data(group_b_values, group_b_press_values)

    def update_chart_pressure_c(self):
        group_c_values = [self.ui.pressure_sv_c_1.value(),
                        self.ui.pressure_pv_c_2.value(),
                        self.ui.pressure_pv_c_3.value(),
                        self.ui.pressure_pv_c_4.value()]
        group_c_press_values = [self.ui.pressure_sv_c_5.value(),
                                self.ui.pressure_pv_c_5.value()]
        self.chart_pressure_c.append_data(group_c_values, group_c_press_values)

    def update_clock(self):
        self.ui.date_displ.setDateTime(QDateTime.currentDateTime())

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
            for i in range(1, 5):
                self.pressure_a_sv_obj[i].setEnabled(status)
            return

        elif channel == "B":
            for i in range(1, 5):
                self.pressure_b_sv_obj[i].setEnabled(status)
            return

        elif channel == "C":
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

        elif channel == "T0":
            for i in [0]:
                self.temp_sv_obj[i].setEnabled(status)
                self.temp_h_alm_obj[i].setEnabled(status)
                self.temp_l_alm_obj[i].setEnabled(status)
                self.temp_offset_obj[i].setEnabled(status)
            return

    def disable_btn(self, channel, status):
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
        
        elif channel == "T0":
            self.ui.heat_btn_t0.setEnabled(status)

    def export_all_tables_to_excel_btn(self):
        current_date = datetime.now().strftime("%d-%m-%Y")  # dùng - thay vì /
        name = self.ui.search_data.text().strip() or "History"
        default_filename_done = f"{name} - Group {self.ui.select_group_name.currentText()} {current_date}"
        list_history_folder = Path(self.stk_mch_folder) / "Excel"
        list_history_folder.mkdir(parents=True, exist_ok=True)  # tạo folder nếu chưa có
        filename_done = list_history_folder / f"{default_filename_done}.xlsx"
        if self.ui.stacked_list_history_page.currentIndex() == 0:
            reply = ltmessage.question(
                self, "Export All File", "This might take a while. Do you want to continue?"
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
        self.ui.error_display.setText(" Exporting... Please wait.")
        self._export_thread = QThread()
        if self.ui.stacked_list_history_page.currentIndex() == 0:
            self._export_worker = ExportWorker(self.history_db_path, file_path) # type: ignore
        elif self.ui.stacked_list_history_page.currentIndex() == 1:
            self._export_worker = ExportWorker(
                db_path=self.history_db_path,   # type: ignore
                file_path=file_path,
                name=self.ui.search_data.text(),
                group=self.ui.select_group_name.currentText(),
                start_date=self.ui.search_data_start_edit.dateTime().toString("yyyy/MM/dd HH:mm"),
                end_date=self.ui.search_data_end_edit.dateTime().toString("yyyy/MM/dd HH:mm"),
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
        self.ui.error_display.setText("")
        if error:
            ltmessage.error(self, "Error", f"Export failed:\n{error}")
        else:
            reply = ltmessage.custom(
                self, "Export Success", f"Go to Save Folder?",
                msg_type="success",      # ← icon success
                buttons=["Yes", "No"]
            )
            if reply == ltmessage.Yes:
                folder = str(Path(file_path.split("|")[0]).parent)
                os.startfile(folder)
            else:
                pass
        self.ui.export_all_tables_to_excel_btn.setEnabled(True)

    def resizeEvent(self, event): # type: ignore
        super().resizeEvent(event)
        self._resize_table_columns(self.ui.list_history)
        self._resize_table_columns(self.ui.list_history_2)
        if hasattr(self, '_maximized_chart_idx') and self._maximized_chart_idx == -1:
            QTimer.singleShot(50, self._save_grid_rects)
            
    def closeEvent(self, event):
        reply = ltmessage.question(
            self, "Exit Confirmation", "Are you sure you want to exit?"
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
        for timer in getattr(self, 'all_timer', []):
            if timer.isActive():
                timer.stop()
            timer.deleteLater()
        self.all_timer.clear()
        self.hide()

        if self.plc_read_worker:
            self.plc_read_worker.stop()
        if self.plc_writer_worker:
            self.plc_writer_worker.stop()

        if self.plc_read_thread:
            self.plc_read_thread.wait()
        if self.plc_writer_thread:
            self.plc_writer_thread.wait()
        
        self.stop_simulate_threads() if SIMULATE else None

    def stop_simulate_threads(self):
        try:
            simulate_thread = self.thread_dict.get("data_simulator")

            if simulate_thread is not None:
                if hasattr(simulate_thread, "stop"):
                    simulate_thread.stop()

                simulate_thread.quit()

                if not simulate_thread.wait(3000):
                    simulate_thread.terminate()
                    simulate_thread.wait()

                del self.thread_dict["data_simulator"]

        except Exception as e:
            self.logger.error(f"Stop thread error: {e}")
