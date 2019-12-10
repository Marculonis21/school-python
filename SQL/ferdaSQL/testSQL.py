#!/usr/bin/env python3

""" Vypsání všech třídních učitelů podle roku maturity """
import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host='localhost',
                           user='skolnik',
                           password='123456789',
                           db='skola',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

    cursor = conn.cursor()

    print("Výpis třídních učitelů dle roku maturity")
    print("----------------------------------------")
    print("Zadejte rok maturity:")
    while True:
        try:
            rokmat = int(input())
            break
        except:
            print("Špatně zadáno - zadejte číselnou hodnotu")

    sql = "select profesor.titul, profesor.prijmeni, profesor.jmeno from profesor, tridni where profesor.id_prof = tridni.id_prof and tridni.rokmat = %s"

    cursor.execute(sql, rokmat)

    print("\nV roce {} byli třídními maturitních ročníků učitelé:".format(rokmat))
    for item in cursor:
        print("{} {} {}".format(item['titul'],item['prijmeni'],item['jmeno']))

    conn.close()



