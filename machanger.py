import subprocess
import platform
import re

class MaChanger:
    
    def result(res):
        return res
    def linuxMac(interface, new_mac):
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])
    def macMac(interface, new_mac):
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])
    def winMac(interface, new_mac):
        try:
            subprocess.call(["netsh", "interface", "set", "interface", "name=", interface, "admin=disable"])
            subprocess.call(["netsh", "interface", "set", "interface", "name=", interface, "admin=enable"])
            current_mac = subprocess.check_output(["getmac", "/v", "/fo", "list"])
        
            if new_mac in str(current_mac):
                print(f"MAC address successfully changed to {new_mac}")
        except Exception as kek:
            print(kek,"kafjasdfa")

            
