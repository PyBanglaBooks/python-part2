import csv

with open("marks.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        total = int(row["bangla"]) + int(row["english"]) + int(row["math"])
        average = total / 3
        print(f"{row['name']}: total {total}, average {average:.2f}")
