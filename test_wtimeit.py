import time

import wtimeit


def test_timeit_as_func(a, b):
    return sum([i*j for j in range(b) for i in range(a)])


@wtimeit.timeit(repeat=100)
def test_timeit_as_decorator(a, b):
    return sum([i*j for j in range(b) for i in range(a)])


if __name__ == '__main__':
    start = time.time()
    print(wtimeit.timeit(lambda: test_timeit_as_func(100, 1000), repeat=100))
    print(time.time() - start)

    start = time.time()
    print(test_timeit_as_decorator(100, 1000))
    print(time.time() - start)
