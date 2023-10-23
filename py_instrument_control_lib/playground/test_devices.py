import time

from py_instrument_control_lib.device_base.DeviceConfigs import TCPDeviceConfig, SerialDeviceConfig
from py_instrument_control_lib.device_types.FunctionGenerator import *
from py_instrument_control_lib.device_types.Oscilloscope import *
from py_instrument_control_lib.device_types.PowerSupply import *
from py_instrument_control_lib.device_types.SMU import *
from py_instrument_control_lib.devices.KEI2600 import KEI2600
from py_instrument_control_lib.devices.KST3000 import KST3000
from py_instrument_control_lib.devices.KST33500 import KST33500
from py_instrument_control_lib.devices.SPD1305X import SPD1305X
from py_instrument_control_lib.devices.SwitchMatrix import SwitchMatrix


def test_smu() -> None:
    config = TCPDeviceConfig(ip='132.231.14.105', port=5025)
    smu: SMU = KEI2600(config)
    smu.connect()

    print(smu.measure(Unit.VOLTAGE, SMUChannel.CHANNEL_A))
    print(smu.measure(Unit.CURRENT, SMUChannel.CHANNEL_A))
    print(smu.measure(Unit.POWER, SMUChannel.CHANNEL_A))
    print(smu.measure(Unit.RESISTANCE, SMUChannel.CHANNEL_A))

    smu.toggle_channel(SMUChannel.CHANNEL_A, True)
    smu.set_level(Unit.VOLTAGE, SMUChannel.CHANNEL_A, 0.42)
    smu.set_limit(Unit.VOLTAGE, SMUChannel.CHANNEL_A, 0.69)
    smu.toggle_autorange(Unit.VOLTAGE, SMUChannel.CHANNEL_A, SMUMode.MEASURE, False)
    smu.toggle_measure_analog_filter(SMUChannel.CHANNEL_A, False)
    smu.set_range(Unit.VOLTAGE, SMUChannel.CHANNEL_A, SMUMode.MEASURE, 1.0)
    smu.set_sense_mode(SMUChannel.CHANNEL_A, SMUSense.LOCAL)
    smu.set_measure_plc(SMUChannel.CHANNEL_A, 1.0)
    smu.set_measure_low_range(Unit.VOLTAGE, SMUChannel.CHANNEL_A, 1.0)
    smu.set_measure_auto_zero(SMUChannel.CHANNEL_A, Autozero.AUTO)
    smu.set_measure_count(SMUChannel.CHANNEL_A, 10)
    smu.set_source_function(SMUChannel.CHANNEL_A, SourceFunction.DC_VOLTS)
    smu.set_source_off_mode(SMUChannel.CHANNEL_A, SourceOffMode.OUTPUT_ZERO)
    smu.set_source_settling(SMUChannel.CHANNEL_A, SourceSettling.SMOOTH)
    smu.toggle_source_sink(SMUChannel.CHANNEL_A, True)
    smu.display_measure_function(SMUChannel.CHANNEL_A, SMUDisplay.MEASURE_DC_VOLTS)
    smu.toggle_beep(True)
    smu.beep(0.3, 1000)

    smu.disconnect()


def test_fg() -> None:
    config = TCPDeviceConfig(ip='132.231.14.107', port=5025)
    fg: FunctionGenerator = KST33500(config)
    fg.connect()

    fg.toggle(True)
    fg.set_frequency(1000)
    fg.set_amplitude(3, '')
    fg.set_offset(4.2)
    fg.set_phase(1.0)
    fg.set_function(FunctionType.DC_VOLTAGE)
    fg.display('Funktioniert!')
    fg.set_pulsewidth(1000)

    fg.disconnect()


def test_uart_sm() -> None:
    config = SerialDeviceConfig(interface='/dev/ttyUSB0')
    matrix = UARTSwitchMatrix(config)
    matrix.connect()

    time.sleep(1)
    matrix.set_row_col(1, 1)

    matrix.disconnect()


def test_eth_sm() -> None:
    config = TCPDeviceConfig(ip='192.168.0.2', port=2000, timeout=2)
    matrix = SwitchMatrix(config)
    matrix.connect()

    time.sleep(1)
    matrix.set_row(4, True)
    matrix.set_col(10, True)
    matrix.set_row_col(1, 2, True)

    matrix.disconnect()


def test_ps() -> None:
    config = TCPDeviceConfig(ip='132.231.14.104', port=5025)
    ps: PowerSupply = SPD1305X(config)
    ps.connect()
    ps.set_voltage(PSChannel.CHANNEL_1, 12)
    ps.set_current(PSChannel.CHANNEL_1, 0.1)


def test_osc() -> None:
    config = TCPDeviceConfig(ip='132.231.14.115', port=5025)
    osc: KST3000 = KST3000(config)
    osc.connect()

    # print(osc.get_waveform_points())
    # time.sleep(0.3)
    # print(osc.get_waveform_preamble())
    # time.sleep(0.3)

    osc.run()
    time.sleep(1)
    osc.stop()
    osc.single()
    osc.auto_scale()

    osc.set_time_range(1)
    time.sleep(0.3)
    osc.set_channel_offset(OscChannel.CHANNEL_1, 1)
    time.sleep(0.3)
    osc.set_channel_scale(OscChannel.CHANNEL_1, 1)
    time.sleep(0.3)
    osc.set_channel_range(OscChannel.CHANNEL_1, 1, VoltageUnit.VOLT)
    time.sleep(0.3)
    osc.set_trigger_edge(TriggerEdge.POS_EDGE)
    time.sleep(0.3)
    osc.set_trigger_source(OscChannel.CHANNEL_1)
    time.sleep(0.3)
    osc.set_time_delay(1)
    time.sleep(0.3)
    osc.set_waveform_source(OscChannel.CHANNEL_1)
    time.sleep(0.3)
    print(osc.set_waveform_points(100))
    time.sleep(0.3)
    # osc.set_waveform_points_mode()
    osc.set_waveform_format(FileFormat.BYTE)
    time.sleep(0.3)
    # osc.save_waveform_data()
    print(osc.get_waveform_data())
    time.sleep(0.3)
    osc.get_real_data()
    time.sleep(0.3)
    osc.digitize(OscChannel.CHANNEL_1)
    time.sleep(0.3)
    print(osc.get_system_setup())
    time.sleep(0.3)
    osc.set_display_mode(DisplayModes.XY)
    time.sleep(0.3)
    osc.set_channel_display(OscChannel.CHANNEL_1, True)

    osc.disconnect()


if __name__ == '__main__':
    # test_smu()
    # test_fg(config)
    # test_uart_sm()
    test_eth_sm()
    # test_osc()
    # test_ps()
