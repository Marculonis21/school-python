#!/usr/bin/env python3

import xml.etree.ElementTree as ET
tree = ET.parse('prijimacky_cermat.xml')
root = tree.getroot()

aList = []
for child in root.iter('uchazec'):
    radek = []
    for sub in child:
        if(sub.text != "\n"):
            radek.append(sub.text)
    for x in child.iter("zkouska"):
        #Někdo z uchazečů nemá vyplněné body
        #program tedy házel None
        #ThePowerOfTheDuck

        p = x.find("predmet").text
        if(p == None):
            radek.append("0")
        else:
            radek.append(p)

        b = x.find("body").text
        if(b == None):
            radek.append("0")
        else:
            radek.append(b)

    aList.append(radek)

aList.sort(key = lambda x: int(x[6]) + int(x[8]), reverse=True)

for loop in range(len(aList)):
    single = aList[loop]
    if(loop < 90):
        print("Pořadí: {}. - {} {} ({}. ročník)\nbody: Čj: {}; Ma: {}\nbody celkem: {}\n".format(loop+1,single[0],single[1],single[2],single[6],single[8],int(single[6])+int(single[8])))
    if(loop == 90):
        print(50*"="+"\n"+50*"="+"\n"+50*"=")
        print()
    if(loop >= 90):
        print("Pořadí: {}. - {} {} ({}. ročník)\nbody: Čj: {}; Ma: {}\nbody celkem: {}\n".format(loop+1,single[0],single[1],single[2],single[6],single[8],int(single[6])+int(single[8])))
