import xml.etree.ElementTree as ET
import sys
import os

if len(sys.argv) != 3:
    print("Please enter 2 file names")
    sys.exit(-1)
gamelist_file_name = sys.argv[1]
gamelist_file = open(gamelist_file_name)

gamelist_path = os.path.dirname(os.path.abspath(gamelist_file_name))

tree = ET.parse('./gamelist.xml')
root = tree.getroot()

for child in root.findall('game'):
    favorite = child.findall('favorite')
    if len(favorite) == 1:
        print(gamelist_path + "\\" + child.find("path").text[2:])

    # print(child.find("name").text)
    # print(child. find("name").text)
