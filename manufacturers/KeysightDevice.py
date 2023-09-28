from abc import ABC

from devices.TCPDevice import TCPDevice


class KeysightDevice(TCPDevice, ABC):

    def query(self, query: str) -> str:
        self.execute(query)
        response = self._socket.recv(1024)

        return response.decode()

    def disconnect(self) -> None:
        self._socket.close()