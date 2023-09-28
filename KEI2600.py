"""
This code is automatically generated from 'KEI2600.json'.
Any changes made to this file are overwritten if you regenerate this module.
Only make changes in the source file.
"""

from devices.types.SMU import *
from devices.KeithleyDevice import KeithleyDevice


class KEI2600(SMU, KeithleyDevice):

    def measure(self, unit: Unit, channel: SMUChannel, check_errors: bool = False) \
            -> float:    
        """
        This function measures a certain unit on a specific channel. Can be used to measure voltage, current, power or resistance.
        :param unit: The thing to measure.
        :param channel: The channel to measure on.
        :param check_errors: Whether to check the error buffer after the execution.
        :return: None.
        """    
        val = self.query(f'{channel.value}.measure.{unit.value}()')
        if check_errors:
            self.check_error_buffer()
        return float(val)
    
    def toggle_channel(self, channel: SMUChannel, enable: bool, check_errors: bool = False) \
            -> None:        
        self.execute(f'{channel.value}.source.output = {channel.value}.OUTPUT_{("ON" if enable else "OFF")}')
        if check_errors:
            self.check_error_buffer()
    
    def set_level(self, unit: Unit, channel: SMUChannel, level: float, check_errors: bool = False) \
            -> None:        
        if not (unit in (Unit.VOLTAGE, Unit.CURRENT)):
            raise ValueError('Requirements not satisfied')
        
        self.execute(f'{channel.value}.source.level{unit.value} = {level}')
        if check_errors:
            self.check_error_buffer()
    
    def set_limit(self, unit: Unit, channel: SMUChannel, limit: float, check_errors: bool = False) \
            -> None:        
        if not (unit in (Unit.VOLTAGE, Unit.CURRENT, Unit.POWER)):
            raise ValueError('Requirements not satisfied')
        
        self.execute(f'{channel.value}.source.limit{unit.value} = {str(limit)}')
        if check_errors:
            self.check_error_buffer()
    
    def toggle_autorange(self, unit: Unit, channel: SMUChannel, mode: SMUMode, enable: bool, check_errors: bool = False) \
            -> None:        
        if not (unit in (Unit.VOLTAGE, Unit.CURRENT)):
            raise ValueError('Requirements not satisfied')
        
        self.execute(f'{channel.value}.{mode.value}.autorange{unit.value} = {int(enable) if mode == SMUMode.MEASURE else channel.value + ".AUTORANGE_" + ("ON" if enable else "OFF")}')
        if check_errors:
            self.check_error_buffer()
    
    def toggle_measure_analog_filter(self, channel: SMUChannel, enable: bool, check_errors: bool = False) \
            -> None:        
        self.execute(f'{channel.value}.measure.analogfilter = {int(enable)}')
        if check_errors:
            self.check_error_buffer()
    
    def set_range(self, unit: Unit, channel: SMUChannel, mode: SMUMode, range_: float, check_errors: bool = False) \
            -> None:        
        if not (unit in (Unit.VOLTAGE, Unit.CURRENT)):
            raise ValueError('Requirements not satisfied')
        
        self.execute(f'{channel.value}.{mode.value}.range{unit.value} = {range_}')
        if check_errors:
            self.check_error_buffer()
    
    def set_sense_mode(self, channel: SMUChannel, sense_arg: SMUSense, check_errors: bool = False) \
            -> None:        
        self.execute(f'{channel.value}.sense = {channel.value}.{sense_arg.value}')
        if check_errors:
            self.check_error_buffer()
    
    def set_measure_plc(self, channel: SMUChannel, value: float, check_errors: bool = False) \
            -> None:        
        if not (0.001 < value < 25):
            raise ValueError('Requirements not satisfied')
        
        self.execute(f'{channel.value}.measure.nplc = {value}')
        if check_errors:
            self.check_error_buffer()
    
    def set_measure_low_range(self, unit: Unit, channel: SMUChannel, value: float, check_errors: bool = False) \
            -> None:        
        if not (unit in (Unit.VOLTAGE, Unit.CURRENT)):
            raise ValueError('Requirements not satisfied')
        
        self.execute(f'{channel.value}.measure.lowrange{unit.value} = {value}')
        if check_errors:
            self.check_error_buffer()
    
    def set_measure_auto_zero(self, channel: SMUChannel, auto_zero: Autozero, check_errors: bool = False) \
            -> None:        
        self.execute(f'{channel.value}.measure.autozero = {channel.value}.{auto_zero.value}')
        if check_errors:
            self.check_error_buffer()
    
    def set_measure_count(self, channel: SMUChannel, nr_of_measurements: int, check_errors: bool = False) \
            -> None:        
        self.execute(f'{channel.value}.measure.count = {nr_of_measurements}')
        if check_errors:
            self.check_error_buffer()
    
    def set_source_function(self, channel: SMUChannel, src_func: SourceFunction, check_errors: bool = False) \
            -> None:        
        self.execute(f'{channel.value}.source.func = {channel.value}.{src_func.value}')
        if check_errors:
            self.check_error_buffer()
    
    def set_source_off_mode(self, channel: SMUChannel, src_off_mode: SourceOffMode, check_errors: bool = False) \
            -> None:        
        self.execute(f'{channel.value}.source.offmode = {channel.value}.{src_off_mode.value}')
        if check_errors:
            self.check_error_buffer()
    
    def set_source_settling(self, channel: SMUChannel, src_settling: SourceSettling, check_errors: bool = False) \
            -> None:        
        self.execute(f'{channel.value}.source.settling = {channel.value}.{src_settling.value}')
        if check_errors:
            self.check_error_buffer()
    
    def toggle_source_sink(self, channel: SMUChannel, enable: bool, check_errors: bool = False) \
            -> None:        
        self.execute(f'{channel.value}.source.sink = {str(int(enable))}')
        if check_errors:
            self.check_error_buffer()
    
    def display_measure_function(self, channel: SMUChannel, diplay_measure_func: SMUDisplay, check_errors: bool = False) \
            -> None:        
        self.execute(f'display.{channel.value}.measure.func = display.{diplay_measure_func.value}')
        if check_errors:
            self.check_error_buffer()
    
    def toggle_beep(self, enable: bool, check_errors: bool = False) \
            -> None:        
        self.execute(f'beeper.enable = beeper.{"ON" if enable else "OFF"}')
        if check_errors:
            self.check_error_buffer()
    
    def beep(self, duration: float, frequency: int, check_errors: bool = False) \
            -> None:    
        """
        Send a beeping sound with a specific duration and frequency to the SMU.
        :param duration: Time in seconds to play the beeping sound.
        :param frequency: Frequency in HZ of the sound to play.
        :param check_errors: Whether to check the error buffer after the execution.
        :return: None.
        """    
        self.execute(f'beeper.beep({duration}, {frequency})')
        if check_errors:
            self.check_error_buffer()
