"""
This code is automatically generated from '../../specifications/KST33500.json'.
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


class KST33500(FunctionGenerator, KeysightDevice):

    def toggle(self, enable: bool, check_errors: bool = False) \
            -> None:        
        self.execute(f'OUTPut {"ON" if enable else "OFF"}')
        if check_errors:
            self.check_error_buffer()
    
    def set_frequency(self, frequency: float, check_errors: bool = False) \
            -> None:        
        self.execute(f'FREQuency {frequency}')
        if check_errors:
            self.check_error_buffer()
    
    def set_amplitude(self, frequency: float, constrain: str, check_errors: bool = False) \
            -> None:        
        self.execute(f'VOLTage{":" + constrain if constrain else ""} {frequency}')
        if check_errors:
            self.check_error_buffer()
    
    def set_offset(self, offset: float, check_errors: bool = False) \
            -> None:        
        self.execute(f'VOLTage:OFFSet {offset}')
        if check_errors:
            self.check_error_buffer()
    
    def set_phase(self, phase: float, check_errors: bool = False) \
            -> None:        
        self.execute(f'PHASe {phase}')
        if check_errors:
            self.check_error_buffer()
    
    def set_function(self, function: FunctionType, check_errors: bool = False) \
            -> None:        
        self.execute(f'FUNCtion {function.value}')
        if check_errors:
            self.check_error_buffer()
    
    def display(self, text: str, check_errors: bool = False) \
            -> None:        
        self.execute(f"DISP:TEXT '{text}'")
        if check_errors:
            self.check_error_buffer()
    
    def display_clear(self, check_errors: bool = False) \
            -> None:        
        self.execute('DISPlay:TEXT:CLEar')
        if check_errors:
            self.check_error_buffer()
    
    def set_pulsewidth(self, pulsewidth: float, check_errors: bool = False) \
            -> None:    
        """
        Pulswidth unit: ms
        """    
        self.execute(f'FUNCtion:PULSe:WIDTh {pulsewidth} ms')
        if check_errors:
            self.check_error_buffer()
