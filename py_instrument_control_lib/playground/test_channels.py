from py_instrument_control_lib.channels.Channel import MeasureChannel, SourceChannel
from py_instrument_control_lib.channels.ChannelEnums import ChannelUnit, ChannelIndex
from py_instrument_control_lib.device_base.DeviceConfigs import TCPDeviceConfig
from py_instrument_control_lib.devices.KEI2600 import KEI2600
from py_instrument_control_lib.devices.KST33500 import KST33500

smu_config = TCPDeviceConfig(ip='132.231.14.169', port=5025, timeout=5)
smu = KEI2600(smu_config)
smu.connect()

sigg_config = TCPDeviceConfig(ip='132.231.14.172', port=5025, timeout=5)
sigg = KST33500(sigg_config)
sigg.connect()

source_channel_source: SourceChannel = smu.get_channel(ChannelIndex(1))
source_channel_measure: MeasureChannel = smu.get_channel(ChannelIndex(1))
other_channel_source: SourceChannel = smu.get_channel(ChannelIndex(2))
other_channel_measure: MeasureChannel = smu.get_channel(ChannelIndex(2))
gate_channel: SourceChannel = sigg.get_channel(ChannelIndex(1))

source_channel_source.toggle_buffering(True)

source_channel_source.toggle(True)
other_channel_source.toggle(True)
gate_channel.toggle(True)

source_channel_source.set_level(ChannelUnit.VOLTAGE, 1)
other_channel_source.set_level(ChannelUnit.VOLTAGE, 1)
gate_channel.set_level(ChannelUnit.VOLTAGE, 2)

print(source_channel_measure.measure(ChannelUnit.VOLTAGE))
print(source_channel_measure.measure(ChannelUnit.CURRENT))
print(other_channel_measure.measure(ChannelUnit.VOLTAGE))
print(other_channel_measure.measure(ChannelUnit.CURRENT))

source_channel_source.execute_buffered_script(True)
buff = source_channel_source.read_buffer()

source_channel_source.toggle(False)
other_channel_source.toggle(False)
gate_channel.toggle(False)

print(f'source_channel_measure.measure(ChannelUnit.VOLTAGE) = {source_channel_measure.next_buffer_element()}')
print(f'source_channel_measure.measure(ChannelUnit.CURRENT) = {source_channel_measure.next_buffer_element()}')
print(f'other_channel_measure.measure(ChannelUnit.VOLTAGE) = {other_channel_measure.next_buffer_element()}')
print(f'other_channel_measure.measure(ChannelUnit.CURRENT) = {other_channel_measure.next_buffer_element()}')

pass
