# modules/abuseipdb.py

import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.config import ABUSEIPDB_API_KEY


def check_threat_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Accept": "application/json",
        "Key": ABUSEIPDB_API_KEY
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        data = response.json()["data"]
        return {
            "ip": data["ipAddress"],
            "abuseConfidenceScore": data["abuseConfidenceScore"],
            "countryCode": data["countryCode"],
            "isp": data.get("isp", "N/A"),
            "domain": data.get("domain", "N/A"),
            "totalReports": data["totalReports"]
        }
    except Exception as e:
        print(f"[!] Error fetching threat intel for {ip}: {e}")
        return None
