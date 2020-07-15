from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
from weekList import WeekList

class WebScraper:
	def __init__(self):
		self.weekList = WeekList()
		WebScraper.main(self)
	
	def main(self):
		weekList = self.weekList.List()
		print(weekList)
		url = "https://www.rentebox.nl/renteoverzicht/renteberichten.aspx?relid=863857FC-96E0-4875-82E3-902151893771"
		page = requests.get(url)   
		data = page.text
		soup = BeautifulSoup(data, "html.parser")
		#print(soup)
		print(len(weekList))
		for i in range(len(weekList)):
			for link in soup.find_all('a', href = True, text = re.compile(weekList[i])):
				print(link.get('id'))
				#print(link)
	
if __name__ == "__main__":
	WebScraper()