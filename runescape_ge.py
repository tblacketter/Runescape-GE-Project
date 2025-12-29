#The main driver for the runescape program.
#Handles command line arguments and executes the desired command passed by the user 

import argparse
import datetime

time_of_execution = datetime.datetime.now()

parser = argparse.ArgumentParser()

parser.add_argument("-r", "--refresh", action="store_true", help="refreshes the data file")

group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("-s", "--search", metavar="NAME", help="search for an item by name, returns 3 items with the closest matching names")
group.add_argument("-q", "--query", metavar="ID", type=int, help="provide an item id number to retrieve infomartion about the item")


args = parser.parse_args()

if not (args.refresh or args.search or args.query):
    parser.error(
        "You must specify an option."
    )

#For initial testing
# if args.refresh:
#     print("The file was refreshed.")
# if args.search:
#     print(args.search)
# if args.query:
#     print(args.query)
