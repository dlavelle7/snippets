#!/usr/bin/env python


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
    return fib(n-1) + fib(n-2)


true_fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

assert [fib(n) for n in range(len(true_fib))] == true_fib
