from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
import io
import os
import shutil
#complementary code  
from daysList import List
from PDFtoCSV import Converter 
from compareCSV import CompareCSV

class WebScraper:
	def __init__(self):
		self.List = List()
		self.converter = Converter()
		self.compareCSV = CompareCSV()
		self.name = ''
		self.nameList = []
		self.linkList = []
		#self.cleaner = CSVcleaner()
		WebScraper.main(self)
		WebScraper.getName(self)
		WebScraper.moveFiles(self)

	#Function to find the company name in a string of html code.
	def getName(self):		
		dictionary = ['Rentewijziging', 'Renteverhoging', 'Renteverlaging']
		for i in range(len(dictionary)):
			index = self.name.find(dictionary[i])
			if (index > 0):
				#The index is at the word in the dictionary. 
				#To get the name, one needs to add the length of the word + one space
				index += len(dictionary[i]) + 1
				self.name = self.name[index:-4]
				break;

	def moveFiles(self):
		dirpath = 'C:/Users/Thomas/Desktop/AI 3rd year/Mortgage Interest Rates/output'
		destpath = 'C:/Users/Thomas/Desktop/AI 3rd year/Mortgage Interest Rates/database'
		#(final product will have to compare output files with previous output files)
		for filename in os.listdir(dirpath):
			filepath = os.path.join(dirpath, filename)
			filedestination = os.path.join(destpath, filename)
			#if previous version is present in database, need comparison
			if (os.path.isfile(filedestination)):
				self.compareCSV.compareCSV(filepath, filedestination)
				#remove file in database
				try:
					shutil.rmtree(filedestination)
				except OSError:
					os.remove(filedestination)
			shutil.move(filepath, filedestination)	
	
	def main(self):
		List = self.List.createList()
		url = "https://www.rentebox.nl/renteoverzicht/renteberichten.aspx?relid=863857FC-96E0-4875-82E3-902151893771"
		page = requests.get(url)   
		data = page.text
		soup = BeautifulSoup(data, "html.parser")
		for i in range(len(List)):
			#Checks for href corresponding to the dates in the list.
			for link in soup.find_all('a', text = re.compile(List[i])):
				self.name = str(link)
				self.getName()
				self.nameList.append(self.name)
				link = link.get('onclick')
				link = link[13:-3]
				self.linkList.append(link)

		for i in range(len(self.linkList)):
			print('name :', self.nameList[i])
			print('link :', self.linkList[i])	
			self.converter.convertPDFtoCSV(self.linkList[i], self.nameList[i], i)
			self.moveFiles()
			print('index = ', i)
			print('################LINK DONE################')
		print('DONE')

if __name__ == "__main__":
	WebScraper()