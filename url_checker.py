# CyberScan Toolkit
# Module 2 - URL Reputation Checker
# Author: rudranoir0-dot

import urllib.request
import json

def check_url(url):
    try:
        api = f"https://urlhaus-api.abuse.ch/v1/url/"
        data = f"url={url}".encode()
        req = urllib.request.Request(api, data=data, method="POST")
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode())
            return result
    except Exception as e:
        return {"query_status": "error", "detail": str(e)}

url = input("Enter URL to check: ")
print(f"\nChecking {url}...\n")

result = check_url(url)

status = result.get("query_status", "unknown")

if status == "is_malware":
    print(f"[DANGER] This URL is MALICIOUS")
    print(f"Threat: {result.get('threat', 'unknown')}")
    print(f"Date added: {result.get('date_added', 'unknown')}")
elif status == "no_results":
    print(f"[SAFE] No threats found for this URL")
elif status == "error":
    print(f"[ERROR] Could not check URL")
else:
    print(f"[INFO] Status: {status}")

print("\nCheck complete.")