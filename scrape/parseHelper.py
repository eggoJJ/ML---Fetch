from bs4 import BeautifulSoup
import copy
import csv
import os


def parseHTML():
    
    with open('parse-0.html', 'r') as f:
        data = f.read()
    
    soup = BeautifulSoup(data, 'html.parser')
    roster = []    
    Player = [None for i in range(25)]
    count = 0 
    
    #firstParse = soup.find("td", { "class" : "left" }) 
    firstParse = soup.find_all('table')[2].find_all('tr')


    for things in firstParse:
        tempPlayer = copy.deepcopy(Player)
        x = str(things).split('>')
        tempPlayer[0] = ((x[5].split('<'))[0])
        i = 8 
        j = 1
        if count > 0 and count < 16:
            while(i < 55):
                tempPlayer[j] = ((x[i].split('<'))[0])
                i+=2
                j+=1
            roster.append(tempPlayer)
        count +=1

    secondParse = soup.find("div", { "class" : "overthrow table_container" }) 
    j = 0
    draftCheck = []
    for seconds in secondParse:
        if j == 1:
            y = str(seconds).split('<tbody>')
            z = y[1].split('</tr')
            for k in range(len(roster)):
                t = z[k].split('left')
                if t[1][1] != 's': draftCheck.append(0)
                else: draftCheck.append(1)
        j+=1

    for j in range(len(roster)):
        roster[j].append(draftCheck[j])

    with open('tmp_file.txt', 'a') as f:
        csv.writer(f, delimiter=',').writerows(roster)
    
    if os.path.exists("parse-0.html"):
        os.remove("parse-0.html")
    else:
        print("The file does not exist")    


def parseSchools():
    with open('schoolList.html', 'r') as f:
        data = f.read()
    soup = BeautifulSoup(data, 'html.parser')

    ayeRefs = soup.find_all('a' ,href = True)

    schoolEnds = []
    for i in range (34,470):
        #temp = str(ayeRefs[i])(.split('schools'))[1].split('/">')[0]
        temp = str(ayeRefs[i]).split('schools')[1].split('">')[0]
        schoolEnds.append('https://www.sports-reference.com/cbb/schools' + temp + '2017.html')
        schoolEnds.append('https://www.sports-reference.com/cbb/schools' + temp + '2016.html')
        schoolEnds.append('https://www.sports-reference.com/cbb/schools' + temp + '2015.html')
        schoolEnds.append('https://www.sports-reference.com/cbb/schools' + temp + '2014.html')
        schoolEnds.append('https://www.sports-reference.com/cbb/schools' + temp + '2013.html')

    with open('schoolURLS.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % urls for urls in schoolEnds)

def readURLS():
    with open('schoolURLS.txt', 'r') as f:
        x = f.readlines()
    return x
parseSchools()
#parseHTML()