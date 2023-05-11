import glob

from PyPDF2 import PdfFileReader, PdfFileWriter
#split range
import pdfplumber
start_page = []
End_page = []
def split_one():
    pdf_document1 = "230239896467.pdf"
    file_name = pdf_document1.split(".")
    pdf = pdfplumber.open(pdf_document1)
    n = len(pdf.pages)
    a120 = []
    for page in range(n):
        f = pdf.pages[page].extract_text()
        f1 = f.find("-60")
        if f1 != -1:
            start_page.append(page)
        f2 = f.find("-64")
        if f2 != -1:
            End_page.append(page)
    pdf_document = pdf_document1
    file_name = pdf_document.split(".")
    pdf = PdfFileReader(pdf_document)
    pgi=start_page[0] #start
    pgf=End_page[0]
    pdf_writer = PdfFileWriter()
    for page in range(pgi-1,pgf):
        current_page = pdf.getPage(page)
        pdf_writer.addPage(current_page)
    with open(f'E:/Desktop all/Desktop 09-2020/تقرير عمل/مناقصات اعتماد/10-5-2023/BOQ/'+str(file_name[0])+'_BOQ.pdf', "wb") as out:
        pdf_writer.write(out)
#split_one()
folder_name = glob.glob('E:/Desktop all/Desktop 09-2020/تقرير عمل/مناقصات اعتماد/11-5-2023/*.pdf')
for file in folder_name:
    print(file)
    def split_much():
        pdf_document1 = file
        #file_name = pdf_document1.split(".")
        pdf = pdfplumber.open(pdf_document1)
        n = len(pdf.pages)
        a120 = []
        for page in range(n):
            f = pdf.pages[page].extract_text()
            f1 = f.find("-60")
            if f1 != -1:
                start_page.append(page)
            f2 = f.find("-64")
            if f2 != -1:
                End_page.append(page)
        pdf_document = pdf_document1
        file_name = pdf_document.split(".")
        pdf = PdfFileReader(pdf_document)
        print(start_page)
        pgi= start_page[0]+1
        pgf=End_page[0]
        print(End_page)
        pdf_writer = PdfFileWriter()
        for page in range(pgi-1,pgf):
            current_page = pdf.getPage(page)
            pdf_writer.addPage(current_page)
        #with open(f'E:/Desktop all/Desktop 09-2020/تقرير عمل/مناقصات اعتماد/11-5-2023'+str(file_name[0])+'_BOQ.pdf', "wb") as out:
        with open(f'' + str(file_name[0]) + '_BOQ.pdf', "wb") as out:
                pdf_writer.write(out)
    split_much()
    start_page.clear()
    End_page.clear()
