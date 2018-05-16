"""Argparsing example using a custom Action and type (Python 3.6).

Accept a list of ip addresses as strings, that needs to be converted to a
list of sets containing ip_address() IPv4 objects.
Encounted using: aiohttp_remotes.XForwardedStrict.

Call script like:
    python python/argparsing_custom_action.py -t 192.168.1.1 192.168.2.2
"""
import argparse

from ipaddress import ip_address

ANY_IPV4_ADDRESS = ip_address("0.0.0.0")


class StoreNargsAsListOfSets(argparse.Action):

    def __call__(self, parser_used, namespace, values, option_string=None):
        """Convert list of strs to list of sets for aiohttp_remotes."""
        new_values = [{ip_address(val)} for val in values]
        setattr(namespace, self.dest, new_values)


def not_any_ipv4_ip_address(value):
    """Only valid IPv4 addresses allowed. Don't allow 'any IPv4 address at all'

    Remember "type" validates nargs independently.
    """
    try:
        ip_value = ip_address(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc))
    if ip_value.version != 4:
        msg = f"'{value}' is not a valid IPv4 address."
        raise argparse.ArgumentTypeError(msg)
    if ip_value == ANY_IPV4_ADDRESS:
        msg = f"Can't specify all IPv4 addresses '{str(ANY_IPV4_ADDRESS)}'."
        raise argparse.ArgumentTypeError(msg)
    return ip_value


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        '--trusted-hosts',
        help='A list of trusted hosts (IPv4).',
        dest="TRUSTED_HOSTS",
        default=[{ip_address("127.0.0.1")}],
        nargs="+",
        action=StoreNargsAsListOfSets,
        type=not_any_ipv4_ip_address
    )
    pargs = parser.parse_args()
    print(f"Trusted IPv4 hosts: {pargs.TRUSTED_HOSTS}")
