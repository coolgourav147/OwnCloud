#! /usr/bin/python2

import os
import socket

os.system('setenforce 0')
os.system('iptables -F')

ip="192.168.0.29"
port=7767
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",7789))

os.system('dialog --inputbox "ENTER USERNAME:" 20 35  2>/tmp/r_name.txt')

f1=open("/tmp/r_name.txt","r")
u1=f1.read()
f1.close()

s.sendto(u1,(ip,port))

os.system('dialog --insecure --passwordbox "ENTER PASSWORD:" 20 35 2>/tmp/r_pswd.txt')

f2=open("/tmp/r_pswd.txt","r")
p1=f2.read()
f2.close()

s.sendto(p1,(ip,port))

os.system('dialog --inputbox "ENTER EMAIL ID:"  20 35 2>/tmp/r_email.txt')

f3=open("/tmp/r_email.txt","r")
e1=f3.read()
f3.close()

s.sendto(e1,(ip,port))

while True:
	data=s.recvfrom(100)[0]
	if data=="REGISTRATION SUCCESSFUL":
		os.system('dialog --msgbox "REGISTRATION SUCCESSFUL" 5 50')
		
	else:
		os.system('dialog --msgbox "REGISTRATION UNSUCCESSFUL" 5 50')
s.close()

import services.service





