import json
from abc import ABC

from py_instrument_control_lib.device_base.DeviceException import DeviceException, ErrorCode
from py_instrument_control_lib.device_base.TCPDevice import TCPDevice


class FloDevice(TCPDevice, ABC):

    def query(self, query: str) -> str:
        self.execute(query)
        response = self._socket.recv(1024)

        return response.decode()

    def check_error_buffer(self) -> None:
        response = self._socket.recv(1024)
        response_dict = json.loads(response.decode())
        if response_dict['status'] != 'ok':
            raise DeviceException(f'Error on SwitchMatrix: {response_dict["msg"]}')

    def disconnect(self) -> None:
        self._socket.close()
