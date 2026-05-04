# Constants
# Các hằng số
import sys
from PySide6.QtCore import QMutex  # Import QMutex from PyQt5

class SystemState:
    """Thread-safe system state container with categorized attributes"""
    """Vùng chứa trạng thái hệ thống an toàn cho luồng với các thuộc tính được phân loại"""
    _instance = None
    _mutex = QMutex()
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SystemState, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize all attributes with thread-safe access"""
        """Khởi tạo tất cả các thuộc tính với quyền truy cập an toàn cho luồng"""
        # Robot Position Data
        # Dữ liệu vị trí robot
        self._moving_status = None
        self._dis = 0.0
        self._total_time_count = None # "00:00:00"
        self._grn_light = 0
        self._ylw_light = 1
        self._red_light = 2
        self._buzz_light = 3

        # System States
        # Trạng thái hệ thống
        self._presser_toggle = None
        self._ready_status = True
        self._manual = True
        self._auto = False
        self._pause = False
        self._data_put = False
        self._stop_run = False
        self._cur_step = None
        
        # PLC Parameters
        # Tham số PLC
        self._db_number = 1
        self._db_size = 256
        self._start_offset = 0
        self._bit_offset = 1
        self._presser_add = 6
        self._light_alarm_add = 272
        self._value = 1
        self._sv_temperature = 0
        self._sv_pressure = 0
        self._start_address = 2 
        self._plc_client_1 = None
        self._plc_client_2 = None
        self._plc_client_3 = None
        self._plc_client_4 = None
        self._plc_client_5 = None
        self._plc_client_6 = None
        self._plc_client_7 = None
        self._plc_client_8 = None
        self._data_group_index = 0
        self._db_data_recv = {
            
        }
        self._db_data_send = {
            
        }

        # Database System
        self._total_unit_today = 0
        self._day_of_week = 0
        self._total_issue_today = 0
        self._unit_per_day_in_week = [2, 3, 4, 5, 6, 7, 8] # 0,0,0,0,0,0,0
        self._issue_per_day_in_week = [2, 3, 4, 5, 6, 7, 8] # 0,0,0,0,0,0,0

    def _get_attr(self, attr_name):
        """Thread-safe getter"""
        """Trình lấy an toàn cho luồng"""
        self._mutex.lock()
        try:
            return getattr(self, f"_{attr_name}")
        finally:
            self._mutex.unlock()

    def _set_attr(self, attr_name, value):
        """Thread-safe setter"""
        """Trình đặt an toàn cho luồng"""
        self._mutex.lock()
        try:
            setattr(self, f"_{attr_name}", value)
        finally:
            self._mutex.unlock()

    @property
    def grn_light(self): return self._get_attr('grn_light')
    @grn_light.setter
    def grn_light(self, value): self._set_attr('grn_light', value)

    @property
    def ylw_light(self): return self._get_attr('ylw_light')
    @ylw_light.setter
    def ylw_light(self, value): self._set_attr('ylw_light', value)

    @property
    def red_light(self): return self._get_attr('red_light')
    @red_light.setter
    def red_light(self, value): self._set_attr('red_light', value)

    @property
    def buzz_light(self): return self._get_attr('buzz_light')
    @buzz_light.setter
    def buzz_light(self, value): self._set_attr('buzz_light', value)

    # State Properties
    # Thuộc tính trạng thái
    @property
    def ready_status(self): return self._get_attr('ready_status')
    @ready_status.setter
    def ready_status(self, value): self._set_attr('ready_status', value)

    @property
    def pause(self): return self._get_attr('pause')
    @pause.setter
    def pause(self, value): self._set_attr('pause', value)

    @property
    def cur_mode(self): return self._get_attr('cur_mode')
    @cur_mode.setter
    def cur_mode(self, value): self._set_attr('cur_mode', value)

    # @property
    # def cur_alrm(self) -> str: return self._get_attr('cur_alrm')
    # @cur_alrm.setter
    # def cur_alrm(self, value: str): self._set_attr('cur_alrm', str(value) if value is not None else None)

    @property
    def cur_alrm(self): return self._get_attr('cur_alrm')
    @cur_alrm.setter
    def cur_alrm(self, value): self._set_attr('cur_alrm', value)

    @property
    def cur_step(self): return self._get_attr('cur_step')
    @cur_step.setter
    def cur_step(self, value): self._set_attr('cur_step', value)

    # PLC Properties
    # Thuộc tính PLC
    @property
    def db_number(self): return self._get_attr('db_number')
    @db_number.setter
    def db_number(self, value): self._set_attr('db_number', value)
    
    @property
    def db_size(self): return self._get_attr('db_size')
    @db_size.setter
    def db_size(self, value): self._set_attr('db_size', value)
    
    @property
    def start_offset(self): return self._get_attr('start_offset')
    @start_offset.setter
    def start_offset(self, value): self._set_attr('start_offset', value)
    
    @property
    def bit_offset(self): return self._get_attr('bit_offset')
    @bit_offset.setter
    def bit_offset(self, value): self._set_attr('bit_offset', value)

    @property
    def plc_client_1(self): return self._get_attr('plc_client_1')
    @plc_client_1.setter
    def plc_client_1(self, value): self._set_attr('plc_client_1', value)

    @property
    def plc_client_2(self): return self._get_attr('plc_client_2')
    @plc_client_2.setter
    def plc_client_2(self, value): self._set_attr('plc_client_2', value)

    @property
    def plc_client_3(self): return self._get_attr('plc_client_3')
    @plc_client_3.setter
    def plc_client_3(self, value): self._set_attr('plc_client_3', value)

    @property
    def plc_client_4(self): return self._get_attr('plc_client_4')
    @plc_client_4.setter
    def plc_client_4(self, value): self._set_attr('plc_client_4', value)

    @property
    def plc_client_5(self): return self._get_attr('plc_client_5')
    @plc_client_5.setter
    def plc_client_5(self, value): self._set_attr('plc_client_5', value)

    @property
    def plc_client_6(self): return self._get_attr('plc_client_6')
    @plc_client_6.setter
    def plc_client_6(self, value): self._set_attr('plc_client_6', value)

    @property
    def plc_client_7(self): return self._get_attr('plc_client_7')
    @plc_client_7.setter
    def plc_client_7(self, value): self._set_attr('plc_client_7', value)

    @property
    def plc_client_8(self): return self._get_attr('plc_client_8')
    @plc_client_8.setter
    def plc_client_8(self, value): self._set_attr('plc_client_8', value)

    @property
    def query_status(self): return self._get_attr('query_status')
    @query_status.setter
    def query_status(self, value): self._set_attr('query_status', value)

    @property
    def presser_add(self): return self._get_attr('presser_add')
    @presser_add.setter
    def presser_add(self, value): self._set_attr('presser_add', value)

    @property
    def light_alarm_add(self): return self._get_attr('light_alarm_add')
    @light_alarm_add.setter
    def light_alarm_add(self, value): self._set_attr('light_alarm_add', value)

    @property
    def value(self): return self._get_attr('value')
    @value.setter
    def value(self, value): self._set_attr('value', value)
    
    @property
    def start_address(self): return self._get_attr('start_address')
    @start_address.setter
    def start_address(self, value): self._set_attr('start_address', value)

    # Database System
    @property
    def total_unit_today(self): return self._get_attr('total_unit_today')
    @total_unit_today.setter
    def total_unit_today(self, value): self._set_attr('total_unit_today', value)

    @property
    def day_of_week(self): return self._get_attr('day_of_week')
    @day_of_week.setter
    def day_of_week(self, value): self._set_attr('day_of_week', value)

    @property
    def total_issue_today(self): return self._get_attr('total_issue_today')
    @total_issue_today.setter
    def total_issue_today(self, value): self._set_attr('total_issue_today', value)

    @property
    def unit_per_day_in_week(self): return self._get_attr('unit_per_day_in_week')
    @unit_per_day_in_week.setter
    def unit_per_day_in_week(self, value): self._set_attr('unit_per_day_in_week', value)
    
    @property
    def issue_per_day_in_week(self): return self._get_attr('issue_per_day_in_week')
    @issue_per_day_in_week.setter
    def issue_per_day_in_week(self, value): self._set_attr('issue_per_day_in_week', value)


# Create singleton instance 
# Tạo instance singleton
syss = SystemState()