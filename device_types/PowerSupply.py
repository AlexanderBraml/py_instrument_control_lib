from abc import ABC
from enum import Enum

from py_instrument_control_lib.device_base.Device import Device


class PSChannel(Enum):
    CHANNEL_1 = "CH1"
    CHANNEL_2 = "CH2"


class PSUnit(Enum):
    CURRENT = "CURRent"
    VOLTAGE = "VOLTage"
    POWER = "POWEr"


class PSMode(Enum):
    W2 = "2W"
    W4 = "4W"


class PowerSupply(Device, ABC):  # TODO: TCPDevice was here previously, mistake?

    def toggle(self, channel: PSChannel, enable: bool) -> None:
        pass

    def set_current(self, channel: PSChannel, current: float) -> None:
        pass

    def set_voltage(self, channel: PSChannel, voltage: float) -> None:
        pass
