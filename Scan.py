import sys
import socket
from datetime import datetime as dt

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Incorrect Usage")
    print("Syntax: python3 scan.py <IP>")
    sys.exit(0)

print("-"*50)
print("Scanning Target: "+target)
print("Scanning started at: "+str(dt.now()))
try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExiting the scanner")
    sys.exit()
except socket.gaierror:
    print("Hostname cannot be resolved")
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    sys.exit()

print("-"*50)
