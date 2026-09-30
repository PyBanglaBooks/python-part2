import csv

with open("marks.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)
