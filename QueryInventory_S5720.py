# -*- coding: utf-8 -*-

from netmiko import ConnectHandler
from datetime import datetime
import paramiko
import logging
import re
import pprint

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
huawei_5720 = {}

with open('out.txt', 'r') as f:
    for line in f:
        print(line)
        IPaddres = " + line.rstrip() + "

try:
    huawei_5720 = {'device_type': 'huawei_ssh', 'ip': IPaddres, 'username': 'iteco', 'password': 'Iteco@2010'}
    net_connect = ConnectHandler(**huawei_5720)
    output = net_connect.send_config_from_file('display_commands.txt')
    print(output)
    net_connect.disconnect()
    name_module = "Netmiko"
except ():
    Print ( "Ошибка в модуле: "  + str(name_module))
finally:
    print("Модуль " + str(name_module) + " - OK")

