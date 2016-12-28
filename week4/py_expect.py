#!/usr/bin/env python

import sys
import re
import pexpect

# 

def main():
    addr = '9.88.0.6'
    usern = 'rwuser'
    passw = 'Password2'
    #
    conn = pexpect.spawn('ssh -l {} {}'.format(usern,addr))
    #conn.logfile = sys.stdout
    conn.timeout = 3
    #
    conn.expect('ssword:')
    conn.sendline(passw)
    conn.expect('>')
    print conn.before
    #
    conn.sendline("en")
    conn.sendline(passw)
    conn.expect('#')
    print conn.before
    #
    conn.sendline("term len 0")
    conn.sendline("sh ver")
    conn.expect('#')
    print conn.after
    print conn.before

    if(False):
        pattern = re.compile(r'^Conf$', re.MULTILINE)
        conn.sendline("show version")
        conn.expect(pattern)

if __name__=="__main__":
	main()



