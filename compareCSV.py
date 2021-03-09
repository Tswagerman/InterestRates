import re #Also imported in main.py. Python only adds lookup time in 'sys.modules' to execution time. 

class CompareCSV:
	def __init__ (self):
		#The rows in the current file
		self.rowStringList1 = []
		#The rows in the database file
		self.rowStringList2 = []
		self.rowIndexList = []

		#The columns in the current file
		self.colStringList1 = []
		#The columns in the database file
		self.colStringList2 = []
		self.colIndexList = []

	def compareCSV(self, currentFile, databaseFile):
		print('compare here')
		with open(currentFile, 'r', newline='') as t1, open(databaseFile, 'r', newline='') as t2:
			print('Opening files')
			currFile = t1.readlines()
			dataFile = t2.readlines()
			self.createRowLists(currFile, dataFile)
			for index in range(len(self.rowIndexList)):
				self.createColumnLists(self.rowStringList1[index], self.rowStringList2[index], index)
			self.getValueSpecs()
			self.clearLists()

	def createRowLists(self, currFile, dataFile):
		#Comparing every row within the new file and the old file
		index = 0
		for row1 in currFile:
			index2 = 0
			for row2 in dataFile:
				if ((index == index2) and (row1 != row2)):
					self.rowStringList1.append(row1)
					self.rowStringList2.append(row2)
					self.rowIndexList.append(index)
					break
				index2 += 1
			index += 1

	def createColumnLists(self, row1, row2, rowIndex):
		#To make sure ',' in between numbers are not seen as separator
		#In the CSV files a comma seperator is denoted as ",". Hence the extra ""
		string = '"' + "," + '"'
		#Comparing the columns within the provided rows
		index1 = 0
		for column1 in row1.split(string):
			index2 = 0
			for column2 in row2.split(string):
				#If statement that does not allow letters. Using the 're.search' function.
				if ((index1 == index2) and (column1 != column2) 
					and ((re.search('[a-zA-Z]', column1)) == None) 
						and ((re.search('[a-zA-Z]', column2)) == None)):
					#Adding the strings that do not match to the column lists.
					self.colStringList1.append(column1)
					self.colStringList2.append(column2)
					self.colIndexList.append(index1)
					print('row = ', rowIndex, 'column = ', index1, 'current value = ', column1, 'previous value = ', column2)
				index2 += 1
			index1 += 1

	def getValueSpecs(self):
		for rowIndex in range(len(self.rowStringList1)):
			print('self.rowStringList1[rowIndex] = ', self.rowStringList1[rowIndex])

	def clearLists(self):
		self.rowStringList1.clear()
		self.rowStringList2.clear()
		self.rowIndexList.clear()
		self.colStringList1.clear()
		self.colStringList2.clear()
		self.colIndexList.clear()