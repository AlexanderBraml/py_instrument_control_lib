from py_instrument_control_lib.channels.ChannelEnums import ChannelIndex
from py_instrument_control_lib.device_base.DeviceConfigs import TCPDeviceConfig
from py_instrument_control_lib.devices.KEI2600 import KEI2600

smu_config = TCPDeviceConfig(ip='132.231.14.169', port=5025, timeout=5)
smu = KEI2600(smu_config)
smu.connect()

smu.perform_linear_voltage_sweep(ChannelIndex(1), 0, 2, 0.1, 0.3, True)

smu.disconnect()
