from abc import ABC
from typing import Protocol, Any

from py_instrument_control_lib.channels.ChannelEnums import ChannelUnit, ChannelIndex


class ParentDevice(Protocol):

    def toggle_buffering(self, enable: bool) -> None:
        pass

    def execute_buffered_script(self, blocking: bool, check_errors: bool) -> None:
        pass

    def read_buffer(self, check_errors: bool) -> list:
        pass

    def next_buffer_element(self, channel_idx: ChannelIndex) -> Any:
        pass


class SourceDevice(ParentDevice, Protocol):

    def set_channel_level(self, unit: ChannelUnit, channel: ChannelIndex, value: float, check_errors: bool) -> None:
        pass

    def toggle_channel(self, channel: ChannelIndex, enable: bool, check_errors: bool) -> None:
        pass


class MeasureDevice(ParentDevice, Protocol):

    def measure_channel(self, unit: ChannelUnit, channel_number: ChannelIndex, check_errors: bool) -> float:
        pass


class Channel(ABC):

    def __init__(self, device: ParentDevice, channel_idx: ChannelIndex, supported_source_units: list[ChannelUnit],
                 supported_measure_units: list[ChannelUnit], buffering_available: bool = False):
        self._device = device
        self._channel_idx = channel_idx
        self._supported_source_units = supported_source_units
        self._supported_measure_units = supported_measure_units
        self._buffering_available = buffering_available

    def toggle_buffering(self, enable: bool) -> None:
        self.__check_buffering_available()
        self._device.toggle_buffering(enable)

    def execute_buffered_script(self, blocking: bool, check_errors: bool = False) -> None:
        self.__check_buffering_available()
        self._device.execute_buffered_script(blocking, check_errors)

    def read_buffer(self, check_errors: bool = False) -> list:
        self.__check_buffering_available()
        return self._device.read_buffer(check_errors)

    def next_buffer_element(self) -> Any:
        self.__check_buffering_available()
        return self._device.next_buffer_element(self._channel_idx)

    def __check_buffering_available(self) -> None:
        if not self._buffering_available:
            raise ValueError("Buffering is not available for this channel.")


class SourceChannel(Channel):
    _device: SourceDevice

    def __init__(self, device: ParentDevice, channel_idx: ChannelIndex, supported_source_units: list[ChannelUnit],
                 buffering_available: bool = False):
        super().__init__(device, channel_idx, supported_source_units, [], buffering_available)

    def set_level(self, unit: ChannelUnit, value: float, check_errors: bool = False) -> None:
        if unit not in self._supported_source_units:
            raise ValueError(f"Unit {unit} is not supported by this channel.")
        self._device.set_channel_level(unit, self._channel_idx, value, check_errors)

    def toggle(self, enabled: bool, check_errors: bool = False) -> None:
        self._device.toggle_channel(self._channel_idx, enabled, check_errors)


class MeasureChannel(Channel):
    _device: MeasureDevice

    def __init__(self, device: ParentDevice, channel_idx: ChannelIndex, supported_measure_units: list[ChannelUnit],
                 buffering_available: bool = False):
        super().__init__(device, channel_idx, [], supported_measure_units, buffering_available)

    def measure(self, unit: ChannelUnit, check_errors: bool = False) -> float:
        if unit not in self._supported_source_units:
            raise ValueError(f"Unit {unit} is not supported by this channel.")
        return self._device.measure_channel(unit, self._channel_idx, check_errors)


class SourceMeasureChannel(SourceChannel, MeasureChannel):

    def __init__(self, device: ParentDevice, channel_idx: ChannelIndex, supported_source_units: list[ChannelUnit],
                 supported_measure_units: list[ChannelUnit], buffering_available: bool = False):
        self._device = device
        self._channel_idx = channel_idx
        self._supported_source_units = supported_source_units
        self._supported_measure_units = supported_measure_units
        self._buffering_available = buffering_available
