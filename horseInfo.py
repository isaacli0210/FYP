import urllib.request
from bs4 import BeautifulSoup

header = "country, age, sex, import_type, total_stakes, first, second, third, total_race_no, sire, dam, dam_sire"

#file = open("HorseInfo.csv", "w")
horseIDFile = open("horseID/HorseID_E.txt", "r")

#file.write(header)

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
cookie = "LocalRaceCardSetting=1%7C1%7C0%7C1%7C0%7C0%7C0%7C1%7C1%7C1%7C1%7C0%7C0%7C1%7C1%7C0%7C0%7C0%7C0%7C1%7C1%7C0%7C1%7C1%7C0; s_fid=1AC1B116BD9C53EE-228034BA782B560E; localDragTable=5%2F8%2C8%2F5; language=english; custProIn=; AMCVS_06AB2C1653DB07AD0A490D4B%40AdobeOrg=1; AMCV_06AB2C1653DB07AD0A490D4B%40AdobeOrg=-330454231%7CMCIDTS%7C17834%7CMCMID%7C22588011069404082340999913768390403196%7CMCAAMLH-1541490322%7C11%7CMCAAMB-1541490322%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1540892722s%7CNONE%7CMCAID%7C2DC32E28052AB5FE-40000301E01929CB%7CMCSYNCSOP%7C411-17792%7CvVersion%7C3.1.2; s_cc=true; HKJCSSOGP=1540889588024; s_visit=1; BotMitigationCookie_9518109003995423458=\"263985001540889594I/d5jl/CiSbWztYB6/UAJxImCts=\"; s_sq=%5B%5BB%5D%5D; gpv_p5=http%3A%2F%2Fracing.hkjc.com%2Fracing%2Finformation%2FEnglish%2FHorse%2FHorse.aspx%3FHorseNo%3DA051"
headers = {"User-Agent": user_agent, "Cookie": cookie}


for horseID in horseIDFile.read().splitlines():

    theURL = "http://racing.hkjc.com/racing/information/English/Horse/Horse.aspx?HorseNo=" + horseID
    request = urllib.request.Request(theURL, headers=headers)

    print(horseID + "..................")
    while(True):
        response = urllib.request.urlopen(request)
        soup = BeautifulSoup(response, 'html.parser')

        table = soup.find('table', {'width': '492'})
        if table is not None:
            record = []
            i = 0
            for tRows in table.find_all('tr'):
                for tDatas in tRows.find_all('td'):
                    #print(str(i) + tDatas.text)
                    i += 1
                    record.append(tDatas.text)

            countryAndAge = record[1].split("/")
            country = countryAndAge[0][2:]
            if len(countryAndAge) == 1:
                age = "NA"
            else:
                age = countryAndAge[1].strip()

            if age == "NA":
                totalStake = record[13][3:]
            else:
                totalStake = record[17][3:]

            print(country)
            print(age)
            print(totalStake)
            break

        else:
            print("No such table")
            break
