import io
import requests
from PyPDF2 import PdfFileReader

PERC = '%'

class Converter:
    def __init__(self):
        self.contentsCheck = ['1','2','3','4','5','6','7','8','9','0','%']
    #Does not work for 100% of the pdf files... pdfMiner should be more accurate
    def convertPDFtoText(self, url):
        print('url = ', url)
        r = requests.get(url)
        f = io.BytesIO(r.content)
        reader = PdfFileReader(f, strict=False)
        print(reader)
        number_of_pages = reader.getNumPages()
        print('number of pages = ', number_of_pages)
        file2write=open("example.txt",'a')
        file2write.write('############BEGINNING OF FILE###############\n')
        for page_number in range(number_of_pages):
            contents = reader.getPage(page_number).extractText().split('\n')
            for i in range(len(contents)):
                if PERC in contents[i] and not any(c.isalpha() for c in contents[i]):
                    file2write.write(contents[i])
                    continue
        file2write.write('\n############END OF FILE############\n')
        file2write.close()