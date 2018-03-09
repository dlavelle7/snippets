"""Explaining Python Closures."""


def outer_function(value):
    """Basic closure."""
    outer_value = value

    def inner_function():
        return outer_value

    return inner_function


# outer_value is set to 2
inner = outer_function(2)

# inner_function can access variables that were in it's scope through closures
assert inner() == 2


def outer_function_2(value):
    """Modifying variables via closure."""
    outer_list = [value]  # list are mutable

    def add(add_value):
        return outer_list[0] + add_value

    def reset(new_value):
        """Variables accessible through closures can also be reset."""
        outer_list[0] = new_value

    return add, reset


# outer_value is set to 4 initially
adder, resetter = outer_function_2(4)

# add 1 to the variable via closure
assert adder(1) == 5

# reset outer_value via closure
resetter(10)

# add 5 to the new outer_value
assert adder(5) == 15
