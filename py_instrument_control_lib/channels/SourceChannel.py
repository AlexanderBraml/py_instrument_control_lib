from py_instrument_control_lib.channels.Channel import Channel, ChannelUnit
from py_instrument_control_lib.device_base.Device import Device


class SourceChannel(Channel):

    def __init__(self, device: Device, channel_number: int, supported_source_units: list[ChannelUnit]):
        super().__init__(device, channel_number, supported_source_units, [])

    def set_level(self, unit: ChannelUnit, value: float, check_errors: bool = False) -> None:
        if unit not in self._supported_source_units:
            raise ValueError(f"Unit {unit} is not supported by this channel.")
        self._device.set_level_2(unit, self._channel_number, value, check_errors)
