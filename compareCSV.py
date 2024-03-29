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
		self.name = ''


	def compareCSV(self, currentFile, databaseFile, name):
		print('compare here')
		self.name = name
		with open(currentFile, 'r', encoding="utf-8", newline='') as t1, open(databaseFile, 'r', encoding="utf-8", newline='') as t2:
			currFile = t1.readlines()
			dataFile = t2.readlines()
			self.createRowLists(currFile, dataFile)
			for index in range(len(self.rowIndexList)):
				self.createColumnLists(self.rowStringList1[index], self.rowStringList2[index], index)
			self.clearLists()

	def createRowLists(self, currFile, dataFile):
		#Comparing every row within the new file and the old file
		index = 0 #The indices are here to keep track of the columns and rows. 
		for row1 in currFile: #row1 and row2 are the contents of the rows
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
		index1 = 0 #Column index of current file
		for column1 in row1.split(string):
			index2 = 0 #Column index of the database file
			for column2 in row2.split(string):
				#Statement looking for differences in the two files, that does not allow letters.
				#Using the 're.search' function.
				if ((index1 == index2) and (column1 != column2) 
					and ((re.search('[a-zA-Z]', column1)) == None) 
						and ((re.search('[a-zA-Z]', column2)) == None)):
					#Adding the strings that do not match to the column lists.
					self.colStringList1.append(column1)
					self.colStringList2.append(column2)
					self.colIndexList.append(index1)
					print('row = ', rowIndex, 'column = ', index1, 'current value = ', column1, 'previous value = ', column2)
					self.getValueSpecs(rowIndex, index1)
				index2 += 1
			index1 += 1

	def getValueSpecs(self, rowIndex, columnIndex):
		nameList = ['Centraal_Beheer', 'Woonfonds_Hypotheken']
		NHGlist = []
		interestList = []
		#print('name = ', self.name)
		if self.name in nameList:
			#print('GETTING VALUE SPECS')
			NHGlist = ['', 'NHG', '<= 60%', '<= 70%', '<= 80%', '<= 90%', '<= 95%', '> 95%']
			interestList = ['3 maanden','1 jaar', '2 jaar', '3 jaar', '4 jaar', '5 jaar', '6 jaar', '7 jaar', '8 jaar', '9 jaar', '10 jaar', '12 jaar', '15 jaar', '20 jaar', '30 jaar']
		else: 
			return
		if columnIndex >= len(NHGlist):
			columnIndex %= len(NHGlist)
		if rowIndex >= len(interestList):
			rowIndex %= len(interestList)		
		#print('column = ', columnIndex, 'row = ', rowIndex)
		#print('nhgLen = ', len(NHGlist), 'interest = ', len(interestList))
		print('NHG = ', NHGlist[columnIndex], 'rente over ', interestList[rowIndex])
		#print('row = ', self.rowIndexList[rowIndex], 'column = ', self.colIndexList[columnIndex])
		#string = '"' + "," + '"'
		#for row in self.rowStringList1:
			#for column in row.split(string):
				#print('self.rowStringList1[rowIndex] = ', column)


	def clearLists(self):
		self.rowStringList1.clear()
		self.rowStringList2.clear()
		self.rowIndexList.clear()
		self.colStringList1.clear()
		self.colStringList2.clear()
		self.colIndexList.clear()