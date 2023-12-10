from abc import ABC
from dataclasses import dataclass


@dataclass
class DeviceConfig(ABC):
    pass


@dataclass
class TCPDeviceConfig(DeviceConfig):
    ip: str
    port: int
    timeout: int = 2  # in s


@dataclass
class SerialDeviceConfig(DeviceConfig):
    interface: str
    baud_rate: int = 9600
    timeout: int = 2
    number_of_connection_attempts: int = 3
