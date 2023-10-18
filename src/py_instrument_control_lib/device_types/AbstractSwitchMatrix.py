from abc import ABC

from src.py_instrument_control_lib.device_base.Device import Device


class AbstractSwitchMatrix(Device, ABC):

    def set_row(self, row: int) -> None:
        pass

    def set_col(self, col: int) -> None:
        pass

    def set_row_col(self, row: int, col: int) -> None:
        pass
