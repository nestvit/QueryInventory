# -*- coding: utf-8 -*-
__author__ = 'nestvit'

import re
import os, sys
import sqlite3
import pprint
import datetime

now = datetime.datetime.now()
CurrentData = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
CurrentTime = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

with open("out.txt") as f:
    data  = f.read()
#print(data)

con = sqlite3.connect('C:/Users/NestVit/PycharmProjects/QueryInventory_S5720/inventory.sqlite')
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
try:
    con.execute(text)
except sqlite3.IntegrityError as e:
    text = 'UPDATE nodes set HW_type = "' + str(Type) + '", SW_version = "' + str(SW_version) + '", \
    Status = "' + str(Status) + '", Data = "' + CurrentData + '", Time = "' + CurrentTime + '" \
    WHERE Hostname = "' + str(hostname) + '"'
    con.execute(text)
    #print("Error occured: ", e)

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


