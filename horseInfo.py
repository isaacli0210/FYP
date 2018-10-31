import urllib.request
from bs4 import BeautifulSoup

#header = "horse_id, country, age, sex, import_type, total_stakes, first, second, third, total_race_no, sire, dam, dam_sire"

file = open("HorseInfo.csv", "a")
horseIDFile = open("horseID/HorseID_V.txt", "r")

#file.write(header)

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
cookie = "LocalRaceCardSetting=1%7C1%7C0%7C1%7C0%7C0%7C0%7C1%7C1%7C1%7C1%7C0%7C0%7C1%7C1%7C0%7C0%7C0%7C0%7C1%7C1%7C0%7C1%7C1%7C0; s_fid=1AC1B116BD9C53EE-228034BA782B560E; localDragTable=5%2F8%2C8%2F5; language=english; AMCVS_06AB2C1653DB07AD0A490D4B%40AdobeOrg=1; custProIn=; s_cc=true; s_sq=%5B%5BB%5D%5D; AMCV_06AB2C1653DB07AD0A490D4B%40AdobeOrg=-330454231%7CMCIDTS%7C17836%7CMCMID%7C22588011069404082340999913768390403196%7CMCAAMLH-1541605848%7C11%7CMCAAMB-1541605848%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1541008248s%7CNONE%7CMCAID%7C2DC32E28052AB5FE-40000301E01929CB%7CMCSYNCSOP%7C411-17792%7CvVersion%7C3.1.2; BotMitigationCookie_9518109003995423458=\"695892001541003047ssew390Dt8Z12Y+XtS7nIu/vHKc=\"; s_visit=1; gpv_p5=http%3A%2F%2Fracing.hkjc.com%2Fracing%2Finformation%2FEnglish%2FHorse%2FHorse.aspx%3FHorseNo%3DV026; HKJCSSOGP=1541003050311"
headers = {"User-Agent": user_agent, "Cookie": cookie}

for horseID in horseIDFile.read().splitlines():

    theURL = "http://racing.hkjc.com/racing/information/English/Horse/Horse.aspx?HorseNo=" + horseID
    #theURL = "http://racing.hkjc.com/racing/information/English/Horse/Horse.aspx?HorseNo=CC228"
    request = urllib.request.Request(theURL, headers=headers)

    while(True):
        response = urllib.request.urlopen(request)
        soup = BeautifulSoup(response, 'html.parser')

        table = soup.find('table', {'width': '492'})
        saveRecord = ""

        if table is not None:
            record = []
            #i = 0
            for tRows in table.find_all('tr'):
                for tDatas in tRows.find_all('td'):
                    #print(str(i) + tDatas.text)
                    #i += 1
                    record.append(tDatas.text)


            countryAndAge = record[1].split("/")
            colorAngSex = record[5].split("/")

            country = countryAndAge[0][2:].rstrip()
            sex = colorAngSex[1].lstrip()
            importType = record[9][2:]

            if len(countryAndAge) == 1:
                age = "NA"
                totalStake = record[13][3:].rstrip().split(",")
                raceResults = record[17].split("-")
                sire = record[11][2:]
                dam = record[15][2:]
                dam_sire = record[19][2:]
            else:
                age = countryAndAge[1].strip()
                totalStake = record[17][3:].rstrip().split(",")
                raceResults = record[21].split("-")
                sire = record[19].split(":")[1].strip()
                dam = record[23][2:]
                dam_sire = record[27][2:]

            if len(totalStake) == 3:
                totalStake_1 = int(totalStake[0]) * 1000000
                totalStake_2 = int(totalStake[1]) * 1000
                totalStake_3 = int(totalStake[2])
                totalStakes = totalStake_1 + totalStake_2 + totalStake_3
            elif len(totalStake) == 2:
                totalStake_1 = int(totalStake[0]) * 1000
                totalStake_2 = int(totalStake[1])
                totalStakes = totalStake_1 + totalStake_2
            else:
                totalStakes = int(totalStake[0])

            first = raceResults[0][2:]
            second = raceResults[1]
            third = raceResults[2]
            totalRace = raceResults[-1]

            #print(totalStakes)

            saveRecord = saveRecord + "\n" + horseID + ", " + country + ", " + age + ", " + sex + ", " + importType + ", " + str(totalStakes) + ", " + first + ", " + second + ", " + third + ", " + totalRace + ", " + sire + ", " + dam + ", " + dam_sire
            file.write(saveRecord)
            print(saveRecord)
            break

        else:
            print(horseID + "No such table")
            break

horseIDFile.close()
file.close()
