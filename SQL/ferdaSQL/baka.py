#!/usr/bin/env python3
import pymysql

def menuWork():
    print()
    mess = [('s','Zadání studenta'),
            ('z','Zadání známek'),
            ('v','Výpis studenta'),
            ('k','Konec')]

    for kod, text in mess:
        print("{} ----- {}".format(kod,text))

    while True:
        volba = input("Volba? ").lower()
        good=False
        for kod,text in mess:
            if(volba in kod):
                good=True
                break
        if(good):
            break
        else:
            print("Wrong INPUT")

    return volba

def zadejStudenta(cursor):
    sql = "INSERT into student (prijmeni,jmeno) values (%s,%s)"
    prijmeni = input("Zadej příjmení studenta: ")
    jmeno = input("Zadej jméno studenta: " )

    cursor.execute(sql,(prijmeni,jmeno))

def vypisAll_student(cursor):
    sql1 = "SELECT * from student"
    cursor.execute(sql1)
    for item in cursor:
        print("{} {}".format(item['prijmeni'], item['jmeno']))

    return cursor

def vyberStudenta(cursor)
        out = input("Zadej příjmení studenta: ")

        idS = ''
        cursor.execute("select * from student")
        for item in cursor:
            if(out == item['prijmeni']):
                idS = int(item['id'])
                return [idS,item['prijmeni'],item['jmeno']]

    def zadejZnamku(cursor,out):
        sql2 = "INSERT into znamky (id_student, predmet, znamka) values (%s,%s,%s)"
        predmet, znamka = input("Zadejte předmět a známku (př.: M 1 nebo Cj 5):\n").split(' ')

        cursor.execute(sql2, (out[0], predmet, znamka))

if __name__ == '__main__':
    conn = pymysql.connect(host='localhost',
                           user='admin',
                           password='adminadmin',
                           db='baka',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

    cursor = conn.cursor()

    while True:
        act = menuWork()

        if(act == 'k'):
            break
        elif(act == 's'):
            zadejStudenta(cursor)
        elif(act == 'z'):
            vypisAll_student(cursor)
            out = vyberStudenta(cursor)
            zadejZnamku(cursor, out)
        elif(act == 'v'):
            vypisAll_student(cursor)

            pass

        conn.commit()

    conn.close()
