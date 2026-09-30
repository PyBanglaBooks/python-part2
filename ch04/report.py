import csv

with open("marks.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        total = 0
        for subject in ["bangla", "english", "math"]:
            total += int(row[subject])
        average = total / 3
        print(f"{row['name']}: total {total}, average {average:.2f}")
