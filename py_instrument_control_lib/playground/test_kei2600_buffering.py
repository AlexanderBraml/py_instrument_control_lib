from py_instrument_control_lib.channels.ChannelEnums import ChannelUnit, ChannelIndex
from py_instrument_control_lib.device_base.DeviceConfigs import TCPDeviceConfig
from py_instrument_control_lib.device_types.SMU import SMUDisplay, SMUMode, SourceFunction, \
    SourceOffMode, SourceSettling, Autozero
from py_instrument_control_lib.devices.KEI2600 import KEI2600

smu_config = TCPDeviceConfig(ip='132.231.14.169', port=5025, timeout=5)
smu = KEI2600(smu_config)
smu.connect()
smu.toggle_buffering(True)

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
smu.toggle_channel(ChannelIndex(1), True)
smu.toggle_channel(ChannelIndex(2), True)
smu.set_level(ChannelUnit.VOLTAGE, ChannelIndex(1), 1)
smu.set_level(ChannelUnit.VOLTAGE, ChannelIndex(2), 1)
for i in range(0, 10):
    smu.measure(ChannelUnit.CURRENT, ChannelIndex(1))
    smu.measure(ChannelUnit.VOLTAGE, ChannelIndex(1))
    smu.measure(ChannelUnit.VOLTAGE, ChannelIndex(2))
    smu.measure(ChannelUnit.CURRENT, ChannelIndex(1))
    smu.measure(ChannelUnit.VOLTAGE, ChannelIndex(2))
smu.toggle_channel(ChannelIndex(1), False)
smu.toggle_channel(ChannelIndex(2), False)

smu.execute_buffered_script(blocking=True)
smu.read_buffer()
buff = smu.get_buffer()

for i in range(0, 10):
    print(f'smu.measure(ChannelUnit.CURRENT, ChannelIndex(1)) = {smu.next_buffer_element(ChannelIndex(1))}\n')
    print(f'smu.measure(ChannelUnit.VOLTAGE, ChannelIndex(1)) = {smu.next_buffer_element(ChannelIndex(1))}\n')
    print(f'smu.measure(ChannelUnit.VOLTAGE, ChannelIndex(2)) = {smu.next_buffer_element(ChannelIndex(2))}\n')
    print(f'smu.measure(ChannelUnit.CURRENT, ChannelIndex(1)) = {smu.next_buffer_element(ChannelIndex(1))}\n')
    print(f'smu.measure(ChannelUnit.VOLTAGE, ChannelIndex(2)) = {smu.next_buffer_element(ChannelIndex(2))}\n')

pass
