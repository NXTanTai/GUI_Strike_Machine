from PySide6.QtCore import QThread, Signal, Slot
import time
import random

class DataSimulator(QThread):
    db_data_convert = Signal(list, list, list)

    def __init__(self):
        super().__init__()
        self.running = False

        self.target_pressure_a = 0.0
        self.target_pressure_b = 0.0
        self.target_pressure_c = 0.0

        self.target_temp_a = 25.0
        self.target_temp_b = 25.0
        self.target_temp_c = 25.0

        self.pressure_a = 0.0
        self.pressure_b = 0.0
        self.pressure_c = 0.0

        self.temp_a_t1 = 25.0
        self.temp_a_t2 = 25.0
        self.temp_a_t3 = 25.0

        self.temp_b_t1 = 25.0
        self.temp_b_t2 = 25.0
        self.temp_b_t3 = 25.0

        self.temp_c_t1 = 25.0
        self.temp_c_t2 = 25.0
        self.temp_c_t3 = 25.0

    @Slot(str, float, float)
    def set_channel_active(self, channel: str, pressure_sv: float, temp_sv: float):
        if   channel == "A":
            self.target_pressure_a = pressure_sv
            self.target_temp_a     = temp_sv if temp_sv > 36 else self.target_temp_a
        elif channel == "B":
            self.target_pressure_b = pressure_sv
            self.target_temp_b     = temp_sv if temp_sv > 36 else self.target_temp_b
        elif channel == "C":
            self.target_pressure_c = pressure_sv
            self.target_temp_c     = temp_sv if temp_sv > 36 else self.target_temp_c

    @Slot(list, list)
    def update_sv(self, pressure_sv: list, temp_sv: list):
        self.target_pressure_a = pressure_sv[0]
        self.target_pressure_b = pressure_sv[1]
        self.target_pressure_c = pressure_sv[2]

        self.target_temp_a = temp_sv[0]
        self.target_temp_b = temp_sv[1]
        self.target_temp_c = temp_sv[2]

    def _approach(self, current: float, target: float, step_ratio=0.02, noise=1.0) -> float:
        diff = target - current
        if abs(diff) < noise * 2:
            return target + random.uniform(-noise, noise)

        return current + diff * step_ratio + random.uniform(-noise * 0.3, noise * 0.3)

    def _approach_pressure(self, current: float, target: float) -> float:
        return self._approach(current, target, step_ratio=0.02, noise=0.3)

    def run(self):
        self.running = True
        while self.running:
            time.sleep(0.5)

            self.pressure_a = self._approach_pressure(self.pressure_a, self.target_pressure_a)
            self.pressure_b = self._approach_pressure(self.pressure_b, self.target_pressure_b)
            self.pressure_c = self._approach_pressure(self.pressure_c, self.target_pressure_c)

            self.temp_a_t1 = self._approach(self.temp_a_t1, self.target_temp_a, noise=1.0)
            self.temp_a_t2 = self._approach(self.temp_a_t2, self.target_temp_a, noise=1.2)
            self.temp_a_t3 = self._approach(self.temp_a_t3, self.target_temp_a, noise=0.8)

            self.temp_b_t1 = self._approach(self.temp_b_t1, self.target_temp_b, noise=1.0)
            self.temp_b_t2 = self._approach(self.temp_b_t2, self.target_temp_b, noise=1.2)
            self.temp_b_t3 = self._approach(self.temp_b_t3, self.target_temp_b, noise=0.8)

            self.temp_c_t1 = self._approach(self.temp_c_t1, self.target_temp_c, noise=1.0)
            self.temp_c_t2 = self._approach(self.temp_c_t2, self.target_temp_c, noise=1.2)
            self.temp_c_t3 = self._approach(self.temp_c_t3, self.target_temp_c, noise=0.8)

            group_a_data = [
                (self.temp_a_t1 + self.temp_a_t2 + self.temp_a_t3) / 3,
                self.temp_a_t1,
                self.temp_a_t2,
                self.temp_a_t3,
                max(self.pressure_a, 0)
            ]

            group_b_data = [
                (self.temp_b_t1 + self.temp_b_t2 + self.temp_b_t3) / 3,
                self.temp_b_t1,
                self.temp_b_t2,
                self.temp_b_t3,
                max(self.pressure_b, 0)
            ]

            group_c_data = [
                (self.temp_c_t1 + self.temp_c_t2 + self.temp_c_t3) / 3,
                self.temp_c_t1,
                self.temp_c_t2,
                self.temp_c_t3,
                max(self.pressure_c, 0)
            ]

            self.db_data_convert.emit(group_a_data, group_b_data, group_c_data)

    def stop(self):
        self.running = False