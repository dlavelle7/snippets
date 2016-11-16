"""Demonstration of how to catch common linux kill signals.

Note: SIGKILL (9) or SIGSTOP cannot be caught, blocked or ignored."""

import signal
import time
import sys


def sigterm_handler(signal_num, stack_frame):
    """kill -15"""
    print "Process shutting down gracefully (signal number %s)" % signal_num
    sys.exit(0)


def sigint_handler(signal_num, stack_frame):
    """Ctrl+C / kill -2: Alternative to catching exception KeyboardInterrupt"""
    print "Keyboard interrupt, exiting (signal number %s)" % signal_num
    sys.exit(0)


def sighup_handler(signal_num, stack_frame):
    """kill -1 / The controlling terminal of the process is closed"""
    # Could also log message / write file, as terminal may be closed
    print "Hanging up, exiting (signal number %s)" % signal_num
    sys.exit(0)


# Set the signal handlers
signal.signal(signal.SIGTERM, sigterm_handler)
signal.signal(signal.SIGINT, sigint_handler)
signal.signal(signal.SIGHUP, sighup_handler)


def main():
    while True:
        print "Waiting indefinitely. . ."
        time.sleep(5)


main()
