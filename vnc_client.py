#! /usr/bin/python2

import os
import socket

os.system("setenforce 0")
os.system("iptables -F")

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",1245))

ip="192.168.0.29"
port=7678

os.system('dialog --menu  "CHOOSE OPERATING SYSTEM"  20  35  3  1 "RedHat" 2 "FEDORA"  3 "CentOS" 2>/tmp/os.txt')

f1=open("/tmp/os.txt","r")
ps=f1.read()
f1.close()

s.sendto(ps,(ip,port))

os.system('dialog --inputbox "ENTER THE NAME OF YOUR OS"  20 35  2>/tmp/newf.txt')

f2=open("/tmp/newf.txt","r")
newf=f2.read()
f2.close()

s.sendto(newf,(ip,port))

os.system('dialog --inputbox "ENTER SYSTEM MEMORY (Mb)"  20 35  2>/tmp/sm.txt')

f3=open("/tmp/sm.txt","r")
sm=f3.read()
f3.close()

s.sendto(sm,(ip,port))

os.system('dialog --inputbox "ENTER HARDISK SIZE (Gb)"  20 35  2>/tmp/hd.txt')

f4=open("/tmp/hd.txt","r")
hd=f4.read()
f4.close()

s.sendto(hd,(ip,port))

os.system('dialog --inputbox "ENTER NUMBER OF VIRTUAL PROCCESSING UNITS"  20 35  2>/tmp/v.txt')

f5=open("/tmp/v.txt")
v=f5.read()
f5.close()

s.sendto(v,(ip,port))

s.close()

os.system("sleep 5")
os.system('vncviewer 192.168.0.29:5911')

import services.service
