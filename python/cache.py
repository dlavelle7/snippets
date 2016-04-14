#!/usr/bin/env python


def cache_fibs(callable_func):
    cache = dict()
    def wrapper(n):
        if n not in cache:
            cache[n] = callable_func(n)
        return cache[n]
    return wrapper
        


#@cache_fibs
def fib(n):
    """Return nth fibonacci number"""
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print fib(4)
