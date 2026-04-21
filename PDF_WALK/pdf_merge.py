from PyPDF2 import PdfWriter

merger = PdfWriter()

n = int(input('Enter how many pdfs you want to merge\n'))

pdfs = []

for i in range(n):
    name = input(f'Enter {i + 1} pdf name: ')
    pdfs.append(name)
    
# print(pdfs)

try:
    for pdf in pdfs:
        merger.append(pdf)

    merger.write('merged-pdf.pdf')
    merger.close()
except FileNotFoundError as e:
    print('File not found')
