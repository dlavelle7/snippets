#!/usr/bin/env python
"""Switch/case control statement in Python

Also included is a handy pattern for delegating work based on Class,
where inheritance for example may not be practical.
"""


def do_a(data):
    print "do_a() with arg '{0}'".format(data)


def do_b(data):
    print "do_b() with arg '{0}'".format(data)


def do_default(data):
    print "do_default() with arg '{0}'".format(data)


def switch(case):
    switches = {
        'A': do_a,
        'B': do_b,
    }
    return switches.get(case, do_default)


class A(object):
    pass


class B(object):
    pass


class C(object):
    """No case for C"""
    pass


for instance in [A(), B(), C()]:
    switch(instance.__class__.__name__)('data')


# Here is an example where each case function may have different args. Maybe
# not the most readable, but is an alternative to if/else branches.
def foo(int1, int2):
    print "foo() with two int args '{0}' & '{1}'".format(int1, int2)


def bar(val):
    print "bar() with a string arg '{0}'".format(val)


alt_switch = {
    "foo": lambda: foo(1, 2),
    "bar": lambda: bar('barbar'),
}


for alt_case in ["foo", "bar"]:
    # Functions can be called without knowning args at this point
    alt_switch.get(alt_case)()
