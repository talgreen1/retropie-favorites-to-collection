import consts
import xml.etree.ElementTree as ET
import sys
import os
import shutil
import datetime


def backup_gamelist_file():
    now = str(datetime.datetime.now())[:19]
    now = now.replace(":", "_")
    shutil.copy(gamelist_file_name, gamelist_file_name + "." + str(now))


if len(sys.argv) != 3:
    print(f"Usage: {os.path.basename(__file__)} <Full_path_to_custom_collection_file> <full_path_to-gamelist_file>\n")
    print(f"Note: Custom collection folder: {consts.CUSTOM_COLLECTION_PATH}")
    print(f"Note: Roms folder for gamelist files: {consts.ROMS_PATH}")
    sys.exit(-1)

collection_file_name = sys.argv[1]
gamelist_file_name = sys.argv[2]

backup_gamelist_file()

col_file = open(collection_file_name, 'r')
col_lines = col_file.readlines()

count = 0
# Strips the newline character
for line in col_lines:
    print(">" + line)

# gamelist_file_name = sys.argv[1]
# collection_file_name = get_collection_file_name()
# collection_file_name = sys.argv[2]
# if not collection_file_name.endswith(".cfg"):
#     collection_file_name += ".cfg"
# if not collection_file_name.startswith(consts.CUSTOM_PREFIX):
#     collection_file_name = consts.CUSTOM_PREFIX + collection_file_name
#
# collection_file_name = consts.CUSTOM_COLLECTION_PATH + collection_file_name
#
# if os.path.isfile(collection_file_name):
#     print(f"file {collection_file_name} already exists. Please supply new file name")
#     sys.exit(-1)
#
# collection_file = open(collection_file_name, "w+")
# gamelist_file = open(gamelist_file_name)
#
# print(f"Creating the following file:{collection_file_name}\n")
#
# gamelist_path = os.path.dirname(os.path.abspath(gamelist_file_name))
#
# tree = ET.parse(gamelist_file_name)
# root = tree.getroot()
#
# print(f"Adding the following games:\n")
# for child in root.findall('game'):
#     favorite = child.findall('favorite')
#     if len(favorite) == 1:
#         print(gamelist_path + "/" + child.find("path").text[2:])
#         collection_file.write(gamelist_path + "/" + child.find("path").text[2:] + "\n")
#
# collection_file.close()
#
# print("\nDone.")
