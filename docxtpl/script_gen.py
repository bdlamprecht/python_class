#!/usr/bin/env python

import time
import os
import pwd
from getpass import getuser
from docxtpl import DocxTemplate

doc = DocxTemplate("test_env.tpl.docx")
output = { 'test_name' : 'Test Envrionment',
           'tester' : "{} ({})".format(pwd.getpwuid(os.getuid())[4],
                                     pwd.getpwuid(os.getuid())[0]),
           'date' : time.strftime("%d%b%Y"),}
x = 0
y = 9
print("x is {}, and y is {}".format(x,y))

for i in range(x,y):
    output['test{}_result'.format(i+1)]='result {}'.format(i+1)
    output['test{}_comment'.format(i+1)]='comment {}'.format(i+1)
    print("test{}_result".format(i+1))
    print("test{}_comment".format(i+1))

#           'test1_result' : 'show inventory',
#           'test1_comment': 'inventory results',
#           'test2_result' : 'show envrionment',
#           'test2_comment': 'envrionment results',
#           'test3_result' : 'show version',
#           'test3_comment': 'version results',
#           'test4_result' : 'show lldp neighbors',
#           'test4_comment': 'lldp results',
#           'test5_result' : 'show run',
#           'test5_comment': 'run results',
#           'test6_result' : 'show clock',
#           'test6_comment': 'clock results',
#           'test7_result' : 'show users',
#           'test7_comment': 'user results',
#           'test8_result' : 'show boot',
#           'test8_comment': 'boot results',
#           'test9_result' : 'show interface status',
#           'test9_comment': 'interface results'}

doc.render(output)
doc.save('generated.docx')
