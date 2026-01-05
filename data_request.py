# This script uses the requests library to grab json data from a runescape webpage
# It then strips out the data we want:
#   id
#   name
#   value
#   price
#   lastprice
#   volume
#   limit
#   examine
# And creates a new dictionary that is store in the file ge_data.txt

import requests
import json
import datetime


def refresh():
    try:
        response = requests.get('https://chisel.weirdgloop.org/gazproj/gazbot/os_dump.json')

        data = response.json()

        data_to_store = {}

        #loop through all objects in data 
        for itemid, itemdata in data.items():

            #skip unwanted (non dictionary) objects, i.e. timestamps
            if not isinstance(itemdata, dict):
                continue
            
            #create new dictionary from the data we want 
            new_item = {
                "id" : itemid,
                "name" : itemdata["name"],
                "value" : itemdata["value"],
                "price" : itemdata.get("price", -99),
                "last" : itemdata.get("last", -99),
                "volume" : itemdata.get("volume", -99),
                "limit" : itemdata.get("limit", -99),
                "examine" : itemdata["examine"]
            }

            #add the new dictionary
            data_to_store[itemdata["name"]] = new_item

        #add timestamp
        data_to_store["updated"] = str(datetime.datetime.now())

        #write to file
        with open("ge_data.txt", "w") as f:
            json.dump(data_to_store, f, indent=4)

    except Exception as e:
        print(f"Unexpected error occured: {e}")