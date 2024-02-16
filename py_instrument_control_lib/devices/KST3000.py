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
    
    def set_channel_offset(self, channel_idx: ChannelIndex, offset: float, check_errors: bool = False) \
            -> None:        
        self.execute(f'CHANnel{self.__to_channel(channel_idx)}:offset {offset}')
        if check_errors:
            self.check_error_buffer()
    
    def set_channel_scale(self, channel_idx: ChannelIndex, scale: float, check_errors: bool = False) \
            -> None:        
        self.execute(f'CHANnel{self.__to_channel(channel_idx)}:SCALe {scale}')
        if check_errors:
            self.check_error_buffer()
    
    def set_channel_range(self, channel_idx: ChannelIndex, value: float, voltage_unit: VoltageUnit, check_errors: bool = False) \
            -> None:        
        self.execute(f'CHANnel{self.__to_channel(channel_idx)}:RANGe range {"mV" if voltage_unit == VoltageUnit.MILLI_VOLT else ""}')
        if check_errors:
            self.check_error_buffer()
    
    def set_trigger_edge(self, edge: TriggerEdge, check_errors: bool = False) \
            -> None:        
        self.execute(f'TRIGger:SLOPe {edge.value}')
        if check_errors:
            self.check_error_buffer()
    
    def set_trigger_source(self, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> None:        
        self.execute(f'TRIGger:SOURceCHAN{self.__to_channel(channel_idx)}')
        if check_errors:
            self.check_error_buffer()
    
    def set_time_delay(self, delay: float, check_errors: bool = False) \
            -> None:        
        self.execute(f'TIMebase:DELay {delay}')
        if check_errors:
            self.check_error_buffer()
    
    def set_waveform_source(self, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> None:        
        self.execute(f'WAVeform:SOURce CHANnel{self.__to_channel(channel_idx)}')
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
        self.execute('WAVeform:DATA?')
        response = self._socket.recv(1024)
        if check_errors:
            self.check_error_buffer()
        return response
    
    def get_real_data(self, check_errors: bool = False) \
            -> tuple[list[float], list[float]]:        
        preamble = self.get_waveform_preamble().split(',')
        x_increment = float(preamble[4])
        x_origin = float(preamble[5])
        x_reference = float(preamble[6])
        y_increment = float(preamble[7])
        y_origin = float(preamble[8])
        y_reference = float(preamble[9])
        
        data = self.get_waveform_data()[10:]
        result = ([], [])
        for i in range(self.get_waveform_points()):
            time = ((i - x_reference) * x_increment) + x_origin
            voltage_data = int(data[i])
            if voltage_data != 0:  # Not a hole. Holes are locations where data has not yet been acquired.
                voltage = ((voltage_data - y_reference) * y_increment) + y_origin
                result[0].append(time)
                result[1].append(voltage)
        
        if check_errors:
            self.check_error_buffer()
        return result
    
    def digitize(self, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> None:        
        self.execute(f'DIGitize CHAnnel{self.__to_channel(channel_idx)}')
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
    
    def set_channel_display(self, channel_idx: ChannelIndex, enable: bool, check_errors: bool = False) \
            -> None:        
        self.execute(f'CHANnel:DISPLAY{self.__to_channel(channel_idx)} {int(enable)}')
        if check_errors:
            self.check_error_buffer()
    
    def get_channel(self, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> None:        
        raise NotImplementedError('Channels are not supported yet.')
    
    def __to_channel(self, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> str:        
        channel_idx.check(4)
        return str(channel_idx)
    
    def check_error_buffer(self, check_errors: bool = False) \
            -> None:        
        pass
