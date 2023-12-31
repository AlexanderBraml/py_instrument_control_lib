from abc import ABC, abstractmethod

from py_instrument_control_lib.device_base.DeviceConfigs import DeviceConfig


class Device(ABC):
    def __init__(self, config: DeviceConfig) -> None:
        self._config: DeviceConfig = config

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def execute(self, command: str) -> None:
        pass

    @abstractmethod
    def query(self, query: str) -> str:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass
