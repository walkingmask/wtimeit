# The wrapper of timeit
Inspired by 

- [https://qiita.com/sw1227/items/09de9e6b501b2be79b54](https://qiita.com/sw1227/items/09de9e6b501b2be79b54)
- [timeit](https://docs.python.jp/3/library/timeit.html)
- [timeitd](https://github.com/canercidam/timeitd)


## Usage
```
import wtimeit


def test_func(a, b):
    return sum([i*j for j in range(b) for i in range(a)])


def test_timeit():
    return wtimeit.timeit(lambda: test_func(100, 1000))


@wtimeit.wtimeit()
def test_wtimeit():
    return test_func(100, 1000)
```
