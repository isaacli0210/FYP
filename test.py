import urllib.request
from bs4 import BeautifulSoup

theURL = "http://racing.hkjc.com/racing/Info/Meeting/Results/English/Local/20080412/ST/9"

while(True):
    thePage = urllib.request.urlopen(theURL)
    soup = BeautifulSoup(thePage, "html.parser")

    table = soup.find('table', {'class': 'tableBorder trBgBlue tdAlignC number12 draggable'})
    # Wait for page fully loaded.
    if table != None:
        tBody = table.find('tbody')
        print(tBody)
        break