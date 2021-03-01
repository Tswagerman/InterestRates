import io
import requests
import tabula
from PyPDF2 import PdfFileReader
from tabula import read_pdf
from tabula import convert_into
from fpdf import FPDF 

PERC = '%'

class Converter:
    def __init__(self):
        self.contentsCheck = ['1','2','3','4','5','6','7','8','9','0','%']
    #Does not work for 100% of the pdf files... pdfMiner should be more accurate
    def convertPDFtoCSV(self, url, index):
        print('url = ', url)
        r = requests.get(url)
        f = io.BytesIO(r.content)
        #Not necessary, but here for debugging resons
        reader = PdfFileReader(f, strict=True)
        print("Opening '{}', pages={}".format(url, reader.getNumPages()))
        df = read_pdf(url, multiple_tables = True, pages='all', encoding = 'utf-8', silent = False, lattice = False, stream = False)
        print("Start DF", df, "End DF")
        #Every table is added to the corresponding file separately
        for i in df:
            print('Saving in output\\output' + str(index) + '.csv')
            i.to_csv('output\\output' + str(index) + '.csv', mode='a', index = False)
        
        
#class Converter:
#    def __init__(self):

#        self.contentsCheck = ['1','2','3','4','5','6','7','8','9','0','%']
#    #Does not work for 100% of the pdf files... pdfMiner should be more accurate
#    def convertPDFtoText(self, url):
#        print('url = ', url)
#        r = requests.get(url)
#        f = io.BytesIO(r.content)
#        reader = PdfFileReader(f, strict=False)
#        print(reader)
#        number_of_pages = reader.getNumPages()
#        print('number of pages = ', number_of_pages)
#        file2write=open("example.txt",'a')
#        file2write.write('############BEGINNING OF FILE###############\n')
#        for page_number in range(number_of_pages):
#            contents = reader.getPage(page_number).extractText().split('\n')
#            for i in range(len(contents)):
#                if PERC in contents[i] and not any(c.isalpha() for c in contents[i]):
#                    file2write.write(contents[i])
#                    continue
#        read_pdf(url, output_format = "json", pages=number_of_pages)
#        file2write.write('\n############END OF FILE############\n')
#        file2write.close()

#if (len(df) == 0):
#            print('if-statement!!!')
#            pdf = FPDF()  
#            pdf.add_page() 
#            pdf.set_font("Arial", size = 15) 
#            f = open("pdf/F7F0D399-94C7-4088-9A81-7903CDC4ECD9.txt", "r") 
#            for x in f: 
#                pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
#            pdf.output('pdf/F7F0D399-94C7-4088-9A81-7903CDC4ECD9.pdf') 
#            df = read_pdf("pdf/F7F0D399-94C7-4088-9A81-7903CDC4ECD9.pdf", multiple_tables = True, pages='all', encoding = 'utf-8', silent = True, lattice = False, stream = False)