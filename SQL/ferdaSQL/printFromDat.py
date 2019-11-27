#!/usr/bin/env python3

import pymysql

conn = pymysql.connect(host='localhost',
                       user='skolnik',
                       password='123456789',
                       db='skola',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

curr = conn.cursor()


print("Jaké žáky chcete najít? př.: třída:B rokmat:2014 třídní:Kout")
selectQ = input().split(' ')
print(selectQ)

sqlEND = ''
start = True
for item in selectQ:
    if not(start):
        sqlEND.join(' and ')

    if('třída' in item):
        sqlEND+=("abs.para='{}'".format(item.split(':')[1].upper())) 
    if('rokmat' in item):
        sqlEND+=("abs.rokmat='{}'".format(item.split(':')[1]))
    if('třídní' in item):
        sqlEND+=("profesor.prijmeni='{}'".format(item.split(':')[1])) 
    if('příjmení' in item):
        sqlEND+=("abs.prijmeni='{}'".format(item.split(':')[1]))
    if('jméno' in item):
        sqlEND+=("abs.jmeno='{}'".format(item.split(':')[1]))

print(sqlEND)
curr.execute("SELECT concat(abs.jmeno, ' ', abs.prijmeni) as 'Jméno', abs.para as 'Třída', abs.rokmat as 'Rok maturity', concat(profesor.jmeno,' ',profesor.prijmeni) as 'Třídní' from abs,profesor,tridni where tridni.id_prof=profesor.id_prof and abs.para=tridni.para and abs.rokmat=tridni.rokmat and abs.stdel=tridni.stdel and {}".format(sqlEND))
for i in curr:
    print(i)
conn.close()
