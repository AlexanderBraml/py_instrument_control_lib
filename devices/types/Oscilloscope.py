from abc import ABC
from enum import Enum

from devices.Device import Device


class OscChannel(Enum):
    CHANNEL_1 = "1"
    CHANNEL_2 = "2"
    CHANNEL_3 = "3"
    CHANNEL_4 = "4"


class VoltageUnit(Enum):
    VOLT = ""
    MILLI_VOLT = ""


class TriggerEdge(Enum):
    POS_EDGE = "POS"
    NEG_EDGE = "NEG"
    EITHER = "EITH"
    ALTERNATING = "ALT"


class DisplayModes(Enum):
    MAIN = "MAIN"
    WIND = "WIND"
    XY = "XY"
    ROLL = "ROLL"


class FileFormat(Enum):
    ASCII = "ASCII"
    WORD = "WORD"
    BYTE = "BYTE"


class Oscilloscope(Device, ABC):

    def run(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def single(self) -> None:
        pass

    def auto_scale(self) -> None:
        pass

    def set_time_range(self, value: float) -> None:
        pass

    def set_channel_offset(self, channel: OscChannel, offset: float) -> None:
        pass

    def set_channel_scale(self, channel: OscChannel, value: float) -> None:
        pass

    def set_channel_range(self, channel: OscChannel, value: float, voltage_unit: VoltageUnit) -> None:
        pass

    def set_trigger_edge(self, edge: TriggerEdge) -> None:
        pass

    def set_trigger_source(self, channel: OscChannel) -> None:
        pass
