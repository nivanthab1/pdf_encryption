#Below functions are related to the conversion of word documents to PDFs and subsequent encryption
#=================================================================================================

#Importing libraries
from docx2pdf import convert
from PyPDF2 import PdfReader, PdfWriter

#Creating function to read word documents into PDFs
#=================================================================================================
def read(file):
    data = convert(file)
    return data

#Creating function to apply encryption
#=================================================================================================
def pwd_protect(file):

    #Opening the input PDF file
    reader = PdfReader(file)

    #Creating a writer object
    writer = PdfWriter()

    #Adding all pages to the writer
    for page in reader.pages:
        writer.add_page(page)
    
    #Encrypting the PDF with desired password
    writer.encrypt("1234")

    #Writing the encrypted PDF to an output file
    with open(f"{file}","wb") as result_pdf:
        return writer.write(result_pdf)