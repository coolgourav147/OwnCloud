#! /usr/bin/python2

import os
import socket

os.system('setenforce 0')
os.system('iptables -F')

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",1885))

ip="192.168.0.29"
port=9888

os.system('dialog --inputbox "ENTER NAME OF SPHERE"  20 35 2>/tmp/name_spheres.txt')

f21=open("/tmp/name_spheres.txt")
sp_name=f21.read()
f21.close()

s.sendto(sp_name,(ip,port))

os.system('dialog --inputbox "ENTER SIZE OF SPHERE (Mb)"  20 35 2>/tmp/size_sp.txt')

f22=open("/tmp/size_sp.txt","r")
f22.close()

s.sendto(sp_size,(ip,port))


os.system('yum install iscsi�)
os.system('service iscsid restart')

os.system('sleep 15')
os.system('iscsiadm --mode discoverdb --type sendtargets --portal 192.168.0.29 --discover')

os.system("sleep 5")

s.close()

import service.service





