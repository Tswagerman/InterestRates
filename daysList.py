import datetime
from datetime import date
import time
import locale

class List:
	def __init__(self):
		self.List = []

	def createList(self):
		locale.setlocale(locale.LC_ALL, 'nl_NL') 
		#Creates a list of dates for the 'lenList' upcoming days. 
		lenList = 15
		for i in range(lenList):
			if (i == 0):
				current = datetime.datetime.today()
			else:
				current = current + datetime.timedelta(1)
			currentTime = datetime.datetime.strftime(current,"%#d %B %Y") 
			self.List.append(currentTime)
		return self.List