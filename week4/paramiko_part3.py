#!/usr/bin/env python

import paramiko
import sys
from time import sleep
#from getpass import getpass

addr  = '9.88.0.6'
usern = 'rwuser'
#passw = getpass()
passw = 'Password2'

mydev_pre = paramiko.SSHClient()
mydev_pre.load_system_host_keys()
#mydev_pre.load_host_keys("/home/bl839s/.ssh/known_hosts")
#mydev_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
mydev_pre.connect(addr, username=usern, password=passw, look_for_keys=False, allow_agent=False)

# Used for individual commands:
#stdin, stdout, sterr = mydev_pre.exec_command('show version | i uptime')
#print stdout.print()

mydev = mydev_pre.invoke_shell()
mydev.send("\n")
print mydev.recv(5000)
mydev.send("show version | i uptime\n")
outp = mydev.recv(5000)
print outp

# Used for setting timeouts on the recv command:
mydev.settimeout(6)
mydev.gettimeout()

# Useful for checking if new data is available:
if mydev.recv_ready():
	outp = mydev.recv(5000)

mydev.send("en\n" + passw + "\n")
mydev.send("term len 0\n")
outp = mydev.recv(1000)

# Example for using loop for big output:

mydev.send("term len 0\n")
mydev.send("sh run\n")
outp = ""

while mydev.recv_ready():
	#print mydev.recv_ready()
	outp += mydev.recv(1000)
	sleep(0.01)

print outp
print "The End"

