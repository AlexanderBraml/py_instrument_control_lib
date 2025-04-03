"""
This code is automatically generated from '../../specifications/SPD1305X.json'.
Any changes made to this file are overwritten if you regenerate this module.
Only make changes in the source file.
"""
from channels.Channel import Channel
from channels.ChannelEnums import ChannelIndex

from py_instrument_control_lib.device_types.PowerSupply import *
from py_instrument_control_lib.manufacturers.KeysightDevice import KeysightDevice


class SPD1305X(PowerSupply, KeysightDevice):

    def measure(self, unit: PSUnit, channel: PSChannel, check_errors: bool = False) \
            -> None:
        self.execute(f'MEASure:{unit.value} {channel.value}')
        if check_errors:
            self.check_error_buffer()

    def toggle(self, channel: PSChannel, enable: bool, check_errors: bool = False) \
            -> None:
        self.execute(f'OUTPut {channel.value},{"ON" if enable else "OFF"}')
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
            -> float:
        ret = self.query(f'{channel.value}:VOLTage?')
        if check_errors:
            self.check_error_buffer()
        return float(ret)

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

    def check_error_buffer(self, check_errors: bool = False) \
            -> None:
        pass

    def get_system_status(self, check_errors: bool = False) -> dict:
        ret = int(self.query('SYSTem:STATus?'), 16)
        ret_dict = {
            'constant_current_voltage_mode': PSPowerMode.CONSTANT_VOLTAGE if (ret & 1) == 0 else PSPowerMode.CONSTANT_CURRENT,
            'output': False if (ret & 0x10) == 0 else True,
            'wire_mode': PSMode.W2 if (ret & 0x20) == 0 else PSMode.W4,
            'timer': False if (ret & 0x40) == 0 else True,
            'display': 'digital_display' if (ret & 0x100) == 0 else 'waveform_display'
        }
        if check_errors:
            self.check_error_buffer()
        return ret_dict


    def get_channel(self, channel_idx: ChannelIndex, check_errors: bool = False) -> Channel:
        raise NotImplementedError('Channels are not supported yet.')


