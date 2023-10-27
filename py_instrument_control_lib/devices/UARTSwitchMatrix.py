import time

import serial

from py_instrument_control_lib.device_base.Device import Device
from py_instrument_control_lib.device_base.DeviceConfigs import SerialDeviceConfig


class UARTSwitchMatrix(Device):

    def __init__(self, config: SerialDeviceConfig):
        super().__init__(config)
        self.serial_port = serial.Serial(config.interface, config.baud_rate, timeout=config.timeout)

    def connect(self) -> None:
        self.serial_port.flush()
        self.__connect_to_arduino()

    def set_row_col(self, row: int, col: int) -> None:
        """
        Send r: <row idx> and c: <col idx> to the Arduino nano
        Args:
            :param row: row to set, valid values are 0 - 12
            :param col: column to set, valid values are 0 - 12
        """
        self.set_row(row)
        self.set_column(col)

    def set_row(self, row_idx, timeout_in_secs=2):
        """
        Sends r: <row idx> to the Arduino nano
        Args:
            row_idx: row to set valid values are 0 - 12. 12 means no row is selected.
            timeout_in_secs: Timeout in seconds to wait for the acknowledgement.
        """
        self.execute(f'r: {row_idx}\n')
        return self.__wait_for_response(timeout_in_secs)

    def set_column(self, column_idx, timeout_in_secs=2):
        """
         Sends c: <column idx> to the Arduino nano
         Args:
             column_idx: column to set valid values are 0 - 12. 12 means no column is selected.
             timeout_in_secs: Timeout in seconds to wait for the acknowledgement.
         """
        self.execute(f'c: {column_idx}\n')
        return self.__wait_for_response(timeout_in_secs)

    def __connect_to_arduino(self, number_of_attempts=3):
        """
        Sends a connection request to the Arduino Nano as long as the connection is established.
        Args:
            :param number_of_attempts
        """
        for i in range(number_of_attempts):
            if self.__send_connect_message():
                return True
        else:
            print("Timeout when trying to connect")

    def __send_connect_message(self, timeout_in_secs=2):
        """
        Sends the connect message to the Arduino Nano.
        Args:
            timeout_in_secs: Timeout in seconds to wait for the acknowledgement.
        """
        self.execute('connect\n')
        return self.__wait_for_response(timeout_in_secs)

    def __wait_for_response(self, timeout_in_secs):
        time.sleep(0.4)
        start_ts = time.time()
        while time.time() < start_ts + timeout_in_secs:
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

    def __send_disconnect_message(self, timeout_in_secs=2):
        """
        Sends the disconnect message to the Arduino Nano.
        Args:
            timeout_in_secs: Timeout in seconds to wait for the acknowledgement.
        """
        self.execute('disconnect\n')
        self.__wait_for_response(timeout_in_secs)
        self.serial_port.close()
