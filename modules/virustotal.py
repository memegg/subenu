# modules/virustotal.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("VT_API_KEY")

def get_virustotal_info(domain):
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    headers = {
        "x-apikey": API_KEY
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "reputation": data.get("data", {}).get("attributes", {}).get("reputation"),
                "last_analysis_stats": data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}),
                "categories": data.get("data", {}).get("attributes", {}).get("categories", {})
            }
        else:
            return {"error": f"Failed: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}
