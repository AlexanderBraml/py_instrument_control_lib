"""
This code is automatically generated from '../../specifications/SPD1305X.json'.
Any changes made to this file are overwritten if you regenerate this module.
Only make changes in the source file.
"""

from py_instrument_control_lib.channels.ChannelEnums import ChannelIndex, ChannelUnit
from py_instrument_control_lib.channels.Channel import SourceChannel, MeasureChannel, SourceMeasureChannel
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


class SPD1305X(PowerSupply, KeysightDevice):

    def measure(self, unit: PSUnit, channel: PSChannel, check_errors: bool = False) \
            -> None:        
        self.execute(f'MEASure:{unit.value} {channel.value}')
        if check_errors:
            self.check_error_buffer()
    
    def toggle(self, channel: PSChannel, enable: bool, check_errors: bool = False) \
            -> None:        
        self.execute(f'OUTPut {channel.value}, {"ON" if enable else "OFF"}')
        if check_errors:
            self.check_error_buffer()
    
    def set_current(self, channel: PSChannel, current: float, check_errors: bool = False) \
            -> None:        
        self.execute(f'{channel.value}:CURRent {current}')
        if check_errors:
            self.check_error_buffer()
    
    def get_current(self, channel: PSChannel, check_errors: bool = False) \
            -> None:        
        self.execute(f'{channel.value}:CURRent?')
        if check_errors:
            self.check_error_buffer()
    
    def set_voltage(self, channel: PSChannel, voltage: float, check_errors: bool = False) \
            -> None:        
        self.execute(f'{channel.value}:VOLTage {voltage}')
        if check_errors:
            self.check_error_buffer()
    
    def get_voltage(self, channel: PSChannel, check_errors: bool = False) \
            -> None:        
        self.execute(f'{channel.value}:VOLTage?')
        if check_errors:
            self.check_error_buffer()
    
    def set_mode(self, mode: PSMode, check_errors: bool = False) \
            -> None:        
        self.execute(f'MODE:SET {mode.value}')
        if check_errors:
            self.check_error_buffer()
    
    def lock_input(self, check_errors: bool = False) \
            -> None:        
        self.execute('LOCK')
        if check_errors:
            self.check_error_buffer()
    
    def unlock_input(self, check_errors: bool = False) \
            -> None:        
        self.execute('*UNLOCK')
        if check_errors:
            self.check_error_buffer()
