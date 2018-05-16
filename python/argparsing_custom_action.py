"""Argparsing example using a custom Action (Python 3).

Accept a list of ip addresses as strings, that needs to be converted to a
list of sets containing ip_address() objects.
Encounted using: aiohttp_remotes.XForwardedStrict.
"""
import argparse

from ipaddress import ip_address


class StoreNargsAsListOfSets(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        """Convert list of strs to list of sets for aiohttp_remotes."""
        new_values = [{ip_address(val)} for val in values]
        setattr(namespace, self.dest, new_values)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        '--trusted-hosts',
        help='A list of trusted hosts.',
        dest="TRUSTED_HOSTS",
        default=[{ip_address("127.0.0.1")}],
        nargs="+",
        action=StoreNargsAsListOfSets,
        type=ip_address
    )
    pargs = parser.parse_args()
    print(pargs.TRUSTED_HOSTS)
