# Extract Text from a PDF

from PyPDF2 import PdfReader, PdfWriter


# reader = PdfReader('read.pdf')
# page = reader.pages[0]
# print(page.extract_text())

merger = PdfWriter()
pdfs = ['read.pdf', 'example.pdf']
for pdf in pdfs:
    merger.append(pdf)
    merger.write('merged.pdf')
    merger.close()