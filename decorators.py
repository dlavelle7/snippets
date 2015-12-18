#!/usr/bin/env python
# -*- coding: utf-8 -*-


def log_ex_time(func):


def decorator_with_args(*dec_args, **dec_kwargs):
    def actual_decorator(func):
        def wrapped():
            print 'decorator args', dec_args, dec_kwargs
            print 'before function call'
            ret = func()
            print 'after function call'
            return ret
        return wrapped
    return actual_decorator





@decorator_with_args('dec1', blah='blah2')
def foo():
    print 'foo'

foo()
