#! /usr/bin/python2

import socket
import os

os.system('setenforce 0')
os.system('iptables -F')

def service():

	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind(("",4657))

	ip="192.168.0.29"
	port=8793

	os.system('dialog --menu "SELECT SERVICES" 20  35  3  1 "StaaS"  2 "SaaS" 3 "IaaS" 2>/tmp/service.txt')

	f1=open("/tmp/service.txt",'r')
	ch=f1.read()
	f1.close()

	if int(ch)==1:
		os.system('dialog --menu "SELECT TYPE OF STORAGE" 20 35 2 1 "CUBES"  2 "SPHERES"  2>/tmp/staas.txt')

		f2=open("/tmp/staas.txt")
		ch1=f2.read()
		f2.close()

		if int(ch1)==1:
			s.sendto("cubes",(ip,port))
			os.system("sleep 2")		
			import cubes_client
		
		elif int(ch1)==2:
			s.sendto("spheres",(ip,port))		
			os.system("sleep 2")
			import spheres_client		

	elif int(ch)==2:
		os.system('dialog --menu "SELECT RPM" 20 35 2 1 "FIREFOX" 2 "VLC" 3 "MEDIA PLAYER"  2>/tmp/saas.txt')

		f3=open("/tmp/saas.txt")
		ch2=f3.read()
		f3.close()

		if int(ch2)==1:
			import saas_firefox

		elif int(ch2)==2:
			import saas_vlc

		elif int(ch2)==3:
			import saas_media_play
		
	
	elif int(ch)==3:
		os.system('dialog --menu "SELECT BOOT TYPE" 20 35 2 1 "CLOUD BOOT" 2 "CLIENT BOOT" 2>/tmp/boot.txt')

		f4=open("/tmp/boot.txt")
		ch3=f4.read()
		f4.close()
	
		if int(ch3)==1:
			os.system('dialog --menu "SELECT PROTOCOL" 20 35 3 1 "SSH" 2 "RDP" 3 "VNC" 2>/tmp/proto.txt')
		
			f8=open("/tmp/proto.txt")
			ch31=f8.read()
			f8.close()

			if int(ch31)==1:
				import ssh_client

			elif int(ch31)==2:
				s.sendto("rdp",(ip,port))
				os.system("sleep 5")
				import rdp_client

			elif int(ch31)==3:
				s.sendto("vnc",(ip,port))
				os.system("sleep 2")
				import vnc_client

		if int(ch3)==2:
			os.system('dialog --menu "SELECT PROTOCOL" 20 35 3 1 "NFS BOOT" 2 "ISCSI BOOT" 2>/tmp/clboot.txt')
		
			f9=open("/tmp/clboot.txt")
			ch32=f9.read()
			f9.close()

			if int(ch32)==1:
				s.sendto("nfs",(ip,port))
				os.system("sleep 2")
				import nfs_iaas_client

			elif int(ch32)==2:
				s.sendto("iscsi",(ip,port))
				os.system("sleep 2")
				import iscsi_client_boot

	s.close()
	

service()
