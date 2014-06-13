#/usr/bin/python

import platform
import socket
import dmidecode

def print_head(str_item):
    print '*' * 50
    print "%s Info" %str_item
    print '*' * 50



def header():
    print_head('Header')
    hostname = platform.node()
    system = platform.system()
    ipaddr = socket.gethostbyname(socket.gethostname())
    print "Hostname : %s" %hostname
    print "Operator System : %s" %system
    print "IP : %s" %ipaddr


BIOSdict = {}

def getBIOS():
    print_head('BIOS Info')
    for v in dmidecode.bios().values():
        if type(v) == dict and v['dmi_type'] == 0:
            BIOSdict["Name"] = str((v['data']['Vendor']))
            BIOSdict["BuildNumber"] = str((v['data']['Version']))
            BIOSdict["SoftwareElementID"] = str((v['data']['BIOS Revision']))
            print "BIOS Name: %s" % BIOSdict["Name"]
            print "BIOS BuildNumber: %s" % BIOSdict["BuildNumber"]
            print "BIOS SoftwareElementID: %s" % BIOSdict["SoftwareElementID"]




Systemdict = {}

def getSystem():
    print_head('System Info')
    for v in dmidecode.system().values():
        if type(v) == dict and v['dmi_type'] == 1:
            Systemdict["Manufacturer"] = str((v['data']['Manufacturer']))
            Systemdict["Product Name"] = str((v['data']['Product Name']))
            Systemdict["Serial Number"] = str((v['data']['Serial Number']))

            print "Server Manufacture: %s" % Systemdict["Manufacturer"] 
            print "Server Product Name: %s" % Systemdict["Product Name"] 
            print "Server Serial Number: %s" % Systemdict["Serial Number"] 



Processordict = {}

def getProcessor():
    print_head('Processor Info')
    for v in dmidecode.processor().values():
        if type(v) == dict and v['dmi_type'] == 4:
            Processordict["Manufacturer"] = str((v['data']['Manufacturer']['Vendor']))
            Processordict["Version"] = str((v['data']['Version']))
            Processordict["Family"] = str((v['data']['Family']))
            Processordict["Core Enabled"] = str((v['data']['Core Enabled']))

    print "Processor Manufacturer: %s" % Processordict["Manufacturer"]
    print "Processor Version: %s" % Processordict["Version"]
    print "Processor Family: %s" % Processordict["Family"]
    print "Processor Core Number: %s" % Processordict["Core Enabled"]


Memorydict = {}

def getMemory():
    print_head('Memory Info')
    for v in dmidecode.memory().values():
        if type(v) == dict and v['dmi_type'] == 17:
            Memorydict["Locator"] = str((v['data']['Locator']))
            Memorydict["Serial Number"] = str((v['data']['Serial Number']))
            Memorydict["Manufacturer"] = str((v['data']['Manufacturer']))
            Memorydict["Size"] = str((v['data']['Size']))


            print "Memory Locator: %s" % Memorydict["Locator"] 
            print "Memory Serial Number: %s" % Memorydict["Serial Number"] 
            print "Memory Manufacturer: %s" % Memorydict["Manufacturer"] 
            print "Memory Size: %s" % Memorydict["Size"] 

Connectordict = {}

def getConnector():
    print_head('Connector Info')
    for v in dmidecode.connector().values():
        if type(v) == dict and v['dmi_type'] == 8:
            Connectordict["Port Type"] = str((v['data']['Port Type']))

            print "Connector: %s" % Connectordict["Port Type"] 

header()

getBIOS()
getSystem()

getProcessor()
getMemory()
getConnector()





