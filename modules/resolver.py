# modules/resolver.py

import socket


def resolve_subdomains(subdomains: list[str]) -> dict[str, str]:
    """
    Resolves subdomains to their corresponding IP addresses.

    Returns a dictionary: {subdomain: ip}
    """
    resolved = {}

    for subdomain in subdomains:
        try:
            ip = socket.gethostbyname(subdomain)
            resolved[subdomain] = ip
        except socket.gaierror:
            continue

    return resolved
