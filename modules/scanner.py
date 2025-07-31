# modules/scanner.py

import socket
import ssl
import threading
from contextlib import closing

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

MAX_THREADS = 50


def get_banner(ip, port):
    try:
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            s.settimeout(2)
            s.connect((ip, port))
            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024).decode(errors='ignore')
            return banner.strip()
    except:
        return None


def is_ssl(ip, port):
    try:
        context = ssl.create_default_context()
        with closing(context.wrap_socket(socket.socket(), server_hostname=ip)) as s:
            s.settimeout(2)
            s.connect((ip, port))
            return True
    except:
        return False


def identify_os_from_banner(banner):
    if not banner:
        return None
    banner = banner.lower()
    if "windows" in banner:
        return "Windows"
    elif "linux" in banner:
        return "Linux"
    elif "ubuntu" in banner:
        return "Ubuntu"
    elif "debian" in banner:
        return "Debian"
    elif "centos" in banner:
        return "CentOS"
    return "Unknown"


def scan_port(ip, port, results):
    service_info = {
        "port": port,
        "status": "closed",
        "service": COMMON_PORTS.get(port, "Unknown"),
        "ssl": False,
        "banner": None,
        "os_guess": None
    }

    try:
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                service_info["status"] = "open"
                try:
                    banner = get_banner(ip, port)
                    service_info["banner"] = banner
                    service_info["os_guess"] = identify_os_from_banner(banner)

                    if banner:
                        if "apache" in banner.lower():
                            service_info["service"] = "Apache"
                        elif "nginx" in banner.lower():
                            service_info["service"] = "Nginx"
                        elif "ssh" in banner.lower():
                            service_info["service"] = "SSH"
                        elif "ftp" in banner.lower():
                            service_info["service"] = "FTP"
                        elif "iis" in banner.lower():
                            service_info["service"] = "IIS"

                    service_info["ssl"] = is_ssl(ip, port)
                except:
                    pass
    except:
        pass

    if service_info["status"] == "open":
        results.append(service_info)


def scan_target(ip: str) -> list[dict]:
    threads = []
    results = []

    for port in COMMON_PORTS:
        thread = threading.Thread(target=scan_port, args=(ip, port, results))
        thread.start()
        threads.append(thread)

        if len(threads) >= MAX_THREADS:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    return results


def scan_targets(resolved_hosts: dict[str, str]) -> dict[str, list[dict]]:
    """
    Scans IPs for open common ports.
    Returns a dictionary: {ip: [list of port info dicts]}
    """
    full_results = {}
    for ip in set(resolved_hosts.values()):
        full_results[ip] = scan_target(ip)
    return full_results
