import json

import requests

url = "https://api.github.com/orgs/PyBanglaBooks/repos"
response = requests.get(url, timeout=10)
response.raise_for_status()
repos = response.json()

for repo in repos:
    name = repo["name"]
    language = repo["language"]
    stars = repo["stargazers_count"]
    print(f"{name} ({language}), stars: {stars}")

with open("repos.json", "w", encoding="utf-8") as f:
    json.dump(repos, f, indent=4, ensure_ascii=False)
