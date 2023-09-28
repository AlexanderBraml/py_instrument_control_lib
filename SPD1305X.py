"""
This code is automatically generated from 'SPD1305X.json'.
Any changes made to this file are overwritten if you regenerate this module.
Only make changes in the source file.
"""

from devices.types.PowerSupply import *
from devices.KeysightDevice import KeysightDevice


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
    
    def get_voltage(self, check_errors: bool = False) \
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
