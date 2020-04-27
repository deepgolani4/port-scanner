#!/bin/python3

import sys
import socket 
from datetime import datetime 

if len(sys.argv) == 2:
	target=socket.gethostbyname(sys.argv[1])
else:
	print("invalid amount of argument")
	print("syntax: pyhton3 scanner.py <ip>")
	sys.exit()

print("scanning target"+target)
print("time started: "+ str(datetime.now()))

try:
	for port in range(50,100):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target,port))
		print("checking port {}".format(port))
		if result==0:
			print("port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("sorry in hurry")
	sys.exit()

except socket.gaierror:
	print("hostname could be not resovled")
	sys.exit()

except socket.error:
	print("couldn't cpnnect server")
	sys.exit()
