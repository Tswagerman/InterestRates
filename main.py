from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
import PyPDF2 as pypdf
import io
import os
import shutil
import pandas as pd  
#complementary code  
from daysList import List
from PDFtoCSV import Converter 
#from cleanCSV import Csvcleaner

class WebScraper:
	def __init__(self):
		self.List = List()
		self.nameList = []
		self.linkList = []
		self.converter = Converter()
		self.index = 0
		#self.cleaner = CSVcleaner()
		WebScraper.main(self)
	
	def main(self):
		List = self.List.createList()
		url = "https://www.rentebox.nl/renteoverzicht/renteberichten.aspx?relid=863857FC-96E0-4875-82E3-902151893771"
		page = requests.get(url)   
		data = page.text
		soup = BeautifulSoup(data, "html.parser")
		dirpath = 'C:/Users/Thomas/Desktop/AI 3rd year/Mortgage Interest Rates/output'
		#(final product will have to compare output files with previous output files)
		for filename in os.listdir(dirpath):
			filepath = os.path.join(dirpath, filename)
			try:
				shutil.rmtree(filepath)
			except OSError:
				os.remove(filepath)
		for i in range(len(List)):
			#Checks for href corresponding to the dates in the list.
			for link in soup.find_all('a', text = re.compile(List[i])):
				name = str(link)
				dictionary = ['Rentewijziging', 'Renteverhoging', 'Renteverlaging']
				for i in range(len(dictionary)):
					index = name.find(dictionary[i])
					if (index > 0):
						index += len(dictionary[i]) + 1
						name = name[index:-4]
						break;
				link = link.get('onclick')
				link = link[13:-3]
				self.nameList.append(name)
				self.linkList.append(link)

		for i in range(len(self.linkList)):
			print('name = ', self.nameList[i])
			print('link = ', self.linkList[i])	
			self.converter.convertPDFtoCSV(self.linkList[i], self.nameList[i], i)
			print('index = ', i)
			print('################LINK DONE################')
		print('DONE')

		


if __name__ == "__main__":
	WebScraper()