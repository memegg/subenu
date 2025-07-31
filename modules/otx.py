import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.config import OTX_API_KEY

SECTIONS = [
    "general",
    "geo",
    "url_list",
    "passive_dns",
    "malware",
    "whois",
    "http_scans"
]

def query_otx(indicator):
    otx_data = {}
    headers = {
        "X-OTX-API-KEY": OTX_API_KEY
    }

    for section in SECTIONS:
        url = f"https://otx.alienvault.com/api/v1/indicators/domain/{indicator}/{section}"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            otx_data[section] = response.json()
        except requests.exceptions.RequestException as e:
            print(f"[!] OTX query failed for section '{section}': {e}")
            otx_data[section] = None

    return otx_data
