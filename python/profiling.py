#!/usr/bin/env python
"""Example of profiling using the cProfile module."""
import time
import sys
import StringIO
import cProfile
import pstats

pr = cProfile.Profile()


def long_wait(secs):
    time.sleep(secs)


def short_wait(secs):
    time.sleep(secs / 2)


def profile(original_func):
    """Profiling decorator."""
    def new_func(*args, **kwargs):
        pr.enable()
        result = original_func(*args, **kwargs)
        pr.disable()

        sortby = 'cumulative'

        # Write report to file
        filename = "/tmp/profiling_" + time.strftime("%d%b%H%M%S")
        with open(filename, 'a') as f:
            ps = pstats.Stats(pr, stream=f).sort_stats(sortby)
            ps.print_stats()

        # Print report to stdout
        s = StringIO.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print s.getvalue()

        return result
    return new_func


@profile
def main(n):
    for i in range(n):
        long_wait(i)
        short_wait(i)


if __name__ == "__main__":
    try:
        main(3)
    except Exception as error:
        print error
        sys.exit(1)
