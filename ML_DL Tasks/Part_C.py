# Question2 (c) Extract text data in Key Value Pair, like KeyA : Value of KeyA --- (Sorry For That)

from PyPDF2 import PdfReader
from tabula import read_pdf

reader = PdfReader("Sample_Test.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(number_of_pages) # Print thw number of pages in the pdf file
print(page)

# Output should be like this. in Google Colab
"""
1
{'/Contents': [IndirectObject(15, 0, 140656914947152), IndirectObject(16, 0, 140656914947152), 
               IndirectObject(17, 0, 140656914947152), IndirectObject(18, 0, 140656914947152), 
               IndirectObject(19, 0, 140656914947152), IndirectObject(20, 0, 140656914947152), 
               IndirectObject(21, 0, 140656914947152), IndirectObject(22, 0, 140656914947152)], 
               '/CropBox': [0, 0, 612, 792], '/MediaBox': [0, 0, 612, 792], 
               '/Parent': IndirectObject(9, 0, 140656914947152), '/Resources': {'/ExtGState': {'/GS0': 
               IndirectObject(38, 0, 140656914947152)}, '/Font': {'/C2_0': IndirectObject(43, 0, 140656914947152), 
               '/C2_1': IndirectObject(45, 0, 140656914947152), '/C2_2': IndirectObject(47, 0, 140656914947152), 
               '/C2_3': IndirectObject(49, 0, 140656914947152), '/C2_4': IndirectObject(51, 0, 140656914947152), '/C2_5': 
               IndirectObject(53, 0, 140656914947152), '/TT0': IndirectObject(56, 0, 140656914947152), 
               '/TT1': IndirectObject(59, 0, 140656914947152)}, '/ProcSet': ['/PDF', '/Text', '/ImageB'], 
               '/XObject': {'/Fm0': IndirectObject(33, 0, 140656914947152), '/Im0': IndirectObject(34, 0, 140656914947152)}}, 
               '/Rotate': 0, '/Type': '/Page'} """


# print the whole table in the pdf file
# table_pdf = read_pdf('Sample_Test.pdf', guess=False, pages=1, stream=True)
# print(table_pdf) 