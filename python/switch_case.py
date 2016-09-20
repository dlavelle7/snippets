#!/usr/bin/env python
"""Switch/case control statement in Python

Also included is a handy pattern for delegating work based on Class,
where inheritance for example may not be practical.
"""


def do_a(data):
    print "do_a() with '{0}'".format(data)


def do_b(data):
    print "do_b() with '{0}'".format(data)


def do_c(data):
    print "do_c() with '{0}'".format(data)


def do_default(data):
    print "do_default() with '{0}'".format(data)


def switch(caseStatement):
    switches = {
        'A': do_a,
        'B': do_b,
        'C': do_c
    }
    return switches.get(caseStatement, do_default)


class A(object):
    pass


class B(object):
    pass


class C(object):
    pass


class D(object):
    """No switch for D"""
    pass


a = A()
b = B()
c = C()
d = D()

switch(a.__class__.__name__)('data')
switch(b.__class__.__name__)('data')
switch(c.__class__.__name__)('data')
switch(d.__class__.__name__)('data')
