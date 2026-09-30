import json

settings = {
    "player": "নুসরাত",
    "level": 3,
    "sound": True,
    "high_scores": [120, 95, 80],
}

with open("settings.json", "w", encoding="utf-8") as f:
    json.dump(settings, f, indent=4, ensure_ascii=False)
