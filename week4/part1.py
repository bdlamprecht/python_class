#!/usr/bin/env python

import paramiko
from getpass import getpass

addr  = '9.88.0.6'
usern = 'rwuser'
#passw = getpass()
passw = 'Password2'

mydev_pre = paramiko.SSHClient()
mydev_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
mydev_pre.connect(addr, username=usern, password=passw, look_for_keys=False, allow_agent=False)
mydev = mydev_pre.invoke_shell()
mydev.send("\n")
print mydev.recv(5000)
mydev.send("show version | i uptime\n")
outp = mydev.recv(5000)
print outp
