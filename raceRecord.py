import urllib.request
import os
from bs4 import BeautifulSoup

""" Define URL """
# years = [str(x) for x in range(2008, 2019)]
# months = ["{:02d}".format(x) for x in range(13)[1:]]
# days = ["{:02d}".format(x) for x in range(32)[1:]]
# venues = ["ST", "HV"]
# races = [str(x) for x in range(13)[1:]]
header = "place, horse_no, horse_name, horse_id, jockey, trainer, actual_weight, declared_weight, draw, length_behind_winner, finish_time, win_odds, running_position_1, running_position_2, running_position_3, running_position_4, running_position_5, running_position_6" + "\n"

# file = open(os.path.expanduser("RaceResult.csv"), "wb")
# file.write(bytes(header, encoding="ascii", errors='ignore'))

for i in range(12):
    #theURL = "http://racing.hkjc.com/racing/Info/Meeting/Results/English/Local/20180905/HV/2"
    # Find the div (class = raceNum clearfix) -> table -> a.value
    theURL = "http://racing.hkjc.com/racing/Info/Meeting/Results/English/Local/20080412/ST/" + races[i]
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

                    # if column == 1 and tDatas.text == "WV":
                    #     isWV = True
                    #     record = record + "," + tDatas.text
                    # elif column == 10 and isWV:   # Skip the Running Position if it is WV.
                    #     isWV = False
                    #     continue
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

            file.write(bytes(savedRecord, encoding="ascii", errors='ignore'))
            break

file.close()
