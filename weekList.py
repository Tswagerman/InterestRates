import datetime
from datetime import date
import time
import locale

class WeekList:
	def __init__(self):
		self.weekList = []

	def List(self):
		locale.setlocale(locale.LC_ALL, 'nl_NL') 
		today = datetime.datetime.today()
		todayPlusOne = today + datetime.timedelta(1)
		todayPlusTwo = today + datetime.timedelta(2)
		todayPlusThree = today + datetime.timedelta(3)
		todayPlusFour = today + datetime.timedelta(4)
		today = datetime.datetime.strftime(today,"%d %B %Y") 
		todayPlusOne = datetime.datetime.strftime(todayPlusOne,"%d %B %Y") 
		todayPlusTwo = datetime.datetime.strftime(todayPlusTwo,"%d %B %Y") 
		todayPlusThree = datetime.datetime.strftime(todayPlusThree,"%d %B %Y") 
		todayPlusFour = datetime.datetime.strftime(todayPlusFour,"%d %B %Y") 
		self.weekList = []
		self.weekList.append(today)
		self.weekList.append(todayPlusOne)
		self.weekList.append(todayPlusTwo)
		self.weekList.append(todayPlusThree)
		self.weekList.append(todayPlusFour)
		return self.weekList