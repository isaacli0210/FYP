import csv

file = open('HorseID_Z.txt', 'w')

with open('HorseID.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        if row[0][0] == "Z":
            file.write(row[0] + "\n")

file.close()


