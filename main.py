# pyside6-uic tech_link_theme.ui -o tech_link_theme.py
# pyside6-rcc Icon.qrc -o Icon_rc.py

# pyinstaller --onefile --name="Packing Demo" --icon=icons\Download_Icons\robotic-arm.ico --add-binary "lib\snap7.dll;." --add-data "gifs;gifs" main.py
# pyinstaller --onefile --noconsole --name="Packing App" --icon=icons\Download_Icons\robotic-arm.ico --add-binary "lib\snap7.dll;." --add-data "gifs;gifs" main.py

import sys
import random
import os
import re
import time 
import psutil
import platform
import subprocess
import logging
import logging.handlers
import sqlite3
import socket
import atexit
import snap7
import snap7.util as util
import struct
from dataclasses import dataclass
from PySide6.QtCore import (Qt, QTimer, QMutex, 
                            QSettings, QDateTime, QCoreApplication,
                            QEvent, QUrl, QSharedMemory, 
                            QSystemSemaphore, QThread, QTranslator)
from PySide6.QtGui import QPalette, QColor, QPainter, QFont, QGuiApplication
from PySide6.QtWidgets import (
    QWidget, QGridLayout, QFormLayout, QPushButton, QHBoxLayout, QVBoxLayout, QHeaderView, 
    QComboBox, QCheckBox, QGroupBox, QLabel,QMainWindow, QApplication, QGraphicsProxyWidget
)
from PySide6.QtCharts import (
    QChart, QChartView,
    QLineSeries, QSplineSeries, QScatterSeries,
    QAreaSeries, QPieSeries,
    QStackedBarSeries, QBarSet,
    QValueAxis
)
from tech_link_theme import Ui_MainWindow
from Custom_Widgets import * #type: ignore
from spline_chart import SplineChartWidget
from Custom_Chart_Widgets import CustomChartWidget
from System_Data import syss
from Data_Simulator import DataSimulator

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"
os.environ["QT_FONT_DPI"] = "96"

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(os.path.dirname(__file__))
    
    return os.path.join(base_path, relative_path)

@dataclass
class DBField:
    offset: int      # byte offset trong DB
    size: int        # 4 = REAL (float), 2 = INT, 1 = BYTE
    data_type: str   # 'REAL', 'INT'

# Map từng SV theo offset trong DB layout của PLC
DB_SV_MAP = {
    # Row         offset  size  type
    "pressure":   DBField(0,    4,  "REAL"),   # A=0,  B=40, C=80
    "temp":       DBField(4,    4,  "REAL"),
    "front_temp": DBField(8,    4,  "REAL"),
    "mid_temp":   DBField(12,   4,  "REAL"),
    "end_temp":   DBField(16,   4,  "REAL"),
    "gas_fill":   DBField(20,   4,  "REAL"),
    "gas_hold":   DBField(24,   4,  "REAL"),
    "gas_bleed":  DBField(28,   4,  "REAL"),
    "refuel_start": DBField(32, 4,  "REAL"),
    "refuel_end":   DBField(36, 4,  "REAL"),
    # Mỗi channel A/B/C cách nhau 40 bytes
}

CHANNEL_OFFSET = {
    "A": 0,
    "B": 40,
    "C": 80,
}

class PLCWriter:
    def __init__(self, ip: str, rack: int = 0, slot: int = 1, db_number: int = 1):
        self.client = snap7.client.Client()
        self.ip = ip
        self.rack = rack
        self.slot = slot
        self.db_number = db_number
        self.db_size = 120  # 3 channel x 40 bytes

    def connect(self):
        self.client.connect(self.ip, self.rack, self.slot)

    def disconnect(self):
        self.client.disconnect()

    def _pack_real(self, value: float) -> bytes:
        return struct.pack(">f", value)  # Big-endian float (S7 format)

    def write_all_sv(self, sv_data: dict):
        """
        sv_data = {
            "A": {
                "pressure": 3.5,
                "temp": 0.0,
                "front_temp": 0.0,
                ...
            },
            "B": { ... },
            "C": { ... },
        }
        """
        # Tạo buffer toàn bộ DB
        buffer = bytearray(self.db_size)

        for channel, fields in sv_data.items():
            ch_offset = CHANNEL_OFFSET[channel]
            for field_name, value in fields.items():
                field = DB_SV_MAP[field_name]
                offset = ch_offset + field.offset
                packed = self._pack_real(float(value))
                buffer[offset:offset + field.size] = packed

        # Ghi 1 lần duy nhất
        self.client.db_write(self.db_number, 0, buffer)

class StrikeMachine(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._init_app_data()
        self._init_timer()
        self._init_group_object()
        self._init_list_unit()
        loadJsonStyle(self, self.ui) #type: ignore
        self._create_charts()
        self._simulate_data()
        self._setup_table()
        self._paint_pv_obj("#E53935")
        self._paint_sv_obj("#43A047")
        self._setup_btn_signals()
        self.current_unit = 0
        self.ui.home_page_btn.click()

    def _init_app_data(self):
        self.plc_clients = [
                            syss.plc_client_1, 
                            syss.plc_client_2, 
                            syss.plc_client_3, 
                            syss.plc_client_4, 
                            syss.plc_client_5, 
                            syss.plc_client_6
                            ]
        
        self.thread_dict = {}

        self.group_a_dict = {
            "Refueling Start SV A": 10.0,
            "Refueling End SV A": 20.0,
            "Filling Time SV A": 5.0,
            "G.Holding Time SV A": 3.0,
            "Bleeding Time SV A": 12.0,
            "Pressure PV A": 30.0,
            "Pressure SV A": 45.0,

            "Air Inlet High Alm A": 240.0,
            "Air Inlet PV Temp A": 0.0,
            "Air Inlet Low Alm A": 200.0,
            "Air Inlet SV Temp A": 0.0,
            "Air Inlet Offset A": 0.0,

            "Front High Alm A": 240.0,
            "Front PV Temp A": 0.0,
            "Front Low Alm A": 200.0,
            "Front SV Temp A": 0.0,
            "Front Offset A": 0.0,

            "Middle High Alm A": 240.0,
            "Middle PV Temp A": 0.0,
            "Middle Low Alm A": 200.0,
            "Middle SV Temp A": 0.0,
            "Middle Offset A": 0.0,

            "Back High Alm A": 243.0,
            "Back PV Temp A": 0.0,
            "Back Low Alm A": 203.0,
            "Back SV Temp A": 0.0,
            "Back Offset A": 0.0
        }
        self.group_b_dict = {
            "Refueling Start B": 0.0,
            "Refueling End B": 0.0,
            "Filling Time B": 0.0,
            "G.Holding Time B": 0.0,
            "Bleeding Time B": 0.0,
            "Pressure PV B": 0.0,
            "Pressure SV B": 0.0,

            "Air Inlet High Alm B": 0.0,
            "Air Inlet PV Temp B": 0.0,
            "Air Inlet Low Alm B": 0.0,
            "Air Inlet SV Temp B": 0.0,
            "Air Inlet Offset B": 0.0,

            "Front High Alm B": 0.0,
            "Front PV Temp B": 0.0,
            "Front Low Alm B": 0.0,
            "Front SV Temp B": 0.0,
            "Front Offset B": 0.0,

            "Middle High Alm B": 0.0,
            "Middle PV Temp B": 0.0,
            "Middle Low Alm B": 0.0,
            "Middle SV Temp B": 0.0,
            "Middle Offset B": 0.0,

            "Back High Alm B": 0.0,
            "Back PV Temp B": 0.0,
            "Back Low Alm B": 0.0,
            "Back SV Temp B": 0.0,
            "Back Offset B": 0.0
        }
        self.group_c_dict = {
            "Refueling Start C": 0.0,
            "Refueling End C": 0.0,
            "Filling Time C": 0.0,
            "G.Holding Time C": 0.0,
            "Bleeding Time C": 0.0,
            "Pressure PV C": 0.0,
            "Pressure SV C": 0.0,

            "Air Inlet High Alm C": 0.0,
            "Air Inlet PV Temp C": 0.0,
            "Air Inlet Low Alm C": 0.0,
            "Air Inlet SV Temp C": 0.0,
            "Air Inlet Offset C": 0.0,

            "Front High Alm C": 0.0,
            "Front PV Temp C": 0.0,
            "Front Low Alm C": 0.0,
            "Front SV Temp C": 0.0,
            "Front Offset C": 0.0,

            "Middle High Alm C": 0.0,
            "Middle PV Temp C": 0.0,
            "Middle Low Alm C": 0.0,
            "Middle SV Temp C": 0.0,
            "Middle Offset C": 0.0,

            "Back High Alm C": 0.0,
            "Back PV Temp C": 0.0,
            "Back Low Alm C": 0.0,
            "Back SV Temp C": 0.0,
            "Back Offset C": 0.0

        }

        self.default_temp_room = 25.0
        
    def _init_timer(self):
        self.all_timer = []

        self.timer_stacked_pressure_page = QTimer()
        self.all_timer.append(self.timer_stacked_pressure_page)

    def _init_group_object(self):
        # self.pressure_state_obj = []
        # for i in range(10):
        #     obj = getattr(self.ui, f"pressure_sv_a_{i}")
        #     self.pressure_state_obj.append(obj)
        self.pressure_a_pv_obj = tuple(
            getattr(self.ui, f"pressure_pv_a_{i}") for i in range(1, 11)
        )

        self.pressure_b_pv_obj = tuple(
            getattr(self.ui, f"pressure_pv_b_{i}") for i in range(1, 11)
        )

        self.pressure_c_pv_obj = tuple(
            getattr(self.ui, f"pressure_pv_c_{i}") for i in range(1, 11)
        )

        self.pressure_a_sv_obj = tuple(
            getattr(self.ui, f"pressure_sv_a_{i}") for i in range(1, 11)
        )

        self.pressure_b_sv_obj = tuple(
            getattr(self.ui, f"pressure_sv_b_{i}") for i in range(1, 11)
        )

        self.pressure_c_sv_obj = tuple(
            getattr(self.ui, f"pressure_sv_c_{i}") for i in range(1, 11)
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
                    color: {color};}}""")
            
    def _paint_sv_obj(self, color):
        for obj in self.pressure_a_sv_obj + self.pressure_b_sv_obj + self.pressure_c_sv_obj + self.temp_offset_obj + self.temp_h_alm_obj + self.temp_l_alm_obj + self.temp_sv_obj:
            obj.setStyleSheet(f"""
                QDoubleSpinBox {{
                    color: {color};}}
                QDoubleSpinBox:hover {{
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
        self.chart_temp       = CustomChartWidget("Oven",    num_series=2, y_label="°C", type_unit="temp",     setting=True, chart_font=font)
        self.chart_pressure_a = CustomChartWidget("Group A", num_series=5, y_label="°C", type_unit="pressure", setting=True, chart_font=font)
        self.chart_pressure_b = CustomChartWidget("Group B", num_series=5, y_label="°C", type_unit="pressure", setting=True, chart_font=font)
        self.chart_pressure_c = CustomChartWidget("Group C", num_series=5, y_label="°C", type_unit="pressure", setting=True, chart_font=font)

        self.chart_temp.btn_setting.clicked.connect(self.temperature_page_btn)
        self.chart_pressure_a.btn_setting.clicked.connect(self.ui.home_page_btn.click)
        self.chart_pressure_b.btn_setting.clicked.connect(self.ui.home_page_btn.click)
        self.chart_pressure_c.btn_setting.clicked.connect(self.ui.home_page_btn.click)

        self.ui.card_temperature.addWidget(self.chart_temp)
        self.ui.card_pressure_1.addWidget(self.chart_pressure_a)
        self.ui.card_pressure_2.addWidget(self.chart_pressure_b)
        self.ui.card_pressure_3.addWidget(self.chart_pressure_c)

    #############################------ Button Function Setup ------###########################
    def _setup_btn_signals(self):
        ### Left side menu button
        self.ui.home_page_btn.clicked.connect(self.pressure_page_btn)
        self.ui.chart_page_btn.clicked.connect(self.home_page_btn)
        self.ui.device_page_btn.clicked.connect(self.device_page_btn)
        self.ui.history_page_btn.clicked.connect(self.history_page_btn)

        self.ui.next_group_page_btn.clicked.connect(self.next_previous_pressure_page)
        self.ui.previus_group_page_btn.clicked.connect(self.next_previous_pressure_page)

        self.ui.temp_unit_selection_combox.currentIndexChanged.connect(self._set_cur_unit)
        # self.ui.back_home_btn_4.clicked.connect(self.ui.home_page_btn.click)

        self.ui.plc_io_btn.clicked.connect(self.i_o_page_btn)

        self.ui.heat_btn_a.clicked.connect(lambda checked: self.on_heat_btn_clicked("A", checked))
        self.ui.heat_btn_b.clicked.connect(lambda checked: self.on_heat_btn_clicked("B", checked))
        self.ui.heat_btn_c.clicked.connect(lambda checked: self.on_heat_btn_clicked("C", checked))
        
        # self.ui.vacuum_btn_a.clicked.connect(self.)
        # self.ui.vacuum_btn_b.clicked.connect(self.)
        # self.ui.vacuum_btn_c.clicked.connect(self.)
        
        # self.ui.refuel_btn_a.clicked.connect(self.)
        # self.ui.refuel_btn_b.clicked.connect(self.)
        # self.ui.refuel_btn_c.clicked.connect(self.)
        
        # self.ui.reset_cycle_a_btn.clicked.connect(self.)
        # self.ui.reset_cycle_b_btn.clicked.connect(self.)
        # self.ui.reset_cycle_c_btn.clicked.connect(self.)

    def _setup_table(self):
        header = self.ui.list_history.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        for i in range(1, header.count()):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

    def home_page_btn(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.menu_page)
        # print(f"{self.ui.stackedWidget.currentWidget()}")

    def pressure_page_btn(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.temp_press_page)
        self.ui.stackedWidget.setCurrentWidget(self.ui.pressure_page)
        # print(f"{self.ui.stackedWidget.currentWidget()}")

    def temperature_page_btn(self):
        self.ui.home_page_btn.click()
        self.ui.stackedWidget.setCurrentWidget(self.ui.temperature_page)
        
    def device_page_btn(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.device_page)
        self.connection_page_btn()

    def connection_page_btn(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.connection_page)
    
    def i_o_page_btn(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.i_o_page)
    
    def history_page_btn(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.history_page)

    # def (self):
    
    def next_previous_pressure_page(self):
        index = self.ui.stackedWidget.currentIndex()
        if index == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
        elif index == 1:
            self.ui.stackedWidget.setCurrentIndex(0)

    # def (self):
    
    def _simulate_data(self):
        self.setup_threads()

    def setup_threads(self):
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

    def on_heat_btn_clicked(self, channel: str, checked: bool):
        simulator = self.thread_dict.get("data_simulator")
        if simulator is None:
            return

        if checked:
            # Lấy SV hiện tại từ UI
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

    def _data_group_filter(self, list_group_a_recv, list_group_b_recv, list_group_c_recv):
        if not isinstance(list_group_a_recv, list) and not isinstance(list_group_b_recv, list) and not isinstance(list_group_c_recv, list):
            return
        pv_avg = (list_group_a_recv[1] + list_group_b_recv[1] + list_group_c_recv[1]) / 3
        temp_values = [((self.ui.pressure_sv_a_2.value() + self.ui.pressure_sv_b_2.value() + self.ui.pressure_sv_c_2.value())/3),
                    self.for_display_temp(pv_avg)]
        self.chart_temp.append_data(temp_values)
        self.temp_pv_obj[0].setValue(self.for_display_temp(pv_avg))
        
        group_a_values = [self.ui.pressure_sv_a_2.value(),
                            self.for_display_temp(list_group_a_recv[2]),
                            self.for_display_temp(list_group_a_recv[3]),
                            self.for_display_temp(list_group_a_recv[4]),
                            list_group_a_recv[0]]
        self.chart_pressure_a.append_data(group_a_values)

        self.group_a_dict["Air Inlet PV Temp A"] = list_group_a_recv[0]
        self.group_a_dict["Front PV Temp A"]     = list_group_a_recv[1]
        self.group_a_dict["Middle PV Temp A"]    = list_group_a_recv[2]
        self.group_a_dict["End PV Temp A"]       = list_group_a_recv[3]
        self.group_a_dict["Pressure PV A"]       = list_group_a_recv[4]
        self.temp_pv_obj[1].setValue(self.for_display_temp(list_group_a_recv[1]))

        group_b_values = [self.ui.pressure_sv_b_2.value(),
                        self.for_display_temp(list_group_b_recv[2]),
                        self.for_display_temp(list_group_b_recv[3]),
                        self.for_display_temp(list_group_b_recv[4]),
                        list_group_b_recv[0]
                        ]
        self.chart_pressure_b.append_data(group_b_values)

        self.group_b_dict["Air Inlet PV Temp B"] = list_group_b_recv[0]
        self.group_b_dict["Front PV Temp B"]     = list_group_b_recv[1]
        self.group_b_dict["Middle PV Temp B"]    = list_group_b_recv[2]
        self.group_b_dict["End PV Temp B"]       = list_group_b_recv[3]
        self.group_b_dict["Pressure PV B"]       = list_group_b_recv[4]
        self.temp_pv_obj[2].setValue(self.for_display_temp(list_group_b_recv[1]))

        group_c_values = [self.ui.pressure_sv_c_2.value(),
                        self.for_display_temp(list_group_c_recv[2]),
                        self.for_display_temp(list_group_c_recv[3]),
                        self.for_display_temp(list_group_c_recv[4]),
                        list_group_c_recv[0]]
        self.chart_pressure_c.append_data(group_c_values)

        self.group_c_dict["Air Inlet PV Temp C"] = list_group_c_recv[0]
        self.group_c_dict["Front PV Temp C"]     = list_group_c_recv[1]
        self.group_c_dict["Middle PV Temp C"]    = list_group_c_recv[2]
        self.group_c_dict["End PV Temp C"]       = list_group_c_recv[3]
        self.group_c_dict["Pressure PV C"]       = list_group_c_recv[4]
        self.temp_pv_obj[3].setValue(self.for_display_temp(list_group_c_recv[1]))

        self.timer_stacked_pressure_page.singleShot(0, lambda: self._set_pv_data(list_group_a_recv, list_group_b_recv, list_group_c_recv))

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

    def _set_cur_unit(self, index):
        index = self.ui.temp_unit_selection_combox.currentIndex()
        for i in range(len(self.cel_fah_change)):
            self.cel_fah_change[i].setCurrentIndex(index)
        self.current_unit = index
        self._set_sv_unit_obj()
        self._set_chart_unit()

    def _set_sv_unit_obj(self):
        for i in range(4):
            self.pressure_a_sv_obj[i].setValue(self.convert_cel_fah(self.pressure_a_sv_obj[i].value()))
            self.pressure_b_sv_obj[i].setValue(self.convert_cel_fah(self.pressure_b_sv_obj[i].value()))
            self.pressure_c_sv_obj[i].setValue(self.convert_cel_fah(self.pressure_c_sv_obj[i].value()))

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

    def convert_cel_fah(self, temp):
        if self.current_unit == 1:
            return temp * 9/5 + 32
        elif self.current_unit == 0:
            return (temp - 32) * 5/9

    def cal_fah_to_cel(self, temp):
        if self.current_unit == 1:
            return (temp - 32) * 5/9
        return temp

    def apply_group_to_ui(self, group_dict: dict, widgets: list):
        for widget, value in zip(widgets, group_dict.values()):
            widget.blockSignals(True)
            try:
                if hasattr(widget, 'setValue'):
                    widget.setValue(float(value))
            finally:
                widget.blockSignals(False)

    def update_all_charts(self):
        temp_values = [230,
                    222.5 + random.uniform(-0.5, 2)]
        self.chart_temp.append_data(temp_values)

        pressure_values = [250,
                        220 + random.uniform(-1, 2),
                         110 + random.uniform(-1, 2),
                         60 + random.uniform(-1, 2),
                         25 + random.uniform(-1, 1)]
        self.chart_pressure_a.append_data(pressure_values)

        voltage_values = [250,
                        220 + random.uniform(-1, 2),
                         110 + random.uniform(-1, 2),
                         60 + random.uniform(-1, 2),
                         25 + random.uniform(-1, 1)]
        self.chart_pressure_b.append_data(voltage_values)

        speed_values = [250,
                        220 + random.uniform(-1, 2),
                         110 + random.uniform(-1, 2),
                         60 + random.uniform(-1, 2),
                         25 + random.uniform(-1, 1)]
        self.chart_pressure_c.append_data(speed_values)

    def closeEvent(self, event):
        """Dừng tất cả timer khi đóng cửa sổ"""
        # self.simulation_timer.stop()
        self._close_event_cleanup()
        # Dừng update của từng chart
        event.accept()

    def _close_event_cleanup(self):
        """Properly cleanup all threads and timers"""
        try:
            # Stop all threads gracefully
            for name, thread in list(getattr(self, 'thread_dict', {}).items()):
                try:
                    if thread and thread.isRunning():
                        # Signal thread to stop if it has a stop method
                        if hasattr(thread, 'stop'):
                            thread.stop()
                        
                        # Request thread to quit
                        thread.quit()
                        
                        # Wait for thread to finish (up to 2 seconds)
                        if not thread.wait(2000):
                            # If graceful stop didn't work, force terminate
                            thread.terminate()
                            # Wait for termination
                            if not thread.wait(1000):
                                print(f"Warning: Thread {name} did not terminate properly")
                        
                        # Delete thread object
                        thread.deleteLater()
                    
                    # Remove from dict
                    self.thread_dict.pop(name, None)
                    
                except Exception as e:
                    print(f"Error stopping thread {name}: {str(e)}")
                    self.thread_dict.pop(name, None)
            
            # Stop all timers
            for timer in getattr(self, 'all_timer', []):
                try:
                    if timer.isActive():
                        timer.stop()
                    timer.deleteLater()
                except Exception as e:
                    print(f"Error stopping timer: {str(e)}")
            
            self.all_timer.clear()
            
            # Process events to allow Qt to clean up
            QCoreApplication.processEvents()
            
        except Exception as e:
            print(f"Error during cleanup: {str(e)}")

if __name__ == "__main__":
    # QApplication.setAttribute(Qt.AA_DisableHighDpiScaling, True)
    # QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    # font = QFont("Segoe UI", 25)
    # font.setWeight(QFont.Weight.Bold)
    # app.setFont(font)
    window = StrikeMachine()
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
    def center_window(win):
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - win.width()) // 2
        y = (screen.height() - win.height()) // 2
        win.move(x, y)

    window.show()
    center_window(window)
    
    def cleanup():
        try:
            # window.export_all_tables_to_excel_btn()
            # window._database_auto_check()
            # window.logger.info("Auto-saved before exit")
            window._close_event_cleanup()
        except:
            pass
    print(f"Width: {window.width()}, Height: {window.height()}")
    atexit.register(cleanup)
    
    sys.exit(app.exec_())