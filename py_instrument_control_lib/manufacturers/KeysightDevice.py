from abc import ABC

from py_instrument_control_lib.device_base.TCPDevice import TCPDevice


class KeysightDevice(TCPDevice, ABC):

    def query(self, query: str) -> str:
        self.execute(query)
        response = self._socket.recv(1024)

        return response.decode()

    def disconnect(self) -> None:
        self._socket.close()
