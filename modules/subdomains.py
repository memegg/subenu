import requests
import socket


def get_subdomains_crtsh(domain: str) -> set[str]:
    """
    Retrieves subdomains for the given domain using crt.sh.
    """
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        return set()

    subdomains = set()
    for cert in data:
        name_value = cert.get("name_value", "")
        for entry in name_value.split("\n"):
            entry = entry.strip()
            if entry.endswith(domain):
                subdomains.add(entry)
    return subdomains


def get_subdomains_hackertarget(domain: str) -> set[str]:
    """
    Retrieves subdomains for the given domain using HackerTarget API.
    """
    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        lines = response.text.splitlines()
    except requests.RequestException:
        return set()

    subdomains = set()
    for line in lines:
        parts = line.split(",")
        if parts:
            sub = parts[0].strip()
            if sub.endswith(domain):
                subdomains.add(sub)
    return subdomains


def get_subdomains_with_ips(domain: str) -> dict[str, str | None]:
    """
    Retrieves subdomains from multiple sources and resolves their IPs.
    Returns: {subdomain: ip or None if resolution fails}
    """
    all_subdomains = get_subdomains_crtsh(domain) | get_subdomains_hackertarget(domain)
    resolved = {}

    for sub in all_subdomains:
        try:
            ip = socket.gethostbyname(sub)
        except socket.gaierror:
            ip = None
        resolved[sub] = ip

    return resolved
