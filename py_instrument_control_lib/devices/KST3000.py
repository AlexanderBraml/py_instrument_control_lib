"""
This code is automatically generated from '../../specifications/KST3000.json'.
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


class KST3000(Oscilloscope, KeysightDevice):

    def run(self, check_errors: bool = False) \
            -> None:        
        self.execute('RUN')
        if check_errors:
            self.check_error_buffer()
    
    def stop(self, check_errors: bool = False) \
            -> None:        
        self.execute('STOP')
        if check_errors:
            self.check_error_buffer()
    
    def single(self, check_errors: bool = False) \
            -> None:        
        self.execute('SINGLE')
        if check_errors:
            self.check_error_buffer()
    
    def auto_scale(self, check_errors: bool = False) \
            -> None:        
        self.execute('AUToscale')
        if check_errors:
            self.check_error_buffer()
    
    def set_time_range(self, range_: float, check_errors: bool = False) \
            -> None:        
        self.execute(f'TIMebase:RANGe {range_}')
        if check_errors:
            self.check_error_buffer()
    
    def set_channel_offset(self, channel: OscChannel, offset: float, check_errors: bool = False) \
            -> None:        
        self.execute(f'CHANnel{channel.value}:offset {offset}')
        if check_errors:
            self.check_error_buffer()
    
    def set_channel_scale(self, channel: OscChannel, scale: float, check_errors: bool = False) \
            -> None:        
        self.execute(f'CHANnel{channel.value}:SCALe {scale}')
        if check_errors:
            self.check_error_buffer()
    
    def set_channel_range(self, channel: OscChannel, value: float, voltage_unit: VoltageUnit, check_errors: bool = False) \
            -> None:        
        self.execute(f'CHANnel{channel.value}:RANGe range {"mV" if voltage_unit == VoltageUnit.MILLI_VOLT else ""}')
        if check_errors:
            self.check_error_buffer()
    
    def set_trigger_edge(self, edge: TriggerEdge, check_errors: bool = False) \
            -> None:        
        self.execute(f'TRIGger:SLOPe {edge.value}')
        if check_errors:
            self.check_error_buffer()
    
    def set_trigger_source(self, channel: OscChannel, check_errors: bool = False) \
            -> None:        
        self.execute(f'TRIGger:SOURceCHAN{channel.value}')
        if check_errors:
            self.check_error_buffer()
    
    def set_time_delay(self, delay: float, check_errors: bool = False) \
            -> None:        
        self.execute(f'TIMebase:DELay {delay}')
        if check_errors:
            self.check_error_buffer()
    
    def set_waveform_source(self, channel: OscChannel, check_errors: bool = False) \
            -> None:        
        self.execute(f'WAVeform:SOURce CHANnel{channel.value}')
        if check_errors:
            self.check_error_buffer()
    
    def get_waveform_preamble(self, check_errors: bool = False) \
            -> str:        
        val = self.query(f'WAVeform:PREamble?')
        if check_errors:
            self.check_error_buffer()
        return val
    
    def get_waveform_points(self, check_errors: bool = False) \
            -> int:        
        val = self.query('WAVeform:POINts?')
        if check_errors:
            self.check_error_buffer()
        return int(val)
    
    def set_waveform_points(self, num_points: int, check_errors: bool = False) \
            -> None:        
        self.execute(f'WAVeform:POINts {num_points}')
        if check_errors:
            self.check_error_buffer()
    
    def set_waveform_points_mode(self, mode: str, check_errors: bool = False) \
            -> None:        
        self.execute(f'WAVeform:POINts:MODE {mode}')
        if check_errors:
            self.check_error_buffer()
    
    def set_waveform_format(self, format_: FileFormat, check_errors: bool = False) \
            -> None:        
        self.execute(f'WAVeform:FORMat {format_.value}')
        if check_errors:
            self.check_error_buffer()
    
    def save_waveform_data(self, file_path: str, check_errors: bool = False) \
            -> None:        
        self.execute('')
        if check_errors:
            self.check_error_buffer()
    
    def get_waveform_data(self, check_errors: bool = False) \
            -> str:        
        val = self.query('WAVeform:DATA?')
        if check_errors:
            self.check_error_buffer()
        return val
    
    def get_real_data(self, check_errors: bool = False) \
            -> str:        
        val = self.query('')
        if check_errors:
            self.check_error_buffer()
        return val
    
    def digitize(self, channel: OscChannel, check_errors: bool = False) \
            -> None:        
        self.execute(f'DIGitize CHAnnel{channel.value}')
        if check_errors:
            self.check_error_buffer()
    
    def get_system_setup(self, check_errors: bool = False) \
            -> None:        
        self.execute('SYSTem:SETup?')
        if check_errors:
            self.check_error_buffer()
    
    def set_display_mode(self, display_mode: DisplayModes, check_errors: bool = False) \
            -> None:        
        self.execute(f'TIMebase:MODE {display_mode.value}')
        if check_errors:
            self.check_error_buffer()
    
    def set_channel_display(self, channel: OscChannel, enable: bool, check_errors: bool = False) \
            -> None:        
        self.execute(f'CHANnel:DISPLAY{channel.value} {int(enable)}')
        if check_errors:
            self.check_error_buffer()
