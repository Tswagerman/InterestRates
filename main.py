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

class WebScraper:
	def __init__(self):
		self.List = List()
		self.converter = Converter()
		WebScraper.main(self)
	
	def main(self):
		List = self.List.createList()
		url = "https://www.rentebox.nl/renteoverzicht/renteberichten.aspx?relid=863857FC-96E0-4875-82E3-902151893771"
		page = requests.get(url)   
		data = page.text
		soup = BeautifulSoup(data, "html.parser")
		increment = 0
		dirpath = 'C:/Users/Thomas/Desktop/AI 3rd year/Mortgage Interest Rates/output'
		#Loop for deleting previous output files
		for filename in os.listdir(dirpath):
			filepath = os.path.join(dirpath, filename)
			try:
				shutil.rmtree(filepath)
			except OSError:
				os.remove(filepath)
		for i in range(len(List)):
			#Checks for href corresponding to the dates in the list.
			for link in soup.find_all('a', href = True, text = re.compile(List[i])):
				link = link.get('onclick')
				if link.startswith('window.open('):
					link = link[13:]
				if link.endswith(');'):
					link = link[:-3]
				self.converter.convertPDFtoCSV(link, increment)
				increment += 1
				print('################LINK DONE################')
		print('DONE')

if __name__ == "__main__":
	WebScraper()