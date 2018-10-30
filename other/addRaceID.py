import csv

with open('RaceResultST_old.csv', 'r') as csvinput:
    with open('RaceResultST.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator="\n")
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append("race_id")
        all.append(row)

        for row in reader:
            row.append(row[0] + row[1].zfill(2))
            all.append(row)
            print(row)

        writer.writerows(all)

