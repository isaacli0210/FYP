import urllib
import urllib.request
from bs4 import BeautifulSoup

""" Define URL """
years = [str(x) for x in range(2008, 2019)]
months = ["{:02d}".format(x) for x in range(13)[1:]]
days = ["{:02d}".format(x) for x in range(32)[1:]]
venues = ["ST", "HV"]
races = [str(x) for x in range(13)[1:]]


theURL = "http://racing.hkjc.com/racing/Info/Meeting/Results/English/Local/20180610/ST/9"
thePage = urllib.request.urlopen(theURL)
soup = BeautifulSoup(thePage, "html.parser")


""" For Race General Information Table"""
table = soup.findAll('table', {'class': 'tableBorder0 font13'})
for tRows in table[0].findAll('tr'):
    for tDatas in tRows.findAll('td'):
        print(tDatas.text)


""" For Race Result Table"""
table = soup.findAll('table', {'class': 'tableBorder trBgBlue tdAlignC number12 draggable'})
tBody = soup.find('tbody')
savedRecord = ""
for tRows in tBody.findAll('tr'):
    record = ""
    for tDatas in tRows.findAll('td'):
        record = record + "," + tDatas.text
    savedRecord = savedRecord + "\n" + record[1:]
print(savedRecord)

