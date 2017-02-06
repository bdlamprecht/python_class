#!/usr/bin/env python3

from docxtpl import DocxTemplate

doc = DocxTemplate("test_env.docx")
output = { 'test_name' : 'Test Envrionment',
           'tester' : 'bl839s',
           'date' : 'TODAY',
           'test1_result' : 'show environment',
           'test1_comment': 'environment results',
           'test2_result' : 'version results',
           'test2_comment': 'envrionment results'}
#           'test3_result' : 'version results'
#           'test3_comment': 'inventory results',
#           'test4_result' : 'show environment',
#           'test4_comment': 'envrionment results',
#           'test5_result' : 'version results',
#           'test5_comment': 'envrionment results',
#           'test6_result' : 'show environment',
#           'test6_comment': 'envrionment results',
#           'test7_result' : 'version results',
#           'test7_comment': 'envrionment results',
#           'test8_result' : 'show environment',
#           'test8_comment': 'envrionment results',
#           'test9_result' : 'version results',
#           'test9_comment': 'envrionment results'}

doc.render(output)
doc.save('generated.docx')
