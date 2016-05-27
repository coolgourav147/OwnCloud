#! /usr/bin/python2

import os

os.system('yum install xrdp -y')
os.system('setenforce 0')
os.system('iptables -F')
os.system('service xrdp restart')
import server.svr

