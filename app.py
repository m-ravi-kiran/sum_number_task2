from errors import ApiException, InsufficientArgsException, InputErrorException


class Sum:
    def __init__(self, n=0):
        self.n = n

    def sum_numbers(self, *args):
        return sum(self.get_teen(i) for i in args)

    def get_teen(self, x):
        x = int(x)
        if x in (15, 16):
            return x
        elif x in range(13, 20):
            return 0
        return x

    def is_num(self, x):
        try:
            int(x)
        except ValueError:
            return False
        return True

    def validate(self, *args):
        if type(args) != tuple:
            raise ApiException('input has to be a list', status_code=400)
        if len(args) != self.n:
            raise InsufficientArgsException('Exactly 3 numbers are required', status_code=400)
        for i in args:
            if not self.is_num(i):
                raise InputErrorException('All inputs must be numeric', status_code=400)
        return True
