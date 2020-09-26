#!usr/bin/env/python
#installation file
import os
import time

os.system("clear")
time.sleep(2)
print("INSTALLING SOME DEPENDENCIES IT MAY TAKE SOME TIME")
print("Please Wait")
time.sleep(2)
os.system("clear")
time.sleep(2)
os.system("sudo apt-get update")
time.sleep(2)
print("INSTALLING PYTHON3")
os.system("sudo apt-get install python3")
time.sleep(2)
print("INSTALLING PIP")
os.system("sudo apt-get install python3-pip")
time.sleep(2)
print("INSTALLING PIP MODULES")
time.sleep(2)
os.system("pip3 install scapy")
time.sleep(2)
print("INSTALLATION COMPLETED YOU CAN NOW RUN networkscan.py")
exit()