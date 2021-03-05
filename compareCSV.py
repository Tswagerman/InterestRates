import pandas as pd
from csv_diff import load_csv, compare
import difflib
import csv
from csv import DictReader

class CompareCSV:
	def __init__ (self):
		self.rowStringList = []
		self.rowIndexList = []
	def compareCSV(self, currentFile, databaseFile, filename):
		print('compare here')

		#skipRow = self.getSkipRow(filename)
		
		#df1 = pd.read_csv(currentFile, skiprows = skipRow)
		#df2 = pd.read_csv(databaseFile, skiprows = skipRow)
		with open(currentFile, 'r', newline='') as t1, open(databaseFile, 'r', newline='') as t2:
			print('Opening files')
			currFile = t1.readlines()
			dataFile = t2.readlines()
			i = 0
			index = 0
			for row1 in currFile:
				bool = False
				for row2 in dataFile:
					print('row 1 = ', row1)
					print('row 2 = ', row2)
					print('idx = ', index)
					if ((row1 != row2) and (bool == False)):
						print('bool => True')
						bool = True
						self.rowStringList.append(row1)
						self.rowIndexList.append(index)
					if ((row1 == row2) and (bool == True)):
						print('bool => False')
						bool = False
						del self.rowStringList[-1]
						del self.rowIndexList[-1]
						break
				index += 1
			print('rowStringList = ', self.rowStringList , '\n')
			print('rowIndexList = ', self.rowIndexList)
			self.rowStringList.clear()
			self.rowIndexList.clear()
		#diff = compare(
		#	load_csv(open(databaseFile)),
		#	load_csv(open(currentFile)))
		#print(diff)
		#https://stackoverflow.com/questions/57759807/compare-two-columns-in-two-csv-files-row-by-row-with-csv-dictreader
	
	#def getSkipRow(self, filename):
		