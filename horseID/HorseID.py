# import csv
#
# with open('../RaceResultHV.csv', 'r') as csvinput:
#     with open('HorseID.csv', 'a') as csvoutput:
#         writer = csv.writer(csvoutput, lineterminator="\n")
#         reader = csv.reader(csvinput)
#
#         row = next(reader)
#
#         horseIDArray = []
#
#         for row in reader:
#             if row[6] not in horseIDArray:
#                 horseIDArray.append(row[6])
#                 #writer.writerow(row[6])
#                 #print(row[6] + " add to csv")
#             else:
#                 print("already have this ID")
#
#         for item in horseIDArray:
#             writer.writerow([item])

import csv

with open('HorseID_old.csv', 'r') as csvinput:
    with open('HorseID.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator="\n")
        reader = csv.reader(csvinput)

        horseIDArray = []

        for row in reader:
            if row not in horseIDArray:
                horseIDArray.append(row)

        writer.writerows(horseIDArray)