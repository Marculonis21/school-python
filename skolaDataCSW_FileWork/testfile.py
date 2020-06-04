#!/usr/bin/env python3

infile = open("./skola_data.csv", "r")

alines = infile.readlines()
infile.close()

seznam = []
for line in alines:
    prijmeni,jmeno,trida,other = line.split(',',3)
    seznam.append([jmeno,prijmeni,trida,other])

seznam = sorted(seznam,key=lambda x: x[1])
for jmeno,prijmeni,trida,_ in seznam:
    print(jmeno,prijmeni,trida)

    znamky = {}

    _ = "".join(list(_)[:len(_)-1])

    for z in _.split(','):
        mark,sub= z.split(':')

        try:
            znamky[sub].append(mark)
        except KeyError:
            znamky[sub] = [mark]

    print(_)
    print(znamky)

print("DONE")

