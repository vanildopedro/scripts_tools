#!/bin/python3

import socket
import sys


if len(sys.argv) == 2:
    target =  socket.gethostbyname(sys.argv[1])

else:
        print ("Invalid ammount of argument.")
        print ("Syntax: port_scan.py <ip/hostname>")

try:
    for port in range(53,80):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port)) #1 - Close or 0 - Open

        if result == 0:
                print("Port {} is open".format(port))

        s.close()

except KeyboardInterrupt:
    print("\nProgram Cloded.")
    sys.exit()

except socket.gaierror:
    print("\nName or service not known")
    sys.exit()




