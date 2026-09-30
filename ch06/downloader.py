import sys

import requests

if len(sys.argv) < 2:
    print("Usage: python downloader.py <url> [file name]")
    sys.exit()

url = sys.argv[1]
if len(sys.argv) > 2:
    file_name = sys.argv[2]
else:
    file_name = url.rstrip("/").split("/")[-1]

response = requests.get(url, timeout=10)
if not response.ok:
    sys.exit(f"Download failed: {response.status_code} {response.reason}")

with open(file_name, "wb") as f:
    f.write(response.content)
print(f"Saved {file_name} ({len(response.content)} bytes)")
