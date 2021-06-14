class ApiException(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code


class InputErrorException(ApiException):
    pass


class InsufficientArgsException(ApiException):
    pass
