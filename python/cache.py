#!/usr/bin/env python
import timeit


def cache_fibs(callable_func):
    cache = dict()

    def wrapper(n):
        if n not in cache:
            cache[n] = callable_func(n)
        return cache[n]

    return wrapper


@cache_fibs
def fib(n):
    """Return nth fibonacci number"""
    if n < 2:
        return n
    val1 = fib(n-1)
    val2 = fib(n-2)
    return val1 + val2


true_fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
assert [fib(n) for n in range(len(true_fib))] == true_fib


# Measure execution time with timeit library
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

wrapped_func = wrapper(fib, 40)

print timeit.timeit(wrapped_func, number=1)

"""
Compare without @cache decorator

Output:

With cache decorator   : instantaneous
Without cach decorator : 43 secs
"""
