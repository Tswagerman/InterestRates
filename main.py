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
from termcolor import colored

class WebScraper:
	def __init__(self):
		self.List = List()
		self.converter = Converter()
		self.compareCSV = CompareCSV()
		self.name = ''
		self.nameList = []
		self.linkList = []

		self.cwd = os.getcwd() #Current working directory
		self.outpath = self.cwd + '\\output'
		self.datapath = self.cwd + '\\database'
		self.pdfpath = self.cwd + '\\pdf'
		
		WebScraper.main(self) #Start running program
	
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
			self.moveFiles() #in here the comparison function is called
			print('index = ', i)
			print('################LINK DONE################')
		self.removePDF()
		print('DONE')

	#Function to find the company name in a string of html code.
	def getName(self):		
		dictionary = ['Rentewijziging', 'Renteverhoging', 'Renteverlaging']
		for i in range(len(dictionary)):
			index = self.name.find(dictionary[i])
			if (index > 0):
				#The index is the element corresponding 
				#to the start of the word in the dictionary. 
				#To get the name, one needs to add the length of the word + one space
				index += len(dictionary[i]) + 1
				self.name = self.name[index:-4].replace(" ", "_")
				break

	def moveFiles(self):
		#(final product will have to compare output files with previous output files)
		for filename in os.listdir(self.outpath):
			currentFile = os.path.join(self.outpath, filename)
			databaseFile = os.path.join(self.datapath, filename)
			#if previous version is present in database, need comparison
			if (os.path.isfile(databaseFile)):
				self.compareCSV.compareCSV(currentFile, databaseFile) #Comparison function
				#remove file in database
				try:
					shutil.rmtree(databaseFile)
				except OSError:
					os.remove(databaseFile)
				#Moving the latest file from the output folder to the database folder
				shutil.move(currentFile, databaseFile)	

	def removePDF(self):
		print(colored('REMOVING ALL THE PDF FILES FROM PDF FOLDER', 'green'))
		for filename in os.listdir(self.pdfpath):
			pdfFile = os.path.join(self.pdfpath, filename)
			try:
				shutil.rmtree(pdfFile)
			except OSError:
				os.remove(pdfFile)

if __name__ == "__main__":
	WebScraper()