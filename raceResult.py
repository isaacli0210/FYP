import urllib.request
from bs4 import BeautifulSoup

""" Define URL """
races = [str(x) for x in range(13)[1:]]
header = "date, race_no, place, horse_no, horse_name, horse_id, jockey, trainer, actual_weight, declared_weight, draw, finish_time, win_odds, running_position_1, running_position_2, running_position_3, running_position_4, running_position_5, running_position_6, length_behind_winner" + "\n"
dateFile = open("raceDate/OnlyDateST_2018_2.txt", "r")
def first():

    # file = open("RaceResultHV.csv", "a")

    # file.write(header)
    for date in dateFile.read().splitlines():
        for raceNum in range(12):
            theURL = "http://racing.hkjc.com/racing/Info/Meeting/Results/English/Local/" + date + "/ST/" + races[
                raceNum]
            print(date + "..." + str(raceNum))

            while (True):
                thePage = urllib.request.urlopen(theURL)
                soup = BeautifulSoup(thePage, "html.parser")

                errorDiv = soup.find('div', {'id': 'divErrorMsg'})
                cancelDiv = soup.find('div', {'class': 'tdAlignVT font13 fontStyle color_black'})
                table = soup.find('table', {'class': 'tableBorder trBgBlue tdAlignC number12 draggable'})

                if errorDiv is not None:
                    break
                elif cancelDiv is not None:
                    break
                elif table is not None:
                    tBody = table.find('tbody')
                    savedRecord = ""
                    for tRows in tBody.find_all('tr'):
                        if len(tRows.find_parents(
                                'table')) == 2:  # There is a nested table to store the Running Position result.
                            continue

                        record = ""
                        lbw = ""
                        runningPositionTable = ["NA"] * 6
                        column = 0  # Use to split the horse name and id.

                        for tDatas in tRows.find_all('td'):
                            column += 1
                            if tDatas.find('table'):
                                i = 0
                                for runningPositions in tDatas.find_all('td'):
                                    runningPositionTable[i] = runningPositions.text
                                    i += 1
                                continue

                            if column == 9:
                                if len(tDatas.text) == 1 and tDatas.text != "-":
                                    lbw = tDatas.text
                                elif tDatas.text == "-" or tDatas.text == "---":
                                    lbw = "NA"
                                elif len(tDatas.text) == 2:
                                    lbw = tDatas.text
                                elif len(tDatas.text) == 3 and tDatas.text[1] == "/":
                                    lbw = int(tDatas.text[0]) / int(tDatas.text[-1])
                                elif len(tDatas.text) == 5 and tDatas.text[0] != "+":
                                    lbw = int(tDatas.text[0]) + int(tDatas.text[-3]) / int(tDatas.text[-1])
                                elif len(tDatas.text) > 5:
                                    lbw = int(tDatas.text[0:2]) + int(tDatas.text[-3]) / int(tDatas.text[-1])
                                else:
                                    lbw = tDatas.text
                                continue
                            if column == 10 and tDatas.text == "---":
                                continue
                            elif column == 10 and tDatas.text == "-":
                                continue
                            elif column == 3:  # Use to split the horse name and id.
                                data = tDatas.text.split("(")
                                record = record + "," + data[0] + "," + data[1][0:-1]
                            elif len(tDatas.find_parents('table')) == 2:  # Skip the Running Position Table.
                                continue
                            else:
                                record = record + "," + tDatas.text

                        for runningPositionData in runningPositionTable:  # Running Position Table.
                            record = record + "," + runningPositionData

                        record = record + "," + str(lbw)

                        savedRecord = savedRecord + "\n" + date + "," + str(raceNum + 1) + "," + record[1:]

                    print(savedRecord)

                    #file.write(savedRecord)
                    break

    dateFile.close()
    #file.close()
def second():
    file = open("RaceResultST.csv", "a")

    # file.write(header)
    for date in dateFile.read().splitlines():
        for raceNum in range(12):
            theURL = "http://racing.hkjc.com/racing/Info/Meeting/Results/English/Local/" + date + "/ST/" + races[
                raceNum]
            print(date + "..." + str(raceNum))

            while (True):
                thePage = urllib.request.urlopen(theURL)
                soup = BeautifulSoup(thePage, "html.parser")

                errorDiv = soup.find('div', {'id': 'divErrorMsg'})
                cancelDiv = soup.find('div', {'class': 'tdAlignVT font13 fontStyle color_black'})
                table = soup.find('table', {'class': 'tableBorder trBgBlue tdAlignC number12 draggable'})

                if errorDiv is not None:
                    break
                elif cancelDiv is not None:
                    break
                elif table is not None:
                    tBody = table.find('tbody')
                    savedRecord = ""
                    for tRows in tBody.find_all('tr'):
                        if len(tRows.find_parents(
                                'table')) == 2:  # There is a nested table to store the Running Position result.
                            continue

                        record = ""
                        lbw = ""
                        runningPositionTable = ["NA"] * 6
                        column = 0  # Use to split the horse name and id.

                        for tDatas in tRows.find_all('td'):
                            column += 1
                            if tDatas.find('table'):
                                i = 0
                                for runningPositions in tDatas.find_all('td'):
                                    runningPositionTable[i] = runningPositions.text
                                    i += 1
                                continue

                            if column == 9:
                                if len(tDatas.text) == 1 and tDatas.text != "-":
                                    lbw = tDatas.text
                                elif tDatas.text == "-" or tDatas.text == "---":
                                    lbw = "NA"
                                elif len(tDatas.text) == 2:
                                    lbw = tDatas.text
                                elif len(tDatas.text) == 3 and tDatas.text[1] == "/":
                                    lbw = int(tDatas.text[0]) / int(tDatas.text[-1])
                                elif len(tDatas.text) == 5 and tDatas.text[0] != "+":
                                    lbw = int(tDatas.text[0]) + int(tDatas.text[-3]) / int(tDatas.text[-1])
                                elif len(tDatas.text) > 5:
                                    lbw = int(tDatas.text[0:2]) + int(tDatas.text[-3]) / int(tDatas.text[-1])
                                else:
                                    lbw = tDatas.text
                                continue
                            if column == 10 and tDatas.text == "---":
                                continue
                            elif column == 10 and tDatas.text == "-":
                                continue
                            elif column == 3:  # Use to split the horse name and id.
                                data = tDatas.text.split("(")
                                record = record + "," + data[0] + "," + data[1][0:-1]
                            elif len(tDatas.find_parents('table')) == 2:  # Skip the Running Position Table.
                                continue
                            else:
                                record = record + "," + tDatas.text

                        for runningPositionData in runningPositionTable:  # Running Position Table.
                            record = record + "," + runningPositionData

                        record = record + "," + str(lbw)

                        savedRecord = savedRecord + "\n" + date + "," + str(raceNum + 1) + "," + record[1:]

                    print(savedRecord)

                    file.write(savedRecord)
                    break

    dateFile.close()
    file.close()

#first()
second()

