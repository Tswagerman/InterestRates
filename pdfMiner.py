import urllib.request
import io
import os
import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


# from datetime import datetime
# a = datetime.now()
class Converter:
    def __init__(self):
        self.innerList = []
        self.List = []

    def convertPDFtoText(self, url):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        f = urllib.request.urlopen(url)
        f = f.read()
        # Cast to StringIO object
        fp = io.BytesIO(f)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        caching = True
        pagenos=set()
        for page in PDFPage.get_pages(fp, pagenos, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
        fp.close()
        device.close()
        string = retstr.getvalue()
        retstr.close()
        with open("example.txt", "w", encoding="utf-8") as text_file:
            for i in range(len(string)):
                #the file is split in single characters
                if (string[i] == '\n' and string[i+1].isdigit()):
                    number = ''
                    #When a character in the string is part of a number it is added.
                    for j in range(len(string) - i):
                        j += 1
                        #Every number of interest ends with '%'
                        if ((i+j) < len(string) and string[i+j] == '%'):
                            number += string[i+j]
                            self.innerList.append(number)
                            break
                        #Some files work with '.' and others with ',' to represent a comma.
                        if ((i+j) < len(string) and string[i+j] == '.'):
                            number += string[i+j]
                        if ((i+j) < len(string) and string[i+j] == ','):
                            number += string[i+j]
                        if ((i+j) < len(string) and string[i+j].isdigit()):
                            number += string[i+j]
                        #Coming across a letter means the number is not important.
                        if ((i+j) < len(string) and string[i+j].isalpha()):
                            number = ''
                            break
                    i += j + 1
            #text_file.write(string)
            self.List.append(self.innerList)
            self.innerList = [] 
            for i in range(len(self.List)):
                text_file.write('############BEGINNING OF FILE###############\n')
                for j in range(len(self.List[i])):
                    text_file.write(self.List[i][j])
                text_file.write('\n############END OF FILE############\n')
        return self.List

