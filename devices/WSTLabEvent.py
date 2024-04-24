"""
This code is automatically generated from '../specifications/WSTLabEvent.json'.
Any changes made to this file are overwritten if you regenerate this module.
Only make changes in the source file.
"""

from math import isclose
from time import sleep

from py_instrument_control_lib.device_base.DeviceException import DeviceException
from py_instrument_control_lib.device_types.ClimateChamber import *
from py_instrument_control_lib.device_types.SMU import *
from py_instrument_control_lib.manufacturers.WeisstechnikDevice import WeisstechnikDevice


class WSTLabEvent(ClimateChamber, WeisstechnikDevice):

    def set_target_temperature(self, temperature: int, check_errors: bool = False) \
            -> None:
        self.execute(f'11001¶1¶1¶{temperature:.1f}')
        if check_errors:
            self.check_error_buffer()

    def set_target_humidity(self, humidity: int, check_errors: bool = False) \
            -> None:
        self.execute(f'11001¶1¶2¶{humidity:.1f}')
        if check_errors:
            self.check_error_buffer()

    def get_current_temperature(self, check_errors: bool = False) \
            -> float:
        val = self.query('11004¶1¶1')
        if check_errors:
            self.check_error_buffer()
        return float(val)

    def get_current_humidity(self, check_errors: bool = False) \
            -> float:
        val = self.query('11004¶1¶2')
        if check_errors:
            self.check_error_buffer()
        return float(val)

    def get_target_temperature(self, check_errors: bool = False) \
            -> float:
        val = self.query('11002¶1¶1')
        if check_errors:
            self.check_error_buffer()
        return float(val)

    def get_target_humidity(self, check_errors: bool = False) \
            -> float:
        val = self.query('11002¶1¶2')
        if check_errors:
            self.check_error_buffer()
        return float(val)

    def reset_errors(self, check_errors: bool = False) \
            -> None:
        self.execute('17012¶1')
        if check_errors:
            self.check_error_buffer()

    def get_status(self, check_errors: bool = False) \
            -> Status:
        val = self.query('10012¶1')
        if check_errors:
            self.check_error_buffer()
        return Status(int(val))

    def start(self, check_errors: bool = False) \
            -> None:
        self.execute('14001¶1¶1¶1')
        if check_errors:
            self.check_error_buffer()

    def stop(self, check_errors: bool = False) \
            -> None:
        self.execute('14001¶1¶1¶0')
        if check_errors:
            self.check_error_buffer()

    def wait_for_stable_conditions(self, time_in_seconds: int = 120, abs_tolerance_temp: float = 0.05, abs_tolerance_hum: float = 0.1, check_errors: bool = False) \
            -> None:
        target_temperature, target_humidity = self.get_target_data()
        history = [False] * time_in_seconds
        while any(flag is False for flag in history):
            temperature, humidity = self.get_current_data()
            history.pop()
            history.insert(0, isclose(temperature, target_temperature, abs_tol=abs_tolerance_temp)
                           and isclose(humidity, target_humidity, abs_tol=abs_tolerance_hum))
            sleep(1)

    def get_channel(self, channel_idx: ChannelIndex, check_errors: bool = False) \
            -> None:
        raise NotImplementedError('Channels are not supported when using a climate chamber.')

    def check_error_buffer(self, check_errors: bool = False) \
            -> None:
        if self._last_error is not None:
            raise DeviceException(msg=self._last_error)
