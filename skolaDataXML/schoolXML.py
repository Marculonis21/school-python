#!/usr/bin/env python3

import xml.etree.ElementTree as ET
tree = ET.parse('skola_data.xml')
root = tree.getroot()

Z = "Zsv,Vv,D,F,IVT,Bi,Čj,Z,Aj,Ch,Tv,Hv,Fj,M"
        
sList = []
i = 0
for student in root:
    sList += [[("{} {}".format(student.attrib["jmeno"],student.attrib["prijmeni"])),student.attrib["trida"]]]

zList = [["" for i in range(len(Z.split(",")))] for y in range(len(sList))]

loop = -1
for student in root:
    loop += 1
    for znamky in student.iter("znamky"):
        for x in znamky:
            _pr = x.attrib["predmet"]
            _z = x.text
            zList[loop][(Z.split(",")).index(_pr)] += "{}".format(_z)

#TEXT

for sIndex in range(len(sList)):
    stud = sList[sIndex]
    _name = stud[0]
    _class = stud[1]
    
    _allz = zList[sIndex]
    allAverageS = 0
    allAverageC = 0
    
    print("{} (Třídá {})".format(_name,_class))
    for x in range(len(Z.split(","))):
        
        pZ = list(_allz[x])
        averageS = 0
        averageC = 0
        
        for avg in pZ:
            averageS += int(avg)
            averageC += 1

        try:
            average = averageS/averageC
            allAverageS += average
            allAverageC += 1
            
            print("{:<3}".format(Z.split(",")[x]), end="")
            print(" ({:.2f}): ".format(average), end="")
            for m in pZ:
                print("{} ".format(m), end="")
        except ZeroDivisionError:
            pass
        
        print()
    print("celkový průměr: {:.2f}".format(allAverageS/allAverageC))    
    print()
