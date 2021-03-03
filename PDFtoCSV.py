#I chose camelot over tabula and pdfminer, 
#because camelot showed the best performance with the pdf files I provided.
import camelot 
import os 
from pikepdf import Pdf
import urllib.request
PERC = '%'

class Converter:
	#This works best so far.
	def convertPDFtoCSV(self, url, name, index):
		try:
			tables = camelot.read_pdf(url, pages='all', flavor='stream') 
			for i in range(tables.n):
				try:
					print(tables[i].parsing_report)
					tables[i].to_csv('output\\'+ str(name) + '.csv', mode='w')
				except: #later; Send a clear error message here.
					print('Something went wrong. Most likely no tables were found')
		except:
			#When camelot is not able to read straight from the website
			#Because of "NotImplementedError: only algorithm code 1 and 2 are supported"
			#pikePDF is used to download the file and decrypt it
			#into a readable pdf to be used by camelot
			cwd = os.getcwd() #Current working directory
			pdfPath = cwd + '\\pdf\\'
			outputPath = cwd + '\\output\\'
			urlName = url[45:]
			response = urllib.request.urlopen(url)
			file = open(pdfPath + urlName, 'wb')
			file.write(response.read())
			file.close()
			with Pdf.open(pdfPath + str(urlName), password='') as pdf:
				pdf.save(pdfPath + str(name) + '.pdf')
			tables = camelot.read_pdf(pdfPath + str(name) + '.pdf', pages='all', flavor='stream') 
			for i in range(tables.n):
				try:
					print(tables[i].parsing_report)
					tables[i].to_csv(outputPath + str(name) + '.csv', mode='w')
				except: #later; Send a clear error message here.
					print('Something went wrong. Most likely no tables were found')