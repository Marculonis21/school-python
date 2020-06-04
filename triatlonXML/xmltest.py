#!/usr/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse("./triatlon_prubeh.xml")

root = tree.getroot()

for zavodnik in root:
    data = zavodnik.attrib
    print("{} {}".format(data['jmeno'],data['prijmeni']))

    for vysledky in zavodnik.iter('vysledky'):
        print(vysledky.attrib['kategorie'])
        for cas in vysledky.iter('cas_prubezny'):
            print("D:{} => {}".format(cas.attrib['disciplina'], cas.text))
