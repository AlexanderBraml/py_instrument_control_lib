"""
This code is automatically generated from '../../../specifications/SwitchMatrix.json'.
Any changes made to this file are overwritten if you regenerate this module.
Only make changes in the source file.
"""

from py_instrument_control_lib.device_base.TCPDevice import TCPDevice
from py_instrument_control_lib.device_types.AbstractSwitchMatrix import AbstractSwitchMatrix
from py_instrument_control_lib.device_types.FunctionGenerator import *
from py_instrument_control_lib.device_types.Oscilloscope import *
from py_instrument_control_lib.device_types.PowerSupply import *
from py_instrument_control_lib.device_types.SMU import *
from py_instrument_control_lib.manufacturers.FloDevice import FloDevice
from py_instrument_control_lib.manufacturers.KeithleyDevice import KeithleyDevice
from py_instrument_control_lib.manufacturers.KeysightDevice import KeysightDevice

_, _, _, _, _, _, _, _, _ = (SMU, FunctionGenerator, PowerSupply, Oscilloscope, TCPDevice,
                             KeysightDevice, KeithleyDevice, AbstractSwitchMatrix, FloDevice)


class SwitchMatrix(AbstractSwitchMatrix, FloDevice):

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
