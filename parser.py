# -*- coding: utf-8 -*-
'''
The program reads a log file with serial numbers of equipment and puts them
to the table inventory2 in the database SQLite
The program reads a hostname, type, software version, status of equipment and puts them
to the table nodes in the database SQLite
'''

__author__ = 'Vitaly Nesterov'
__author_email__ = "nestvitaly@gmail.com"

import re
import os, sys
import sqlite3
import pprint
import datetime

# Entry point for program
if __name__ == '__main__':
    # Retrieve command line input
    try:
        log_file = str(sys.argv[1])
        database = str(sys.argv[2])
        print(log_file)
        print(database)
    except (IndexError, ValueError) as e:
        # Indicates no command line parameter was provided
        print("You must provide a log file and a database as a parameters to this script")
        print("Example: ")
        print("  python parser.py out.txt inventory.sqlite")
        #Delete for prod
        log_file = "out.txt"
        database = "inventory.sqlite"

        # Delete # for prod
        #sys.exit(1)

now = datetime.datetime.now()
CurrentData = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
CurrentTime = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

with open(log_file) as f:
    data  = f.read()
#print(data)

con = sqlite3.connect(database)
cur = con.cursor()

search = '\<(NAK07\S*)>'
match = re.search(search,data)
print("Sysname: " + match.group(1))
hostname = match.group(1)

search = 'HUAWEI [^TECH](\S*)'
Type = re.search(search,data)
print("Type: " + Type.group(1))
Type = Type.group(1)

search = 'S5720 (\w*)'
SW_version = re.search(search,data)
print("Version: " + SW_version.group(1))
SW_version = SW_version.group(1)

regex = ('BoardType=(\S*)\n'
        'BarCode=(\S*)\n'
         'Item=(\S*)\n'
         'Description=(.*)\n'
         'Manufactured=(\S*)\n'
        'VendorName=(\S*)')

result = re.findall(regex,data)
# print(result)

# for row in result:
#     print (row)
#     for item in row:
#         print (item)

Segment = "KKS"
Status = "Normal"

for row in result:
    text = 'INSERT INTO "main"."inventory2" ("Hostname","BoardType","BarCode","Item","Description","Manufactured","VendorName")\
            VALUES ("' + hostname + '","' + str(row[0]) + '","' + str(row[1]) + '","' + str(row[2]) + \
           '","' + str(row[3])+ '","' + str(row[4]) + '","' + str(row[5]) + '")'
    # print(text)
    cur.execute(text)

text = 'INSERT INTO "main"."Nodes" ("segment","Hostname","HW_type","SW_version","Status","Data","Time")\
            VALUES ("' + str(Segment) + '","' + str(hostname)  + '","' + str(Type) + '","' + str(SW_version) + \
           '","' + str(Status) + '","' + CurrentData + '","' + CurrentTime + '")'

print()
print("#" * 50)

try:
    con.execute(text)
    print('Hostname "' + str(hostname) + '" is new')
    print('Hostname was added')
except sqlite3.IntegrityError as e:
    text = 'UPDATE nodes set HW_type = "' + str(Type) + '", SW_version = "' + str(SW_version) + '", \
    Status = "' + str(Status) + '", Data = "' + CurrentData + '", Time = "' + CurrentTime + '" \
    WHERE Hostname = "' + str(hostname) + '"'
    con.execute(text)
    print('Hostname "' + str(hostname) + '" is exist' )
    print('Update was made')
finally:
    print ("OK")
print("#" * 50)

con.commit()



















#search = 'BoardType=(\S*)'
#match = re.findall(search,data)
#print(match)

# search = 'BarCode=(\S*)'
# match = re.findall(search,data)
# print(match)
#
# search = 'Item=(\S*)'
# match = re.findall(search,data)
# print(match)
#
# search = 'Description=(.*)'
# match = re.findall(search,data)
# print(match)
#
#
#
# search = 'Manufactured=(\S*)'
# match = re.findall(search,data)
# print(match)
#
# search = 'VendorName=(\S*)'
# match = re.findall(search,data)
# print(match)


