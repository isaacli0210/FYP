import urllib.request
from bs4 import BeautifulSoup

""" Define URL """
days = ["{:02d}".format(x) for x in range(32)[1:]]
races = [str(x) for x in range(13)[1:]]

file = open("RaceDateSTBefore2008.csv", "a")
#file = open("RaceDateSTBefore2008.csv", "w")


for day in range(len(days)):
    #theURL = "http://racing.hkjc.com/racing/Info/Meeting/Results/English/Local/201809" + days[day] + "/ST/1" + "\n"
    theURL = "http://racing.hkjc.com/racing/information/english/Racing/LocalResults.aspx?RaceDate=1998/01/" + days[day] + "&Racecourse=ST&RaceNo=1"

    while(True):
        thePage = urllib.request.urlopen(theURL)
        soup = BeautifulSoup(thePage, "html.parser")

        errorDiv = soup.find('div', {'id': 'errorContainer'})
        #table = soup.find('table', {'class': 'f_tac table_bd'})
        #resultDiv = soup.find('class', {'performance'})
        testDiv = soup.find('class', {'localResults commContent'})
        if errorDiv is not None:
            break
        elif testDiv is not None:
            file.write(theURL)
            print(theURL)
            break
        else:
            print("Table = None AND errrorDiv = None")
            break

file.close()
