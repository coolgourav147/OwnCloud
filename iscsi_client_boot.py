#! /usr/bin/python2

import os

os.system('setenforce 0')
os.system('iptables -F')
os.system('yum install iscsi-initiator-utils')
os.system('sleep 5')
os.system('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.0.29 --discover')
os.system('iscsiadm --mode node --targetname skycloud --portal 192.168.0.29:3260 --login')
os.system('mkdir /media/rjCLOUD')
os.system('sleep 10')
os.system('mount /dev/sdb  /media/rjCLOUD')
os.system("sed -i '31s00/media/rjCLOUD/|' /etc/libvirt/qemu/rhel6.xml")
os.system('service libvirtd restart')

os.system('sleep 2')
import services.service





