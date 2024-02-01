from abc import ABC
from enum import Enum

from py_instrument_control_lib.device_base.Device import Device


class ChannelUnit(Enum):
    VOLTAGE = 'v'
    CURRENT = 'i'
    POWER = 'p'
    RESISTANCE = 'r'


class Channel(ABC):

    def __init__(self, device: Device, channel_number: int, supported_source_units: list[ChannelUnit],
                 supported_measure_units: list[ChannelUnit]):
        self._device = device
        self._channel_number = channel_number
        self._supported_source_units = supported_source_units
        self._supported_measure_units = supported_measure_units
