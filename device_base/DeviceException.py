from enum import Enum


class ErrorCode(Enum):
    TIMEOUT = "Socket timeout"
    ERRNO = "Errno"
    INTERFACE_CLOSED = "Socket is closed"
    INVALID_BAUDRATE = "Baudrate not supported"
    ITEM_IN_ERROR_QUEUE = "Item in error queue"


class DeviceException(Exception):

    def __init__(self, msg="", error=None, method=None, params=None) -> None:
        """
        Initializes the exception.

        :param msg: The message to display.
        :param error: The error code of the instrument.
        :param method: The method that returned the faulty error code.
        :param params: The params of the method that returned the faulty error code.
        """
        super().__init__(msg)

        self.msg = msg
        self.error_code: ErrorCode = error
        self.method = method
        self.params = params

    def __str__(self) -> str:
        if self.msg and self.error_code:
            return f'Device Error: {self.msg}, {self.error_code.value}'
        elif self.msg:
            return f'Device Error: {self.msg}'
        elif self.method and self.params:
            return f'Calling {self.method.__name__}{self.params} failed because: {self.error_code.value}'
        else:
            return self.error_code.value
