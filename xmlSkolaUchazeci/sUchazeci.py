import xml.etree.ElementTree as ET
tree = ET.parse('prijimacky_cermat.xml')
root = tree.getroot()

aList = []
for child in root.iter('uchazec'):
    radek = []
    for sub in child:
        if(sub.text != "\n"):
            radek.append(sub.text)
    for x in child.iter("zkouska"):
        radek.append(x.find("predmet").text)
        radek.append(x.find("body").text)

    aList.append([radek])

aList.sort(key=lambda x: int(x[0][6]))

print(aList[0])
