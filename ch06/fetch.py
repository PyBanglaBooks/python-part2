import requests


def fetch(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout:
        print(f"Too slow: {url}")
    except requests.exceptions.ConnectionError:
        print(f"Could not connect: {url}")
    except requests.exceptions.HTTPError as error:
        print(f"Error {error.response.status_code}: {url}")
    return None


urls = [
    "https://example.com",
    "https://example.com/abc.html",
    "https://no-such-site.example",
    "https://httpbin.org/delay/5",
]
for url in urls:
    response = fetch(url, timeout=2)
    if response:
        print(f"OK: {url}")
