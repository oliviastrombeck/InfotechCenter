#Libraries HERE
import sys
import time

print("Welcome Branch - Developer: Olivia Strombeck")

print ("\n\tWelcome to InfoTechCenter V1.0")

x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("Infotech Center System Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + message)
    time.sleep(1)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\nOperating System Booted Up - Retina Scanned - Access Granted")