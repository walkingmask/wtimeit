from functools import wraps
import inspect
import re
import timeit as _timeit


UNITS = {
    '': 1e1,
    'm': 1e3,
    'u': 1e6,
    'n': 1e9,
}


def timeit(lambda_func, repeat=1, unit='', ndigits=5, func_name=None):
    if not func_name:
        func_name = re.findall('lambda: *(.+)\(', inspect.getsource(lambda_func))[0]
    time = _timeit.timeit(lambda_func, number=repeat)
    result = lambda_func()
    print("time of '{name}': {t} {unit}".format(
        name=func_name,
        t=round(time / repeat * UNITS[unit], ndigits),
        unit=unit + 'sec')
    )
    return result


def wtimeit(repeat=1, unit='', ndigits=5):
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            return timeit(lambda: func(*args, **kwargs),
                          repeat=repeat, unit=unit, ndigits=ndigits,
                          func_name=func.__name__)
        return inner_wrapper
    return outer_wrapper

