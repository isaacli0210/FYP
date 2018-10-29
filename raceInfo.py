import urllib.request
from bs4 import BeautifulSoup

races = [str(x) for x in range(13)[1:]]
header = "race_id, date, race_no, class, distance, rating_upper, rating_lower, condition, course_type, track" + "\n"

file = open("RaceInfoHV.csv", "a")
dateFile = open("raceDate/OnlyDateHV_2018_2.txt", "r")

#file.write(header)
for date in dateFile.read().splitlines():
    for raceNum in range(12):

        theURL = "http://racing.hkjc.com/racing/Info/Meeting/Results/English/Local/" + date + "/HV/" + races[raceNum]
        raceID = date + "{:02d}".format(raceNum + 1)
        print(date + "..." + str(raceNum + 1))

        while(True):

            thePage = urllib.request.urlopen(theURL)
            soup = BeautifulSoup(thePage, "html.parser")

            div = soup.find('div', {'class': 'clearDivFloat paddingTop5'})
            table = soup.find('table', {'class': 'tableBorder0 font13'})

            record = []
            saveRecord = ""
            raceClass = ""
            rateUpper = ""
            rateLower = ""
            if table is not None:
                for tRows in table.find_all('tr'):
                    for tDatas in tRows.find_all('td'):
                        record.append(tDatas.text)

                classAndRating = record[0].split("-")
                print(classAndRating)
                if classAndRating[0][0] != "C":
                    raceClass = classAndRating[0].rstrip()
                else:
                    raceClass = classAndRating[0][6]

                distance = classAndRating[1].strip()

                if len(classAndRating) > 3:
                    rateUpper = classAndRating[2].strip().split("(")[1]
                    rateLower = classAndRating[3].split(")")[0]
                elif len(classAndRating) == 3:
                    rateUpper = classAndRating[-1].strip().split("(")[1].split(")")[0].strip()
                    rateLower = rateUpper
                else:
                    rateUpper = "NA"
                    rateLower = "NA"

                condition = record[2]

                course = record[5].split("-")
                courseType = course[0].rstrip()
                if len(course) <= 1:
                    track = "NA"
                else:
                    track = course[1].lstrip().split("\"")[1]

                saveRecord = saveRecord + "\n" + raceID + "," + date + "," + str(raceNum + 1) + "," + raceClass + "," + distance + "," + rateUpper + "," + rateLower + "," + condition + "," + courseType + "," + track
                file.write(saveRecord)
                print(saveRecord)
                break
            else:
                print("No such table")
                break


dateFile.close()
file.close()