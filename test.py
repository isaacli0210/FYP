import urllib.request
from bs4 import BeautifulSoup

# theURL = "http://racing.hkjc.com/racing/Info/Meeting/Results/English/Local/20080412/ST/9"
#
# while(True):
#     thePage = urllib.request.urlopen(theURL)
#     soup = BeautifulSoup(thePage, "html.parser")
#
#     table = soup.find('table', {'class': 'tableBorder trBgBlue tdAlignC number12 draggable'})
#     # Wait for page fully loaded.
#     if table != None:
#         tBody = table.find('tbody')
#         print(tBody)
#         break

theURL = "http://racing.hkjc.com/racing/Info/Meeting/Results/English/Local/20080412/ST/1"

while(True):
    thePage = urllib.request.urlopen(theURL)
    soup = BeautifulSoup(thePage, 'html.parser')

    div = soup.find('div', {'id': 'divErrorMsg'})
    print(div)
    break
    # div = soup.find('div', {'class': 'raceNum clearfix'})
    # counter = 0
    # if div is not None:
    #     for hrefs in div.find_all('a'):
    #         counter += 1
    #         print(counter)
    #     break


