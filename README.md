# The wrapper of timeit
Inspired by 

- [https://qiita.com/sw1227/items/09de9e6b501b2be79b54](https://qiita.com/sw1227/items/09de9e6b501b2be79b54)
- [timeit](https://docs.python.jp/3/library/timeit.html)
- [timeitd](https://github.com/canercidam/timeitd)


## Usage
```
import wtimeit


@wtimeit.wtimeit(repeat=100)
def test_decorator(a, b):
    return sum([i*j for j in range(b) for i in range(a)])


def test_func(a, b):
    return sum([i*j for j in range(b) for i in range(a)])


test_decorator(100, 1000)
wtimeit.timeit(lambda: test_func(100, 1000), repeat=100)
```
