# Question2 (a) Upload a document and extract some text from the pdf. (try for Both Handwritten and Printed) (Required)

from PyPDF2 import PdfFileReader

path = "Sample_Test.pdf"

file = open(path, 'rb') #Open the pdf file an read mode
pdf = PdfFileReader(file)

 #extract data from pdf
text=''
for i in range(0,pdf.numPages):
    # creating a page object
    page_no = pdf.getPage(i)
    # extracting text from page
    text=text+page_no.extractText()
print(text)

file.close() # Close the file
