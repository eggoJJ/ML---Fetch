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

#parseHTML()