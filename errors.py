class ApiException(Exception):
    """Exception for raising exceptions for APIs."""

    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code


class InvalidInputsException(ApiException):
    """Exception used for invalid inputs."""
    pass


class InsufficientNumbersException(ApiException):
    """Exception used if the numbers sent are not exactly 3."""
    pass
