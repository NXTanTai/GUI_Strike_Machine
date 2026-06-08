from PySide6.QtCore import QThread, Signal, Slot
from dataclasses import dataclass
import time
import random


@dataclass
class ChannelState:
    target_pressure:     float = 0.0
    target_pressure_itv: float = 0.0
    target_temp:         float = 25.0
    pressure:            float = 0.0
    pressure_itv:        float = 0.0
    temp_t1:             float = 25.0
    temp_t2:             float = 25.0
    temp_t3:             float = 25.0
    active:              bool  = False


class DataSimulator(QThread):
    db_data_convert = Signal(list, list, list)

    def __init__(self):
        super().__init__()
        self._running = False
        self.channels = {
            "A": ChannelState(),
            "B": ChannelState(),
            "C": ChannelState(),
        }

    @Slot(str, float)
    def set_heat_active(self, channel: str, temp_sv: float):
        ch = self.channels.get(channel)
        if ch:
            ch.target_temp = temp_sv

    @Slot(str, float)
    def set_pressure_active(self, channel: str, pressure_sv: float, pressure_itv_sv: float):
        ch = self.channels.get(channel)
        if ch:
            ch.target_pressure     = pressure_sv
            ch.target_pressure_itv = pressure_itv_sv
            ch.active              = pressure_sv > 0 or pressure_itv_sv > 0

    @Slot(list, list, list)
    def update_sv(self, pressure_sv: list, pressure_itv_sv: list, temp_sv: list):
        for ch, p, p_itv, t in zip(
            self.channels.values(),
            pressure_sv,
            pressure_itv_sv,
            temp_sv
        ):
            ch.target_pressure     = p
            ch.target_pressure_itv = p_itv
            ch.target_temp         = t

    def _approach(self, current: float, target: float,
                  step_ratio: float = 0.02, noise: float = 1.0) -> float:
        diff = target - current
        if abs(diff) < noise * 2:
            return target + random.uniform(-noise, noise)
        return current + diff * step_ratio + random.uniform(-noise * 0.3, noise * 0.3)

    def _approach_temp(self, current: float, target: float) -> float:
        return self._approach(current, target, step_ratio=0.02, noise=0.15)

    def _approach_pressure(self, current: float, target: float,
                            active: bool = False) -> float:
        if active:
            return self._approach(current, target, step_ratio=0.35, noise=0.01)
        return self._approach(current, target, step_ratio=0.02, noise=0.025)

    def _update_channel(self, ch: ChannelState):
        ch.pressure     = self._approach_pressure(ch.pressure,     ch.target_pressure,     ch.active)
        ch.pressure_itv = self._approach_pressure(ch.pressure_itv, ch.target_pressure_itv, ch.active)
        ch.temp_t1      = self._approach_temp(ch.temp_t1, ch.target_temp)
        ch.temp_t2      = self._approach_temp(ch.temp_t2, ch.target_temp)
        ch.temp_t3      = self._approach_temp(ch.temp_t3, ch.target_temp)

    def _build_group_data(self, ch: ChannelState) -> list:
        return [
            max(ch.pressure, 0),
            (ch.temp_t1 + ch.temp_t2 + ch.temp_t3) / 3,
            ch.temp_t1,
            ch.temp_t2,
            ch.temp_t3,
            ch.pressure_itv,
        ]
    
    def run(self):
        self._running = True
        while self._running:
            time.sleep(0.5)

            for ch in self.channels.values():
                self._update_channel(ch)

            self.db_data_convert.emit(
                self._build_group_data(self.channels["A"]),
                self._build_group_data(self.channels["B"]),
                self._build_group_data(self.channels["C"]),
            )

    def stop(self):
        self._running = False