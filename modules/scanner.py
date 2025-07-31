# modules/scanner.py

import socket
import threading
from queue import Queue

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


def scan_target(ip: str, result: dict[str, list[int]]):
    open_ports = []

    def scan_port(port: int):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            try:
                if s.connect_ex((ip, port)) == 0:
                    open_ports.append(port)
            except socket.error:
                pass

    threads = []
    for port in COMMON_PORTS:
        thread = threading.Thread(target=scan_port, args=(port,))
        thread.start()
        threads.append(thread)

        if len(threads) >= MAX_THREADS:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    if open_ports:
        result[ip] = sorted(open_ports)


def scan_targets(resolved_hosts: dict[str, str]) -> dict[str, list[int]]:
    """
    Scans IPs for open common ports.
    Returns a dictionary: {ip: [open_ports]}
    """
    results = {}
    for ip in set(resolved_hosts.values()):
        scan_target(ip, results)
    return results
