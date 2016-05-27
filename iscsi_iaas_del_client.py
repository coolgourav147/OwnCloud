#! /usr/bin/python2

import os

os.system('iscsiadm --mode node --targetname skycloud --portal 192.168.0.29:3260 --logout')
os.system('rm -f /etc/libvirt/qemu/rhel6.xml')
os.system('umount /media/rjcloud')
os.system('rmdir /media/rjcloud')
