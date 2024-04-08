import time

from py_instrument_control_lib.channels.Channel import SourceMeasureChannel
from py_instrument_control_lib.channels.ChannelEnums import ChannelUnit, ChannelIndex
from py_instrument_control_lib.device_base.DeviceConfigs import TCPDeviceConfig
from py_instrument_control_lib.device_types.SMU import SMUDisplay, SMUMode, SourceFunction, \
    SourceOffMode, SourceSettling, Autozero
from py_instrument_control_lib.devices.KEI2600 import KEI2600

smu_config = TCPDeviceConfig(ip='132.231.14.169', port=5025, timeout=5)
smu = KEI2600(smu_config)
smu.connect()

iterations = 2

smu.set_limit(ChannelUnit.CURRENT, ChannelIndex(1), 1)
smu.set_limit(ChannelUnit.CURRENT, ChannelIndex(2), 1)
smu.display_measure_function(ChannelIndex(1), SMUDisplay.MEASURE_DC_AMPS)
smu.display_measure_function(ChannelIndex(2), SMUDisplay.MEASURE_DC_VOLTS)
for channel in (ChannelIndex(1), ChannelIndex(2)):
    smu.toggle_measure_analog_filter(channel, True)
    smu.toggle_autorange(ChannelUnit.VOLTAGE, channel, SMUMode.MEASURE, True)
    smu.set_measure_plc(channel, 2)
    smu.set_measure_auto_zero(channel, Autozero.ONCE)
    smu.set_source_function(channel, SourceFunction.DC_VOLTS)
    smu.set_source_off_mode(channel, SourceOffMode.OUTPUT_ZERO)
    smu.set_source_settling(channel, SourceSettling.SMOOTH)
    smu.toggle_source_sink(channel, True)


voltages_1 = []
voltages_2 = []
currents_1 = []
currents_2 = []

channel_1: SourceMeasureChannel = smu.get_channel(ChannelIndex(1))
channel_2: SourceMeasureChannel = smu.get_channel(ChannelIndex(2))

channel_1.toggle_buffering(True)
channel_2.toggle_buffering(True)

smu.toggle_channel(ChannelIndex(1), True)
smu.toggle_channel(ChannelIndex(2), True)
smu.set_level(ChannelUnit.VOLTAGE, ChannelIndex(1), 1.42)
smu.set_level(ChannelUnit.VOLTAGE, ChannelIndex(2), 1)

for i in range(iterations):
    voltages_1.append(channel_1.measure(ChannelUnit.VOLTAGE))
    currents_1.append(channel_1.measure(ChannelUnit.CURRENT))
    voltages_2.append(channel_2.measure(ChannelUnit.VOLTAGE))
    voltages_1.append(channel_1.measure(ChannelUnit.VOLTAGE))
    currents_2.append(channel_2.measure(ChannelUnit.CURRENT))

channel_1.toggle(False)
channel_2.toggle(False)

channel_1.read_values(True, voltages_1, currents_1)
channel_2.read_values(True, voltages_2, currents_2)

pass
