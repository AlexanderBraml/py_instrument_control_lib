"""
This code is automatically generated from '../../specifications/KST33500.json'.
Any changes made to this file are overwritten if you regenerate this module.
Only make changes in the source file.
"""

from py_instrument_control_lib.channels.Channel import SourceChannel
from py_instrument_control_lib.device_types.FunctionGenerator import *
from py_instrument_control_lib.device_types.SMU import *
from py_instrument_control_lib.manufacturers.KeysightDevice import KeysightDevice


class KST33500(FunctionGenerator, KeysightDevice):

    def toggle(self, channel_idx: ChannelIndex, enable: bool, check_errors: bool = False) \
            -> None:
        self.execute(f'OUTPut{channel_idx.get()} {"ON" if enable else "OFF"}')
        if check_errors:
            self.check_error_buffer()

    def set_frequency(self, channel_idx: ChannelIndex, frequency: float, check_errors: bool = False) \
            -> None:
        self.execute(f'SOURce{channel_idx.get()}:FREQuency {frequency}')
        if check_errors:
            self.check_error_buffer()

    def set_amplitude(self, channel_idx: ChannelIndex, frequency: float, constrain: str, check_errors: bool = False) \
            -> None:
        self.execute(f'SOURce{channel_idx.get()}:VOLTage{":" + constrain if constrain else ""} {frequency}')
        if check_errors:
            self.check_error_buffer()

    def set_offset(self, channel_idx: ChannelIndex, offset: float, impedance: float = float('inf'), check_errors: bool = False) \
            -> None:
        self.set_impedance(channel_idx, impedance)
        self.execute(f'SOURce{channel_idx.get()}:VOLTage:OFFSet {offset}')

    def set_phase(self, channel_idx: ChannelIndex, phase: float, check_errors: bool = False) \
            -> None:
        self.execute(f'SOURce{channel_idx.get()}:PHASe {phase}')
        if check_errors:
            self.check_error_buffer()

    def set_function(self, channel_idx: ChannelIndex, function: FunctionType, check_errors: bool = False) \
            -> None:
        self.execute(f'SOURce{channel_idx.get()}:FUNCtion {function.value}')
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

    def set_pulsewidth(self, channel_idx: ChannelIndex, pulsewidth: float, check_errors: bool = False) \
            -> None:
        """
        Pulswidth unit: ms
        """
        self.execute(f'SOURce{channel_idx.get()}:FUNCtion:PULSe:WIDTh {pulsewidth} ms')
        if check_errors:
            self.check_error_buffer()

    def get_channel(self, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> SourceChannel:
        channel_idx.check(2)
        return SourceChannel(self, channel_idx, [ChannelUnit.VOLTAGE])

    def toggle_channel(self, channel_idx: ChannelIndex, enable: bool, check_errors: bool = False) \
            -> None:
        channel_idx.check(2)
        self.toggle(channel_idx, enable)

    def set_channel_level(self, unit: ChannelUnit, channel_idx: ChannelIndex, level: float, impedance: float = float('inf'), check_errors: bool = False) \
            -> None:
        channel_idx.check(2)
        self.set_offset(channel_idx, level, impedance)

    def set_impedance(self, channel_idx: ChannelIndex, impedance: float, check_errors: bool = False) \
            -> None:
        if not (0 < impedance < 10000 or impedance == float('inf')):
            raise ValueError('Impedance has to be between 0 and 10,000 or equal to infinity!')
        if impedance == float('inf'):
            impedance = 'INFinity'
        else:
            impedance = int(impedance)
        self.execute(f'OUTPut{channel_idx.get()}:LOAD {impedance}')

    def check_error_buffer(self, check_errors: bool = False) \
            -> None:
        pass
