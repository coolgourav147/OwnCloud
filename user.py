#!/usr/bin/python2

import socket
import os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",2233))

data=s.recvfrom(100)[0]

if data=="login":
	s.close()	
	import user_login_svr.py
	

elif data=="register":
	s.close()
	import r_user_svr.py
	
