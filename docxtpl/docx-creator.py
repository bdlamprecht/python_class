#!/usr/bin/env python

import os
import pwd
import time
import argparse

from docxtpl import DocxTemplate

doc = DocxTemplate("test_env.tpl.docx")
output = { 'test_name' : 'Test Envrionment',
           'tester' : "{} ({})".format(pwd.getpwuid(os.getuid())[4],
                                     pwd.getpwuid(os.getuid())[0]),
           'date' : time.strftime("%d%b%Y"),}
x = 0
y = 9
#print("x is {}, and y is {}".format(x,y))

for i in range(x,y):
    output['test{}_result'.format(i+1)]='result {}'.format(i+1)
    output['test{}_comment'.format(i+1)]='comment {}'.format(i+1)
#    print("test{}_result".format(i+1))
#    print("test{}_comment".format(i+1))

doc.render(output)
doc.save('test_env.docx')
