#!/usr/bin/env python
import argparse


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    # Positional argument
    parser.add_argument("base", help="base value", type=int)
    # Optional argument
    parser.add_argument("-e", "--expodent",
                        help="expodent value (defaults to 2)", 
                        type=int, default=2, choices=[0, 1, 2, 3, 4])
    group.add_argument("-v", "--verbose", help="increased output verbosity",
                       action="store_true")
    group.add_argument("-q", "--quiet", help="minimum output verbosity",
                       action="store_true")
    args = parser.parse_args()
    answer = args.base ** args.expodent
    if args.verbose:
        print "{0} to the power of {1} equals {2}".format(
            args.base, args.expodent, answer)
    elif args.quiet:
        print answer
    else:
        print "{0}^{1} == {2}".format(args.base, args.expodent, answer)


if __name__ == "__main__":
    main()
