#!/usr/bin/env python

from docx import Document
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE

# This was added to try and get the text inside tables to format
# correctly by adding a paragraph immidiately before the table
# and then remove it.  It never quite worked correctly as it
# altered all tables in the resulting docx file.
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
  p for p in styles if p.type == WD_STYLE_TYPE.PARAGRAPH
]

table_styles = [
  t for t in styles if t.type == WD_STYLE_TYPE.TABLE
]

print('\nParapgrah Sytles:')
for style in paragraph_styles:
  print('Style Name: \t{}'.format(style.name))

print('\nTable Styles:')
for style in table_styles:
  print('Style Name: \t{}'.format(style.name))

j2var_open  =  '{{ '
j2var_close = ' }}'

#doc.add_paragraph('{{ test_name }} - {{ device }}', style='test_title')
#h_table = doc.add_table(2,3)

for i in range(1,4):
  doc.add_paragraph('Test {}'.format(i), style='test_header')
  doc.add_paragraph('Description', style='desc_header')
  doc.add_paragraph('This is test {} text.'.format(i), style='normal_text')

  doc.add_paragraph('Commands To Execute', style='desc_header')
  doc.add_paragraph('Cisco:', style='bold')
  doc.add_paragraph('[ios command here]', style='output')
  doc.add_paragraph('Juniper:', style='bold')
  doc.add_paragraph('[junos command here]', style='output')

  doc.add_paragraph('Test Output', style='desc_header')
  result = j2var_open + 'test{}_result'.format(i) + j2var_close + '\n'
  o_table = doc.add_table(1,1,style='test_output')
  o_table.cell(0,0).add_paragraph(result,style='output_sm')

  doc.add_paragraph('Test Comments', style='desc_header')
  comment = j2var_open + 'test{}_comment'.format(i) + j2var_close + '\n'
  c_table = doc.add_table(1,1,style='test_comment')
  c_table.cell(0,0).add_paragraph(comment,style='normal_text')

doc.save('report.docx')
