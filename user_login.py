#! /usr/bin/python2

import os
import socket

os.system('setenforce 0')
os.system('iptables -F')

os.system('dialog --inputbox "ENTER USERNAME:" 20 35 2>/tmp/user.txt')
os.system('dialog --insecure --passwordbox "ENTER PASSWORD:"  20 35 2>/tmp/pswd.txt')
os.system('dialog --inputbox "ENTER EMAIL ID:"  20 35 2>/tmp/email.txt')

f1=open("/tmp/user.txt","r")
u1=f1.read()
f1.close

f2=open("/tmp/pswd.txt","r")
p1=f2.read()
f2.close()

f3=open("/tmp/email.txt","r")
e1=f3.read()
f3.close()

ip="192.168.0.29"
port=1001
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",1000))
s.sendto(u1,(ip,port))
s.sendto(p1,(ip,port))
s.sendto(e1,(ip,port))

s.recvfrom(100)[0]

os.system("sleep 2")

if data=="success":
	import services.service

s.close()
