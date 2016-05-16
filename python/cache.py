#!/usr/bin/env python
"""
Caching decorator for storing fibonacci numbers.

Measure execution time with 'timeit' library. For example, output compared
without use of the @cache decorator:

With decorator      : 0.0364 secs
Without decorator   : 1.9738 secs
"""
import timeit


def cache_fibs(callable_func):
    """Decorator to cache known fibonacci numbers"""
    cache = dict()

    def wrapper(n):
        if n not in cache:
            cache[n] = callable_func(n)
        return cache[n]
    return wrapper


@cache_fibs
def fib(n):
    """Return nth fibonacci number"""
    sequence = [0, 1]
    if n < len(sequence):
        return sequence[n]
    while len(sequence) <= n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence.pop()


# Measure execution time with the timeit library
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

wrapped_func = wrapper(fib, 100)

print "Execution time: %s" % timeit.timeit(wrapped_func, number=100000)


# Test fib() function
true_fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
assert [fib(n) for n in range(len(true_fib))] == true_fib
