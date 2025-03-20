from abc import abstractmethod, ABC
from enum import Enum

from py_instrument_control_lib.channels.ChannelEnums import ChannelIndex, ChannelUnit
from py_instrument_control_lib.device_base.Device import Device

class SMUFilterType(Enum):
    FILTER_MEDIAN = 'FILTER_MEDIAN'
    FILTER_MOVING_AVG = 'FILTER_MOVING_AVG'
    FILTER_REPEAT_AVG = 'FILTER_REPEAT_AVG'


class SMUMode(Enum):
    SOURCE = 'source'
    MEASURE = 'measure'


class Autozero(Enum):
    OFF = "AUTOZERO_OFF"
    ONCE = "AUTOZERO_ONCE"
    AUTO = "AUTOZERO_AUTO"


class SourceFunction(Enum):
    DC_AMPS = "OUTPUT_DCAMPS"
    DC_VOLTS = "OUTPUT_DCVOLTS"


class SourceOffMode(Enum):
    OUTPUT_NORMAL = "OUTPUT_NORMAL"
    OUTPUT_ZERO = "OUTPUT_ZERO"
    OUTPUT_HIGH_Z = "OUTPUT_HIGH_Z"


class SourceSettling(Enum):
    SMOOTH = "SETTLE_SMOOTH"
    FAST_RANGE = "SETTLE_FAST_RANGE"
    FAST_POLARITY = "SETTLE_FAST_POLARITY"
    DIRECT_IRANGE = "SETTLE_DIRECT_IRANGE"
    SMOOTH_100nA = "SETTLE_SMOOTH_100NA"
    FAST_ALL = "SETTLE_FAST_ALL"


class SMUDisplay(Enum):
    MEASURE_DC_AMPS = "MEASURE_DCAMPS"
    MEASURE_DC_VOLTS = "MEASURE_DCVOLTS"
    MEASURE_OHMS = "MEASURE_OHMS"
    MEASURE_WATTS = "MEASURE_WATTS"


class SMUSense(Enum):
    LOCAL = "SENSE_LOCAL"
    REMOTE = "SENSE_REMOTE"
    CALIBRATION = "SENSE_CALA"


class SMU(Device, ABC):

    @abstractmethod
    def measure(self, unit: ChannelUnit, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> float:
        pass

    @abstractmethod
    def toggle_channel(self, channel_idx: ChannelIndex, enable: bool, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def set_level(self, unit: ChannelUnit, channel_idx: ChannelIndex, level: float, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def set_limit(self, unit: ChannelUnit, channel_idx: ChannelIndex, limit: float, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def toggle_autorange(self, unit: ChannelUnit, channel_idx: ChannelIndex, mode: SMUMode, enable: bool,
                         check_errors: bool = False) -> None:
        pass

    @abstractmethod
    def toggle_measure_analog_filter(self, channel_idx: ChannelIndex, enable: bool, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def set_range(self, unit: ChannelUnit, channel_idx: ChannelIndex, mode: SMUMode, range_: float, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def set_sense_mode(self, channel_idx: ChannelIndex, sense_arg: SMUSense, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def set_measure_plc(self, channel_idx: ChannelIndex, value: float, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def set_measure_low_range(self, unit: ChannelUnit, channel_idx: ChannelIndex, value: float, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def set_measure_auto_zero(self, channel_idx: ChannelIndex, auto_zero: Autozero, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def set_measure_count(self, channel_idx: ChannelIndex, nr_of_measurements: int, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def set_source_function(self, channel_idx: ChannelIndex, src_func: SourceFunction, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def set_source_off_mode(self, channel_idx: ChannelIndex, src_off_mode: SourceOffMode, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def set_source_settling(self, channel_idx: ChannelIndex, src_settling: SourceSettling, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def toggle_source_sink(self, channel_idx: ChannelIndex, enable: bool, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def display_measure_function(self, channel_idx: ChannelIndex, diplay_measure_func: SMUDisplay,
                                 check_errors: bool = False) -> None:
        pass

    @abstractmethod
    def toggle_beep(self, enable: bool, check_errors: bool = False) \
            -> None:
        pass

    @abstractmethod
    def beep(self, duration: float, frequency: int, check_errors: bool = False) \
            -> None:
        pass
