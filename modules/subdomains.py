import requests
import socket
import dns.resolver  # pip install dnspython
import http.client


def get_subdomains_crtsh(domain: str) -> set[str]:
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


def resolve_cname(subdomain: str) -> str | None:
    try:
        answers = dns.resolver.resolve(subdomain, 'CNAME')
        for rdata in answers:
            return str(rdata.target).rstrip('.')  # remove trailing dot
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return None


def is_subdomain_live(subdomain: str) -> bool:
    try:
        conn = http.client.HTTPConnection(subdomain, timeout=3)
        conn.request("HEAD", "/")
        response = conn.getresponse()
        return response.status < 500  # consider 2xx–4xx as live
    except Exception:
        return False


def get_subdomains_with_details(domain: str) -> list[dict]:
    all_subdomains = get_subdomains_crtsh(domain) | get_subdomains_hackertarget(domain)
    results = []

    for sub in all_subdomains:
        entry = {
            "subdomain": sub,
            "ip": None,
            "cname": None,
            "is_live": False
        }

        try:
            entry["ip"] = socket.gethostbyname(sub)
        except socket.gaierror:
            pass

        entry["cname"] = resolve_cname(sub)
        entry["is_live"] = is_subdomain_live(sub)

        results.append(entry)

    return results
