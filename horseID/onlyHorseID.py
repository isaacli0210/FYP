import csv

# with open("HorseID_old.csv", "r") as csvinput:
#     with open('HorseID.csv', 'w') as csvoutput:
#         writer = csv.writer(csvoutput, lineterminator="\n")
#         reader = csv.reader(csvinput)
#
#         horseIDArray = []
#
#         for row in reader:
#             if row not in horseIDArray:
#                 horseIDArray.append(row)
#                 print("add to csv")
#             else:
#                 print("already have this ID")
#
#         writer.writerows(horseIDArray)

file = open('HorseID_Z.txt', 'w')

with open('HorseID.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        if row[0][0] == "Z":
            file.write(row[0] + "\n")

file.close()


