"""
This code is automatically generated from '../../specifications/SwitchMatrix.json'.
Any changes made to this file are overwritten if you regenerate this module.
Only make changes in the source file.
"""

import socket
import time

from py_instrument_control_lib.device_base.DeviceException import DeviceException
from py_instrument_control_lib.device_types.AbstractSwitchMatrix import AbstractSwitchMatrix
from py_instrument_control_lib.device_types.SMU import *
from py_instrument_control_lib.manufacturers.FloDevice import FloDevice


class SwitchMatrix(AbstractSwitchMatrix, FloDevice):

    def query(self, query: str, check_errors: bool = False) \
            -> None:
        query += '\n' if not query.endswith('\n') else ''
        print(query, end='')
        self._socket.sendall(query.encode())
        response = self._socket.recv(1024)
        return response.decode()

    def execute(self, command: str, ttl: int = 10, num_tries: int = 0, check_errors: bool = False) \
            -> None:
        if num_tries >= ttl:
            raise DeviceException(msg=f'Fatal error, cannot establish connection after {ttl} attempts. Aborting.')

        if num_tries > 0:
            time.sleep(2 ** num_tries)
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                self._socket.settimeout(self._config.timeout)
                self._socket.connect((self._config.ip, self._config.port))
            except TimeoutError | OSError:
                print(f'Error when trying to execute {command}. Already tried {num_tries} times.')

        try:
            self.query(command)
        except TimeoutError | OSError:
            self.execute(command, ttl, num_tries + 1)

    def set_row(self, row: int, check_errors: bool = False) \
            -> None:
        if not (0 <= row <= 11):
            raise ValueError('Requirements not satisfied')

        self.execute(f'{{"cmd": "SET_ROW", "row": "{row}"}}')
        if check_errors:
            self.check_error_buffer()

    def set_col(self, col: int, check_errors: bool = False) \
            -> None:
        if not (0 <= col <= 11):
            raise ValueError('Requirements not satisfied')

        self.execute(f'{{"cmd": "SET_COLUMN", "column": "{col}"}}')
        if check_errors:
            self.check_error_buffer()

    def set_row_col(self, row: int, col: int, check_errors: bool = False) \
            -> None:
        if not (0 <= row <= 11 and 0 <= col <= 11):
            raise ValueError('Requirements not satisfied')

        self.execute(f'{{"cmd": "SET_ROW_COLUMN", "row": "{row}", "column": "{col}"}}')
        if check_errors:
            self.check_error_buffer()

    def get_channel(self, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> None:
        raise NotImplementedError('Channels are not supported when using a switch matrix.')
