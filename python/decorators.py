#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


def log_ex_time(original_func):
    def new_func():
       start = time.time()
       result = original_func()
       end = time.time()
       print "{0} secs".format(end - start)
       return result
    return new_func


def decorator_with_args(*dec_args, **dec_kwargs):
    def actual_decorator(original_func):
        def new_func():
            print 'decorator args', dec_args, dec_kwargs
            result = original_func()
            return result
        return new_func
    return actual_decorator


@decorator_with_args('dec1', blah='blah2')
def foo():
    print 'foo'

@log_ex_time
def bar():
    print 'bar'

foo()
bar()
