
import re

with open("out.txt") as f:
    data  = f.read()

print(data)

search = '\<NAK07\S*>'
match = re.search(search,data)
print("Sysname: " + match.group())

search = 'HUAWEI [^TECH](\S*)'
match = re.search(search,data)
print("Type: " + match.group(1))

search = 'S5720 (\w*)'
match = re.search(search,data)
print("Version: " + match.group(1))

search = 'BoardType=(\S*)'
match = re.findall(search,data)
print(match)

search = 'BarCode=(\S*)'
match = re.findall(search,data)
print(match)

search = 'Item=(\S*)'
match = re.findall(search,data)
print(match)

search = 'Manufactured=(\S*)'
match = re.findall(search,data)
print(match)

search = 'VendorName=(\S*)'
match = re.findall(search,data)
print(match)
