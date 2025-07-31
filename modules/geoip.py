import requests

def geoip_lookup(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        res = requests.get(url, timeout=5)
        if res.status_code != 200:
            return None

        data = res.json()
        if data.get("status") != "success":
            return None

        return {
            "country": data.get("country"),
            "region": data.get("regionName"),
            "city": data.get("city"),
            "lat": data.get("lat"),
            "lon": data.get("lon"),
            "isp": data.get("isp"),
        }

    except Exception as e:
        print(f"[!] Error during GeoIP lookup for {ip}: {e}")
        return None
