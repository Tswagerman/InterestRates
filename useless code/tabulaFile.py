import tabula
import urllib.request
import io
import os
import re
import pandas as pd
import pdfminer
from io import StringIO  
from pdfminer.converter import LTChar, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

class Converter:

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
        #For working with the dataframe I need 'pandas'
        dfs = tabula.read_pdf(url, pages='all', encoding='ISO-8859-1', multiple_tables=True)
        print(dfs)
        #https://stackoverflow.com/questions/39485920/how-to-add-unicode-in-truetype0font-on-pdfbox-2-0-0/39644941
        #https://stackoverflow.com/questions/50661750/pdfbox-throws-error-while-extracting-text-encoded-with-font-dejavu-sans-condense
        #print('iloc = ',dfs.iloc[0])
        #tabula.convert_into(url, "output.csv", output_format="csv", pages='all')
        #table = pd.read_table("output.csv", encoding="ISO-8859-1")
        #data_top = table.head()  
        #print(list(data_top.columns)) 
        #print(data_top)
        #print(table)
        #df2 =  tabula.read_pdf(url, encoding='utf-8', pages="all", multiple_tables=True)
        #data = pd.read_csv("output.csv",sep='delimiter', header=None, engine="python")
        #print(data)
        #print(df2)

    def pdf_to_csv(filename):

        class CsvConverter(TextConverter):
            def __init__(self, *args, **kwargs):
                TextConverter.__init__(self, *args, **kwargs)

            def end_page(self, i):
                from collections import defaultdict
                lines = defaultdict(lambda : {})
                for child in self.cur_item._objs:                #<-- changed
                    if isinstance(child, LTChar):
                        (_,_,x,y) = child.bbox                   
                        line = lines[int(-y)]
                        line[x] = child._text.encode(self.codec) #<-- changed

                for y in sorted(lines.keys()):
                    line = lines[y]
                    self.outfp.write(";".join(line[x] for x in sorted(line.keys())))
                    self.outfp.write("\n")

        # ... the following part of the code is a remix of the 
        # convert() function in the pdfminer/tools/pdf2text module
        rsrc = PDFResourceManager()
        outfp = StringIO()
        device = CsvConverter(rsrc, outfp, codec="utf-8", laparams=LAParams())
            # becuase my test documents are utf-8 (note: utf-8 is the default codec)

        doc = PDFDocument()
        fp = open(filename, 'rb')
        parser = PDFParser(fp)       
        parser.set_document(doc)     
        doc.set_parser(parser)       
        doc.initialize('')

        interpreter = PDFPageInterpreter(rsrc, device)

        for i, page in enumerate(doc.get_pages()):
            outfp.write("START PAGE %d\n" % i)
            if page is not None:
                interpreter.process_page(page)
            outfp.write("END PAGE %d\n" % i)

        device.close()
        fp.close()

        return outfp.getvalue()