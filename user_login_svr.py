#! /usr/bin/python2

import os
import socket

os.system("setenforce 0")
os.system("iptables -F")

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",1001))
	
username=s.recvfrom(100)[0]
print username
password=s.recvfrom(100)[0]
print password
email=s.recvfrom(100)[0]
print email

ip="192.168.0.13"
port=1000

if username=="ravi":
	if password=="redhat":
		if email=="ravi@gmail.com":
			s.sendto("success",(ip,port))


#elif username=="jalsut":
#	if password=="12345":
#		if email=="jal@gmail.com":
#			s.sendto("Success",(ip,port)



s.close()

import server.svr


