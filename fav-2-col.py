import xml.etree.ElementTree as ET
import sys
import os

#todo: add print for output file name, and all added file
#todo: if dest file name does not have .cfg, add it
#todo: In usage - add info that the gameinfo file should be in the roms folder

CUSTOM_COLLECTION_PATH = "/home/pi/.emulationstation/collections/"

if len(sys.argv) != 3:
    print(f"Usage: {os.path.basename(__file__)} <path to gamelist file> <collection file name>")
    sys.exit(-1)

gamelist_file_name = sys.argv[1]
collection_file_name = CUSTOM_COLLECTION_PATH + sys.argv[2]

if os.path.isfile(collection_file_name):
    print(f"file {collection_file_name} already exists. Please supply new file name")
    sys.exit(-1)
collection_file = open(collection_file_name, "w+")
gamelist_file = open(gamelist_file_name)

gamelist_path = os.path.dirname(os.path.abspath(gamelist_file_name))

tree = ET.parse(gamelist_file_name)
root = tree.getroot()

for child in root.findall('game'):
    favorite = child.findall('favorite')
    if len(favorite) == 1:
        print(gamelist_path + "/" + child.find("path").text[2:])
        collection_file.write(gamelist_path + "/" + child.find("path").text[2:] + "\n")

collection_file.close()
# print(child.find("name").text)
# print(child. find("name").text)
