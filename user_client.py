#! /usr/bin/python2

import os
import socket

os.system('setenforce 0')
os.system('iptables -F')

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",5347))

ip="192.168.0.29"
port=1110

os.system('dialog --menu "WELCOME TO jalCLOUD" 20 35 2 1 "USER MANAGEMENT" 2 "CLOUD SYSTEM" 2>/tmp/cl.txt')

f=open("/tmp/cl.txt")
ch=f.read()
f.close()

if int(ch)==1:
	import start.py
	
else:
	import services.py
	
