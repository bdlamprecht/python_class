#!/usr/bin/env python

from docx import Document
from docx.enum.style import WD_STYLE_TYPE

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

for style in paragraph_styles:
  print("Style Name: \t{}".format(style.name))

title = doc.add_paragraph('{{ test_name }} - {{ device }}', style='test_title')
print(title)
doc.save('styles.docx')