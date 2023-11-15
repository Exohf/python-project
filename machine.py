import platform
import os
# pip install psutil
import psutil
from os import listdir

def createAndWriteInFile(config):
    configFile = open('./config.txt', 'w+')
    configFile.writelines(config)

def formatNetInterface():
    if_addrs = psutil.net_if_addrs()
    toWrite = ["======== Ip Config ========\n"]

    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            toWrite.append(f"=== Interface: {interface_name} ===\n")
            if str(address.family) == 'AddressFamily.AF_INET':
                toWrite.append(f"  IP Address: {address.address}\n")
                toWrite.append(f"  Netmask: {address.netmask}\n")
                toWrite.append(f"  Broadcast IP: {address.broadcast}\n")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                toWrite.append(f"  MAC Address: {address.address}\n")
                toWrite.append(f"  Netmask: {address.netmask}\n")
                toWrite.append(f"  Broadcast MAC: {address.broadcast}\n")

    createAndWriteInFile(toWrite)

def readFileOfPath(path):
    f = open(path, "r")
    lines = f.readlines()
    for line in lines:
        print(line, end="")

def listFilesInFolder(path):
    print(listdir(path))

def runOnWindows():
    print("Running on Windows")

def runOnLinux():
    print("Running on Linux")
    formatNetInterface()


def main():
    operating_system = platform.system()

    if operating_system == "Windows":
        runOnWindows()
    elif operating_system == "Linux":
        runOnLinux()
        print("\n===================\n")
        formatNetInterface()
        listFilesInFolder('./')
        print("\n===================\n")
        readFileOfPath('./config.txt')
    else:
        print(f"Unsupported operating system: {operating_system}")

if __name__ == "__main__":
    main()