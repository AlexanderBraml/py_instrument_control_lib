from py_instrument_control_lib.channels.Channel import ChannelUnit, Channel
from py_instrument_control_lib.channels.MeasureChannel import MeasureChannel
from py_instrument_control_lib.channels.SourceChannel import SourceChannel
from py_instrument_control_lib.device_base.Device import Device


class SourceMeasureChannel(SourceChannel, MeasureChannel):

    def __init__(self, device: Device, channel_number: int, supported_source_units: list[ChannelUnit],
                 supported_measure_units: list[ChannelUnit]):
        self._device = device
        self._channel_number = channel_number
        self._supported_source_units = supported_source_units
        self._supported_measure_units = supported_measure_units
