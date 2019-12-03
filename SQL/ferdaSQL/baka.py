#!/usr/bin/env python3
import pymysql

def menuWork():
    print()
    mess = [('s','Zadání studenta'),
            ('z','Zadání známek'),
            ('v','Výpis studenta'),
            ('k','Konec')]
    
    for kod, text in mess:
        print("{:>16} ----- {}".format(text,kod.upper()))

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

    print()
    return volba

def zadejStudenta(cursor):
    sql = "INSERT into student (prijmeni,jmeno) values (%s,%s)"
    prijmeni = input("Zadej příjmení studenta: ")
    jmeno = input("Zadej jméno studenta: " )

    cursor.execute(sql,(prijmeni,jmeno))

# return [id,prijmeni,jmeno]
def vyberStudenta(cursor):
    out = input("\nZadej příjmení studenta: ")

    idS = ''
    cursor.execute("select * from student")
    for item in cursor:
        if(out == item['prijmeni']):
            idS = int(item['id'])
            return [idS,item['prijmeni'],item['jmeno']]

def vypisStudenta(cursor, out):
    sql = "SELECT predmet, znamka from znamky, student where znamky.id_student=student.id and student.prijmeni=%s"
    cursor.execute(sql, (out[1]))
    
    #seznam známek
    Z_list = {} 
    for item in cursor:
        try:
            Z_list[item['predmet']].append(item['znamka'])
        except KeyError:
            Z_list[item['predmet']] = []
            Z_list[item['predmet']].append(item['znamka'])

    print("-"*40)
    print("Student: {} {}".format(out[1],out[2]))
    print("Známky:")

    keys = list(Z_list)
    for key in keys:
        print("{:3} -> ".format(key), end="")
        
        avg = 0
        for znamka in Z_list[key]:
            print("{:2}|".format(znamka), end="")
            if('-' in str(znamka)): avg += int(str(znamka)[1:])+0.5
            else: avg += znamka

        avg = avg/len(Z_list[key])
        print("  avg: {}".format(avg))

    print("-"*40)


def vypisAll_student(cursor):
    sql1 = "SELECT * from student"
    cursor.execute(sql1)
    for item in cursor:
        print("{} {}".format(item['prijmeni'], item['jmeno']))

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
            out = vyberStudenta(cursor)
            vypisStudenta(cursor, out)
            pass

        conn.commit()

    conn.close()
