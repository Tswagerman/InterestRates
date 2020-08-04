from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
import PyPDF2 as pypdf
from daysList import List
#from pdfMiner import Converter
#from PDFtoText import Converter
from tabulaFile import Converter
#from tableMaker import Converter
import io
import pandas as pd     

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
		#erasing previous content in text file
		file = open("example.txt","w")
		file.close()
		for i in range(len(List)):
			#Checks for href corresponding to the dates in the list.
			#print('soup ================', soup)
			for link in soup.find_all('a', href = True, text = re.compile(List[i])):
				link = link.get('onclick')
				if link.startswith('window.open('):
					link = link[13:]
				if link.endswith(');'):
					link = link[:-3]
				self.converter.convertPDFtoText(link)
				print('################Link done###############3')
		print('DONE')

if __name__ == "__main__":
	WebScraper()