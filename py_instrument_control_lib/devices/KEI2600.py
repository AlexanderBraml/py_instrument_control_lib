"""
This code is automatically generated from '../../specifications/KEI2600.json'.
Any changes made to this file are overwritten if you regenerate this module.
Only make changes in the source file.
"""

import copy
import time
from typing import Optional

import requests

from py_instrument_control_lib.channels.Channel import SourceMeasureChannel
from py_instrument_control_lib.device_base.DeviceException import DeviceException
from py_instrument_control_lib.device_types.SMU import *
from py_instrument_control_lib.manufacturers.KeithleyDevice import KeithleyDevice


class KEI2600(SMU, KeithleyDevice):

    def execute(self, command: str, check_errors: bool = False) \
            -> None:
        if hasattr(self, '_buffering_enabled') and self._buffering_enabled:
            self._buffered_script.append(command)
        else:
            super().execute(command)

    def query(self, query: str, check_errors: bool = False) \
            -> Optional[str]:
        if hasattr(self, '_buffering_enabled') and self._buffering_enabled:
            buffer_name = 'A_M_BUFFER' if query.startswith('smua') else 'B_M_BUFFER'
            query = query[:-1] + buffer_name + ')'
            self._buffered_script.append(query)
            return "inf"
        else:
            command = 'reading = ' + query
            self.execute(command)
            self.execute('print(reading)')
            response = self._socket.recv(1024)
            response_decoded = response.decode()
            if 'TSP>' in response_decoded:
                raise DeviceException(msg='Do not use the web interface before or during use of this control lib! '
                                          'You have to restart your device in order to continue.')
            return response_decoded

    def measure(self, unit: ChannelUnit, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> float:
        """
        This function measures a certain unit on a specific channel. Can be used to measure voltage, current, power or resistance.
        :param unit: The thing to measure.
        :param channel_idx: The channel to measure on.
        :param check_errors: Whether to check the error buffer after the execution.
        :return: None.
        """
        val = self.query(f'{self.__to_channel(channel_idx)}.measure.{unit.value}()')
        if check_errors:
            self.check_error_buffer()
        return float(val)

    def __to_channel(self, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> str:
        channel_idx.check(2)
        return 'smua' if channel_idx.get() == 1 else 'smub'

    def toggle_channel(self, channel_idx: ChannelIndex, enable: bool, check_errors: bool = False) \
            -> None:
        self.execute(
            f'{self.__to_channel(channel_idx)}.source.output = {self.__to_channel(channel_idx)}.OUTPUT_{("ON" if enable else "OFF")}')
        if check_errors:
            self.check_error_buffer()

    def set_level(self, unit: ChannelUnit, channel_idx: ChannelIndex, level: float, check_errors: bool = False) \
            -> None:
        if not (unit in (ChannelUnit.VOLTAGE, ChannelUnit.CURRENT)):
            raise ValueError('Requirements not satisfied')

        self.execute(f'{self.__to_channel(channel_idx)}.source.level{unit.value} = {level}')
        if check_errors:
            self.check_error_buffer()

    def set_limit(self, unit: ChannelUnit, channel_idx: ChannelIndex, limit: float, check_errors: bool = False) \
            -> None:
        if not (unit in (ChannelUnit.VOLTAGE, ChannelUnit.CURRENT, ChannelUnit.POWER)):
            raise ValueError('Requirements not satisfied')

        self.execute(f'{self.__to_channel(channel_idx)}.source.limit{unit.value} = {str(limit)}')
        if check_errors:
            self.check_error_buffer()

    def toggle_autorange(self, unit: ChannelUnit, channel_idx: ChannelIndex, mode: SMUMode, enable: bool, check_errors: bool = False) \
            -> None:
        if not (unit in (ChannelUnit.VOLTAGE, ChannelUnit.CURRENT)):
            raise ValueError('Requirements not satisfied')

        self.execute(f'{self.__to_channel(channel_idx)}.{mode.value}.autorange{unit.value} = {int(enable) if mode == SMUMode.MEASURE else self.__to_channel(channel_idx) + ".AUTORANGE_" + ("ON" if enable else "OFF")}')
        if check_errors:
            self.check_error_buffer()

    def toggle_measure_analog_filter(self, channel_idx: ChannelIndex, enable: bool, check_errors: bool = False) \
            -> None:
        self.execute(f'{self.__to_channel(channel_idx)}.measure.analogfilter = {int(enable)}')
        if check_errors:
            self.check_error_buffer()

    def set_range(self, unit: ChannelUnit, channel_idx: ChannelIndex, mode: SMUMode, range_: float, check_errors: bool = False) \
            -> None:
        if not (unit in (ChannelUnit.VOLTAGE, ChannelUnit.CURRENT)):
            raise ValueError('Requirements not satisfied')

        self.execute(f'{self.__to_channel(channel_idx)}.{mode.value}.range{unit.value} = {range_}')
        if check_errors:
            self.check_error_buffer()

    def set_sense_mode(self, channel_idx: ChannelIndex, sense_arg: SMUSense, check_errors: bool = False) \
            -> None:
        self.execute(f'{self.__to_channel(channel_idx)}.sense = {self.__to_channel(channel_idx)}.{sense_arg.value}')
        if check_errors:
            self.check_error_buffer()

    def set_measure_plc(self, channel_idx: ChannelIndex, value: float, check_errors: bool = False) \
            -> None:
        if not (0.001 < value < 25):
            raise ValueError('Requirements not satisfied')

        self.execute(f'{self.__to_channel(channel_idx)}.measure.nplc = {value}')
        if check_errors:
            self.check_error_buffer()

    def set_measure_low_range(self, unit: ChannelUnit, channel_idx: ChannelIndex, value: float, check_errors: bool = False) \
            -> None:
        if not (unit in (ChannelUnit.VOLTAGE, ChannelUnit.CURRENT)):
            raise ValueError('Requirements not satisfied')

        self.execute(f'{self.__to_channel(channel_idx)}.measure.lowrange{unit.value} = {value}')
        if check_errors:
            self.check_error_buffer()

    def set_measure_auto_zero(self, channel_idx: ChannelIndex, auto_zero: Autozero, check_errors: bool = False) \
            -> None:
        self.execute(f'{self.__to_channel(channel_idx)}.measure.autozero = {self.__to_channel(channel_idx)}.{auto_zero.value}')
        if check_errors:
            self.check_error_buffer()

    def set_measure_count(self, channel_idx: ChannelIndex, nr_of_measurements: int, check_errors: bool = False) \
            -> None:
        self.execute(f'{self.__to_channel(channel_idx)}.measure.count = {nr_of_measurements}')
        if check_errors:
            self.check_error_buffer()

    def set_source_function(self, channel_idx: ChannelIndex, src_func: SourceFunction, check_errors: bool = False) \
            -> None:
        self.execute(f'{self.__to_channel(channel_idx)}.source.func = {self.__to_channel(channel_idx)}.{src_func.value}')
        if check_errors:
            self.check_error_buffer()

    def set_source_off_mode(self, channel_idx: ChannelIndex, src_off_mode: SourceOffMode, check_errors: bool = False) \
            -> None:
        self.execute(f'{self.__to_channel(channel_idx)}.source.offmode = {self.__to_channel(channel_idx)}.{src_off_mode.value}')
        if check_errors:
            self.check_error_buffer()

    def set_source_settling(self, channel_idx: ChannelIndex, src_settling: SourceSettling, check_errors: bool = False) \
            -> None:
        self.execute(
            f'{self.__to_channel(channel_idx)}.source.settling = {self.__to_channel(channel_idx)}.{src_settling.value}')
        if check_errors:
            self.check_error_buffer()

    def toggle_source_sink(self, channel_idx: ChannelIndex, enable: bool, check_errors: bool = False) \
            -> None:
        self.execute(f'{self.__to_channel(channel_idx)}.source.sink = {str(int(enable))}')
        if check_errors:
            self.check_error_buffer()

    def display_measure_function(self, channel_idx: ChannelIndex, diplay_measure_func: SMUDisplay, check_errors: bool = False) \
            -> None:
        self.execute(f'display.{self.__to_channel(channel_idx)}.measure.func = display.{diplay_measure_func.value}')
        if check_errors:
            self.check_error_buffer()

    def toggle_beep(self, enable: bool, check_errors: bool = False) \
            -> None:
        self.execute(f'beeper.enable = beeper.{"ON" if enable else "OFF"}')
        if check_errors:
            self.check_error_buffer()

    def beep(self, duration: float, frequency: int, check_errors: bool = False) \
            -> None:
        """
        Send a beeping sound with a specific duration and frequency to the SMU.
        :param duration: Time in seconds to play the beeping sound.
        :param frequency: Frequency in HZ of the sound to play.
        :param check_errors: Whether to check the error buffer after the execution.
        :return: None.
        """
        self.execute(f'beeper.beep({duration}, {frequency})')
        if check_errors:
            self.check_error_buffer()

    def toggle_buffering(self, enable: bool, check_errors: bool = False) \
            -> None:
        self._buffering_enabled = enable
        if not hasattr(self, '_buffered_script'):
            self._buffered_script = []

    def execute_buffered_script(self, blocking: bool = True, script_name: str = 'BufferedScript', check_errors: bool = False) \
            -> None:
        for buffer in ('A_M_BUFFER', 'B_M_BUFFER'):
            buffer_entries = len([line for line in self._buffered_script if buffer in line])
            self._buffered_script.insert(0, f'{buffer} = smu{buffer[0].lower()}.makebuffer({buffer_entries})')
            self._buffered_script.insert(1, f'{buffer}.appendmode = 1')
        self.send_execute_script(self._buffered_script, script_name, blocking)
        self._buffer = None

    def send_script(self, script: list[str] | str, script_name: str, check_errors: bool = False) \
            -> None:
        if isinstance(script, str):
            script = script.split('\n')
        script = [f'loadscript {script_name}', *script, 'endscript']

        chunk_size = 32
        chunks = [script[i:i + chunk_size] for i in range(0, len(script), chunk_size)]
        exit_payload: dict = {'command': 'keyInput', 'value': 'K'}
        payloads: list[dict] = [exit_payload,
                                *[self.__make_payload('\n'.join(chunk)) for chunk in chunks],
                                self.__make_payload(f'{script_name}.save()'),
                                exit_payload]

        for payload in payloads:
            response = requests.post('http://' + self._config.ip + '/HttpCommand', json=payload)
            if response.status_code != 200:
                raise DeviceException(msg='Failed to send and execute buffered script')
            time.sleep(0.5)

    def execute_script(self, script_name: str, blocking: bool = True, check_errors: bool = False) \
            -> None:
        buffering_enabled = hasattr(self, '_buffering_enabled') and self._buffering_enabled
        self.toggle_buffering(False)
        self.execute(f'{script_name}()')
        self.toggle_buffering(buffering_enabled)

        if blocking:
            time.sleep(2)
            poll_payload = {"command": "shellOutput", "timeout": 3, "acceptsMultiple": True}
            print('Waiting for script to complete')
            status = requests.post('http://' + self._config.ip + '/HttpCommand', json=poll_payload)
            while status.json()['status']['value'] == 'timeout':
                status = requests.post('http://' + self._config.ip + '/HttpCommand', json=poll_payload)
            print('Script finished')

    def send_execute_script(self, script: list[str] | str, script_name: str, blocking: bool = True, check_errors: bool = False) \
            -> None:
        self.send_script(script, script_name)
        self.execute_script(script_name, blocking)

    def __make_payload(self, value: str, check_errors: bool = False) \
            -> dict:
        return {'command': 'shellInput', 'value': value}

    def read_channel_buffers(self, script: list[str] = None, check_errors: bool = False) \
            -> list[list[str]]:
        if script is None:
            script = self._buffered_script
        buffering_enabled = hasattr(self, '_buffering_enabled') and self._buffering_enabled
        self.toggle_buffering(False)
        self._buffer = [self.read_channel_buffer(script, ChannelIndex(
            1)), self.read_channel_buffer(script, ChannelIndex(2))]
        self.toggle_buffering(buffering_enabled)
        return copy.deepcopy(self._buffer)

    def read_channel_buffer(self, script: list[str], channel_idx: ChannelIndex, check_errors: bool = False) \
            -> list[str]:
        channel_idx.check(2)
        buffer_name = ('A' if channel_idx.get() == 1 else 'B') + '_M_BUFFER'
        buffer_size = len([line for line in script if buffer_name in line]) - 2
        return self.read_buffer(buffer_name, buffer_size, check_errors)

    def read_buffer(self, buffer_name: str, buffer_size: int, check_errors: bool = False) \
            -> list[str]:
        batch_size = 1024 // 15
        buffer = []
        offset = 1
        while offset + batch_size <= buffer_size:
            buffer += self.__get_buffer_content(offset, batch_size, buffer_name)
            offset += batch_size
        if (remaining := buffer_size % batch_size) > 0:
            buffer += self.__get_buffer_content(offset, remaining, buffer_name)

        self.execute(f'{buffer_name}.clear()')
        return buffer

    def get_buffer(self, check_errors: bool = False) \
            -> list[list[str]]:
        return copy.deepcopy(self._buffer) if hasattr(self, '_buffer') else None

    def __get_buffer_content(self, offset: int, batch_size: int, buffer_name: str, check_errors: bool = False) \
            -> list[str]:
        print_query = f'printbuffer({offset}, {offset + batch_size - 1}, {buffer_name})'
        self.execute(print_query)
        return self._socket.recv(1024).decode().replace('\n', '').split(', ')

    def next_buffer_element(self, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> float:
        channel_idx.check(2)
        if len(self._buffer) == 0:
            raise Exception('Buffer is empty!')
        buffer_idx = channel_idx.get() - 1
        return float(self._buffer[buffer_idx].pop(0))

    def set_channel_level(self, unit: ChannelUnit, channel_idx: ChannelIndex, level: float, check_errors: bool = False) \
            -> None:
        channel_idx.check(2)
        self.set_level(unit, channel_idx, level)

    def measure_channel(self, unit: ChannelUnit, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> float:
        channel_idx.check(2)
        return self.measure(unit, channel_idx)

    def get_channel(self, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> SourceMeasureChannel:
        return SourceMeasureChannel(self, channel_idx, [ChannelUnit.VOLTAGE, ChannelUnit.CURRENT], [ChannelUnit.VOLTAGE, ChannelUnit.CURRENT, ChannelUnit.POWER, ChannelUnit.RESISTANCE], True)

    def perform_linear_voltage_sweep(self, channel_idx: ChannelIndex, start_voltage: float, stop_voltage: float, increase_rate: float, current: float, blocking: bool = True, check_errors: bool = False) \
            -> None:
        precision = 1000
        factor = 1 if start_voltage <= stop_voltage else -1
        script = f'''channel = {self.__to_channel(channel_idx)}
        channel.source.func = channel.OUTPUT_DCVOLTS
        channel.source.output = channel.OUTPUT_ON
        channel.source.limitv = {factor * stop_voltage} + 0.1
        channel.source.limiti = {current} + 0.0001
        channel.source.leveli = {current}
        for current_voltage = {factor * start_voltage * precision}, {factor * stop_voltage * precision} do
            channel.source.levelv = {factor} * current_voltage / {precision}
            delay(1 / {increase_rate * precision})
            end
        channel.source.output = channel.OUTPUT_OFF'''
        self.send_execute_script(script, "LinearVoltageSweep", blocking)
