import urllib.request
from bs4 import BeautifulSoup

""" Define URL """
days = ["{:02d}".format(x) for x in range(32)[1:]]
races = [str(x) for x in range(13)[1:]]

file = open("RaceDateST.csv", "a")
#file = open("RaceDateST.csv", "w")


for day in range(len(days)):
    theURL = "http://racing.hkjc.com/racing/Info/Meeting/Results/English/Local/201809" + days[day] + "/ST/1" + "\n"

    while(True):
        thePage = urllib.request.urlopen(theURL)
        soup = BeautifulSoup(thePage, "html.parser")

        errorDiv = soup.find('div', {'class': 'contentDiv'})
        if errorDiv is not None:
            break
        else:
            table = soup.find('table', {'class': 'tableBorder trBgBlue tdAlignC number12 draggable'})

            if table is not None:
                file.write(theURL)
                print(theURL)
                break
            else:
                print("Table = None AND errrorDiv = None")
                break

file.close()
