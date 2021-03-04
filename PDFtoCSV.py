#I chose camelot over tabula and pdfminer, (camelot uses PDFminer)
#because camelot showed the best performance with the pdf files I provided.
import camelot 
import os #Also imported this in main.py. Python only adds lookup time in 'sys.modules' to execution time. 
import urllib.request
from pikepdf import Pdf
from termcolor import colored #Also imported this in main.py. Python only adds lookup time in 'sys.modules' to execution time. 

class Converter:
	def __init__ (self):
		self.cwd = os.getcwd() #Current working directory
		self.pdfPath = self.cwd + '\\pdf\\'
		self.outputPath = self.cwd + '\\output\\'
		os.system('color')

	def convertPDFtoCSV(self, url, name, index):
		try:
			tables = camelot.read_pdf(url, pages='all', flavor='stream', lattice=True, split_text=True) 
			self.loopOverTables(tables, name)
		except:
			self.decryptPikePDF(url, name)
			tables = camelot.read_pdf(self.pdfPath + str(name) + '.pdf', pages='all', flavor='stream') 
			self.loopOverTables(tables, name)

	def loopOverTables(self, tables, name):
		for i in range(tables.n):
			try:
				tables[i].to_csv(self.outputPath + str(name) + '.csv', mode='w')
				print(tables[i].parsing_report)
			except: #later; Send a clear error message here.
				print(colored('Something went wrong. Most likely no tables were found', 'red'))

	def decryptPikePDF(self, url, name):
		#When camelot is not able to read straight from the website
		#Because of "NotImplementedError: only algorithm code 1 and 2 are supported"
		#pikePDF is used to download the file and decrypt it
		#into a readable pdf to be used by camelot
		print(colored('File is encrypted', 'green'))
		urlName = url[45:]
		response = urllib.request.urlopen(url)
		file = open(self.pdfPath + urlName, 'wb')
		file.write(response.read())
		file.close()
		with Pdf.open(self.pdfPath + str(urlName), password='') as pdf:
			pdf.save(self.pdfPath + str(name) + '.pdf')	