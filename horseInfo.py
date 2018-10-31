import urllib.request
from bs4 import BeautifulSoup

#header = "horse_id, country, age, sex, import_type, total_stakes, first, second, third, total_race_no, sire, dam, dam_sire"

#file = open("HorseInfo.csv", "a")
horseIDFile = open("horseID/HorseID_E.txt", "r")

#file.write(header)

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
cookie = "LocalRaceCardSetting=1%7C1%7C0%7C1%7C0%7C0%7C0%7C1%7C1%7C1%7C1%7C0%7C0%7C1%7C1%7C0%7C0%7C0%7C0%7C1%7C1%7C0%7C1%7C1%7C0; AMCVS_06AB2C1653DB07AD0A490D4B%40AdobeOrg=1; AMCV_06AB2C1653DB07AD0A490D4B%40AdobeOrg=-330454231%7CMCIDTS%7C17836%7CMCMID%7C43943549019558521101997079126246629764%7CMCAAMLH-1541572328%7C11%7CMCAAMB-1541572328%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1540974728s%7CNONE%7CMCAID%7C2DC531E1052AB1A6-40000301A00288F1%7CMCSYNCSOP%7C411-17792%7CvVersion%7C3.1.2; custProIn=; s_visit=1; s_cc=true; s_sq=%5B%5BB%5D%5D; gpv_p5=http%3A%2F%2Fracing.hkjc.com%2Fracing%2Finformation%2FEnglish%2FHorse%2FOtherHorse.aspx%3FHorseNo%3DA018; HKJCSSOGP=1540970303468; BotMitigationCookie_9518109003995423458=\"170279001540971459f1z9uBVdTAFeoVqliqoPzRZv+Lw=\""
headers = {"User-Agent": user_agent, "Cookie": cookie}

for horseID in horseIDFile.read().splitlines():

    theURL = "http://racing.hkjc.com/racing/information/English/Horse/Horse.aspx?HorseNo=" + horseID
    #theURL = "http://racing.hkjc.com/racing/information/English/Horse/Horse.aspx?HorseNo=A018"
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

            print(totalStakes)

            #saveRecord = saveRecord + "\n" + horseID + ", " + country + ", " + age + ", " + sex + ", " + importType + ", " + totalStake + ", " + first + ", " + second + ", " + third + ", " + totalRace + ", " + sire + ", " + dam + ", " + dam_sire
            #file.write(saveRecord)
            print(saveRecord)
            break

        else:
            print(horseID + "No such table")
            break

horseIDFile.close()
#file.close()
