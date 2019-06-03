#!/usr/bin/env python3

def RotujMrizku(mrizka):
    novaMrizka = []
    for x in range(8):
        sloupec = []
        for _y in range(7,-1,-1):
            sloupec.append(mrizka[_y][x])

        novaMrizka.append(sloupec)

    return novaMrizka

f1 = open("mrizka.txt")
mLines = f1.readlines()
f1.close()

f2 = open("mat19_sifra.txt")

mrizka = []
for line in mLines:
    radek = []
    s = list(line)
    s.pop()
    for p in s:
        radek.append([p])

    mrizka.append(radek)

'''
for i in mrizka:
    print(i)
'''

sLines = f2.readlines()
MatSifry = []
sifra = []
for item in sLines:
    _item = [x for x in list(item) if not x == " "]
    _item.pop()
    
    if(len(_item) == 0):
        MatSifry.append(sifra)
        sifra = []
        continue
        
    radek = []
    for p in _item:
        radek.append([p])

    sifra.append(radek)

'''
for i in MatSifry:
    for x in i:
        print(x)
   '''
#RotujMrizku(mrizka)
ss = ""
for loop in range(len(MatSifry)):
    for yLoop in range(4):
        sifra = MatSifry[loop]

        for y in range(len(mrizka)):
            for x in range(len(mrizka)):
                if(mrizka[y][x][0] == "1"):
                    ss += str(sifra[y][x][0])

        mrizka = RotujMrizku(mrizka)
    
print(ss)
