
"""
FILE: skeleton_parser.py
------------------
Author: 
Modified: 

Skeleton parser for CS360 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

def transformText(TEXTVALUE):
    return "\"" + TEXTVALUE.replace("\"","\"\"") + "\""

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file):
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items']['Item'] # creates a Python dictionary of Items for the supplied json file

        table_Item = ""
        table_User = ""
        table_Category = ""
        table_Bid = ""
        table_Sell = ""
        table_belong_to_Cat = ""
        for item in items:
            # """
            # TODO: traverse the items dictionary to extract information from the
            # given `json_file' and generate the necessary .dat files to generate
            # the SQL tables based on your relation design
            # """

            ItemID = item["_ItemID"] #INTEGER
            Name = transformText( item['Name'] )         #TEXT
            if item['Description'] == "":
                Description = "NULL"
            else:
                Description = transformText(item['Description']) #TEXT
            Started = "\"" + transformDttm(item['Started']) + "\""#dttm TEXT
            Ends = "\"" + transformDttm(item['Ends']) + "\""#dttm TEXT
            First_Bid = transformDollar(item['First_Bid']) #REAL
            Currently = transformDollar(item['Currently']) #REAL
            Number_of_Bids = item['Number_of_Bids'] #INTEGER
            if 'Buy_Price' in item:
                Buy_Price = transformDollar(item['Buy_Price']) #REAL
            else:
                Buy_Price = 'NULL'

            table_Item = (table_Item + ItemID + columnSeparator + Name + columnSeparator 
                + Description + columnSeparator + Started + columnSeparator + Ends +
                columnSeparator + First_Bid + columnSeparator+ Currently + columnSeparator
                + Number_of_Bids + columnSeparator + Buy_Price + "\n")

            Seller = item['Seller']
            UserID = transformText(Seller['_UserID']) # UserID TEXT PRIMARY KEY
            Rating = Seller['_Rating'] # Rating INTEGER
            Country = transformText(item['Country']) # Country TEXT
            Location = transformText(item['Location']) # Location TEXT

            table_User = (table_User + UserID + columnSeparator + Rating + columnSeparator
                + Country + columnSeparator + Location + "\n")

            table_Sell = (table_Sell + ItemID + columnSeparator + UserID + "\n")

            for cat in item["Category"]:
                CategoryName = transformText(cat)
                table_Category = (table_Category + CategoryName + "\n")  #CREATE TABLE Category CategoryName TEXT
                table_belong_to_Cat = (table_belong_to_Cat + ItemID + columnSeparator + CategoryName + "\n")


            # if 'Bids' in item:
            if Number_of_Bids != "0":
                # if 'bid' in item['Bids']:
                for bid in item['Bids']['Bid']:    
                    BTime = "\"" + transformDttm(bid['Time']) + "\"" # BTime TEXT,
                    Amount = transformDollar(bid['Amount']) #Amount REAL,

                    Bidder = bid['Bidder']
                    UserID = transformText(Bidder['_UserID']) # UserID TEXT PRIMARY KEY
                    Rating = Bidder['_Rating'] # Rating INTEGER

                    if 'Country' in Bidder:
                        Country = transformText(Bidder['Country']) # Country TEXT
                    else:
                        Country = "NULL"

                    if 'Location' in Bidder:
                        Location = transformText(Bidder['Location']) # Location TEXT
                    else:
                        Location = "NULL"
                        

                    table_User = (table_User + UserID + columnSeparator + Rating + columnSeparator
                        + Country + columnSeparator + Location + "\n")

                    table_Bid = (table_Bid + BTime + columnSeparator + ItemID + columnSeparator + UserID + columnSeparator
                        + Amount + "\n")

        f_Item = open( "Item.dat", "a" ) # "a")
        f_Item.write( table_Item )
        f_Item.close()

        f_User = open( "User.dat", "a" ) # "a")
        f_User.write( table_User )
        f_User.close()

        f_Category = open( "Category.dat", "a" ) # "a")
        f_Category.write( table_Category )
        f_Category.close()

        f_Bid = open( "Bid.dat", "a" ) # "a")
        f_Bid.write( table_Bid )
        f_Bid.close()

        f_Sell = open( "Sell.dat", "a" ) # "a")
        f_Sell.write( table_Sell )
        f_Sell.close()

        f_belong_to_Cat = open( "belong_to_Cat.dat", "a" ) # "a")
        f_belong_to_Cat.write( table_belong_to_Cat )
        f_belong_to_Cat.close()

    

"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        sys.stderr.write('Usage: python skeleton_json_parser.py <path to json files>\n')
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print("Success parsing " + f)

if __name__ == '__main__':
    main(sys.argv)
