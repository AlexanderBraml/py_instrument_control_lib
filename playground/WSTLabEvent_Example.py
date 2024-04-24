from py_instrument_control_lib.device_base.DeviceConfigs import TCPDeviceConfig
from py_instrument_control_lib.device_types.ClimateChamber import ClimateChamber
from py_instrument_control_lib.devices.WSTLabEvent import WSTLabEvent

if __name__ == '__main__':
    config = TCPDeviceConfig(ip='132.231.14.180', port=2049, timeout=10)
    chamber: ClimateChamber = WSTLabEvent(config)
    chamber.connect()
    chamber.set_target_temperature(30)
    chamber.set_target_humidity(70)
    chamber.start()
    chamber.wait_for_stable_conditions(time_in_seconds=10, abs_tolerance_temp=3, abs_tolerance_hum=5)
    chamber.disconnect()
