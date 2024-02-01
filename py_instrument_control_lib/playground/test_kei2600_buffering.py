from py_instrument_control_lib.device_base.DeviceConfigs import TCPDeviceConfig
from py_instrument_control_lib.device_types.SMU import SMUChannel, Unit, SMUDisplay, SMUMode, SourceFunction, \
    SourceOffMode, SourceSettling, Autozero
from py_instrument_control_lib.devices.KEI2600 import KEI2600

smu_config = TCPDeviceConfig(ip='132.231.14.169', port=5025, timeout=5)
smu = KEI2600(smu_config)
smu.connect()
smu.toggle_buffering(True)

smu.set_limit(Unit.CURRENT, SMUChannel.CHANNEL_A, 1)
smu.set_limit(Unit.CURRENT, SMUChannel.CHANNEL_B, 1)
smu.display_measure_function(SMUChannel.CHANNEL_A, SMUDisplay.MEASURE_DC_AMPS)
smu.display_measure_function(SMUChannel.CHANNEL_B, SMUDisplay.MEASURE_DC_VOLTS)
for channel in (SMUChannel.CHANNEL_A, SMUChannel.CHANNEL_B):
    smu.toggle_measure_analog_filter(channel, True)
    smu.toggle_autorange(Unit.VOLTAGE, channel, SMUMode.MEASURE, True)
    smu.set_measure_plc(channel, 2)
    smu.set_measure_auto_zero(channel, Autozero.ONCE)
    smu.set_source_function(channel, SourceFunction.DC_VOLTS)
    smu.set_source_off_mode(channel, SourceOffMode.OUTPUT_ZERO)
    smu.set_source_settling(channel, SourceSettling.SMOOTH)
    smu.toggle_source_sink(channel, True)
smu.toggle_channel(SMUChannel.CHANNEL_A, True)
smu.toggle_channel(SMUChannel.CHANNEL_B, True)
smu.set_level(Unit.VOLTAGE, SMUChannel.CHANNEL_A, 1)
smu.set_level(Unit.VOLTAGE, SMUChannel.CHANNEL_B, 1)
for i in range(0, 10):
    smu.measure(Unit.CURRENT, SMUChannel.CHANNEL_A)
    smu.measure(Unit.VOLTAGE, SMUChannel.CHANNEL_A)
    smu.measure(Unit.VOLTAGE, SMUChannel.CHANNEL_B)
    smu.measure(Unit.CURRENT, SMUChannel.CHANNEL_A)
    smu.measure(Unit.VOLTAGE, SMUChannel.CHANNEL_B)
smu.toggle_channel(SMUChannel.CHANNEL_A, False)
smu.toggle_channel(SMUChannel.CHANNEL_B, False)

smu.execute_buffered_script(blocking=True)
smu.read_buffer()
buff = smu.get_buffer()

for i in range(0, 10):
    print(f'smu.measure(Unit.CURRENT, SMUChannel.CHANNEL_A) = {smu.next_buffer_element(SMUChannel.CHANNEL_A)}\n')
    print(f'smu.measure(Unit.VOLTAGE, SMUChannel.CHANNEL_A) = {smu.next_buffer_element(SMUChannel.CHANNEL_A)}\n')
    print(f'smu.measure(Unit.VOLTAGE, SMUChannel.CHANNEL_B) = {smu.next_buffer_element(SMUChannel.CHANNEL_B)}\n')
    print(f'smu.measure(Unit.CURRENT, SMUChannel.CHANNEL_A) = {smu.next_buffer_element(SMUChannel.CHANNEL_A)}\n')
    print(f'smu.measure(Unit.VOLTAGE, SMUChannel.CHANNEL_B) = {smu.next_buffer_element(SMUChannel.CHANNEL_B)}\n')

pass
