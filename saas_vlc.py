#! /usr/bin/python

import os

os.system("yum install openssh-server -y")
os.system('ssh -X -l rohit1 192.168.0.29 vlc')

import services.service

