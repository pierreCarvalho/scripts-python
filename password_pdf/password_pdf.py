from PyPDF2 import PdfFileReader, PdfFileWriter

def secure_pdf(_file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(_file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)
    with open(f"encrypted_{_file}","wb") as f:
        parser.write(f)
        f.close()
    print(f"encrypted_{_file} created..")

if __name__ == "__main__" :
    _file = "pdf_file_name.pdf"
    password = "thisispassword"
    secure_pdf(_file,password)