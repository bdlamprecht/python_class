#!/usr/bin/env python

from netmiko import ConnectHandler

username = 'rwuser'
password = 'Password2'

dev1 = {
    'device_type': 'cisco_wlc',
    'ip': 'sms-wlc-a',
    'username': username,
    'password': password
}


wlc = ConnectHandler(**dev1)

# WLC Examples #

print wlc.find_prompt()
print wlc.check_config_mode()

print "Results of command 'show system route' \n"
print wlc.send_command('show system route')

wlc.disconnect()
