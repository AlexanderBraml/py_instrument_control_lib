from abc import ABC, abstractmethod
from enum import Enum

from py_instrument_control_lib.device_base.Device import Device


class Status(Enum):
    NOT_RUNNING = 1
    RUNNING = 3
    WARNINGS_PRESENT = 4
    ALARMS_PRESENT = 8


class ClimateChamber(Device, ABC):

    @abstractmethod
    def set_target_temperature(self, temperature: float) -> None:
        pass

    @abstractmethod
    def set_target_humidity(self, humidity: float) -> None:
        pass

    def set_target_data(self, temperature: float, humidity: float) -> None:
        self.set_target_temperature(temperature)
        self.set_target_humidity(humidity)

    @abstractmethod
    def get_target_temperature(self) -> float:
        pass

    @abstractmethod
    def get_target_humidity(self) -> float:
        pass

    def get_target_data(self) -> tuple[float, float]:
        return self.get_target_temperature(), self.get_target_humidity()

    @abstractmethod
    def get_current_temperature(self) -> float:
        pass

    @abstractmethod
    def get_current_humidity(self) -> float:
        pass

    def get_current_data(self) -> tuple[float, float]:
        return self.get_current_temperature(), self.get_current_humidity()

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def wait_for_stable_conditions(self, time_in_seconds: int = 120, abs_tolerance_temp: float = 0.05,
                                   abs_tolerance_hum: float = 0.1) -> None:
        pass

    @abstractmethod
    def get_status(self) -> Status:
        pass

    @abstractmethod
    def reset_errors(self) -> None:
        pass
