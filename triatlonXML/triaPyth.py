#!/usr/bin/env python3

import xml.etree.ElementTree as ET
tree = ET.parse('triatlon_prubeh.xml')
root = tree.getroot()

for zavodnik in root:
    print(zavodnik.attrib["prijmeni"], zavodnik.attrib["jmeno"])
    print(zavodnik.find("vysledky").attrib["kategorie"])
    for x in zavodnik.iter("cas_prubezny"):
        print(x.attrib["disciplina"])
        print(x.text)

    quit()
    
