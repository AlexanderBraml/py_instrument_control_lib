from enum import Enum


class ChannelUnit(Enum):
    VOLTAGE = 'v'
    CURRENT = 'i'
    RESISTANCE = 'r'
    POWER = 'p'


class ChannelIndex:

    def __init__(self, index: int) -> None:
        if index < 1:
            raise ValueError("Channel index must be greater than zero!")
        self._index = index

    def check(self, number_channels: int) -> None:
        if self._index > number_channels:
            raise ValueError(f"Channel index {self._index} is out of range! Max index is {number_channels}.")

    def get(self) -> int:
        return self._index
