import time

import serial

from py_instrument_control_lib.device_base.DeviceConfigs import SerialDeviceConfig
from py_instrument_control_lib.device_types.AbstractSwitchMatrix import AbstractSwitchMatrix


class UARTSwitchMatrix(AbstractSwitchMatrix):
    _config: SerialDeviceConfig

    def __init__(self, config: SerialDeviceConfig):
        super().__init__(config)
        self.serial_port = serial.Serial(config.interface, config.baud_rate, timeout=config.timeout)

    def connect(self) -> None:
        self.serial_port.flush()
        self.__connect_to_arduino()

    def set_row(self, row):
        """
        Sends r: <row idx> to the Arduino nano
        Args:
            row: row to set valid values are 0 - 12. 12 means no row is selected.
        """
        self.execute(f'r: {row}\n')
        return self.__wait_for_response()

    def set_col(self, col):
        """
         Sends c: <column idx> to the Arduino nano
         Args:
             col: column to set valid values are 0 - 12. 12 means no column is selected.
         """
        self.execute(f'c: {col}\n')
        return self.__wait_for_response()

    def set_row_col(self, row: int, col: int) -> None:
        """
        Send r: <row idx> and c: <col idx> to the Arduino nano
        Args:
            :param row: row to set, valid values are 0 - 12
            :param col: column to set, valid values are 0 - 12
        """
        self.set_row(row)
        self.set_col(col)

    def __connect_to_arduino(self):
        """
        Sends a connection request to the Arduino Nano as long as the connection is established.
        """
        for i in range(self._config.number_of_connection_attempts):
            if self.__send_connect_message():
                return True
        else:
            print("Timeout when trying to connect")

    def __send_connect_message(self):
        """
        Sends the connect message to the Arduino Nano.
        """
        self.execute('connect\n')
        return self.__wait_for_response()

    def __wait_for_response(self):
        time.sleep(0.4)
        start_ts = time.time()
        while time.time() < start_ts + self._config.timeout:
            ack = self.serial_port.readline()
            ack = ack.decode('ascii')
            if 'ack' in ack:
                self.serial_port.flush()
                return True
            if 'error' in ack:
                print(ack)
                return False
        return False

    def execute(self, command: str) -> None:
        self.serial_port.write(command.encode('ASCII'))

    def query(self, query: str) -> str:
        raise NotImplementedError('Query is not supported on a SwitchMatrix')

    def disconnect(self) -> None:
        self.__send_disconnect_message()

    def __send_disconnect_message(self):
        """
        Sends the disconnect message to the Arduino Nano.
        """
        self.execute('disconnect\n')
        self.__wait_for_response()
        self.serial_port.close()
