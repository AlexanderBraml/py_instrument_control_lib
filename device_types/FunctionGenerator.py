from abc import abstractmethod, ABC
from enum import Enum

from py_instrument_control_lib.channels.ChannelEnums import ChannelIndex
from py_instrument_control_lib.device_base.Device import Device


class FuncChannel(Enum):
    CHANNEL_A = "A"
    CHANNEL_B = "B"


class FGUnit(Enum):
    CURRENT = "CURRent"
    VOLTAGE = "VOLTage"
    POWER = "POWEr"


class FunctionType(Enum):
    SINUS = "SIN"
    SQUARE = "SQU"
    RAMP = "RAMP"
    NEGATIVE_RAMP = "NRAM"
    TRIANGLE = "TRI"
    NOISE = "NOIS"
    PSEUDO_RANDOM_BIT_STREAM = "PRBS"
    ARBITRARY = "ARB"
    DC_VOLTAGE = "DC"


class FunctionGenerator(Device, ABC):

    @abstractmethod
    def toggle(self, channel_idx: ChannelIndex, enable: bool, check_errors: bool = False):
        pass

    @abstractmethod
    def set_frequency(self, channel_idx: ChannelIndex, frequency: float, check_errors: bool = False):
        pass

    @abstractmethod
    def set_amplitude(self, channel_idx: ChannelIndex, frequency: float, constrain: str, check_errors: bool = False):
        pass

    @abstractmethod
    def set_phase(self, channel_idx: ChannelIndex, phase: float, check_errors: bool = False):
        pass

    @abstractmethod
    def set_function(self, channel_idx: ChannelIndex, function: FunctionType, check_errors: bool = False):
        pass

    @abstractmethod
    def set_offset(self, channel_idx: ChannelIndex, offset: float, impedance: float = float('inf'), check_errors: bool = False):
        pass

    @abstractmethod
    def set_impedance(self, channel_idx: ChannelIndex, impedance: float):
        pass
