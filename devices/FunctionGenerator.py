from abc import abstractmethod, ABC
from enum import Enum

from devices.Device import Device


class FuncChannel(Enum):
    CHANNEL_A = ""
    CHANNEL_B = ""


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
    def toggle(self, enable: bool, check_errors: bool = False):
        pass

    @abstractmethod
    def set_frequency(self, frequency: float, check_errors: bool = False):
        pass

    @abstractmethod
    def set_amplitude(self, frequency: float, constrain: str, check_errors: bool = False):
        pass

    @abstractmethod
    def set_phase(self, phase: float, check_errors: bool = False):
        pass

    @abstractmethod
    def set_function(self, function: FunctionType, check_errors: bool = False):
        pass

    @abstractmethod
    def set_offset(self, offset: float, check_errors: bool = False):
        pass
