import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from modules import (
    subdomains,
    resolver,
    scanner,
    web_detector,
    abuseipdb,   
    geoip,
    whois_info,
    virustotal
)


class Controller:
    def __init__(self, target: str):
        self.target = target

    def run_all(self):
        # 1. جمع الـ subdomains من crt.sh فقط
        resolved_hosts = subdomains.get_subdomains_with_ips(self.target)
        subdomain_list = list(resolved_hosts.keys())

        # 2. حل الـ subdomains لـ IPs
        resolved_hosts = resolver.resolve_subdomains(subdomain_list)

        # 3. مسح البورتات على الـ IPs
        port_scan_results = scanner.scan_targets(resolved_hosts)

        # 4. كشف تقنيات الويب
        tech_stack = web_detector.detect_tech(resolved_hosts)

        # 5. معلومات التهديدات (abuseipdb) على IPs
        threat_data_ips = {}
        for ip in set(resolved_hosts.values()):
            abuse_info = abuseipdb.check_threat_ip(ip)
            threat_data_ips[ip] = abuse_info

        # 6. معلومات فيرس توتال على الدومين
        threat_data_domain = virustotal.get_virustotal_info(self.target)

        # 7. بيانات الموقع الجغرافي (GeoIP)
        geoip_data = {}
        for ip in set(resolved_hosts.values()):
            geoip_data[ip] = geoip.geoip_lookup(ip)

        # 8. بيانات WHOIS
        whois_result = whois_info.get_whois_info(self.target)

        results = {
            "subdomains": subdomain_list,
            "resolved_hosts": resolved_hosts,
            "port_scan": port_scan_results,
            "web_technologies": tech_stack,
            "threat_data_domain": threat_data_domain,
            "threat_data_ips": threat_data_ips,
            "geoip_data": geoip_data,
            "whois_data": whois_result,
        }

        return results
