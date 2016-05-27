#!/usr/bin/python2

import os
import socket
import crypt

os.system("setenforce 0")
os.system("iptables -F")

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",7767))
username=s.recvfrom(100)[0]
print username
password=s.recvfrom(100)[0]
print password
email=s.recvfrom(100)[0]
print email


passwd=crypt.crypt(password+"$$$")
os.system("echo  '"+ username +":x:502:502::/home/"+ username +":/bin/bash' >>/etc/passwd")
os.system("echo '"+ username +":"+ passwd +"16251:0:99999:7:::' >>/etc/shadow")
os.system("echo '"+ username +":x:502:' >>/etc/group")
os.system("echo '"+ username +":!::' >>/etc/gshadow")
os.system("mkdir /home/" + username + "")
os.system("chmod 777 /home/"+username+"")
os.system("touch /var/spool/mail/"+ username+"")
os.system("cp -rvf /etc/skel/.bashrc /home/"+ username +"")
os.system("cp -rvf /etc/skel/.bash_logout /home/"+ username +"")
os.system("cp -rvf /etc/skel/.bash_profile /home/"+ username +"")
os.system("cp -rvf /etc/skel/.gnome2 /home/"+ username +"")
os.system("cp -rvf /etc/skel/.mozilla /home/"+ username +"")

s.sendto("REGISTRATION SUCCESSFUL",("192.168.0.13",7789))

s.close()

import server.svr
