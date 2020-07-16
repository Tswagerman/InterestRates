from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
from weekList import List

class WebScraper:
	def __init__(self):
		self.List = List()
		WebScraper.main(self)
	
	def main(self):
		List = self.List.createList()
		print(List)
		url = "https://www.rentebox.nl/renteoverzicht/renteberichten.aspx?relid=863857FC-96E0-4875-82E3-902151893771"
		page = requests.get(url)   
		data = page.text
		soup = BeautifulSoup(data, "html.parser")
		#print(soup)
		print(len(List))
		for i in range(len(List)):
			for link in soup.find_all('a', href = True, text = re.compile(List[i])):
				print(link.get('id'))
				#print(link)
	
if __name__ == "__main__":
	WebScraper()