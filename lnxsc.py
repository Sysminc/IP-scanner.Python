#!/bin/python3

import sys
import socket
from datetime import datetime

# Memasukan Ip target

if len(sys.argv) == 2:
    target = socket.gethostname(sys.argv[1])    #Translate menjadi ip
else:
    print("Argument tidak vaild")
    print("Syntax: python3 scnner.py <ip>")

#Menambahkan Bannaer
print("~" * 50)
print("Scanning target : " + target)
print("Time dimulai : " + str(datetime.now()))
print("~" * 50)

try:
    for port in range(1,100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))    #Menampilkan indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nMengakhir Program")
    sys.exit

except socket.gaierror:
    print("Hostname tidak di temukan")
    sys.close

except socket.error:
    print("Tidak menemukan server yang connect")
    sys.exit

