import webbrowser
from pathlib import Path

import requests

url = "https://example.com"
response = requests.get(url, timeout=10)

page = Path("example.html")
page.write_text(response.text, encoding="utf-8")
print(f"Saved {page}")

webbrowser.open(page.resolve().as_uri())
