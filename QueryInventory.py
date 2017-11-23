# -*- coding: utf-8 -*-

from netmiko import ConnectHandler
from datetime import datetime
import paramiko
huawei_5720 = {}

try:
    pass
    name_module =6
except ():
    Print ( "Ошибка в модуле: "  + str(name_module))
finally:
    print("Модуль " + str(name_module) + " - OK")


huawei_5720 = {'device_type': 'huawei_ssh','ip': '172.26.30.78','username': 'iteco','password': 'iteco2010'}

net_connect = ConnectHandler(**huawei_5720)

output = net_connect.send_command("disp ip int brief")
print(output)
output = net_connect.send_command("disp device")
print(output)
net_connect.disconnect()


