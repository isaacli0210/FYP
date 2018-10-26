import csv

file = open("OnlyDateHV.txt", "a")

with open("RaceDateHV.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        file.write(row[0][-13:-5] + "\n")

file.close()