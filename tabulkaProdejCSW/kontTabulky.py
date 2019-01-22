#!/usr/bin/env python3

file = open("tabulka_prodej.csv")

lines = file.readlines()

file.close

aLines = []
for line in lines:
    x = list(line)
    x.remove("\n")
    aLines += ["".join(x)]

names = []
places = []

for line in aLines:
    sss = line.split(",")
    if(sss[1] in names):
        pass
    else:
        names += ["{}".format(sss[1])]

    if(sss[2] in places):
        pass
    else:
        places += ["{}".format(sss[2])]


names = sorted(names)
places = sorted(places)

allList = [[0 for x in range(len(places))] for i in range(len(names))]

'''
print(names)
print(places)
print(allList)
'''

for line in aLines:
    x = line.split(",")
    _name = x[1]
    _place = x[2]
    _value = x[3]

    allList[names.index(_name)][places.index(_place)] += int(_value)

#head
print("{:<20}".format("Města/Prodejce"),end="")
for name in names:
    print("{:<12}".format(name),end="")

print()

#body
for _place in places:
    print("{:<20}".format(_place),end="")
    for _name in names:
        if(allList[names.index(_name)][places.index(_place)] == 0):
            print("{:<12}".format(6*"-"),end="")
        else:
            print("{:<12}".format("{:6}".format(allList[names.index(_name)][places.index(_place)])),end="")

    print()
