from typing import Any

from py_instrument_control_lib.channels.ChannelEnums import ChannelIndex


class FutureValue:

    def __init__(self, channel_idx: ChannelIndex, buffer_index: int):
        self.channel_index = channel_idx
        self.buffer_index = buffer_index

    def get(self, buffer: list) -> Any:
        channel_buffer = buffer[self.channel_index.get() - 1]
        if not channel_buffer or len(channel_buffer) <= self.buffer_index:
            raise ValueError('Buffer is not filled appropriately.')
        return channel_buffer[self.buffer_index]

    def __repr__(self) -> str:
        return f'FutureValue @ {self.buffer_index} @ C{self.channel_index.get()}'
