import socket
from abc import ABC, abstractmethod

from py_instrument_control_lib.device_base.Device import Device
from py_instrument_control_lib.device_base.DeviceConfigs import TCPDeviceConfig


class TCPDevice(Device, ABC):
    _config: TCPDeviceConfig

    def __init__(self, config: TCPDeviceConfig) -> None:
        super().__init__(config)
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self) -> None:
        self._socket.settimeout(self._config.timeout)
        self._socket.connect((self._config.ip, self._config.port))

    def execute(self, command: str) -> None:
        command += '\n' if not command.endswith('\n') else ''
        print(command, end='')
        self._socket.sendall(command.encode())

    @abstractmethod
    def query(self, query: str) -> str:
        pass

    def disconnect(self) -> None:
        self._socket.close()
