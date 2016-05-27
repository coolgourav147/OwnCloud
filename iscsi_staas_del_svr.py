#! /usr/bin/python2

import os

os.system('tgtadm --lld iscsi --mode logicalunit --op delete --tid 1 --lun 1')
os.system('tgtadm --lld iscsi --mode target --op delete --tid 1')
os.system('rm -f /etc/tgt/targets.conf')
os.system('cp /etc/tgt/backup.conf  /etc/tgt/targets.conf ')
os.system('service tgtd restart')
