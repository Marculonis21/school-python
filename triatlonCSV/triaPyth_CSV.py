#!/usr/bin/env python3

file = open("triatlon_data.csv")
lines = file.readlines()
file.close()

def timeCounter(timeValue):
    hour = 0
    minu = 0
    secs = 0

    x = []
    for i in timeValue:
        time = i.split(':')
        
        hour += int(time[0])
        minu += int(time[1])
        secs += int(time[2])

        if(secs >= 60):
            minu += 1
            secs -= 60
            
        if(minu >= 60):
            hour += 1
            minu -= 60

    
    timeSplit = "{}:{}:{}".format(hour,minu,secs)
    timeSum = 3600*hour + 60*minu + secs
    return [timeSplit, timeSum]

aLines = []
for line in lines:
    xx = list(line)
    xx.remove(xx[len(xx)-1])
    aLines.append("".join(xx))

allList = []
CATS = ""


for loop in range(len(aLines)):
    item = aLines[loop]
    sitem = item.split(',')
    
    if not (sitem[2] in CATS):
        CATS += "{},".format(sitem[2])
    
    row = []
    row.append(sitem)

    row.append(timeCounter([sitem[3],sitem[4],sitem[5]]))
    allList.append(row)

x = CATS.split(",")
x.pop()
CATS = x

catList = [[] for i in range(len(CATS))]

for item in allList:
    catList[CATS.index(item[0][2])].append(item)

for loop in range(len(CATS)):
    catList[loop] = sorted(catList[loop], key = lambda x: int(x[1][1]))

for it in range(len(CATS)):
    print("Výsledky kategorie: {}\n".format(CATS[it]))
    
    for item in catList[it]:
        print("{:<20}{:<20}{:<15}{:<15}{:<15}{:<15}".format(item[0][0],item[0][1],item[0][3],item[0][4],item[0][5],item[1][0]))

    print("\n")
