#!/usr/bin/env python
import re


def format_list(my_list):
    """Convert list values into a nicely formated string

    Example:
    ['x', 'y', 'z'] => "x, y and z"
    ['x', 'y']      => "x and y"
    ['x']           => "x"
    """
    return re.sub(r'(.*),', r'\1 and', ', '.join(my_list))


print format_list(['x', 'y', 'z'])
print format_list(['x', 'y'])
print format_list(['x'])

assert format_list(['x', 'y', 'z']) == "x, y and z"
assert format_list(['x', 'y']) == "x and y"
assert format_list(['x']) == "x"
