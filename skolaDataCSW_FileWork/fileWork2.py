#!/usr/bin/env python3

import locale
locale.setlocale(locale.LC_ALL, 'cs_CZ.UTF-8')

f = open("skola_data.csv")

lines = f.readlines()

f.close()

_zList_ = "Čj,Aj,Nj,Fj,Zsv,D,M,F,Ch,Bi,IVT,Tv,Vv,Hv"

allList = []
for line in lines:
    s = line.split(",", 3)
    s[3] = "".join(list(s[3])[:len(s[3])-1])
    allList += [s]

allList.sort(key = lambda x: x[2])

classList = []
for X in range(6):
    for Y in range(3):
        tridaList = []

        trida = ""
        if(Y == 0):
            trida = "S{}.A".format(X+1)
        elif(Y == 1):
            trida = "S{}.B".format(X+1)
        elif(Y == 2):
            trida = "S{}.C".format(X+1)

        for student in allList:
            if(student[2] == trida):
                tridaList.append(student)

        tridaList.sort(key = lambda x: locale.strxfrm(x[0]))
        classList += [tridaList]

classList.pop()

while True:
    try:
        dec1 = int(input("Vyhledat: Třídu --> 1\n"+
                         "          Žáka  --> 2\n"+
                         "          Vše   --> 3\n"))

        if(dec1 > 0 and dec1 < 4):
            break
    except ValueError:
        print("INVALID INPUT\n")

_classL_ = ["S1.A","S1.B","S1.C",
            "S2.A","S2.B","S2.C",
            "S2.A","S3.B","S3.C",
            "S4.A","S4.B","S4.C",
            "S5.A","S5.B","S5.C",
            "S6.A","S6.B","S6.C"]

if(dec1 == 1):
    while True:
        try:
            dec2 = input("Jakou třídu: ").upper()

            if(dec2 in _classL_):
                print()
                break
            else:
                print("Tato třída není v seznamu.\n")
        except ValueError:
            print("INVALID INPUT\n")

if(dec1 == 2):
    while True:
        try:
            dec2 = input("Zadejte jméno, příjmení žáka: ")

            dec2.strip()

            if(" " in dec2):
                n1, n2 = dec2.split(" ")
            else:
                n1 = "".join([dec2[i].upper() if i == 0 else dec2[i].lower() for i in range(len(dec2))])
                n2 = ""

            found = False
            for y in range(len(classList)-1):
                for x in classList[y]:
                    if((n1 in x and n2 in x) or (n1 in x and n2 == "")):
                        found = True
                        break

                if(found):
                    break

            if not(found):
                print("Tento žák není v seznamu.\n")
            else:
                print()
                break

        except ValueError:
            print("INVALID INPUT\n")

for trida in classList:
    if(dec1 == 1):
        if(trida[0][2] == dec2):
            print("#\n#")
            print("--------------------------Třída {}:------------------------".format(trida[0][2]))
            print("#\n#")

            for student in trida:
                print("{} {}:".format(student[0],student[1]))

                znamky = {}

                # print(student)
                for pair in student[3].split(","):
                    znamka,predmet = pair.split(":")

                    if(predmet in znamky):
                        znamky.update({predmet : znamky[predmet] + "," + znamka})
                    else:
                        znamky.update({predmet : znamka})

                for x in _zList_.split(","):
                    if(x in znamky):
                        print("{}:  {}  ({:.2f})".format(x, "".join(txt if not txt == "," else "; " for txt in znamky[x]), sum([float(num) for num in znamky[x].split(",")])/len(znamky[x].split(","))))

                print()

    elif(dec1 == 2):
        for student in trida:
            if((n1 in student and n2 in student) or (n1 in student and n2 == "")):
                print("{} {} ({}):".format(student[0],student[1],student[2]))

                znamky = {}

                # print(student)
                for pair in student[3].split(","):
                    znamka,predmet = pair.split(":")

                    if(predmet in znamky):
                        znamky.update({predmet : znamky[predmet] + "," + znamka})
                    else:
                        znamky.update({predmet : znamka})

                for x in _zList_.split(","):
                    if(x in znamky):
                        print("{}:  {}  ({:.2f})".format(x, "".join(txt if not txt == "," else "; " for txt in znamky[x]), sum([float(num) for num in znamky[x].split(",")])/len(znamky[x].split(","))))

                print()

    else:
        for trida in classList:
            print("#\n#")
            print("--------------------------Třída {}:------------------------".format(trida[0][2]))
            print("#\n#")

            for student in trida:
                print("{} {}:".format(student[0],student[1]))

                znamky = {}

                # print(student)
                for pair in student[3].split(","):
                    znamka,predmet = pair.split(":")

                    if(predmet in znamky):
                        znamky.update({predmet : znamky[predmet] + "," + znamka})
                    else:
                        znamky.update({predmet : znamka})

                for x in _zList_.split(","):
                    if(x in znamky):
                        print("{}:  {}  ({:.2f})".format(x, "".join(txt if not txt == "," else "; " for txt in znamky[x]), sum([float(num) for num in znamky[x].split(",")])/len(znamky[x].split(","))))

                print()
