#!/usr/bin/env python
import time
import sys
import traceback


def main():
    while True:
        print "Interrupt me!"
        a
        time.sleep(3)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print 'Keyboard Interrupt, exiting . . .'
        sys.exit(1)
    except Exception as e:
        traceback.print_exc()
        print 'Something went wrong, exiting . . .'
        sys.exit(1)
