from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
import PyPDF2 as pypdf
from weekList import List
#from PDFtoText import convert

class WebScraper:
	def __init__(self):
		self.List = List()
		WebScraper.main(self)
	
	def main(self):
		List = self.List.createList()
		url = "https://www.rentebox.nl/renteoverzicht/renteberichten.aspx?relid=863857FC-96E0-4875-82E3-902151893771"
		page = requests.get(url)   
		data = page.text
		soup = BeautifulSoup(data, "html.parser")
		for i in range(len(List)):
			#Checks for href corresponding to the dates in the list.
			for link in soup.find_all('a', href = True, text = re.compile(List[i])):
				link = link.get('onclick')
				if link.endswith(');'):
					link = link[:-3]
				if link.startswith('window.open('):
					link = link[13:]
					print(link)

if __name__ == "__main__":
	WebScraper()