#! /usr/bin/python2

import os
import socket

os.system("setenforce 0")
os.system("iptables -F")

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",7678))

ps=(s.recvfrom(100)[0])
print ps
osname=s.recvfrom(100)[0]
print osname
sm=(s.recvfrom(100)[0])
print sm
hd=s.recvfrom(100)[0]
print hd
v=(s.recvfrom(100)[0])
print v

if int(ps)==1:
	os.system("/usr/sbin/virt-install --vnc --vncport=5911 --vnclisten=0.0.0.0 --noautoconsole --name=" + osname + " --ram=" + sm + "  --arch=x86_64 --vcpus=" + v + " --os-type=linux --os-variant=rhel6 --hvm  --accelerate --disk=/tmp/" + osname + ",size=" + hd + " -m 52:54:00:00:00:22 --location=ftp://192.168.0.29/pub/Rhel --extra-args='ftp://192.168.0.29/pub/kick.cfg ip=192.168.0.29  netmask=255.255.255.0 gateway=192.168.1.1 dns=8.8.8.8 noipv6 --network bridge=jalbridge'")


import server.py

#if os==2:
#	os.system("virt-install --name="+ osname +" --ram="+ sm +" --arch=x86_64 --vcpus="+ vcpu +" --os-type=linux --os-variant=rhel6 --hvm  --accelerate --disk/img,size="+ hd +" -m location=ftp://192.168.137.9/dvd --extra-args='ftp:// ip=192.168.137.109 netmask=255.255.255.0 gateway=192.168.1.1 dns=8.8.8.8 noipv6' --network bridge=jalCLOUD")


#if os==3:
#	os.system("virt-install --name="+ osname +" --ram="+ sm +" --arch=x86_64 --vcpus="+ vcpu +" --os-type=linux --os-va/img,size="+ hd +" -m 52:54:00:00:00:22 --location=ftp://192.168.137.9/dvd --extra-args='ftp:// ip=192.168.137.109 netmask=255.255.255.0 gateway=192.168.1.1 dns=8.8.8.8 noipv6' --network bridge=jalCLOUD")


import server.svr

