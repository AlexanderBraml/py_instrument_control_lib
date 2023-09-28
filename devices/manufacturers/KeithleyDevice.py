import socket
from abc import ABC

from devices.Device import Device
from devices.DeviceConfigs import TCPDeviceConfig
from devices.DeviceException import DeviceException, ErrorCode
from devices.TCPDevice import TCPDevice


class KeithleyDevice(TCPDevice, ABC):

    def query(self, query: str) -> str:
        command = 'reading = ' + query
        self.execute(command)
        self.execute('print(reading)')
        response = self._socket.recv(1024)

        return response.decode()

    def check_error_buffer(self) -> None:
        error_count = int(self.query('errorqueue.count'))
        if error_count > 0:
            raise DeviceException(error=ErrorCode.ITEM_IN_ERROR_QUEUE)

    def disconnect(self) -> None:
        self._socket.close()
