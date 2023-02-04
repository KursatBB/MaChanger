import os
import platform
import pyfiglet
import argparse
from machanger import MaChanger

parser = argparse.ArgumentParser(description='KeK maChanger')
parser.add_argument("--i", help="Enter the interface whose MAC address you want to change.")
parser.add_argument("--m", help="Enter the desired new MAC address.")
args = parser.parse_args()

if __name__ == '__main__':
    ascii_banner= pyfiglet.figlet_format("KeK MaChanger")
    print(ascii_banner)
    
    os = platform.system()
    
    if  os=="Linux":
        MaChanger.linuxMac(args.i,args.m)
    elif  os=="Darwin":
        MaChanger.macMac(args.i,args.m)
    elif  os=="Windows":
        MaChanger.windowsMac(args.i, args.m)
