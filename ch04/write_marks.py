import csv

rows = [
    ["name", "bangla", "english", "math"],
    ["Rahim", 78, 65, 92],
    ["Nusrat", 88, 79, 85],
    ["Karim", 55, 71, 60],
    ["Tania", 91, 84, 97],
]

with open("marks.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
