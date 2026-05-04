import time
import snap7
from snap7.util import get_real, get_bool, get_dint, get_int, get_word
from PySide6.QtCore import QThread, Signal
from System_Data import syss

class PLCQueryData(QThread):
    world_position_updated = Signal(float, float, float)
    emergency_stop_signal = Signal()
    pause_signal = Signal()
    sensor_signal = Signal()
    lost_connect_signal = Signal(str, str)
    disconnect_signal = Signal()

    def __init__(self, logger, dialog_notification):
        super().__init__()
        self.running = False
        self.plcc = None
        self.logger = logger
        self.dialog_notification = dialog_notification
        syss.query_status = True
        self.lamda_emg_signal = False
        self.count = 0
        self.disconnect_attemp = 0
        self.alarm_triggered = False  # Thêm cờ để theo dõi báo động
        self.logger.info("PLCQueryData initialized")

    def run(self):
        """Continuously read status from robot"""
        self.running = True
        self.logger.info("[PLCQueryData]: PLCQueryData thread started")
        timeout_disconnect = 0

        while self.running:
            self.plcc = syss.plc_client_1
            time.sleep(0.1)
            if not self.running:
                self.logger.info("[PLCQueryData]: self.running failed! Connection closed")
                break
                
            if not syss.query_status:
                self.count += 1
                if self.count == (275*3):
                    self.count = 0
                    self.logger.info(f"[PLCQueryData]: Query Status: {syss.query_status}")
                    timeout_disconnect+=1
                    if self.plcc.plc_reconnect():
                        syss.query_status = True
                        self.disconnect_attemp = 0
                        self.lamda_emg_signal = False
                        self.logger.info("[PLCQueryData]: Reconnected to robot. Resuming query.")
                    if timeout_disconnect > 3:
                        self.disconnect_signal.emit()
                continue
            
            try:
                self.read_db_to_groups(self.plcc, syss.db_number, syss.db_size)
            except Exception as e:
                self.logger.error(f"[PLCQueryData]: Error in PLCQueryData thread: {e}")
                continue

    

    def read_db_to_groups(self, plc, db_number: int, db_size: int = 100):
        """Đọc DB và chia thành 3 dict: data_group_a, b, c"""
        
        raw_data = plc.db_read(db_number=db_number, start=0, size=db_size)
        
        offset = 0
        db_dict = {}   # dict tạm để parse trước

        # ==================== 1. Temperature - 40 bytes (10 x REAL) ====================
        temp_list = [get_real(raw_data, offset + i*4) for i in range(10)]
        offset += 40
        db_dict["Temperature"] = temp_list

        # ==================== 2. Pressure - 20 bytes (5 x REAL) ====================
        press_list = [get_real(raw_data, offset + i*4) for i in range(5)]
        offset += 20
        db_dict["Pressure"] = press_list

        # ==================== 3. Bool - 10 bytes (lấy ví dụ 20 bit) ====================
        bool_list = []
        for byte_idx in range(10):
            for bit_idx in range(8):
                bool_list.append(get_bool(raw_data, byte_idx, bit_idx))
                if len(bool_list) >= 20:
                    break
            if len(bool_list) >= 20:
                break
        offset += 10
        db_dict["Bool_Values"] = bool_list

        # ==================== 4. Dint - 10 bytes (2 x DINT) ====================
        dint_list = [get_dint(raw_data, offset + i*4) for i in range(2)]
        offset += 8   # 2*4 = 8 bytes (dư 2 bytes)
        db_dict["Dint_Values"] = dint_list

        # ==================== 5. Int - 10 bytes (5 x INT) ====================
        int_list = [get_int(raw_data, offset + i*2) for i in range(5)]
        offset += 10
        db_dict["Int_Values"] = int_list

        # ==================== 6. Word - phần byte còn lại ====================
        word_list = []
        while offset + 1 < db_size:
            word_list.append(get_word(raw_data, offset))
            offset += 2
        db_dict["Word_Values"] = word_list

        # ==================== CHIA THÀNH 3 DICT ====================
        data_group_a = {
            "Temperature": db_dict["Temperature"],
            "Pressure":    db_dict["Pressure"]
        }

        data_group_b = {
            "Bool_Values": db_dict["Bool_Values"],
            "Dint_Values": db_dict["Dint_Values"]
        }

        data_group_c = {
            "Int_Values":  db_dict["Int_Values"],
            "Word_Values": db_dict["Word_Values"]
        }

        return data_group_a, data_group_b, data_group_c

    def stop(self):
        self.running = False
        self.logger.info("[PLCQueryData]: PLCQueryData stopped successfully.")