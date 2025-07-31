import sys
import os
import time  # ⬅️ لحساب وقت التشغيل

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
    virustotal,
    otx,
)

from core import config


class Controller:
    def __init__(self, target: str):
        self.target = target

    def run_all(self):
        start_time = time.time()  # ⏱️ بداية الوقت

        # 1. Subdomain discovery with details (IP + CNAME)
        detailed_subdomains = subdomains.get_subdomains_with_details(self.target)

        subdomain_list = [entry["subdomain"] for entry in detailed_subdomains]
        resolved_hosts = {
            entry["subdomain"]: entry["ip"] for entry in detailed_subdomains if entry["ip"]
        }

        # 2. Port scanning with banner, service, SSL
        port_scan_results = scanner.scan_targets(resolved_hosts)

        # 3. Web technology detection
        tech_stack = web_detector.detect_tech(resolved_hosts)

        # 4. Threat intelligence on IPs (AbuseIPDB)
        threat_data_ips = {}
        for ip in set(resolved_hosts.values()):
            abuse_info = abuseipdb.check_threat_ip(ip)
            threat_data_ips[ip] = abuse_info

        # 5. VirusTotal domain check
        threat_data_domain = virustotal.get_virustotal_info(self.target)

        # 6. AlienVault OTX
        otx_data = otx.query_otx(self.target)

        # 7. GeoIP lookup
        geoip_data = {}
        for ip in set(resolved_hosts.values()):
            geoip_data[ip] = geoip.geoip_lookup(ip)

        # 8. WHOIS info
        whois_result = whois_info.get_whois_info(self.target)

        # ⏱️ حساب مدة التنفيذ
        end_time = time.time()
        execution_time = round(end_time - start_time, 2)

        results = {
            "subdomains": subdomain_list,
            "resolved_hosts": resolved_hosts,
            "port_scan": port_scan_results,
            "web_technologies": tech_stack,
            "threat_data_domain": threat_data_domain,
            "threat_data_ips": threat_data_ips,
            "otx_data": otx_data,
            "geoip_data": geoip_data,
            "whois_data": whois_result,
            "subdomain_details": detailed_subdomains,
            "execution_time_seconds": execution_time  # ⬅️ الوقت المستغرق
        }

        return results
