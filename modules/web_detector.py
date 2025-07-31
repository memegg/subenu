from Wappalyzer import Wappalyzer, WebPage

def detect_tech(resolved_hosts: dict[str, str]) -> dict[str, dict]:
    results = {}
    wappalyzer = Wappalyzer.latest()

    for host in resolved_hosts.keys():
        for scheme in ["http", "https"]:
            url = f"{scheme}://{host}"

            try:
                webpage = WebPage.new_from_url(url, timeout=5)
                technologies = wappalyzer.analyze(webpage)

                results[host] = {
                    "technologies": list(technologies)
                }
                break  # stop after first successful scheme
            except Exception as e:
                continue

    return results
