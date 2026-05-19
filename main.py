# pyside6-uic tech_link_theme.ui -o tech_link_theme.py
# pyside6-rcc Icon.qrc -o Icon_rc.py
# pyside6-rcc icons.qrc -o icons_rc.py

# pyinstaller --onefile --name="Packing Demo" --icon=icons\Download_Icons\robotic-arm.ico --add-binary "lib\snap7.dll;." --add-data "gifs;gifs" main.py
# pyinstaller --onefile --name="Testing App" --add-binary "lib\snap7.dll;." main.py

import sys
import os
import time 
import pandas as pd
import logging
import logging.handlers
import atexit
from PySide6.QtCore import (Qt, QTimer, QObject,
                            QSettings, QDateTime, 
                            QEvent, QSharedMemory,
                            QSystemSemaphore, QThread, Slot)
from PySide6.QtGui import (QFont, QMovie)
from PySide6.QtWidgets import (QVBoxLayout, QHeaderView, QAbstractSpinBox, 
                               QLabel,QMainWindow, QApplication, QLineEdit,
                                QFileDialog, QDialog, QTableWidget, QTableWidgetItem
)

from typing import List, Optional, Tuple, Dict, Any
from pathlib import Path
from datetime import datetime 
from openpyxl.styles import Font
from tech_link_theme import Ui_MainWindow
from Custom_Widgets import * #type: ignore
# from Custom_Chart_Widgets import CustomChartWidget
from matplot_chart_widget import CustomChartWidget
from message_box import LightThemeMessageBox as ltmessage
from password_dialog import *
from marquee_label import MarqueeLabel
from System_Data import syss
from Data_Simulator import DataSimulator
from query_plc_thread_V2 import PLCRead
from write_plc_thread_V2 import PLCWrite
from qtimer_thread import Worker

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"
os.environ["QT_FONT_DPI"] = "96"

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

class StrikeMachine(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = QSettings("TechLink", "STKMApp")
        self._find_stk_mch_folder()
        self._init_logger()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui) #type: ignore
        self._init_app_data()
        self._init_db_layout_and_size()
        self._init_timer()
        self._init_group_object()
        self._init_list_unit()
        self._create_charts()
        self._simulate_data()
        self._setup_table()
        self._paint_pv_obj("#E53935")
        self._paint_sv_obj("#43A047")
        self._setup_btn_signals()
        # self._setup_plc_threads()
        self.current_unit = 0
        self.ui.home_page_btn.click()

    def _find_stk_mch_folder(self):
        default_path = str(self.settings.value("stk_mch_folder", "C:\\", type=str))
        stk_mch_folder = Path(default_path) / "SM_PRD"

        if not stk_mch_folder.is_dir():
            response = ltmessage.question(self, "Warning", "Data Folder not found! Create a new one?")

            if response == ltmessage.Yes:
                # Cho người dùng chọn nơi tạo thư mục SM_PRD
                parent_folder = QFileDialog.getExistingDirectory(
                    self,
                    "Select a Path for SM_PRD folder",
                    str(Path(default_path)),
                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks #type: ignore
                )
                if parent_folder:
                    stk_mch_folder = Path(parent_folder) / "SM_PRD"
                    stk_mch_folder.mkdir(parents=True, exist_ok=True)
                    # Lưu đường dẫn vào QSettings
                    self.settings.setValue("stk_mch_folder", str(stk_mch_folder.parent))
                else:
                    return None
            else:
                return None
    
        if not stk_mch_folder.exists():
            stk_mch_folder.mkdir(parents=True, exist_ok=True)
    
        # Lưu đường dẫn vào thuộc tính của lớp
        self.stk_mch_folder = stk_mch_folder

    def _init_db_layout_and_size(self):
        stk_mch_file = Path(self.stk_mch_folder) / "DB_address"
        file_name = "DB Memory Address Default.xlsx"
        path = os.path.join(stk_mch_file, file_name)
        if not os.path.isfile(path):
            file_str, _ = QFileDialog.getOpenFileName(
                self,
                "Select DB Address File",
                str(stk_mch_file),
                "Excel Files (*.xlsx *.xls)"
            )
            if not file_str:  # User cancel
                return
            path = Path(file_str)

        df = pd.read_excel(path, sheet_name='Sheet1', header=None)

        db_layout: List[Tuple[str, str, int, Any]] = []
        max_byte = 0
        
        for i in range(4, len(df)):
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
                byte_addr = int(float(addr_str.split('.')[0])) if '.' in addr_str else int(float(addr_str))
            except:
                byte_addr = 0
            
            # Cập nhật max byte
            if byte_addr > max_byte:
                max_byte = byte_addr
            
            # Xử lý Bit cho BOOL
            bit: Any = None
            if data_type == "BOOL":
                addr_str = str(row[4]).strip()
                if '.' in addr_str:
                    try:
                        bit = int(addr_str.split('.')[1])  # lấy phần sau dấu .
                    except:
                        bit = 0
                else:
                    bit = 0 
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
        self._gui_update_connection_group(stk_mch_file)
        # print(f"Generated DB Layout: \n{self.db_dict}")

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
                self.ui.plc_io_btn    : self.i_o_page_btn
            }
            if obj in double_click_actions:
                double_click_actions[obj]()
        return super().eventFilter(obj, event)

    def _show_loading_dialog(self):
        if hasattr(self, '_loading_dialog') and self._loading_dialog:
            self._loading_dialog.close()
            self._loading_dialog = None
        dialog = QDialog(self)
        dialog.setAttribute(Qt.WA_TranslucentBackground, True) # type: ignore
        dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog) # type: ignore
        vbox = QVBoxLayout()
        lbl = QLabel(self)
        lbl.setStyleSheet("background: transparent;")
        gif_path = resource_path('gifs/Loading.gif')
        print(f"[ProductionApp]-[_show_loading_dialog]: Trying to load gif from: {gif_path}")
        print(f"[ProductionApp]-[_show_loading_dialog]: File exists: {os.path.exists(gif_path)}")

        self.moviee = QMovie(gif_path)
        if not self.moviee.isValid():
            print(f"[ProductionApp]-[_show_loading_dialog]: Failed to load Loading.gif from {gif_path}")
            dialog.close()
            self._loading_dialog = None
            return
        lbl.setMovie(self.moviee)
        self.moviee.start()
        vbox.addWidget(lbl)
        dialog.setLayout(vbox)
        dialog.show()
        QApplication.processEvents()
        self._loading_dialog = dialog

    def _close_loading_dialog(self):
        if hasattr(self, '_loading_dialog'):
            self._loading_dialog.close()# type: ignore
            del self._loading_dialog
        if not self._ui_shown:
            self._init_scene_before_show()
            self.center_window()
            self.show()  # Show UI chính ở đây
            # self._check_user()
            self._ui_shown = True
            QApplication.instance().installEventFilter(self) # type: ignore

    def _init_app_data(self):
        self.plc_clients = [
            syss.plc_client_1, 
            syss.plc_client_2, 
            syss.plc_client_3, 
            syss.plc_client_4, 
            syss.plc_client_5, 
            syss.plc_client_6
        ]
        self._lastpos = None

        self.db_dict: Optional[dict] = None

        self.user = False
        self._dialog_open = False
        self.worker_dict = {}
        self.thread_dict = {}

        self.plc_read_worker = None
        self.plc_read_connection = False
        self.plc_read_thread = None
        self.plc_writer_worker = None
        self.plc_writer_connection = False
        self.plc_writer_thread = None

        # Group A
        self.group_a_pv_dict = {
            "Front PV Temp A": 0.0,
            "Middle PV Temp A": 0.0,
            "Back PV Temp A": 0.0,
            "Pressure PV A": 0.0,
            "Pressure ITV A": 0.0,
            "Filling Time PV A": 0,
            "G.Holding Time PV A": 0,
            "Bleeding Time PV A": 0,
            "Refueling Start PV A": 0,
            "Refueling End PV A": 0,
            "Number Test Times A": 0,
        }
        self.group_a_sv_dict = {
            "Refueling Start SV A": 10.0,
            "Refueling End SV A": 20.0,
            "Filling Time SV A": 5.0,
            "G.Holding Time SV A": 3.0,
            "Bleeding Time SV A": 12.0,
            "Pressure SV A": 45.0,
            "Front High Alm A": 240.0,
            "Front Low Alm A": 200.0,
            "Front SV Temp A": 0.0,
            "Front Offset A": 0.0,
            "Middle High Alm A": 240.0,
            "Middle Low Alm A": 200.0,
            "Middle SV Temp A": 0.0,
            "Middle Offset A": 0.0,
            "Back High Alm A": 243.0,
            "Back Low Alm A": 203.0,
            "Back SV Temp A": 0.0,
            "Back Offset A": 0.0
        }

        # Group B
        self.group_b_pv_dict = {
            "Front PV Temp B": 0.0,
            "Middle PV Temp B": 0.0,
            "Back PV Temp B": 0.0,
            "Pressure PV B": 0.0,
            "Pressure ITV B": 0.0,
            "Filling Time PV B": 0,
            "G.Holding Time PV B": 0,
            "Bleeding Time PV B": 0,
            "Refueling Start PV B": 0,
            "Refueling End PV B": 0,
            "Number Test Times B": 0
        }
        self.group_b_sv_dict = {
            "Refueling Start B": 0.0,
            "Refueling End B": 0.0,
            "Filling Time B": 0.0,
            "G.Holding Time B": 0.0,
            "Bleeding Time B": 0.0,
            "Pressure SV B": 0.0,
            "Front High Alm B": 0.0,
            "Front Low Alm B": 0.0,
            "Front SV Temp B": 0.0,
            "Front Offset B": 0.0,
            "Middle High Alm B": 0.0,
            "Middle Low Alm B": 0.0,
            "Middle SV Temp B": 0.0,
            "Middle Offset B": 0.0,
            "Back High Alm B": 0.0,
            "Back Low Alm B": 0.0,
            "Back SV Temp B": 0.0,
            "Back Offset B": 0.0
        }

        # Group C
        self.group_c_pv_dict = {
            "Front PV Temp C": 0.0,
            "Middle PV Temp C": 0.0,
            "Back PV Temp C": 0.0,
            "Pressure PV C": 0.0,
            "Pressure ITV C": 0.0,
            "Filling Time PV C": 0,
            "G.Holding Time PV C": 0,
            "Bleeding Time PV C": 0,
            "Refueling Start PV C": 0,
            "Refueling End PV C": 0,
            "Number Test Times C": 0,
        }
        self.group_c_sv_dict = {
            "Refueling Start C": 0.0,
            "Refueling End C": 0.0,
            "Filling Time C": 0.0,
            "G.Holding Time C": 0.0,
            "Bleeding Time C": 0.0,
            "Pressure SV C": 0.0,
            "Front High Alm C": 0.0,
            "Front Low Alm C": 0.0,
            "Front SV Temp C": 0.0,
            "Front Offset C": 0.0,
            "Middle High Alm C": 0.0,
            "Middle Low Alm C": 0.0,
            "Middle SV Temp C": 0.0,
            "Middle Offset C": 0.0,
            "Back High Alm C": 0.0,
            "Back Low Alm C": 0.0,
            "Back SV Temp C": 0.0,
            "Back Offset C": 0.0
        }

        self.default_temp_room = 25.0
        
    def _init_timer(self):
        self.all_timer = []

        self.timer_alarm = QTimer()
        self.all_timer.append(self.timer_alarm)

        self.timer_stacked_pressure_page = QTimer()
        self.all_timer.append(self.timer_stacked_pressure_page)
        
        # self.timeout_duration = 600000
        # self.inactivity_timer = QTimer(self)
        # self.inactivity_timer.timeout.connect(self.handle_timeout)
        # self.all_timer.append(self.inactivity_timer)

        self.date_time_timer = QTimer(self)
        self.all_timer.append(self.date_time_timer)
        self.date_time_timer.timeout.connect(self.update_clock)
        self.date_time_timer.start(1000)
        self.update_clock()

    def _init_group_object(self):
        # self.pressure_state_obj = []
        # for i in range(10):
        #     obj = getattr(self.ui, f"pressure_sv_a_{i}")
        #     self.pressure_state_obj.append(obj)
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

        # self.all_widgets = (
        #     self.pressure_state_obj +
        #     self.inlet_temp_obj     +
        #     self.front_temp_obj     +
        #     self.middle_temp_obj    +
        #     self.end_temp_obj
        # )
        # assert len(self.all_widgets) == 22, f"Widget count mismatch: {len(self.all_widgets)}"

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

        self.io_group_1_switch_obj = tuple(
            getattr(self.ui, f"i_o_group_1_switch_{i}") for i in range(1, 9)
        )

    # def _create_charts(self):
    #     font = QFont("Segoe UI", 17)
    #     font.setWeight(QFont.Weight.Bold)

    #     # Chart Nhiệt độ (Oven)
    #     self.chart_temp = CustomChartWidget(
    #         title="Oven",
    #         num_temp=1,
    #         num_pressure=2,
    #         temp_label="Temperature (°C)",
    #         pressure_label="Pressure (bar)",
    #         temp_range=(0, 200),
    #         pressure_range=(0, 10),
    #         max_seconds=60,
    #         chart_font=font
    #     )

    #     # Chart Group A
    #     self.chart_pressure_a = CustomChartWidget(
    #         title="Group A",
    #         num_temp=3,
    #         num_pressure=2,
    #         temp_label="Temperature (°C)",
    #         pressure_label="Pressure (bar)",
    #         temp_range=(0, 200),
    #         pressure_range=(0, 10),
    #         max_seconds=60,
    #         chart_font=font
    #     )

    #     # Chart Group B
    #     self.chart_pressure_b = CustomChartWidget(
    #         title="Group B",
    #         num_temp=3,
    #         num_pressure=2,
    #         temp_label="Temperature (°C)",
    #         pressure_label="Pressure (bar)",
    #         temp_range=(0, 200),
    #         pressure_range=(0, 10),
    #         max_seconds=60,
    #         chart_font=font
    #     )

    #     # Chart Group C
    #     self.chart_pressure_c = CustomChartWidget(
    #         title="Group C",
    #         num_temp=3,
    #         num_pressure=2,
    #         temp_label="Temperature (°C)",
    #         pressure_label="Pressure (bar)",
    #         temp_range=(0, 200),
    #         pressure_range=(0, 10),
    #         max_seconds=60,
    #         chart_font=font
    #     )

    #     # Kết nối nút tiêu đề
    #     self.chart_temp.btn_setting.clicked.connect(self.temperature_page_btn)
    #     self.chart_pressure_a.btn_setting.clicked.connect(self.ui.home_page_btn.click)
    #     self.chart_pressure_b.btn_setting.clicked.connect(self.ui.home_page_btn.click)
    #     self.chart_pressure_c.btn_setting.clicked.connect(self.ui.home_page_btn.click)

    #     # Thêm vào layout
    #     self.ui.card_temperature.addWidget(self.chart_temp)
    #     self.ui.card_pressure_1.addWidget(self.chart_pressure_a)
    #     self.ui.card_pressure_2.addWidget(self.chart_pressure_b)
    #     self.ui.card_pressure_3.addWidget(self.chart_pressure_c)

    def _create_charts(self):
        font = QFont("Segoe UI", 17)
        font.setWeight(QFont.Weight.Bold)

        # Chart Nhiệt độ (Oven)
        self.chart_temp = CustomChartWidget(
            title="Oven",
            num_temp=2,
            num_pressure=1,
            temp_label="Temperature (°C)",
            pressure_label="Pressure (bar)",
            max_seconds=60
        )

        self.chart_pressure_a = CustomChartWidget(          # ← gán lại
                title="Group A",
                num_temp=4,
                num_pressure=1,
                temp_label="Temperature (°C)",
                pressure_label="Pressure (bar)",
                max_seconds=60
            )
        self.chart_pressure_b = CustomChartWidget(          # ← gán lại
                title="Group B",
                num_temp=4,
                num_pressure=1,
                temp_label="Temperature (°C)",
                pressure_label="Pressure (bar)",
                max_seconds=60
            )
        self.chart_pressure_c = CustomChartWidget(
                title="Group C",
                num_temp=4,
                num_pressure=1,
                temp_label="Temperature (°C)",
                pressure_label="Pressure (bar)",
                max_seconds=60
            )
        # Kết nối nút
        # self.chart_temp.btn_setting.clicked.connect(self.temperature_page_btn)
        # self.chart_pressure_a.btn_setting.clicked.connect(self.ui.home_page_btn.click)
        # self.chart_pressure_b.btn_setting.clicked.connect(self.ui.home_page_btn.click)
        # self.chart_pressure_c.btn_setting.clicked.connect(self.ui.home_page_btn.click)

        # Thêm vào layout
        self.ui.card_temperature.addWidget(self.chart_temp)
        self.ui.card_pressure_1.addWidget(self.chart_pressure_a)
        self.ui.card_pressure_2.addWidget(self.chart_pressure_b)
        self.ui.card_pressure_3.addWidget(self.chart_pressure_c)

    ###########################################################################################
    #############################------ Button Function Setup ------###########################
    def _setup_btn_signals(self):
        ### Left side menu button
        self.ui.home_page_btn.clicked.connect(self.pressure_page_btn)
        self.ui.chart_page_btn.clicked.connect(self.home_page_btn)
        self.ui.device_page_btn.clicked.connect(self.device_page_btn)
        self.ui.history_page_btn.clicked.connect(self.history_page_btn)
        # self.ui.backward_btn.clicked.connect(lambda: self.ui.home_page_btn.click())

        self.ui.next_group_page_btn.clicked.connect(self.next_previous_pressure_page)
        self.ui.previus_group_page_btn.clicked.connect(self.next_previous_pressure_page)

        self.ui.back_connection_page_btn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.connection_page))
        self.ui.back_home_page_btn.clicked.connect(lambda: self.ui.home_page_btn.click())

        # self.ui.back_home_btn.clicked.connect(lambda: self.ui.chart_page_btn.click())

        self.ui.temp_unit_selection_combox.currentIndexChanged.connect(lambda: QTimer.singleShot(0, self._set_cur_unit))

        self.ui.plc_io_btn.installEventFilter(self)

        self.ui.new_data_btn.clicked.connect(self.new_data_btn)
        
        self.ui.start_btn.clicked.connect(lambda: self.start_stop_btn(self.ui.start_btn))
        self.ui.stop_btn.clicked.connect(lambda: self.start_stop_btn(self.ui.stop_btn))

        self.ui.heat_btn_a.toggled.connect(lambda checked: self.on_heat_btn_clicked("A", checked))
        self.ui.heat_btn_b.toggled.connect(lambda checked: self.on_heat_btn_clicked("B", checked))
        self.ui.heat_btn_c.toggled.connect(lambda checked: self.on_heat_btn_clicked("C", checked))

        # self.ui.heat_btn_a.toggled.connect(lambda checked: self.heating_btn("A", checked, self.ui.heat_btn_a))
        # self.ui.heat_btn_b.toggled.connect(lambda checked: self.heating_btn("B", checked, self.ui.heat_btn_b))
        # self.ui.heat_btn_c.toggled.connect(lambda checked: self.heating_btn("C", checked, self.ui.heat_btn_c))
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

        spinbox_map = {
            "pressure_sv_a_1": self.on_pressure_sv_a_1_changed,
            # "pressure_sv_a_2": self.on_pressure_sv_a_2_changed,
            # "pressure_sv_a_3": self.on_pressure_sv_a_3_changed,
            # "pressure_sv_a_4": self.on_pressure_sv_a_4_changed,
            "pressure_sv_a_5": self.on_pressure_sv_a_5_changed,
            "pressure_sv_a_6": self.on_pressure_sv_a_6_changed,
            "pressure_sv_a_7": self.on_pressure_sv_a_7_changed,
            "pressure_sv_a_8": self.on_pressure_sv_a_8_changed,
            "pressure_sv_a_9": self.on_pressure_sv_a_9_changed,
            "pressure_sv_a_10": self.on_pressure_sv_a_10_changed,
            "pressure_sv_a_11": self.on_cycle_a_displ_2_changed,

            "pressure_sv_b_1": self.on_pressure_sv_b_1_changed,
            # "pressure_sv_b_2": self.on_pressure_sv_b_2_changed,
            # "pressure_sv_b_3": self.on_pressure_sv_b_3_changed,
            # "pressure_sv_b_4": self.on_pressure_sv_b_4_changed,
            "pressure_sv_b_5": self.on_pressure_sv_b_5_changed,
            "pressure_sv_b_6": self.on_pressure_sv_b_6_changed,
            "pressure_sv_b_7": self.on_pressure_sv_b_7_changed,
            "pressure_sv_b_8": self.on_pressure_sv_b_8_changed,
            "pressure_sv_b_9": self.on_pressure_sv_b_9_changed,
            "pressure_sv_b_10": self.on_pressure_sv_b_10_changed,
            "pressure_sv_b_11": self.on_cycle_b_displ_2_changed,

            "pressure_sv_c_1": self.on_pressure_sv_c_1_changed,
            # "pressure_sv_c_2": self.on_pressure_sv_c_2_changed,
            # "pressure_sv_c_3": self.on_pressure_sv_c_3_changed,
            # "pressure_sv_c_4": self.on_pressure_sv_c_4_changed,
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
            "ct_t3_offset_value": self.on_ct_t3_offset_value_changed
        }

        install_clear_on_focus(self.ui.db_file_path_edit)
        install_clear_on_focus(self.ui.plc_ip_address_edit)
        install_clear_on_focus(self.ui.db_number_input)
        install_clear_on_focus(self.ui.db_data_size_input)

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

        self.ui.export_all_tables_to_excel_btn.clicked.connect(self.export_all_tables_to_excel_btn)

    def _setup_table(self):
        header = self.ui.list_history.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        for i in range(1, header.count()):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

    # ── Group A ──────────────────────────────────────────
    def on_pressure_sv_a_1_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_TemperatureSetting", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_a_5_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_PressureSetting", value) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_a_6_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_Air_FillingTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_a_7_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_Air_ReleaseTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_a_8_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_Air_ReleaseTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_a_9_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_Oil_Start_Time", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_a_10_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_Oil_End_Time", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore

    # ── Group B ──────────────────────────────────────────
    def on_pressure_sv_b_1_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_TemperatureSetting", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_b_5_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_PressureSetting", value) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_b_6_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_Air_FillingTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_b_7_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_Air_ReleaseTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_b_8_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_Air_ReleaseTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_b_9_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_Oil_Start_Time", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_b_10_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_Oil_End_Time", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore

    # ── Group C ──────────────────────────────────────────
    def on_pressure_sv_c_1_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_TemperatureSetting", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_c_5_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_PressureSetting", value) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_c_6_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_Air_FillingTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_c_7_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_Air_ReleaseTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_c_8_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_Air_ReleaseTime", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_c_9_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_Oil_Start_Time", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore
    def on_pressure_sv_c_10_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_Oil_End_Time", self.cal_sec_to_msec(value)) if self.plc_writer_connection else None #type: ignore

    # ── Cycle ──────────────────────────────────────────
    def on_cycle_a_displ_2_changed(self, value: int): self.plc_writer_worker.write_value.emit("P1_CountTimes", value) if self.plc_writer_connection else None #type: ignore
    def on_cycle_b_displ_2_changed(self, value: int): self.plc_writer_worker.write_value.emit("P2_CountTimes", value) if self.plc_writer_connection else None #type: ignore
    def on_cycle_c_displ_2_changed(self, value: int): self.plc_writer_worker.write_value.emit("P3_CountTimes", value) if self.plc_writer_connection else None #type: ignore

    # ── Temperature Modify ──────────────────────────────────────────
    def on_t0_sv_changed(self, value: float): self.plc_writer_worker.write_value.emit("T0_TemperatureSetting", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_at_sv_changed(self, value: float): self.plc_writer_worker.write_value.emit("P1_TemperatureSetting", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_bt_sv_changed(self, value: float): self.plc_writer_worker.write_value.emit("P2_TemperatureSetting", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore
    def on_ct_sv_changed(self, value: float): self.plc_writer_worker.write_value.emit("P3_TemperatureSetting", self.cal_fah_to_cel(value)) if self.plc_writer_connection else None #type: ignore

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

    def _setup_plc_threads(self):
        if not self.db_dict:
            ltmessage.error(self, "Error", "DB Layout not found! Cannot start PLC threads.")
            return 

        if not self._setup_read_plc_thread(
            ip=self.db_dict["ip_plc"],
            db_number=self.db_dict["db_name"],
            db_layout=self.db_dict["DB_LAYOUT"],
            db_size=self.db_dict["DB_TOTAL_BYTES"],
            poll_ms=self.db_dict["read_time"]
        ):
            ltmessage.error(self, "Error", "Failed to connect to PLC! Try again later.")

        if not self._setup_write_plc_thread(
            ip=self.db_dict["ip_plc"],
            db_number=self.db_dict["db_name"],
            db_layout=self.db_dict["DB_LAYOUT"],
            db_size=self.db_dict["DB_TOTAL_BYTES"],
            poll_ms=self.db_dict["write_time"]
        ):
            ltmessage.error(self, "Error", "Failed to connect to PLC! Try again later.")

    def _simulate_data(self):
        self.setup_simulate_threads()

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
            return False
        return True

    def _setup_read_plc_thread(
            self, 
            ip: str = "172.16.100.100", 
            db_number: Optional[int] = None, 
            db_layout: Optional[list[tuple[str, str, int, Any]]] = None, 
            db_size: Optional[int] = None, 
            poll_ms: int = 500
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
                poll_ms=poll_ms
            )
            self.plc_read_worker.moveToThread(self.plc_read_thread)

            self.plc_read_thread.started.connect(self.plc_read_worker.run)
            self.plc_read_worker.data_ready.connect(self._data_ready)
            self.plc_read_worker.connected.connect(self._read_status_plc)
            
            self.plc_read_worker.finished.connect(self.plc_read_thread.quit)
            self.plc_read_worker.finished.connect(self.plc_read_worker.deleteLater)
            self.plc_read_thread.finished.connect(self.plc_read_thread.deleteLater)

            self.plc_read_thread.start()
            if not self.plc_read_thread.isRunning():
                raise Exception("plc_read_thread failed to start")
        except Exception as e:
            print("PLC Reader gone wrong:", e)
            return False
        
        self.worker_dict["plc_read_worker"] = self.plc_read_worker
        return True

    def _setup_write_plc_thread(
            self, 
            ip: str = "172.100.16.100", 
            db_number: Optional[int] = None, 
            db_layout: Optional[List] = None, 
            db_size: Optional[int] = None, 
            poll_ms: int = 500
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
                write_gap_ms=poll_ms
            )
            self.plc_writer_worker.moveToThread(self.plc_writer_thread)
            self.plc_writer_thread.started.connect(self.plc_writer_worker.run)
            self.plc_writer_worker.connected.connect(self._write_status_plc)

            self.plc_writer_worker.finished.connect(self.plc_writer_thread.quit)
            self.plc_writer_worker.finished.connect(self.plc_writer_worker.deleteLater)
            self.plc_writer_thread.finished.connect(self.plc_writer_thread.deleteLater)

            self.plc_writer_thread.start()
            
        except Exception as e:
            print("PLC Writer gone wrong:", e)
        self.thread_dict["plc_writer_thread"] = self.plc_writer_thread
        return True

    def _data_ready(self, data: dict):
        try:
            # self.add_row_to_list_history(
            #     "A", 
            #     str(data.get('P1_Current_PressureHose', 0.0)), 
            #     str((data.get('P1_Current_Temp1', 0.0) + data.get('P1_Current_Temp2', 0.0) + data.get('P1_Current_Temp3', 0.0)) / 3), 
            #     str(data.get('P1_Current_Temp1', 0.0)), 
            #     str(data.get('P1_Current_Temp2', 0.0)), 
            #     str(data.get('P1_Current_Temp3', 0.0))
            # )
            # self.add_row_to_list_history(
            #     "B", 
            #     str(data.get('P2_Current_PressureHose', 0.0)), 
            #     str((data.get('P2_Current_Temp1', 0.0) + data.get('P2_Current_Temp2', 0.0) + data.get('P2_Current_Temp3', 0.0)) / 3), 
            #     str(data.get('P2_Current_Temp1', 0.0)), 
            #     str(data.get('P2_Current_Temp2', 0.0)), 
            #     str(data.get('P2_Current_Temp3', 0.0))
            # )
            # self.add_row_to_list_history(
            #     "C", 
            #     str(data.get('P3_Current_PressureHose', 0.0)), 
            #     str((data.get('P3_Current_Temp1', 0.0) + data.get('P3_Current_Temp2', 0.0) + data.get('P3_Current_Temp3', 0.0)) / 3), 
            #     str(data.get('P3_Current_Temp1', 0.0)), 
            #     str(data.get('P3_Current_Temp2', 0.0)), 
            #     str(data.get('P3_Current_Temp3', 0.0))
            # )
            # ====================== INPUT BOOLS ======================
            self._input_data_filter([
                bool(data.get('START', False)),
                bool(data.get('STOP', False)),
                bool(data.get('T0_Start_Heat', False)),
                bool(data.get('T0_StopHeat', False)),
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

            # ====================== T0 ======================
            self._t0_data_filter([
                float(data.get('T0_TemperatureSetting', 0.0)),
                float(data.get('T0_Current_Temp', 0.0))
            ])

            # ====================== P1 ======================
            self._group_a_data_filter([
                float((data.get('P1_Current_Temp1', 0.0) + 
                       data.get('P1_Current_Temp2', 0.0) + 
                       data.get('P1_Current_Temp3', 0.0)) / 3), # Tính trung bình 3 cảm biến nhiệt độ
                float(data.get('P1_Current_Temp1', 0.0)),
                float(data.get('P1_Current_Temp2', 0.0)),
                float(data.get('P1_Current_Temp3', 0.0)),
                float(data.get('P1_Current_PressureHose', 0.0)),
                float(data.get('P1_Current_Air_FillingTime', 0)/1000),
                float(data.get('P1_Current_Air_HoldingTime', 0)/1000),
                float(data.get('P1_Current_Air_ReleaseTime', 0)/1000),
                float(data.get('P1_Current_Oil_Start_Time', 0)/1000),
                float(data.get('P1_Current_Oil_End_Time', 0)/1000)
            ])

            # ====================== P2 ======================
            self._group_b_data_filter([
                float((data.get('P2_Current_Temp1', 0.0) + 
                       data.get('P2_Current_Temp2', 0.0) + 
                       data.get('P2_Current_Temp3', 0.0)) / 3), # Tính trung bình 3 cảm biến nhiệt độ
                float(data.get('P2_Current_Temp1', 0.0)),
                float(data.get('P2_Current_Temp2', 0.0)),
                float(data.get('P2_Current_Temp3', 0.0)),
                float(data.get('P2_Current_PressureHose', 0.0)),
                float(data.get('P2_Current_Air_FillingTime', 0)/1000),
                float(data.get('P2_Current_Air_HoldingTime', 0)/1000),
                float(data.get('P2_Current_Air_ReleaseTime', 0)/1000),
                float(data.get('P2_Current_Oil_Start_Time', 0)/1000),
                float(data.get('P2_Current_Oil_End_Time', 0)/1000)
            ])

            # ====================== P3 ======================
            self._group_c_data_filter([
                float((data.get('P3_Current_Temp1', 0.0) + 
                       data.get('P3_Current_Temp2', 0.0) + 
                       data.get('P3_Current_Temp3', 0.0)) / 3), # Tính trung bình 3 cảm biến nhiệt độ
                float(data.get('P3_Current_Temp1', 0.0)),
                float(data.get('P3_Current_Temp2', 0.0)),
                float(data.get('P3_Current_Temp3', 0.0)),
                float(data.get('P3_Current_PressureHose', 0.0)),
                float(data.get('P3_Current_Air_FillingTime', 0)/1000),
                float(data.get('P3_Current_Air_HoldingTime', 0)/1000),
                float(data.get('P3_Current_Air_ReleaseTime', 0)/1000),
                float(data.get('P3_Current_Oil_Start_Time', 0)/1000),
                float(data.get('P3_Current_Oil_End_Time', 0)/1000)
            ])

            # ====================== Cycle / Number Test Times ======================

            self._set_cycle_time_unit([
                int(data.get('P1_Number_Test_Times', 0)),
                int(data.get('P2_Number_Test_Times', 0)),
                int(data.get('P3_Number_Test_Times', 0))
            ])

            # ====================== AT, BT, CT Widgets ======================
            self._at_data_filter([
                float(data.get('P1_Current_Temp1', 0.0)),
                float(data.get('P1_Current_Temp2', 0.0)),
                float(data.get('P1_Current_Temp3', 0.0))
            ])

            self._bt_data_filter([
                float(data.get('P2_Current_Temp1', 0.0)),
                float(data.get('P2_Current_Temp2', 0.0)),
                float(data.get('P2_Current_Temp3', 0.0))
            ])

            self._ct_data_filter([
                float(data.get('P3_Current_Temp1', 0.0)),
                float(data.get('P3_Current_Temp2', 0.0)),
                float(data.get('P3_Current_Temp3', 0.0))
            ])

            # ====================== ITV Pressure ======================
            self._itv_data_filter([
                float(data.get('P1_Current_PressureITV', 0.0)),
                float(data.get('P2_Current_PressureITV', 0.0)),
                float(data.get('P3_Current_PressureITV', 0.0))
            ])

            # ====================== Alarm ======================
            self._alarm_data_filter([
                bool(data.get('Bit_Alarm', False)),
                str(data.get('Alarm_Info', ""))
            ])

        except Exception as e:
            print("PLC Data Processing Error: %s", e)

    def _write_done(self, address: str, value: Any):
        print(f"Write to {address} successful: {value}")

    def _write_error(self, error: str):
        print(f"Write failed: {error}")

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
        if not isinstance(list_group_a_recv, list) and not isinstance(list_group_b_recv, list) and not isinstance(list_group_c_recv, list):
            return
        pv_avg = [(list_group_a_recv[4] + list_group_b_recv[4] + list_group_c_recv[4]) / 3]
        temp_values = [self.for_display_temp((self.ui.pressure_sv_a_1.value() + self.ui.pressure_sv_a_1.value() + self.ui.pressure_sv_a_1.value())/3),
                        self.for_display_temp((list_group_a_recv[0] + list_group_b_recv[0] + list_group_c_recv[0]) / 3)
                       ]
        self.chart_temp.append_data(temp_values, pv_avg)

        group_a_values = [self.ui.pressure_sv_a_1.value(),
                            self.for_display_temp(list_group_a_recv[2]),
                            self.for_display_temp(list_group_a_recv[3]),
                            self.for_display_temp(list_group_a_recv[4])]
        group_a_press_values = [list_group_a_recv[0]]
        self.chart_pressure_a.append_data(group_a_values, group_a_press_values)

        group_b_values = [self.ui.pressure_sv_b_1.value(),
                        self.for_display_temp(list_group_b_recv[2]),
                        self.for_display_temp(list_group_b_recv[3]),
                        self.for_display_temp(list_group_b_recv[4])]
        group_b_press_values = [list_group_b_recv[0]]
        self.chart_pressure_b.append_data(group_b_values, group_b_press_values)

        group_c_values = [self.ui.pressure_sv_c_1.value(),
                        self.for_display_temp(list_group_c_recv[2]),
                        self.for_display_temp(list_group_c_recv[3]),
                        self.for_display_temp(list_group_c_recv[4])]
        group_c_press_values = [list_group_c_recv[0]]
        self.chart_pressure_c.append_data(group_c_values, group_c_press_values)

    def _input_data_filter(self, list_input_recv):
        for obj, value in zip(self.io_group_1_switch_obj, list_input_recv):
            obj.setCurrentIndex(value)

    def _group_a_data_filter(self, list_group_a_recv):
        group_a_values = [self.ui.pressure_sv_a_1.value(),
                            self.for_display_temp(list_group_a_recv[0]),
                            self.for_display_temp(list_group_a_recv[1]),
                            self.for_display_temp(list_group_a_recv[2]),
                            list_group_a_recv[3]]
        self.chart_pressure_a.append_data(group_a_values)
        self.temp_pv_obj[1].setValue(self.for_display_temp(list_group_a_recv[1]))
        for i, val_a in enumerate(list_group_a_recv):
            self.pressure_a_pv_obj[i].setValue(val_a if i >= 4 else self.for_display_temp(val_a))

    def _group_b_data_filter(self, list_group_b_recv):
        group_b_values = [self.ui.pressure_sv_b_1.value(),
                        self.for_display_temp(list_group_b_recv[0]),
                        self.for_display_temp(list_group_b_recv[1]),
                        self.for_display_temp(list_group_b_recv[2]),
                        list_group_b_recv[3]
                        ]
        self.chart_pressure_b.append_data(group_b_values)
        self.temp_pv_obj[2].setValue(self.for_display_temp(list_group_b_recv[1]))
        for i, val_b in enumerate(list_group_b_recv):
            self.pressure_b_pv_obj[i].setValue(val_b if i >= 4 else self.for_display_temp(val_b))
      
    def _group_c_data_filter(self, list_group_c_recv):
        group_c_values = [self.ui.pressure_sv_c_1.value(),
                        self.for_display_temp(list_group_c_recv[0]),
                        self.for_display_temp(list_group_c_recv[1]),
                        self.for_display_temp(list_group_c_recv[2]),
                        list_group_c_recv[3]]
        self.chart_pressure_c.append_data(group_c_values)
        self.temp_pv_obj[3].setValue(self.for_display_temp(list_group_c_recv[1]))
        for i, val_c in enumerate(list_group_c_recv):
            self.pressure_c_pv_obj[i].setValue(val_c if i >= 4 else self.for_display_temp(val_c))
    def _t0_data_filter(self, list_group_t0_recv):
        sv_t0 = list_group_t0_recv[0]
        pv_t0 = list_group_t0_recv[1]
        temp_values = [self.for_display_temp(sv_t0),
                        self.for_display_temp(pv_t0)]
        self.chart_temp.append_data(temp_values)
        self.temp_pv_obj[0].setValue(self.for_display_temp(pv_t0))

    def _at_data_filter(self, list_group_at_recv):
        self.ui.at_pv.setValue(self.for_display_temp(list_group_at_recv[0] + list_group_at_recv[1] + list_group_at_recv[2])/3)

    def _bt_data_filter(self, list_group_bt_recv):
        self.ui.bt_pv.setValue(self.for_display_temp(list_group_bt_recv[0] + list_group_bt_recv[1] + list_group_bt_recv[2])/3)

    def _ct_data_filter(self, list_group_ct_recv):
        self.ui.ct_pv.setValue(self.for_display_temp(list_group_ct_recv[0] + list_group_ct_recv[1] + list_group_ct_recv[2])/3)

    def _itv_data_filter(self, list_group_itv_recv):
        self.ui.fp1_value.setValue(list_group_itv_recv[0])
        self.ui.fp2_value.setValue(list_group_itv_recv[1])
        self.ui.fp3_value.setValue(list_group_itv_recv[2])

    def _alarm_data_filter(self, alarm_recv):
        if alarm_recv[0]:
            self.ui.error_display.setText(alarm_recv[1])

    def on_heat_btn_clicked(self, channel: str, checked: bool):
        simulator = self.thread_dict.get("data_simulator")
        if simulator is None:
            return

        if checked:
            if   channel == "A":
                pressure_sv = self.pressure_a_sv_obj[4].value() 
                temp_sv     = self.pressure_a_sv_obj[0].value() if self.pressure_a_sv_obj[0].value() > self.default_temp_room else self.default_temp_room
            elif channel == "B":
                pressure_sv = self.pressure_b_sv_obj[4].value()
                temp_sv     = self.pressure_b_sv_obj[0].value() if self.pressure_b_sv_obj[0].value() > self.default_temp_room else self.default_temp_room
            elif channel == "C":
                pressure_sv = self.pressure_c_sv_obj[4].value()
                temp_sv     = self.pressure_c_sv_obj[0].value() if self.pressure_c_sv_obj[0].value() > self.default_temp_room else self.default_temp_room

            simulator.set_channel_active(channel, pressure_sv, temp_sv)
        else:
            simulator.set_channel_active(channel, 0.0, self.default_temp_room)  # Reset về mặc định

    def heating_btn(self, channel: str, checked: bool, btn=None):
        self.disable_controls_group(channel, False)
        if not self.plc_writer_connection:
            ltmessage.error(self, "Error", "PLC Writer not connected!")
            if btn is not None:
                btn.blockSignals(True)   # Chặn signal để tránh gọi đệ quy
                btn.setChecked(False)
                btn.blockSignals(False)
            return
        else:
            if channel == "A":
                if checked:
                    self.plc_writer_worker.write_bool.emit("P1_Start_Heat", True)
                    self.disable_heat_group(channel, False)
                    # ltmessage.information(self, "Heating", "Group A Heating On!")
                else:
                    self.plc_writer_worker.write_bool.emit("P1_Start_Heat", False)
                    self.disable_heat_group(channel, True)
                    print("Group A Heating Off!")
                return
            if channel == "B":
                if checked:
                    self.plc_writer_worker.write_bool.emit("P2_Start_Heat", True)
                    self.disable_heat_group(channel, False)
                    # ltmessage.information(self, "Heating", "Group B Heating On!")
                else:
                    self.plc_writer_worker.write_bool.emit("P2_Start_Heat", False)
                    self.disable_heat_group(channel, True)
                    print("Group B Heating Off!")
                return
            if channel == "C":
                if checked:
                    self.plc_writer_worker.write_bool.emit("P3_Start_Heat", True)
                    self.disable_heat_group(channel, False)
                    # ltmessage.information(self, "Heating", "Group C Heating On!")
                else:
                    self.plc_writer_worker.write_bool.emit("P3_Start_Heat", False)
                    self.disable_heat_group(channel, True)
                    print("Group C Heating Off!")
                return
            if channel == "T0":
                if checked:
                    self.plc_writer_worker.write_bool.emit("T0_Start_Heat", True)
                    self.disable_heat_group(channel, False)
                    # ltmessage.information(self, "Heating", "T0 Heating On!")
                else:
                    self.plc_writer_worker.write_bool.emit("T0_Stop_Heat", False)
                    self.disable_heat_group(channel, True)
                    print("T0 Heating Off!")
                return


    def pumping_btn(self, channel: str, checked: bool, btn=None):
        if not self.plc_writer_connection:
            ltmessage.error(self, "Error", "PLC Writer not connected!")
            if btn is not None:
                btn.blockSignals(True)   # Chặn signal để tránh gọi đệ quy
                btn.setChecked(False)
                btn.blockSignals(False)
            return
        else:
            if channel == "A":
                if checked:
                    self.plc_writer_worker.write_bool.emit("P1_Start_Pressure", True)
                    self.disable_pressure_group(channel, False)
                    # ltmessage.information(self, "Pumping", "Group A Pressure On!")
                else:
                    self.plc_writer_worker.write_bool.emit("P1_Start_Pressure", False)
                    self.disable_pressure_group(channel, True)
                    print("Group A Pressure Off!")

            elif channel == "B":
                if checked:
                    self.plc_writer_worker.write_bool.emit("P2_Start_Pressure", True)
                    self.disable_pressure_group(channel, False)
                    # ltmessage.information(self, "Pumping", "Group B Pressure On!")
                else:
                    self.plc_writer_worker.write_bool.emit("P2_Start_Pressure", False)
                    self.disable_pressure_group(channel, True)
                    print("Group B Pressure Off!")

            elif channel == "C":
                if checked:
                    self.plc_writer_worker.write_bool.emit("P3_Start_Pressure", True)
                    self.disable_pressure_group(channel, False)
                    # ltmessage.information(self, "Pumping", "Group C Pressure On!")
                else:
                    self.plc_writer_worker.write_bool.emit("P3_Start_Pressure", False)
                    self.disable_pressure_group(channel, True)
                    print("Group C Pressure Off!")
            return

    def fill_oil_btn(self, channel: str, checked: bool, btn=None):
        if not self.plc_writer_connection:
            ltmessage.error(self, "Error", "PLC Writer not connected!")
            if btn is not None:
                btn.blockSignals(True)   # Chặn signal để tránh gọi đệ quy
                btn.setChecked(False)
                btn.blockSignals(False)
            return
        else:
            if channel == "A":
                if checked:
                    self.plc_writer_worker.write_bool.emit("P1_Start_Oil", True)
                    self.disable_oil_group(channel, False)
                    # ltmessage.information(self, "Oil Fill", "Group A Oil Filling On!")
                else:
                    self.plc_writer_worker.write_bool.emit("P1_Start_Oil", False)
                    self.disable_oil_group(channel, True)
                    print("Group A Oil Filling Off!")

            if channel == "B":
                if checked:
                    self.plc_writer_worker.write_bool.emit("P2_Start_Oil", True)
                    self.disable_oil_group(channel, False)
                    # ltmessage.information(self, "Oil Fill", "Group B Oil Filling On!")
                else:
                    self.plc_writer_worker.write_bool.emit("P2_Start_Oil", False)
                    self.disable_oil_group(channel, True)
                    print("Group B Oil Filling Off!")

            if channel == "C":
                if checked:
                    self.plc_writer_worker.write_bool.emit("P3_Start_Oil", True)
                    self.disable_oil_group(channel, False)
                    # ltmessage.information(self, "Oil Fill", "Group C Oil Filling On!")
                else:
                    self.plc_writer_worker.write_bool.emit("P3_Start_Oil", False)
                    self.disable_oil_group(channel, True)
                    print("Group C Oil Filling Off!")

    def cycle_loop_btn(self, channel: str, checked: bool, btn=None):
        if not self.plc_writer_connection:
            ltmessage.error(self, "Error", "PLC Writer not connected!")
            if btn is not None:
                btn.blockSignals(True)   # Chặn signal để tránh gọi đệ quy
                btn.setChecked(False)
                btn.blockSignals(False)
            return
        else:
            if channel == "A":
                if checked:
                    self.plc_writer_worker.write_bool.emit("P1_BitCountTimes", True)
                    self.ui.pressure_sv_a_11.setEnabled(False)
                    # ltmessage.information(self, "Set Cycle A", "Group A Auto Repeat!")
                else:
                    self.plc_writer_worker.write_bool.emit("P1_BitCountTimes", False)
                    self.ui.pressure_sv_a_11.setEnabled(True)
                    print("Group A Auto Repeat Off!")
                return
            if channel == "B":
                if checked:
                    self.plc_writer_worker.write_bool.emit("P2_BitCountTimes", True)
                    self.ui.pressure_sv_b_11.setEnabled(False)
                    # ltmessage.information(self, "Set Cycle B", "Group B Auto Repeat!")
                else:
                    self.plc_writer_worker.write_bool.emit("P2_BitCountTimes", False)
                    self.ui.pressure_sv_b_11.setEnabled(True)
                    print("Group B Auto Repeat Off!")
                return
            if channel == "C":
                if checked:
                    self.plc_writer_worker.write_bool.emit("P3_BitCountTimes", True)
                    self.ui.pressure_sv_c_11.setEnabled(False)
                    # ltmessage.information(self, "Set Cycle C", "Group C Auto Repeat!")
                else:
                    self.plc_writer_worker.write_bool.emit("P3_BitCountTimes", False)
                    self.ui.pressure_sv_c_11.setEnabled(True)
                    print("Group C Auto Repeat Off!")
                return

    def start_stop_btn(self, btn=None):
        if not self.plc_writer_connection:
            ltmessage.error(self, "Error", "PLC Writer not connected!")
            if btn is not None:
                btn.blockSignals(True)   # Chặn signal để tránh gọi đệ quy
                btn.setChecked(False)
                btn.blockSignals(False)
            return
        if self.ui.start_stop_stacked.currentIndex() == 0:
            self.ui.sys_state_stacked_wid_39.setCurrentIndex(1)
            self.ui.start_stop_stacked.setCurrentIndex(1)
            self.plc_writer_worker.write_bool.emit("START", True)
            QTimer.singleShot(250, lambda: self.plc_writer_worker.write_bool.emit("START", False))
            # ltmessage.information(self, "Strike Machine", "System On!")
        elif self.ui.start_stop_stacked.currentIndex() == 1:
            self.ui.sys_state_stacked_wid_39.setCurrentIndex(0)
            self.ui.start_stop_stacked.setCurrentIndex(0)
            self.plc_writer_worker.write_bool.emit("STOP", True)
            QTimer.singleShot(250, lambda: self.plc_writer_worker.write_bool.emit("STOP", False))
            print("System Off!")

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
        # path = Path(file_str)

        # df = pd.read_excel(path, sheet_name='Sheet1', header=None)

        # db_layout: List[Tuple[str, str, int, Any]] = []
        # max_byte = 0
        
        # for i in range(4, len(df)):
        #     row = df.iloc[i]
            
        #     # Cột B: Name
        #     name_raw = str(row[1]).strip() if pd.notna(row[1]) else ""
        #     if name_raw == "" or name_raw.lower() == "nan":
        #         break
                
        #     # Chuẩn hóa tên
        #     name = name_raw.replace(" ", "_").replace("-", "_")
            
        #     # Cột C: Type
        #     data_type = str(row[2]).strip().upper() if pd.notna(row[2]) else ""
            
        #     # Cột D: Address
        #     try:
        #         addr_str = str(row[3]).strip()
        #         byte_addr = int(float(addr_str.split('.')[0])) if '.' in addr_str else int(float(addr_str))
        #     except:
        #         byte_addr = 0
            
        #     # Cập nhật max byte
        #     if byte_addr > max_byte:
        #         max_byte = byte_addr
            
        #     # Xử lý Bit cho BOOL
        #     bit: Any = None
        #     if data_type == "BOOL":
        #         addr_str = str(row[3]).strip()
        #         if '.' in addr_str:
        #             try:
        #                 bit = int(addr_str.split('.')[1])  # lấy phần sau dấu .
        #             except:
        #                 bit = 0
        #         else:
        #             bit = 0 
        #     db_layout.append((name, data_type, byte_addr, bit))
        
        # last_item = db_layout[-1] if db_layout else None
        # if last_item and last_item[1] == "STRING":
        #     string_start = last_item[2]
        #     db_total_bytes = string_start + 256
        # else:
        #     db_total_bytes = max_byte + 4
        
        # self.db_dict =  {
        #     "ip_plc": str(df.iloc[0, 1]).strip(),
        #     "cycle_time": int(str(df.iloc[1, 1]).strip()),
        #     "db_name": str(df.iloc[2, 0]).strip(),
        #     "DB_LAYOUT": db_layout,
        #     "DB_TOTAL_BYTES": db_total_bytes
        # }

    def update_simulator_sv(self):
        """Gọi hàm này mỗi khi SV thay đổi trên UI"""
        simulator = self.thread_dict.get("data_simulator")
        if simulator is None:
            return

        pressure_sv = [
            self.pressure_a_sv_obj[0].value(),
            self.pressure_b_sv_obj[0].value(),
            self.pressure_c_sv_obj[0].value(),
        ]

        temp_sv = [
            self.pressure_a_sv_obj[1].value(),
            self.pressure_b_sv_obj[1].value(),
            self.pressure_c_sv_obj[1].value(),
        ]
        simulator.update_sv(pressure_sv, temp_sv)

    def on_write_sv_clicked(self):
        sv_data = {
            "A": {
                "pressure":     self.pressure_a_sv_obj[0].value(),
                "temp":         self.pressure_a_sv_obj[1].value(),
                "front_temp":   self.pressure_a_sv_obj[2].value(),
                "mid_temp":     self.pressure_a_sv_obj[3].value(),
                "end_temp":     self.pressure_a_sv_obj[4].value(),
                "gas_fill":     self.pressure_a_sv_obj[5].value(),
                "gas_hold":     self.pressure_a_sv_obj[6].value(),
                "gas_bleed":    self.pressure_a_sv_obj[7].value(),
                "refuel_start": self.pressure_a_sv_obj[8].value(),
                "refuel_end":   self.pressure_a_sv_obj[9].value(),
            },
            "B": {
                "pressure":     self.pressure_b_sv_obj[0].value(),
                "temp":         self.pressure_b_sv_obj[1].value(),
                "front_temp":   self.pressure_b_sv_obj[2].value(),
                "mid_temp":     self.pressure_b_sv_obj[3].value(),
                "end_temp":     self.pressure_b_sv_obj[4].value(),
                "gas_fill":     self.pressure_b_sv_obj[5].value(),
                "gas_hold":     self.pressure_b_sv_obj[6].value(),
                "gas_bleed":    self.pressure_b_sv_obj[7].value(),
                "refuel_start": self.pressure_b_sv_obj[8].value(),
                "refuel_end":   self.pressure_b_sv_obj[9].value(),
            },
            "C": {
                "pressure":     self.pressure_c_sv_obj[0].value(),
                "temp":         self.pressure_c_sv_obj[1].value(),
                "front_temp":   self.pressure_c_sv_obj[2].value(),
                "mid_temp":     self.pressure_c_sv_obj[3].value(),
                "end_temp":     self.pressure_c_sv_obj[4].value(),
                "gas_fill":     self.pressure_c_sv_obj[5].value(),
                "gas_hold":     self.pressure_c_sv_obj[6].value(),
                "gas_bleed":    self.pressure_c_sv_obj[7].value(),
                "refuel_start": self.pressure_c_sv_obj[8].value(),
                "refuel_end":   self.pressure_c_sv_obj[9].value(),
            },
        }

        try:
            self.plc_writer.write_all_sv(sv_data)
            print("Write PLC success")
        except Exception as e:
            print(f"Write PLC error: {e}")

    def _set_pv_data(self, list_1, list_2, list_3):
        for i, (val_1, val_2, val_3) in enumerate(zip(list_1, list_2, list_3)):
            self.pressure_a_pv_obj[i].setValue(val_1 if i == 4 else self.for_display_temp(val_1))
            self.pressure_b_pv_obj[i].setValue(val_2 if i == 4 else self.for_display_temp(val_2))
            self.pressure_c_pv_obj[i].setValue(val_3 if i == 4 else self.for_display_temp(val_3))

    def _set_cur_unit(self):
        index = self.ui.temp_unit_selection_combox.currentIndex()
        for i in range(len(self.cel_fah_change)):
            self.cel_fah_change[i].setCurrentIndex(index)
        self.current_unit = index
        self._set_sv_widget_pressure_obj()
        self._set_sv_widget_temperature_obj()
        self._set_chart_unit()

    def _set_sv_widget_pressure_obj(self):
        for i in range(1):
            self.pressure_a_sv_obj[i].blockSignals(True)
            self.pressure_a_sv_obj[i].setValue(self.convert_cel_fah(self.pressure_a_sv_obj[i].value()))
            self.pressure_a_sv_obj[i].blockSignals(False)
            self.pressure_b_sv_obj[i].blockSignals(True)
            self.pressure_b_sv_obj[i].setValue(self.convert_cel_fah(self.pressure_b_sv_obj[i].value()))
            self.pressure_b_sv_obj[i].blockSignals(False)
            self.pressure_c_sv_obj[i].blockSignals(True)
            self.pressure_c_sv_obj[i].setValue(self.convert_cel_fah(self.pressure_c_sv_obj[i].value()))
            self.pressure_c_sv_obj[i].blockSignals(False)

    def _set_sv_widget_temperature_obj(self):
        for i in range(4):
            self.temp_sv_obj[i].blockSignals(True)
            self.temp_sv_obj[i].setValue(self.convert_cel_fah(self.temp_sv_obj[i].value()))
            self.temp_sv_obj[i].blockSignals(False)

            self.temp_h_alm_obj[i].blockSignals(True)
            self.temp_h_alm_obj[i].setValue(self.convert_cel_fah(self.temp_h_alm_obj[i].value()))
            self.temp_h_alm_obj[i].blockSignals(False)

            self.temp_l_alm_obj[i].blockSignals(True)
            self.temp_l_alm_obj[i].setValue(self.convert_cel_fah(self.temp_l_alm_obj[i].value()))
            self.temp_l_alm_obj[i].blockSignals(False)

        for i in range(len(self.temp_offset_obj)):
            self.temp_offset_obj[i].blockSignals(True)
            self.temp_offset_obj[i].setValue(self.convert_cel_fah(self.temp_offset_obj[i].value()))
            self.temp_offset_obj[i].blockSignals(False)

    def _set_chart_unit(self):
        if self.current_unit == 0:
            self.chart_temp.set_y_label("°C")
            self.chart_pressure_a.set_y_label("°C")
            self.chart_pressure_b.set_y_label("°C")
            self.chart_pressure_c.set_y_label("°C")

        elif self.current_unit == 1:
            self.chart_temp.set_y_label("°F")
            self.chart_pressure_a.set_y_label("°F")
            self.chart_pressure_b.set_y_label("°F")
            self.chart_pressure_c.set_y_label("°F")

    def for_display_temp(self, celsius):
        if self.current_unit == 1:
            return celsius * 9/5 + 32
        return celsius

    # def _update_alarm_state(self, )

    def convert_cel_fah(self, temp):
        if self.current_unit == 1:
            return temp * 9/5 + 32
        elif self.current_unit == 0:
            return (temp - 32) * 5/9

    def cal_fah_to_cel(self, temp):
        if self.current_unit == 1:
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
                
    def update_clock(self):
        self.ui.date_displ.setDateTime(QDateTime.currentDateTime())

    def disable_oil_group(self, channel, status):
        """
        Enable or disable UI controls during system operation.
        \nBật hoặc tắt các điều khiển UI trong quá trình hoạt động của máy.
        """
        if channel == "A":
            for i in range(9, 11):
                self.pressure_a_sv_obj[i].setEnabled(status)
            return

        elif channel == "B":
            for i in range(9, 11):
                self.pressure_b_sv_obj[i].setEnabled(status)
            return

        elif channel == "C":
            for i in range(9, 11):
                self.pressure_c_sv_obj[i].setEnabled(status)
            return

    def disable_pressure_group(self, channel, status):
        """
        Enable or disable UI controls during system operation.
        \nBật hoặc tắt các điều khiển UI trong quá trình hoạt động của máy.
        """
        if channel == "A":
            for i in range(5, 9):
                self.pressure_a_sv_obj[i].setEnabled(status)
            return

        elif channel == "B":
            for i in range(5, 9):
                self.pressure_b_sv_obj[i].setEnabled(status)
            return

        elif channel == "C":
            for i in range(5, 9):
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

    def add_row_to_list_history(self, group_name: str, pressure_value: str, temp_value: str, front_temp: str, mid_temp: str, end_temp: str):
        """
        Add a new entry to the 'list_history' table, filling empty rows first before adding new ones.
        \nThêm một mục mới vào bảng 'list_history', ưu tiên điền vào hàng trống trước khi thêm hàng mới.
        """
        # TOTAL_COLUMNS = 8

        if not self.ui.list_history:
            print("[ProductionApp]-[add_row_to_list_history]: list_history table is not initialized")
            # self.dialog_notification.check_main_win.emit("MainWindow", "list_history table is not initialized")
            return
        try:
            row_count = self.ui.list_history.rowCount()
            target_row = None

            # Find the first empty row (row without STT)
            for row in range(row_count):
                stt_item = self.ui.list_history.item(row, 0)
                if stt_item is None or not stt_item.text().strip():
                    target_row = row
                    break

            if target_row is None:
                target_row = row_count
                self.ui.list_history.insertRow(target_row)

            # start_time = begin_time or datetime.now().strftime("%H:%M:%S")
            # end_time = done_time or datetime.now().strftime("%H:%M:%S")
            today_date = datetime.now().strftime("%d/%m/%y")

            # Chuyển đổi total_time (chuỗi H:MM:SS hoặc HH:MM:SS) thành số giây
            def time_str_to_seconds(time_str):
                try:
                    parts = [int(x) for x in str(time_str).split(":")]
                    if len(parts) == 3:
                        h, m, s = parts
                    elif len(parts) == 2:
                        h, m = parts
                        s = 0
                    else:
                        return 0
                    return h * 3600 + m * 60 + s
                except Exception:
                    return 0
            
            def time_str_to_minutes(time_str):
                try:
                    parts = [int(x) for x in str(time_str).split(":")]
                    if len(parts) == 3:
                        h, m, s = parts
                    elif len(parts) == 2:
                        h, m = parts
                        s = 0
                    else:
                        return 0
                    return h * 60 + m * 1 + (s/60)
                except Exception:
                    return 0

            # total_time_sec = time_str_to_seconds(total_time)
            # total_time_min = time_str_to_minutes(total_time)
            stt = str(target_row)
            row_data = [
                stt,                    # STT
                group_name,             # A, B, C Group
                pressure_value,         # Pressure Value
                temp_value,             # Temperature
                front_temp,             # Front Temperature
                mid_temp,               # Middle Temperature
                end_temp,               # End Temperature
                today_date              # Date
            ]           

            for col, data in enumerate(row_data):
                self.ui.list_history.setItem(target_row, col, QTableWidgetItem(data))

            self.ui.list_history.resizeColumnsToContents()

        except Exception as e:
            if not hasattr(self, 'dialog_notification') or self.dialog_notification is None:
                self.logger.error("[ProductionApp]-[add_row_to_list_history]: Dialog_Notification not initialized")
            else:
                self.logger.error(f"[ProductionApp]-[add_row_to_list_history]: Error adding row to list_history: {e}")

    def _is_row_complete(self, row_index, total_columns):
        """Check if a specific row has all required data filled.
        \nKiểm tra xem một hàng cụ thể có đầy đủ dữ liệu hay không."""
        for col in range(total_columns):
            item = self.ui.list_history.item(row_index, col)
            if item is None or not item.text().strip():
                return False
        return True

    def export_all_tables_to_excel_btn(self):
        """
        Export both the list_history and list_err tables to two dif Excel files
        \nExport cả bảng list_history và list_err ra 2 file Excel riêng biệt.
        """
        current_date = datetime.now().strftime("%d_%m_%Y")

        file_export = self.ui.list_history
        default_filename_done = f"History {current_date}.xlsx"
        list_history_folder = Path(self.stk_mch_folder) / "Excel"
        filename_done = list_history_folder / default_filename_done
        if filename_done:
            # self._export_table_to_excel(file_export, filename_done)
            self.export_table_to_excel(file_export, str(filename_done))

    def _export_table_to_excel(self, table_widget, filename):
        try:
            original_filename = Path(filename)
            counter = 1
            
            while True:
                try:
                    with open(filename, 'a'):
                        pass
                    break
                except PermissionError:
                    stem = original_filename.stem
                    suffix = original_filename.suffix
                    parent = original_filename.parent
                    filename = str(parent / f"{stem} ({counter}){suffix}")
                    counter += 1
            
            wb = Workbook()
            ws = wb.active
            ws.title = "Exported Data" # type: ignore

            # Ghi dữ liệu
            for row in range(table_widget.rowCount()):
                row_data = []
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    print(f"Row {row}, Col {col}: {item.text() if item else 'None'}")
                    row_data.append(item.text() if item else "")
                ws.append(row_data) # type: ignore

            # Auto-fit cột
            for col in ws.columns: # type: ignore
                max_length = 0
                col_letter = col[0].column_letter # type: ignore
                for cell in col:
                    try:
                        max_length = max(max_length, len(str(cell.value)))
                    except:
                        pass
                ws.column_dimensions[col_letter].width = max_length + 2 # type: ignore

            wb.save(filename)
            self.logger.info(f"[ProductionApp]-[export_table_to_excel]: Exported to {filename}")
            ltmessage.information(self, "Success", f"Exported to {filename}")

        except Exception as e:
            self.logger.error(f"[ProductionApp]-[export_table_to_excel]: Export file Error: {e}")
            ltmessage.error(self, "Export Error", str(e))

    def export_table_to_excel(self, table: QTableWidget, default_filename: str = "export"):
        """Xuất QTableWidget ra file Excel"""
        
        # Chọn nơi lưu file
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Excel File",
            default_filename,
            "Excel Files (*.xlsx)"
        )
        
        if not file_path:  # User cancel
            return
        
        if not file_path.endswith(".xlsx"):
            file_path += ".xlsx"

        # Lấy headers từ QTableWidget
        headers = []
        for col in range(table.columnCount()):
            header = table.horizontalHeaderItem(col)
            headers.append(header.text() if header else f"Column {col + 1}")

        # Lấy data từ QTableWidget
        rows = []
        for row in range(table.rowCount()):
            row_data = []
            for col in range(table.columnCount()):
                item = table.item(row, col)
                row_data.append(item.text() if item else "")
            rows.append(row_data)

        # Tạo DataFrame và xuất Excel
        df = pd.DataFrame(rows, columns=headers)
        
        try:
            with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name="Sheet1")
                
                # Auto-fit column width
                worksheet = writer.sheets["Sheet1"]
                for col_idx, col_name in enumerate(df.columns, start=1):
                    max_len = max(
                        len(str(col_name)),
                        df.iloc[:, col_idx - 1].astype(str).map(len).max() if len(df) > 0 else 0
                    )
                    worksheet.column_dimensions[
                        worksheet.cell(1, col_idx).column_letter
                    ].width = max_len + 4

            ltmessage.information(self, "Success", f"Exported successfully:\n{file_path}")

        except Exception as e:
            ltmessage.error(self, "Error", f"Export failed:\n{e}")

    def closeEvent(self, event):
        reply = ltmessage.question(
            self, "Exit Confirmation", "Are you sure you want to exit?"
        )

        if reply == ltmessage.Yes:
            print("Application is closing...")
            try:
                self._close_event_cleanup()
            except Exception as e:
                ltmessage.error(self, "Error", f"Failed to cleanup: {e}")
                event.ignore()
            event.accept()
        else:
            event.ignore()
        
    def _close_event_cleanup(self):
        self._cleanup()

    def _cleanup(self):
        for timer in getattr(self, 'all_timer', []):
            if timer.isActive():
                timer.stop()
            timer.deleteLater()
        self.all_timer.clear()
        self.off_simulate()
        self.hide()

        if self.plc_read_worker:
            self.plc_read_worker.stop()
        if self.plc_writer_worker:
            self.plc_writer_worker.stop()

        if self.plc_read_thread:
            self.plc_read_thread.wait()
        if self.plc_writer_thread:
            self.plc_writer_thread.wait()

    def off_simulate(self):
        for name, thread in list(getattr(self, 'thread_dict', {}).items()):
            if thread and thread.isRunning():
                if hasattr(thread, 'stop'):
                    thread.stop()
                thread.quit()
                thread.deleteLater()
            self.thread_dict.pop(name, None)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window_id = 'StrikeMachine_Instance'
    shared_mem_id = 'StrikeMachine_SharedMem'
    
    semaphore = QSystemSemaphore(window_id, 1)
    semaphore.acquire()
    
    if sys.platform != 'win32':
        nix_fix_shared_mem = QSharedMemory(shared_mem_id)
        if nix_fix_shared_mem.attach():
            nix_fix_shared_mem.detach()
    
    shared_memory = QSharedMemory(shared_mem_id)
    
    if shared_memory.attach():
        is_running = True
    else:
        shared_memory.create(1)
        is_running = False
    
    semaphore.release()
    
    if is_running:
        sys.exit(1)

    window = StrikeMachine()
    window.show()

    def center_window(win):
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - win.width()) // 2
        y = (screen.height() - win.height()) // 2
        win.move(x, y)

    center_window(window)
    
    def cleanup():
        try:
            # winsdow.export_all_tables_to_excel_btn()
            # window._database_auto_check()
            window._close_event_cleanup()
        except:
            pass

    atexit.register(cleanup)
    
    sys.exit(app.exec())