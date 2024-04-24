from abc import ABC

from py_instrument_control_lib.device_base.DeviceConfigs import TCPDeviceConfig
from py_instrument_control_lib.device_base.TCPDevice import TCPDevice


class WeisstechnikDevice(TCPDevice, ABC):
    _error_code_to_message = {
        1: None,
        -5: 'ERROR_UNSUPPORTED_COMMAND',
        -6: 'ERROR_TOO_FEW_PARAMETERS',
        -8: 'ERROR_DATA_COULD_NOT_BE_READ',
    }

    def __init__(self, config: TCPDeviceConfig) -> None:
        super().__init__(config)
        self._last_error = None

    def __send_command(self, command: str) -> None:
        if not command.endswith('\r'):
            command += '\r'
        self._socket.sendall(command.encode('iso-8859-1'))

    def query(self, query: str) -> str:
        raw_response = self._socket.recv(1024).decode('iso-8859-1')
        processed_response = raw_response.replace('\r', '').replace('\n', '').split('¶')
        error_code = processed_response[0]
        self._last_error = self._error_code_to_message.get(error_code, f'ERROR_{error_code}')
        if len(processed_response) > 1:
            return processed_response[1]

    def execute(self, command: str) -> None:
        self.query(command)
