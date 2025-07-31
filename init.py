import os

folders = [
    "core",
    "modules",
    "output"
]

files = {
    "main.py": "",
    "requirements.txt": "",
    "core/__init__.py": "",
    "core/controller.py": "",
    "core/runner.py": "",
    "core/utils.py": "",
    "modules/__init__.py": "",
    "modules/subdomains.py": "",
    "modules/resolver.py": "",
    "modules/scanner.py": "",
    "modules/webtech.py": "",
    "modules/threatintel.py": "",
    "modules/geoip.py": "",
    "modules/whois_info.py": "",
    "output/logger.py": ""
}


for folder in folders:
    os.makedirs(folder, exist_ok=True)


for filepath, content in files.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Project structure initialized successfully.")
