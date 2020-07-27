import csv 
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
    def __init__(self):
        self.deco = {k:v for k,v in zip("hv012345678","─│┌┬┐├┼┤└┴┘")} 

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
        dfs = tabula.read_pdf(url, pages="all")
        #print(dfs)
        #print('iloc = ',dfs.iloc[0])
        tabula.convert_into(url, "output.csv", output_format="csv", pages='all')
        table = pd.read_table("output.csv", encoding="ISO-8859-1")

    # open outputfile for append
        with open("example.txt", "a", encoding="UTF8") as output:
            output.write("\n" + "-" * 40 + "\n\n")

        # get utf8 art
        open("output.csv","w")
        for line in self.create_table("output.csv"):
            output.write(''.join(line)+"\n")

    def create_table(self, file_name):
        """Takes a file_name to a csv. Produces utf8-art of the data. 
        Missing columns will be assumed to miss at end and replaced 
        by empty columns."""
        # mostly untested code - works for the 2 examples mentioned here
        with open(file_name,"r") as f:
            reader = csv.reader(f) 
            w = self.get_widths(reader)
            row_count = w["last"] 
            del w["last"]
            f.seek(0)
            return self.create_table_string(reader, w, row_count)

    def get_widths(self, csv_reader):
        widths = {}
        row_count = 0
        for row in csv_reader:
            if row: # ignore empties
                row_count += 1
                for idx,data in enumerate(row):
                    widths[idx] = max(widths.get(idx,0),len(data))

        widths["last"] = row_count
        return widths

    # supply other set of lines if you like

    def base_row(self, widths, row, max_key, _v, _h, _l, _m, _r):
        decoration = []
        text_data = []

        decoration.append(_l + _h*widths[0])
        for i in range(1,max_key):
            decoration.append(_m + _h*widths[i])
        decoration.append(_m + _h*widths[max_key] + _r)

        if row:
            for i,data in enumerate(row): 
                text_data.append(_v + "{:<{}}".format(data, widths[i]))

            for empty in range(i+1,max_key+1):
                text_data.append(_v + " "*widths[empty])
            text_data[-1]+=_v

        return [decoration, text_data]

    def get_first_row(self, widths,row):
        return self.base_row(widths, row, max(widths.keys()), self.deco["v"], self.deco["h"], 
                        self.deco["0"], self.deco["1"], self.deco["2"])

    def get_middle_row(self, widths,row):
        return self.base_row(widths, row, max(widths.keys()),  self.deco["v"], self.deco["h"],
                        self.deco["3"], self.deco["4"], self.deco["5"])

    def get_last_row(self, widths):
        decoration, _ = self.base_row(widths, [], max(widths.keys()), self.deco["v"], 
                                 self.deco["h"], self.deco["6"], self.deco["7"], self.deco["8"])

        return [decoration]


    def create_table_string(self, reader, widths, row_count): 
        output = []
        r = 0 
        for row in reader:
            if row:
                r += 1
                if r==1:
                    output.extend(self.get_first_row(widths, row))
                else:
                    output.extend(self.get_middle_row(widths, row))

        output.extend(self.get_last_row(widths))
        return output