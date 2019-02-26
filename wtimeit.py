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


def timeit(lambda_func=None, repeat=1, unit='', ndigits=5):
    if lambda_func:
        return wtimeit(lambda_func, repeat, unit, ndigits, return_result=False)
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            return wtimeit(lambda: func(*args, **kwargs),
                           repeat, unit, ndigits, func.__name__, True)
        return inner_wrapper
    return outer_wrapper



def wtimeit(lambda_func, repeat=1, unit='',
            ndigits=5, func_name=None, return_result=True):
    if not func_name:
        try:
            func_name = re.findall(
                'lambda: *(.+)\(', inspect.getsource(lambda_func))[0]
        except OSError:
            func_name = 'lambda'
    time = _timeit.timeit(lambda_func, number=repeat)
    result = lambda_func()
    print("time of '{name}': {t} {unit}".format(
        name=func_name,
        t=round((time / repeat) * UNITS[unit], ndigits),
        unit=unit + 'sec')
    )
    if return_result:
        return result
