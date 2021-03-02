import camelot

PERC = '%'

class Converter:
    #This works best so far.
    def convertPDFtoCSV(self, url, name, index):
        tables = camelot.read_pdf(url, pages='all', flavor='stream')
        if (tables.n != 0):
            print(tables[0].parsing_report)
        else:
            print('No tables found.')
        for i in range(tables.n):
            print(tables[i].parsing_report)
            tables[i].to_csv('output\\'+ str(name) + '.csv', mode='w')