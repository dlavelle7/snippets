#!/usr/bin/env python
import argparse


def main():
    parser = argparse.ArgumentParser()
    # Positional argument
    parser.add_argument("square",
            help="prints square root of positional arg 1", type=int)
    # Optional argument
    parser.add_argument("-v", "--verbose", help="increased output verbosity",
            action="store_true")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbose:
        print "The square root of {0} is {1}".format(args.square, answer)
    else:
        print answer


if __name__ == "__main__":
    main()
