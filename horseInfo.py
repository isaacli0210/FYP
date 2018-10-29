import urllib.request
from bs4 import BeautifulSoup

theURL = "http://racing.hkjc.com/racing/information/English/Horse/OtherHorse.aspx?HorseNo=J121"
#theURL = "http://racing.hkjc.com/racing/information/English/Horse/Horse.aspx?HorseNo=V071"
thePage = urllib.request.urlopen(theURL)
soup = BeautifulSoup(thePage, 'html.parser')

# table = soup.find_all('table')[0]
# # tr = table.find_all('tr')[0]
# # td = tr.find_all('td')
table = soup.find('table', {'width': '492'})

record = []

for tRows in table.find_all('tr'):
    for tDatas in tRows.find_all('td'):
        record.append(tDatas.text)

countryAndAge = record[1].split("/")
country = countryAndAge[0][2:]
if len(countryAndAge) == 1:
    age = "NA"
else:
    age = countryAndAge[1].strip()

totalStake = record[10]

print(country)
print(age)
print(totalStake)