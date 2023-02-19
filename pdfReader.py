import sys
from PyPDF2 import PdfReader



filename = input('Enter a filename: ') or 'sample01.pdf'
reader = PdfReader(filename)


print(len(reader.pages))

page = reader.pages[0]

text = page.extract_text()
print(text)