#! /usr/bin/python2

import os

os.system("setenforce 0")
os.system("iptables -F")

os.system('gnome-terminal --command="ssh 192.168.0.29"')

os.system("sleep 2")
import services.service
