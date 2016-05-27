#! /usr/bin/python2

import os

os.system('setenforce 0')
os.system('iptables -F')
os.system('mkdir /media/mycloud')
os.system('sleep 10')
os.system('showmount -e 192.168.0.29')
os.system('mount 192.168.0.29:/var/lib/libvirt/images/  /media/mycloud')
os.system("sed -i '31s|/media/ravish/|/media/mycloud/|' /etc/libvirt/qemu/rhel6.xml")
os.system('service nfs stop')
os.system('service nfs start')
os.system('service nfs restart')
os.system('chkconfig nfs on') 
os.system('service libvirtd stop')
os.system('service libvirtd start')
os.system('service libvirtd restart')

os.system("sleep 2")
import services.service
