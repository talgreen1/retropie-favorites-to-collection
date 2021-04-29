import xml.etree.ElementTree as ET
tree = ET.parse('./gamelist.xml')
root = tree.getroot()

for child in root.findall('game'):
    favorite = child.findall('favorite')
    if len(favorite)==1:
        print (child.find("name").text)

    # print(child.find("name").text)
    # print(child. find("name").text)
