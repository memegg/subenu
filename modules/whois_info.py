import whois

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return {
            "domain_name": w.domain_name,
            "registrar": w.registrar,
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
            "name_servers": w.name_servers,
            "emails": w.emails,
        }
    except Exception as e:
        print(f"[!] Error fetching WHOIS for {domain}: {e}")
        return None
