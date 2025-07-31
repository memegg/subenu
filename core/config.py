# core/config.py

import os
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()

# مفاتيح الـ API
VIRUSTOTAL_API_KEY = os.getenv("024227285051a4c62e672daace4c16957339e63f659858caf415e4f1a66496b9")
ABUSEIPDB_API_KEY = os.getenv("112b1d170625ba5e5f380922ca5655ffc8639d2269d5952913b24a82b0ef04410c565bb093aae48a")
