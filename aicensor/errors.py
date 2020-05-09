class AiCensorError(BaseException):
    def __init__(self, type: str, message: str):
        self._type = type
        self._message = message

    def get_type(self) -> str:
        return self._type

    def get_message(self) -> str:
        return self._message
