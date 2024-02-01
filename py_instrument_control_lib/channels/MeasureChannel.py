from py_instrument_control_lib.channels.Channel import Channel, ChannelUnit
from py_instrument_control_lib.device_base.Device import Device


class MeasureChannel(Channel):

    def __init__(self, device: Device, channel_number: int, supported_measure_units: list[ChannelUnit]):
        super().__init__(device, channel_number, [], supported_measure_units)

    def measure(self, unit: ChannelUnit, check_errors: bool = False) -> float:
        if unit not in self._supported_source_units:
            raise ValueError(f"Unit {unit} is not supported by this channel.")
        return self._device.measure_2(unit, self._channel_number, check_errors)
