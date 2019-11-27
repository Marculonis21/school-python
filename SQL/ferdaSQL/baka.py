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
            sql1 = "SELECT prijmeni, jmeno, id from student"
            cursor.execute(sql1)
            for item in cursor:
                print("{} {}".format(item['prijmeni'], item['jmeno']))
            
            out1 = input("Zadejte příjmení studenta: ")
            idS = ''
            for item in cursor:
                if(out1 == item['prijmeni']):
                    idS = item['id']

            sql2 = "INSERT into znamky (id_studenta, )" 
            pass
        elif(act == 'v'):
            pass

        conn.commit()

    conn.close()
