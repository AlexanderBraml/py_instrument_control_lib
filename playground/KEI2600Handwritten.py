from devices.types.SMU import SMU, SMUChannel, Unit, SMUMode
from devices.TCPDevice import TCPDevice


class KEI2600Handwritten(SMU, TCPDevice):

    def measure(self, unit: Unit, channel: SMUChannel, ceb: bool = False) -> float:
        response = self.query(channel.value + 'measure' + '()')
        return float(response)

    def toggle_channel(self, channel: SMUChannel, enable: bool, ceb: bool = False) -> None:
        self.execute(channel.value + '.source.output' + ' = ' + 'OUTPUT_' + ('ON' if enable else 'OFF'))

    def set_level(self, unit: Unit, channel: SMUChannel, level: float, ceb: bool = False) -> None:
        assert unit in (Unit.VOLTAGE, Unit.CURRENT), 'Invalid arguments'
        self.execute(channel.value + '.source.level' + unit.value + ' = ' + str(level))

    def set_limit(self, unit: Unit, channel: SMUChannel, limit: float, ceb: bool = False) -> None:
        assert unit in (Unit.VOLTAGE, Unit.CURRENT, Unit.POWER), 'Invalid arguments'
        self.execute(channel.value + '.source.limit' + unit.value + ' = ' + str(limit))

    def toggle_autorange(self, unit: Unit, channel: SMUChannel, mode: SMUMode, enable: bool, ceb: bool = False) -> None:
        assert unit in (Unit.VOLTAGE, Unit.CURRENT), 'Invalid arguments'
        val = str(int(enable)) if mode == SMUMode.MEASURE else 'AUTORANGE_' + ('ON' if enable else 'OFF')
        self.execute(channel.value + '.' + mode.value + '.autorange' + unit.value + ' = ' + val)

    def toggle_measure_analog_filter(self, channel: SMUChannel, enable: bool, ceb: bool = False) -> None:
        self.execute(channel.value + '.measure.analogfilter = ' + str(int(enable)))
