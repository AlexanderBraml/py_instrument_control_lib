import time
import logging

from device_base.DeviceConfigs import TCPDeviceConfig
from device_types.PowerSupply import PSChannel, PSMode
from devices.SPD1305X import SPD1305X

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

if __name__ == '__main__':
    # Log the start of the process
    logging.info("Starting the power supply configuration script...")

    # Initialize device configuration
    dev_config = TCPDeviceConfig(ip='132.231.14.109', port=5025, timeout=5)
    power_supply = SPD1305X(dev_config, requires_newline=False)

    logging.info("Connecting to the power supply...")
    power_supply.connect()
    time.sleep(0.3)

    logging.info(f"Set mode to 2Wire")
    power_supply.set_mode(PSMode.W2, True)
    time.sleep(0.1)

    voltage = 4
    logging.info(f"Setting voltage for CHANNEL_1 to {voltage}V...")
    power_supply.set_voltage(PSChannel.CHANNEL_1, voltage)
    time.sleep(0.1)

    current = 0.3
    logging.info(f"Setting current for CHANNEL_1 to {current}A...")
    power_supply.set_current(PSChannel.CHANNEL_1, current)
    time.sleep(0.3)

    logging.info("Toggling CHANNEL_1 ON...")
    power_supply.toggle(PSChannel.CHANNEL_1, True)
    time.sleep(0.3)

    logging.info("Get System Status")
    print(power_supply.get_system_status(True))
    time.sleep(0.3)

    logging.info("Getting voltage for CHANNEL_1...")
    ret = power_supply.get_voltage(PSChannel.CHANNEL_1, True)
    logging.info(f"Voltage reading for CHANNEL_1: {ret}")

    logging.info("Toggling CHANNEL_1 OFF...")
    power_supply.toggle(PSChannel.CHANNEL_1, False)

    logging.info("Disconnecting from the power supply...")
    power_supply.disconnect()

    logging.info("Power supply configuration script completed successfully.")
