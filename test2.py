import urllib.request
from bs4 import BeautifulSoup

""" Define URL """
races = [str(x) for x in range(13)[1:]]
header = "place, horse_no, horse_name, horse_id, jockey, trainer, actual_weight, declared_weight, draw, length_behind_winner, finish_time, win_odds, running_position_1, running_position_2, running_position_3, running_position_4, running_position_5, running_position_6" + "\n"

file = open("textRaceResult.csv", "a")
dateFile = open("OnlyDateST.txt", "r")

file.write(header)
for date in dateFile.read().splitlines():
    for i in range(12):
        theURL = "http://racing.hkjc.com/racing/Info/Meeting/Results/English/Local/" + date + "/ST/" + races[i]
        print(date + "..." + str(i))
        while(True):
            thePage = urllib.request.urlopen(theURL)
            soup = BeautifulSoup(thePage, "html.parser")

            """ For Race General Information Table
            table = soup.find_all('table', {'class': 'tableBorder0 font13'})
            for tRows in table[0].find_all('tr'):
                for tDatas in tRows.find_all('td'):
                    print(tDatas.text)
            """

            """ For Race Result Table"""
            errorDiv = soup.find('div', {'id': 'divErrorMsg'})

            table = soup.find('table', {'class': 'tableBorder trBgBlue tdAlignC number12 draggable'})
            if errorDiv is not None:
                break
            elif table is not None:
                tBody = table.find('tbody')
                savedRecord = ""
                for tRows in tBody.find_all('tr'):
                    if len(tRows.find_parents('table')) == 2:   # There is a nested table to store the Running Position result.
                        continue
                    record = ""
                    runningPositionTable = ["NA"] * 6
                    column = 0   # Use to split the horse name and id.
                    # isWV = False   # Use to check the row has WV(Withdrawn-on Veterinary Ground) or not.

                    for tDatas in tRows.find_all('td'):
                        column += 1
                        if tDatas.find('table'):
                            i = 0
                            for runningPositions in tDatas.find_all('td'):
                                runningPositionTable[i] = runningPositions.text
                                i += 1
                            continue

                        if column == 10 and tDatas.text == "---":
                            continue
                        elif column == 10 and tDatas.text == "-":
                            continue
                        elif column == 3:   # Use to split the horse name and id.
                            data = tDatas.text.split("(")
                            record = record + "," + data[0] + "," + data[1][0:4]
                        elif len(tDatas.find_parents('table')) == 2:   # Skip the Running Position Table.
                            continue
                        else:
                            record = record + "," + tDatas.text

                    for runningPositionData in runningPositionTable:   # Running Position Table.
                        record = record + "," + runningPositionData

                    savedRecord = savedRecord + "\n" + record[1:]
                print(savedRecord)

                file.write(savedRecord)
                break

dateFile.close()
file.close()
