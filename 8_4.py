# Task_4

from functools import wraps


def val_checker(checker):
    def val_callback(callback):

        @wraps(callback)
        def wrapper(msg):
            if checker(msg):
                print(callback(msg))
            else:
                raise ValueError(f'wrong val {msg}')

        return wrapper

    return val_callback


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(5)
    print(help(calc_cube))
except (ValueError, TypeError) as err:
    print(err)
