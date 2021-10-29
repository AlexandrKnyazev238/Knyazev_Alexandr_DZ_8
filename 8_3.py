# Task_3

from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num_list = [el for el in (*args, *kwargs.values())]
        n = [f'{func.__name__}({el}: {type(el)})' for el in num_list]
        print(*n, *func(*args, **kwargs), sep=',\n')

    return wrapper


@type_logger
def calc_cube(*x, **y):
    num_list = [el for el in (*x, *y.values()) if isinstance(el, int) or isinstance(el, float)]
    return [i ** 3 for i in num_list]


print(calc_cube.__name__)
a = calc_cube(5, 23.8, {'Task': 8}, (238, 'someone'), {1, 2, 3}, [777, 888], 'Homework', name='Alex', mb=999, bmw=3.5)
