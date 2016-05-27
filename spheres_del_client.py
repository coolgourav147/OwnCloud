#! /usr/bin/python2

import os

os.system('iscsiadm --mode node --targetname mycloud --portal 192.168.0.29:3260 --logout')
os.system('rm -rvf /media/spheres')
