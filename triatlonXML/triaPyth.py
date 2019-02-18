#!/usr/bin/env python3

import xml.etree.ElementTree as ET
tree = ET.parse('triatlon_prubeh.xml')
root = tree.getroot()

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


allList = {}
for zavodnik in root:
    #print(zavodnik.attrib["prijmeni"], zavodnik.attrib["jmeno"])
    name = "{} {}".format(zavodnik.attrib["prijmeni"], zavodnik.attrib["jmeno"])
    #print(zavodnik.find("vysledky").attrib["kategorie"])
    discT = []
    for x in zavodnik.iter("cas_prubezny"):
        #print(x.attrib["disciplina"])
        #print(x.text)
        discT.append(x.text)

    allList[name] = discT

for item in allList:
    allList[item] += [timeCounter(allList[item])]

sList = sorted(allList.items(), key = lambda x: int(x[1][3][1]))


#text
loop = 0
for line in sList:
    loop += 1
    
    _name = line[0]
    _t1 = line[1][0]
    _t2 = line[1][1]
    _t3 = line[1][2]
    _tS = line[1][3][0]

    print("Umístění: {}.".format(loop))
    print("{:<25} Plavání: {}{:>20}\n".format(_name,_t1,"Celkem: "+_tS)+
          " "*26+"Kolo:    {}\n".format(_t2)+
          " "*26+"Běh:     {}\n".format(_t3))
    
    
