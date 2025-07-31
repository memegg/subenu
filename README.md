

**subenu** is a modular Python framework designed for automated reconnaissance and passive intelligence gathering on internet domains. The framework provides a structured and extensible approach to enumerating subdomains, resolving DNS records, scanning ports, fingerprinting technologies, retrieving threat intelligence, geolocating IPs, and collecting WHOIS data.

This tool is intended for cybersecurity professionals, penetration testers, and researchers conducting authorized security assessments.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [API Requirements](#api-requirements)
- [Notes](#notes)


---

## Features

- Passive subdomain enumeration using crt.sh and other APIs.
- DNS resolution for discovered subdomains.
- Port scanning and service identification.
- Web technology detection.
- Integration with threat intelligence platforms.
- IP geolocation lookup.
- WHOIS information extraction.
- Modular structure for future extensions.
- Logging and structured output for further analysis.

---


subenu/
├── core/

│   ├── __init__.py

│   ├── controller.py

│   ├── runner.py

│   └── utils.py
│

├── modules/

│   ├── __init__.py

│   ├── subdomains.py

│   ├── resolver.py

│   ├── scanner.py

│   ├── webtech.py

│   ├── threatintel.py

│   ├── geoip.py

│   ├── otx.py

│   └── whois_info.py
│
├── output/

│   └── logger.py
│
├── main.py

└── requirements.txt 


---

## 
_init__.py — Initializes the core module.

controller.py — Coordinates the overall workflow in the core module.

runner.py — Orchestrates execution of modules in the core module.

utils.py — Contains shared helper functions used in the core module.

__init__.py — Initializes the modules package.

subdomains.py — Performs passive subdomain enumeration in the modules package.

resolver.py — Resolves DNS records for subdomains in the modules package.

scanner.py — Performs port scanning and basic service detection in the modules package.

webtech.py — Detects web technologies (e.g., CMS, frameworks) in the modules package.

threatintel.py — Aggregates data from threat intelligence sources in the modules package.

geoip.py — Maps IP addresses to geographic locations in the modules package.

otx.py — Integrates with AlienVault OTX API in the modules package.

whois_info.py — Retrieves WHOIS information for domains and IPs in the modules package.

logger.py — Formats and manages output logs in the output module.

main.py — Entry point of the application at the root level.

requirements.txt — Lists Python dependencies for installation at the root level.

---

## Setup

1. Clone the repository:

git clone https://github.com/your-username/subenu.git
cd subenu
Create a virtual environment (recommended):


python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Usage
From the root directory:

python main.py
You can configure target domain and module options within the controller script or by extending the CLI (planned in future versions).

---

## API Requirements
To enable full functionality, the following APIs may require registration and API keys:

SecurityTrails API: for enriched subdomain enumeration and DNS data.

AlienVault OTX API: for threat intelligence lookups.

ip-api.com or ipinfo.io: for IP geolocation (optional).

WHOIS services: public access may be rate-limited; private key may be needed for high-volume queries.

These keys should be configured inside the respective modules or loaded from a .env or config.ini file as needed.

---

##Notes
This framework is intended for authorized testing only.

Use responsibly and in compliance with local laws and target policies.

The codebase is structured to be extensible. Developers can add additional modules following the same interface used in the existing structure
---

## Setup
1. Clone the repository:


git clone https://github.com/your-username/subenu.git
cd subenu

Install dependencies:

From the root directory:
---

## Usage
from the root directory:

python main.py
You can configure target domain and module options within the controller script or by extending the CLI (planned in future versions).



---

## API Requirements
To enable full functionality, the following APIs may require registration and API keys:

SecurityTrails API: for enriched subdomain enumeration and DNS data.

AlienVault OTX API: for threat intelligence lookups.

ip-api.com or ipinfo.io: for IP geolocation (optional).

WHOIS services: public access may be rate-limited; private key may be needed for high-volume queries.

These keys should be configured inside the respective modules or loaded from a .env or config.ini file as needed.

python main.py
You can configure target domain and module options within the controller script or by extending the CLI (planned in future versions).

---

## Notes
This framework is intended for authorized testing only.

Use responsibly and in compliance with local laws and target policies.

The codebase is structured to be extensible. Developers can add additional modules following the same interface used in the existing structure.



pip install -r requirements.txt
