# import os
from PyPDF2 import PdfFileMerger

# arr = os.listdir('./files')

pdfs = ['./files/1.pdf', './files/2.pdf']
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("./files/result.pdf")
merger.close()
