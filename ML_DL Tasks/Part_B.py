# QUESTION No 2 (part(b): Extract table Information.

import pdfplumber
import pandas as pd
import numpy as np
from PyPDF2 import PdfFileReader

path = "Sample_Test.pdf"

file = open(path, 'rb') # Open the pdf file an read mode
pdf = PdfFileReader(file)

information = pdf.getDocumentInfo()

# print('\n', information, '\n') # Whole pdf info

# Extract creation date of pdf file
print("\n\n &&&&&&&& Table Inforimation &&&&&&&&&& \n\n")
print(" Creation date of PDF: ", information.creation_date)
# Extract creater of the pdf
print(" Creator of the PDF: ", information.creator)
print(" Producer Information of the PDF: ", information.producer)
print(" Title of the PDF: ", information.title)

PDF_Pages = pdf.getNumPages()
print(" Number of Pages in file: ", PDF_Pages, "\n\n")

# Tables rows, and columns 
with pdfplumber.open(r'Sample_Test.pdf') as pdf:
    page = pdf.pages[0]    
    table = page.extract_table(table_settings={})
    df = pd.DataFrame(table, columns=table[0]).T

print(df, "Number of rows and columns of the pdf")

file.close() # Close the file