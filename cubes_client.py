#! /usr/bin/python2

import os
import socket

os.system("setenforce 0")
os.system("iptables -F")

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",1138))

ip="192.168.0.29"
port=9879

os.system('dialog --inputbox "ENTER NAME OF CUBE"  20 35 2>/tmp/name_cubes.txt')

f21=open("/tmp/name_cubes.txt")
cb_name=f21.read()
f21.close()

s.sendto(cb_name,(ip,port))

os.system('dialog --inputbox "ENTER SIZE OF CUBE (Mb)"  20 35 2>/tmp/size_cubes.txt')

f22=open("/tmp/size_cubes.txt","r")
cb_size=f22.read()
f22.close()

s.sendto(cb_size,(ip,port))

os.system("mkdir /media/"+ cb_name +"")
os.system("chmod 777 /media/"+ cb_name +"")
os.system("sleep 10")
os.system("mount 192.168.0.29/media/  /media/ +"")
os.system("sleep 10")
os.system('dialog --msgbox "CUBE CREATED"  20  35')

s.close()

import services.service




