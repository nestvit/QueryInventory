# -*- coding: utf-8 -*-
__author__ = 'nestvit'

import re
import os, sys
import sqlite3
import pprint

with open("out.txt") as f:
    data  = f.read()

# print(data)

con = sqlite3.connect('C:/Users/NestVit/PycharmProjects/QueryInventory_S5720/inventory.sqlite')
cur = con.cursor()

search = '\<(NAK07\S*)>'
match = re.search(search,data)
print("Sysname: " + match.group(1))
hostname = match.group(1)

search = 'HUAWEI [^TECH](\S*)'
match = re.search(search,data)
print("Type: " + match.group(1))

search = 'S5720 (\w*)'
match = re.search(search,data)
print("Version: " + match.group(1))

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

for row in result:
    text = 'INSERT INTO "main"."inventory2" ("Hostname","BoardType","BarCode","Item","Description","Manufactured","VendorName")\
            VALUES ("' + hostname + '","' + str(row[0]) + '","' + str(row[1]) + '","' + str(row[2]) + \
           '","' + str(row[3])+ '","' + str(row[4]) + '","' + str(row[5]) + '")'
    # print(text)
    cur.execute(text)

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


