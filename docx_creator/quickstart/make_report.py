#!/usr/bin/env python

from docx import Document
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE

def delete_paragraph(paragraph):
  p = paragraph._element
  p.getparent().remove(p)
  p._p = p.element = None

doc = Document('input.docx')

styles = doc.styles

# Remove "latent" styles
#styles['Normal'].delete()
#styles['Heading 1'].delete()
#styles['Heading 2'].delete()
#styles['Heading 3'].delete()
#styles['HTML Preformatted'].delete()

paragraph_styles = [
  s for s in styles if s.type == WD_STYLE_TYPE.PARAGRAPH
]

table_styles = [
  s for s in styles if s.type == WD_STYLE_TYPE.TABLE
]

print('\nParapgrah Sytles:')
for style in paragraph_styles:
  print('Style Name: \t{}'.format(style.name))

print('\nTable Styles:')
for style in table_styles:
  print('Style Name: \t{}'.format(style.name))

j2var_open  =  '{{ '
j2var_close = ' }}'

for i in range(1,3):
  doc.add_paragraph('Test {}'.format(i), style='test_header')
  doc.add_paragraph('Description', style='desc_header')
  doc.add_paragraph('This is test {} text.'.format(i), style='normal_text')

  doc.add_paragraph('Commands To Execute', style='desc_header')
  doc.add_paragraph('Cisco:', style='bold')
  doc.add_paragraph('[ios command here]', style='output')
  doc.add_paragraph('Juniper:', style='bold')
  doc.add_paragraph('[junos command here]', style='output')

  doc.add_paragraph('Test Output', style='desc_header')
  result = j2var_open + 'test{}_result'.format(i) + j2var_close
  o_table = doc.add_table(1,1,style='test_output')
  o_table.cell(0,0).add_paragraph(result,style='output_sm')

  doc.add_paragraph('Test Comments', style='desc_header')
  comment = j2var_open + 'test{}_comment'.format(i) + j2var_close
  c_table = doc.add_table(1,1,style='test_comment')
  c_table.cell(0,0).add_paragraph(comment,style='normal_text')

doc.save('report.docx')
