#The main driver for the runescape program.
#Handles command line arguments and executes the desired command passed by the user 

import argparse
import datetime
import data_request as dr
import search as s
import refresh as r
import sys


parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)

parser.add_argument("-r", "--refresh", action="store_true", help="refreshes the data file")

group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("-s", "--search", metavar="NAME", help="search for an item by name with input surrounded by quotes \"Name of item\"")
group.add_argument("-q", "--query", metavar="ID", type=int, help="provide an item id number to retrieve information about the item")

try:
    args = parser.parse_args()
except:
    parser.print_help()
    print("test")
    sys.exit(1)

if not (args.refresh or args.search or args.query):
    parser.error(
        "You must specify an option."
    )


#For initial testing
if args.refresh:
    dr.refresh()
    print("The file was refreshed.")
if args.search:
     r.check_if_need_refresh()
     s.search(args.search)
# if args.query:
#     print(args.query)
