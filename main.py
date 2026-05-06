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
import struct
import snap7
import plc_data as db_data
from snap7.util import set_bool, get_real, get_dint, get_int, get_bool, get_string
from dataclasses import dataclass
from PySide6.QtCore import (Qt, QTimer, QMutex, 
                            QSettings, QDateTime, QCoreApplication,
                            QEvent, QUrl, QSharedMemory, 
                            QSystemSemaphore, QThread, QTranslator, Slot)
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
from query_plc_thread import PLCWorker, PLCState

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"
os.environ["QT_FONT_DPI"] = "96"

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS #type: ignore
    else:
        base_path = os.path.abspath(os.path.dirname(__file__))
    
    return os.path.join(base_path, relative_path)

class PLCWriter:
    def __init__(self, ip: str, rack: int = 0, slot: int = 1, db_number: int = 1):
        self.client = snap7.client.Client()
        self.ip = ip
        self.rack = rack
        self.slot = slot
        self.db_number = db_number
        self.db_size = 580  # String[254] kết thúc ~578

    def connect(self):
        self.client.connect(self.ip, self.rack, self.slot)

    def disconnect(self):
        self.client.disconnect()

    def is_connected(self) -> bool:
        return self.client.get_connected()

    # ── Pack helpers ──────────────────────────────────────────────────
    @staticmethod
    def _pack_real(value: float) -> bytes:
        return struct.pack(">f", value)

    @staticmethod
    def _pack_dint(value: int) -> bytes:
        return struct.pack(">i", value)

    @staticmethod
    def _pack_int(value: int) -> bytes:
        return struct.pack(">h", value)

    # ── Write đơn lẻ 1 field (read-modify-write) ─────────────────────
    def write_field(self, field_name: str, value) -> bool:
        """
        Ghi 1 field bất kỳ. An toàn vì dùng read-modify-write.
        Trả về True nếu thành công.
        """
        if field_name not in WRITABLE_FIELDS:
            raise ValueError(f"'{field_name}' không nằm trong danh sách WRITABLE_FIELDS")

        field = DB_MAP[field_name]

        if field.data_type == "BOOL":
            byte_idx, bit_idx = BOOL_BIT_INDEX[field_name]
            # Đọc byte hiện tại để không mất bit khác
            raw = self.client.db_read(self.db_number, byte_idx, 1)
            set_bool(raw, 0, bit_idx, bool(value))
            self.client.db_write(self.db_number, byte_idx, raw)

        else:
            if field.data_type == "REAL":
                packed = self._pack_real(float(value))
            elif field.data_type == "DINT":
                packed = self._pack_dint(int(value))
            elif field.data_type == "INT":
                packed = self._pack_int(int(value))
            else:
                raise TypeError(f"Không hỗ trợ write type: {field.data_type}")

            self.client.db_write(self.db_number, field.offset, bytearray(packed))

        return True

    # ── Write nhiều field cùng lúc (batch) ───────────────────────────
    def write_fields(self, data: dict) -> dict:
        """
        Ghi nhiều field một lúc. Read toàn DB → patch → write lại.

        data = {
            "P1_TemperatureSetting": 180.0,
            "P1_AirFillingTime": 5000,
            "P1_CountTimes": 10,
            "P1_StartHeat": True,
            ...
        }
        Trả về dict {field_name: success/error}
        """
        # Validate trước
        invalid = [k for k in data if k not in WRITABLE_FIELDS]
        if invalid:
            raise ValueError(f"Các field không được phép write: {invalid}")

        # Đọc toàn bộ DB hiện tại để patch an toàn
        raw = bytearray(self.client.db_read(self.db_number, 0, self.db_size))
        results = {}

        for field_name, value in data.items():
            try:
                field = DB_MAP[field_name]

                if field.data_type == "BOOL":
                    byte_idx, bit_idx = BOOL_BIT_INDEX[field_name]
                    set_bool(raw, byte_idx, bit_idx, bool(value))

                elif field.data_type == "REAL":
                    packed = self._pack_real(float(value))
                    raw[field.offset:field.offset + 4] = packed

                elif field.data_type == "DINT":
                    packed = self._pack_dint(int(value))
                    raw[field.offset:field.offset + 4] = packed

                elif field.data_type == "INT":
                    packed = self._pack_int(int(value))
                    raw[field.offset:field.offset + 2] = packed

                results[field_name] = "ok"

            except Exception as e:
                results[field_name] = f"error: {e}"

        # Chỉ write 1 lần duy nhất
        self.client.db_write(self.db_number, 0, raw)
        return results

    # ── Write theo Station (T0 / P1 / P2 / P3) ───────────────────────
    def write_station(self, station: str, params: dict) -> dict:
        """
        Ghi toàn bộ setting cho 1 station.

        station = "T0" | "P1" | "P2" | "P3"
        params  = {
            "TemperatureSetting": 180.0,
            "TempLimitHIGH": 190.0,
            ...
        }
        """
        prefixed = {f"{station}_{k}": v for k, v in params.items()}
        return self.write_fields(prefixed)

    # ── Context manager support ───────────────────────────────────────
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *args):
        self.disconnect()

class PLCReader:
    def __init__(self, ip: str, rack: int = 0, slot: int = 1, db_number: int = 1):
        self.client = snap7.client.Client()
        self.ip = ip
        self.rack = rack
        self.slot = slot
        self.db_number = db_number
        self.db_size = 580

    def connect(self):
        self.client.connect(self.ip, self.rack, self.slot)

    def disconnect(self):
        self.client.disconnect()

    def is_connected(self) -> bool:
        return self.client.get_connected()

    @staticmethod
    def _parse_field(raw: bytearray, field: DBField, field_name: str | None = None):
        if field.data_type == "REAL":
            return get_real(raw, field.offset)
        elif field.data_type == "DINT":
            return get_dint(raw, field.offset)
        elif field.data_type == "INT":
            return get_int(raw, field.offset)
        elif field.data_type == "BOOL":
            if field_name is None:
                raise ValueError("field_name is required for BOOL fields")
            byte_idx, bit_idx = BOOL_BIT_INDEX[field_name]
            return get_bool(raw, byte_idx, bit_idx)
        elif field.data_type == "STRING":
            return get_string(raw, field.offset)
        else:
            raise TypeError(f"Không hỗ trợ đọc type: {field.data_type}")

    # ── Read toàn bộ DB 1 lần ────────────────────────────────────────
    def read_all(self) -> dict:
        """
        Đọc toàn bộ DB, trả về dict đầy đủ tất cả fields.
        """
        raw = bytearray(self.client.db_read(self.db_number, 0, self.db_size))
        result = {}
        for field_name, field in DB_MAP.items():
            try:
                result[field_name] = self._parse_field(raw, field, field_name)
            except Exception as e:
                result[field_name] = f"error: {e}"
        return result

    # ── Read 1 field đơn lẻ ──────────────────────────────────────────
    def read_field(self, field_name: str):
        """
        Đọc 1 field theo tên.
        Chỉ đọc đúng số byte cần thiết → nhanh hơn read_all.
        """
        if field_name not in DB_MAP:
            raise KeyError(f"'{field_name}' không tồn tại trong DB_MAP")

        field = DB_MAP[field_name]

        if field.data_type == "BOOL":
            byte_idx, bit_idx = BOOL_BIT_INDEX[field_name]
            raw = bytearray(self.client.db_read(self.db_number, byte_idx, 1))
            # Tạo bytearray tạm để _parse_field không bị lệch offset
            temp = bytearray(byte_idx + 1)
            temp[byte_idx] = raw[0]
            return get_bool(temp, byte_idx, bit_idx)

        elif field.data_type == "STRING":
            # String cần đọc từ offset đến hết
            raw = bytearray(self.client.db_read(self.db_number, field.offset, field.size))
            temp = bytearray(field.offset + field.size)
            temp[field.offset:field.offset + field.size] = raw
            return get_string(temp, field.offset)

        else:
            raw = bytearray(self.client.db_read(self.db_number, field.offset, field.size))
            temp = bytearray(field.offset + field.size)
            temp[field.offset:field.offset + field.size] = raw
            return self._parse_field(temp, field, field_name)

    # ── Read nhiều field cùng lúc ─────────────────────────────────────
    def read_fields(self, field_names: list) -> dict:
        """
        Đọc nhiều field chỉ định. Đọc DB 1 lần duy nhất.

        field_names = ["P1_CurrentTemp1", "P1_CurrentPressureHose", "Bit_Alarm"]
        """
        invalid = [f for f in field_names if f not in DB_MAP]
        if invalid:
            raise KeyError(f"Các field không tồn tại: {invalid}")

        raw = bytearray(self.client.db_read(self.db_number, 0, self.db_size))
        return {
            name: self._parse_field(raw, DB_MAP[name], name)
            for name in field_names
        }

    # ── Read theo Station ─────────────────────────────────────────────
    def read_station(self, station: str) -> dict:
        """
        Đọc toàn bộ field của 1 station.
        station = "T0" | "P1" | "P2" | "P3"

        Trả về dict đã bỏ prefix, ví dụ:
        {"CurrentTemp1": 175.3, "CurrentPressureHose": 4.2, ...}
        """
        valid_stations = {"T0", "P1", "P2", "P3"}
        if station not in valid_stations:
            raise ValueError(f"Station phải là một trong: {valid_stations}")

        raw = bytearray(self.client.db_read(self.db_number, 0, self.db_size))
        prefix = f"{station}_"
        return {
            name[len(prefix):]: self._parse_field(raw, field, name)
            for name, field in DB_MAP.items()
            if name.startswith(prefix)
        }

    # ── Read chỉ Output (sensor readings) ────────────────────────────
    def read_outputs(self) -> dict:
        """
        Chỉ đọc vùng Output (offset 194~322) + Alarm.
        Dùng cho vòng lặp realtime chart — đọc ít byte nhất có thể.
        """
        OUTPUT_START = 192   # Bit_Alarm
        OUTPUT_SIZE  = 134   # đến hết P3_NumberTestTimes (322+2)

        raw_slice = bytearray(
            self.client.db_read(self.db_number, OUTPUT_START, OUTPUT_SIZE)
        )
        # Pad để offset gốc trong DB_MAP vẫn đúng
        raw = bytearray(OUTPUT_START) + raw_slice

        output_fields = [
            "Bit_Alarm",
            "T0_CurrentTemp",
            "P1_CurrentTemp1", "P1_CurrentTemp2", "P1_CurrentTemp3",
            "P1_CurrentPressureHose", "P1_CurrentPressureITV",
            "P1_AirFillingTime_Out", "P1_AirHoldingTime_Out", "P1_AirReleaseTime_Out",
            "P1_OilStartTime_Out", "P1_OilEndTime_Out", "P1_NumberTestTimes",
            "P2_CurrentTemp1", "P2_CurrentTemp2", "P2_CurrentTemp3",
            "P2_CurrentPressureHose", "P2_CurrentPressureITV",
            "P2_AirFillingTime_Out", "P2_AirHoldingTime_Out", "P2_AirReleaseTime_Out",
            "P2_OilStartTime_Out", "P2_OilEndTime_Out", "P2_NumberTestTimes",
            "P3_CurrentTemp1", "P3_CurrentTemp2", "P3_CurrentTemp3",
            "P3_CurrentPressureHose", "P3_CurrentPressureITV",
            "P3_AirFillingTime_Out", "P3_AirHoldingTime_Out", "P3_AirReleaseTime_Out",
            "P3_OilStartTime_Out", "P3_OilEndTime_Out", "P3_NumberTestTimes",
        ]
        return {
            name: self._parse_field(raw, DB_MAP[name], name)
            for name in output_fields
        }

    # ── Context manager ───────────────────────────────────────────────
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *args):
        self.disconnect()

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

        self.timer_stacked_pressure_page = QTimer()
        self.all_timer.append(self.timer_stacked_pressure_page)
        
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
    
    def _setup_plc_thread(self):
        """Thiết lập Thread và Worker cho PLC"""
        self.plc_thread = QThread()
        self.plc_worker = PLCWorker(
            ip="192.168.0.1", 
            db_number=1, 
            interval_ms=500
        )
        
        # Chuyển worker sang thread riêng
        self.plc_worker.moveToThread(self.plc_thread)

        # === KẾT NỐI SIGNAL ===
        self.plc_thread.started.connect(self.plc_worker.start)        # ← start() thay vì start_polling()

        self.plc_worker.data_received.connect(self._on_data)
        self.plc_worker.write_done.connect(self._on_write_done)
        self.plc_worker.state_changed.connect(self._on_state_changed)
        self.plc_worker.error.connect(self._on_error)

        # Nếu bạn vẫn muốn dùng Signal từ UI để ghi
        self.sig_write_field.connect(self.plc_worker.write)           # ← Đổi thành write()
        # self.sig_write_fields.connect(...)                          # Nếu cần batch thì giữ hoặc bỏ

        # Khởi động thread
        self.plc_thread.start()

    @Slot(dict)
    def on_plc_data_received(self, data: dict):
        """Đây là nơi nhận toàn bộ dữ liệu từ PLC"""
        
        # Cách an toàn nhất (dùng .get() để tránh lỗi nếu key không tồn tại)
        try:
            t0_data_list = [
                data.get('T0_CurrentTemp', 0.0)
            ]
            p1_data_list = [
                data.get('P1_CurrentTemp1', 0.0),
                data.get('P1_CurrentTemp2', 0.0),
                data.get('P1_CurrentTemp3', 0.0),
                data.get('P1_CurrentPressureHose', 0.0),
                data.get('P1_CurrentPressureITV', 0.0),
                data.get('P1_AirFillingTime_Out', 0),
                data.get('P1_AirHoldingTime_Out', 0),
                data.get('P1_AirReleaseTime_Out', 0),
                data.get('P1_OilStartTime_Out', 0),
                data.get('P1_OilEndTime_Out', 0),
                data.get('P1_NumberTestTimes', 0)
            ]
            p2_data_list = [
                data.get('P2_CurrentTemp1', 0.0),
                data.get('P2_CurrentTemp2', 0.0),
                data.get('P2_CurrentTemp3', 0.0),
                data.get('P2_CurrentPressureHose', 0.0),
                data.get('P2_CurrentPressureITV', 0.0),
                data.get('P2_AirFillingTime_Out', 0),
                data.get('P2_AirHoldingTime_Out', 0),
                data.get('P2_AirReleaseTime_Out', 0),
                data.get('P2_OilStartTime_Out', 0),
                data.get('P2_OilEndTime_Out', 0),
                data.get('P2_NumberTestTimes', 0)
            ]
            p3_data_list = [
                data.get('P3_CurrentTemp1', 0.0),
                data.get('P3_CurrentTemp2', 0.0),
                data.get('P3_CurrentTemp3', 0.0),
                data.get('P3_CurrentPressureHose', 0.0),
                data.get('P3_CurrentPressureITV', 0.0),
                data.get('P3_AirFillingTime_Out', 0),
                data.get('P3_AirHoldingTime_Out', 0),
                data.get('P3_AirReleaseTime_Out', 0),
                data.get('P3_OilStartTime_Out', 0),
                data.get('P3_OilEndTime_Out', 0),
                data.get('P3_NumberTestTimes', 0)
            ]
            alarm = data.get('Bit_Alarm', False)
            alarm_info = data.get('Alarm_Info', "")

            self._data_filter(t0_data_list, p1_data_list, p2_data_list, p3_data_list)

        except Exception as e:
            print("Lỗi khi xử lý dữ liệu PLC:", e)

    def _data_group_filter(self, list_group_a_recv, list_group_b_recv, list_group_c_recv):
        if not isinstance(list_group_a_recv, list) and not isinstance(list_group_b_recv, list) and not isinstance(list_group_c_recv, list):
            return
        pv_avg = (list_group_a_recv[0] + list_group_b_recv[1] + list_group_c_recv[1]) / 3
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

        self.temp_pv_obj[1].setValue(self.for_display_temp(list_group_a_recv[1]))

        group_b_values = [self.ui.pressure_sv_b_2.value(),
                        self.for_display_temp(list_group_b_recv[2]),
                        self.for_display_temp(list_group_b_recv[3]),
                        self.for_display_temp(list_group_b_recv[4]),
                        list_group_b_recv[0]
                        ]
        self.chart_pressure_b.append_data(group_b_values)
        self.temp_pv_obj[2].setValue(self.for_display_temp(list_group_b_recv[1]))

        group_c_values = [self.ui.pressure_sv_c_2.value(),
                        self.for_display_temp(list_group_c_recv[2]),
                        self.for_display_temp(list_group_c_recv[3]),
                        self.for_display_temp(list_group_c_recv[4]),
                        list_group_c_recv[0]]
        self.chart_pressure_c.append_data(group_c_values)
        self.temp_pv_obj[3].setValue(self.for_display_temp(list_group_c_recv[1]))

        self.timer_stacked_pressure_page.singleShot(0, lambda: self._set_pv_data(list_group_a_recv, list_group_b_recv, list_group_c_recv))

    def _data_filter(self, list_group_0_recv, list_group_a_recv, list_group_b_recv, list_group_c_recv):
        if not isinstance(list_group_a_recv, list) and not isinstance(list_group_b_recv, list) and not isinstance(list_group_c_recv, list):
            return
        pv_avg = list_group_0_recv[0]
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

        # Gán toàn bộ giá trị từ list_group_a_recv vào self.group_a_pv_dict (theo thứ tự key)
        pv_keys = list(self.group_a_pv_dict.keys())
        for i, key in enumerate(pv_keys):
            if i < len(list_group_a_recv):
                self.group_a_pv_dict[key] = list_group_a_recv[i]
        self.temp_pv_obj[1].setValue(self.for_display_temp(list_group_a_recv[1]))

        group_b_values = [self.ui.pressure_sv_b_2.value(),
                        self.for_display_temp(list_group_b_recv[2]),
                        self.for_display_temp(list_group_b_recv[3]),
                        self.for_display_temp(list_group_b_recv[4]),
                        list_group_b_recv[0]
                        ]
        self.chart_pressure_b.append_data(group_b_values)

        pv_keys_b = list(self.group_b_pv_dict.keys())
        for i, key in enumerate(pv_keys_b):
            if i < len(list_group_b_recv):
                self.group_b_pv_dict[key] = list_group_b_recv[i]
        self.temp_pv_obj[2].setValue(self.for_display_temp(list_group_b_recv[1]))


        group_c_values = [self.ui.pressure_sv_c_2.value(),
                        self.for_display_temp(list_group_c_recv[2]),
                        self.for_display_temp(list_group_c_recv[3]),
                        self.for_display_temp(list_group_c_recv[4]),
                        list_group_c_recv[0]]
        self.chart_pressure_c.append_data(group_c_values)

        pv_keys_c = list(self.group_c_pv_dict.keys())
        for i, key in enumerate(pv_keys_c):
            if i < len(list_group_c_recv):
                self.group_c_pv_dict[key] = list_group_c_recv[i]
        self.temp_pv_obj[3].setValue(self.for_display_temp(list_group_c_recv[1]))

        self.timer_stacked_pressure_page.singleShot(0, lambda: self._set_pv_data(list_group_a_recv, list_group_b_recv, list_group_c_recv))

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
                
    def update_clock(self):
        self.ui.date_displ.setDateTime(QDateTime.currentDateTime())
        
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