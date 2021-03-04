import pandas as pd
from csv_diff import load_csv, compare
import difflib
import csv
from csv import DictReader

class CompareCSV:
	def __init__ (self):
		self.rowStringList = []
		self.rowIndexList = []
		self.rowStringList2 = []
	def compareCSV(self, currentFile, databaseFile, filename):
		print('compare here')

		#skipRow = self.getSkipRow(filename)
		
		#df1 = pd.read_csv(currentFile, skiprows = skipRow)
		#df2 = pd.read_csv(databaseFile, skiprows = skipRow)
		with open(currentFile, 'r', newline='') as t1, open(databaseFile, 'r', newline='') as t2:
			currFile = t1.readlines()
			dataFile = t2.readlines()
			i = 0
			bool = False
			index = 0
			for row1 in currFile:
				for row2 in dataFile:
					if ((row1 != row2) and (bool == False)):
						bool = True
						self.rowStringList.append(row1)
						self.rowStringList2.append(row2)
						self.rowIndexList.append(index)
					if ((row1 == row2) and (bool == True)):
						bool = False
						del self.rowStringList[-1]
						del self.rowStringList2[-1]
						del self.rowIndexList[-1]
						break
					index += 1
				index = 0
			print('rowStringList = ', self.rowStringList)
			print('rowStringList = ', self.rowStringList2)
			print('rowIndexList = ', self.rowIndexList)
			self.rowStringList.clear()
			self.rowStringList2.clear()
			self.rowIndexList.clear()
		#diff = compare(
		#	load_csv(open(databaseFile)),
		#	load_csv(open(currentFile)))
		#print(diff)
		#https://stackoverflow.com/questions/57759807/compare-two-columns-in-two-csv-files-row-by-row-with-csv-dictreader
	
	#def getSkipRow(self, filename):
		