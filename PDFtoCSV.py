import io
import requests
import camelot
import pandas


PERC = '%'

class Converter:
    #This works best so far.
    def convertPDFtoCSV(self, url, index):
        print('url = ', url)
        tables = camelot.read_pdf(url,pages='all', flavor='stream')
        if (len(tables)  !=  0):
            print(tables[0].parsing_report)
        else:
            print('No tables found.')
        for i in range(tables.n):
            print(tables[i].parsing_report)
            tables[i].to_csv('output\\output' + str(index) + '.csv', mode='w')
        df = pandas.read_csv('output\\output' + str(index) + '.csv')
        print(df)