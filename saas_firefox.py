#! /usr/bin/python

import os

os.system("yum install openssh* -y")
os.system("cp /root/Desktop/client/mozilla-firefox.desktop  /root/Desktop")
os.system('gnome-terminal --command="ssh -X -l root 192.168.0.29 firefox"')

import services.service


	

