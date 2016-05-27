#! /usr/bin/python2

import os

os.system('setenforce 0')
os.system('iptables -F')
os.system('scp /etc/libvirt/qemu/rhel6.xml  192.168.0.13:/etc/libvirt/qemu')

import server.svr

