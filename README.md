# retropie-favorites-to-collection

In order to get the scrips to your pi: 
from the pi's terminal type:
```shell
 git clone https://github.com/talgreen1/retropie-favorites-to-collection.git
```

Then type: 
```shell
cd retropie-favorites-to-collection
```

## Create collection from favoties in gamelist
You can create a custom collection from all the favorites games in a specific 
gamelist file.

You should use the _fav-2-col.py_ script. Usage: 
```shell
python3 fav-2-col.py <full_path_to_gamelist_file> <Name_of_new_collection_file>
```
**Note**: Roms folder for gamelist files: /home/pi/RetroPie/roms/

For example: 
```shell
python3 ./fav-2-col.py /home/pi/RetroPie/roms/nes/gamelist.xml nes-fav
```