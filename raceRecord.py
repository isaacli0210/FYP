import urllib
import urllib.request
from bs4 import BeautifulSoup

""" Define URL """
years = [str(x) for x in range(2008, 2019)]
months = ["{:02d}".format(x) for x in range(13)[1:]]
days = ["{:02d}".format(x) for x in range(32)[1:]]
venues = ["ST", "HV"]
races = [str(x) for x in range(13)[1:]]


theURL = "http://racing.hkjc.com/racing/Info/Meeting/Results/English/Local/20180905/HV/1"
thePage = urllib.request.urlopen(theURL)
soup = BeautifulSoup(thePage, "html.parser")


""" For Race General Information Table"""
table = soup.find_all('table', {'class': 'tableBorder0 font13'})
for tRows in table[0].find_all('tr'):
    for tDatas in tRows.find_all('td'):
        print(tDatas.text)


""" For Race Result Table
header = "place, horse_no, horse_name, horse_id, jockey, trainer, actual_weight, declared_weight, draw, length_behind_winner, running_position_1, running_position_2, running_position_3, running_position_4, running_position_5, finish_time, win_odds"
table = soup.find_all('table', {'class': 'tableBorder trBgBlue tdAlignC number12 draggable'})
tBody = table[0].find('tbody')
savedRecord = ""
for tRows in tBody.find_all('tr'):
    if len(tRows.find_parents('table')) == 2:   # There is a nested table to store the Running Position result.
        continue
    record = ""
    counter = 0   # Use to split the horse name and id.
    for tDatas in tRows.find_all('td'):
        counter += 1
        if tDatas.find('table'):
            continue
        if counter == 3:   # Use to split the horse name and id.
            data = tDatas.text.split("(")
            record = record + "," + data[0] + "," + data[1][0:4]
        else:
            record = record + "," + tDatas.text
    savedRecord = savedRecord + "\n" + record[1:]
print(savedRecord)"""

""" For Race Result Table"""
header = "place, horse_no, horse_name, horse_id, jockey, trainer, actual_weight, declared_weight, draw, length_behind_winner, finish_time, win_odds, running_position_1, running_position_2, running_position_3, running_position_4, running_position_5, running_position_6"
table = soup.find_all('table', {'class': 'tableBorder trBgBlue tdAlignC number12 draggable'})
tBody = table[0].find('tbody')
savedRecord = ""
for tRows in tBody.find_all('tr'):
    if len(tRows.find_parents('table')) == 2:   # There is a nested table to store the Running Position result.
        continue
    record = ""
    runningPositionTable = ["NA"] * 6
    column = 0   # Use to split the horse name and id.
    for tDatas in tRows.find_all('td'):
        column += 1
        if tDatas.find('table'):
            i = 0
            for runningPositions in tDatas.find_all('td'):
                runningPositionTable[i] = runningPositions.text
                i += 1
            continue
        if tRows
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