import requests

repo = "https://raw.githubusercontent.com/PyBanglaBooks/python-part2"
img_url = repo + "/main/images/vehicle.png"

response = requests.get(img_url, timeout=10)
with open("vehicle.png", "wb") as f:
    f.write(response.content)
print(f"Saved vehicle.png ({len(response.content)} bytes)")
