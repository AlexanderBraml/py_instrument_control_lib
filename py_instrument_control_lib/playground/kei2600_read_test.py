from py_instrument_control_lib.channels.ChannelEnums import ChannelIndex
from py_instrument_control_lib.device_base.DeviceConfigs import TCPDeviceConfig
from py_instrument_control_lib.devices.KEI2600 import KEI2600

smu_config = TCPDeviceConfig(ip='132.231.14.169', port=5025, timeout=5)
smu = KEI2600(smu_config)
smu.connect()
smu.toggle_channel(ChannelIndex(1), False)
smu.toggle_channel(ChannelIndex(2), False)

voltage = 1.3
current = 0.1
samples = 500
opposite_voltage_time = 0.1

script = f'''A_M_BUFFER = smua.makebuffer({samples})
A_M_BUFFER.appendmode = 1
smua.source.levelv = {voltage}
smua.source.leveli = {current}
smua.source.output = smua.OUTPUT_ON
delay({opposite_voltage_time})
smua.source.levelv = {voltage}
smua.source.leveli = {current}
smua.source.output = smua.OUTPUT_ON
for i = 1, {samples} do
    smua.measure.r(A_M_BUFFER)
end
smua.source.output = smua.OUTPUT_OFF'''.split('\n')

smu.send_execute_script(script, 'NewMemristorReadTest', blocking=True)
resistances = smu.read_buffer('A_M_BUFFER', samples)

print(resistances)

smu.disconnect()
