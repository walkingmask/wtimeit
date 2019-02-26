import wtimeit


def test_func(a, b):
    return sum([i*j for j in range(b) for i in range(a)])


def test_timeit():
    return wtimeit.timeit(lambda: test_func(100, 1000))


@wtimeit.wtimeit()
def test_wtimeit(a, b):
    return test_func(a, b)



if __name__ == '__main__':
    print(test_timeit())
    print(test_wtimeit(100, 1000))
