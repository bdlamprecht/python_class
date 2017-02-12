#!/usr/bin/env python

import os,pwd,time
from docxtpl import DocxTemplate

def main(args):

  doc = DocxTemplate(args.input)
  output = {
    'test_name' : args.name,
    'device' :  'localhost',
    'tester' : "{} ({})".format(pwd.getpwuid(os.getuid())[4],
                                pwd.getpwuid(os.getuid())[0]),
    'date' : time.strftime("%d%b%Y"),}

  for i in range(0,3):
    frmt6 = '6_results'
    output['test{}_result'.format(i+1)]=R('Test {} result\nLine2'.format(i+1))
    output['test{}_comment'.format(i+1)]='Test {} comment'.format(i+1)

  doc.render(output)
  doc.save(args.output)

if __name__ == '__main__':
  from argparse import ArgumentParser
  p = ArgumentParser("Generate a docx file using a docxtpl formatted jinja2 template")
  p.add_argument('--input',  help='An input template file with embedded Jinja2 variables.', default='input.tpl.docx')
  p.add_argument('--output', help='The generated docx ouput file.', default='output.docx')
  p.add_argument('--name',   help='The name of the generatored test script', default='Test')
  args = p.parse_args()

  main(args)
