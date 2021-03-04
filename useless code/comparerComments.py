import pandas as pd
from csv_diff import load_csv, compare
import difflib
from csv import DictReader

class CompareCSV:
	def compareCSV(self, currentFile, databaseFile):
		print('compare here')
		#col_list = ["NHG", "65% MW", "65 - 80% MW", "80 - 95% MW", "> 95% MW"]
		#csv1 = open(currentFile, "r").readlines()
		#csv2 = open(databaseFile, "r").readlines()
		#for line in difflib.unified_diff(csv1, csv2):
		#	print(line)
		#skipRow = 0
		#with open(currentFile, 'r') as check_file:
		#	for row in check_file:
		#		if ((row.find('NHG')) > -1):
		#				break	
		#		else:
		#			skipRow += 1
		#	print('rows skipped = ', skipRow)

		
		#df1 = pd.read_csv(currentFile, skiprows = skipRow)
		#df2 = pd.read_csv(databaseFile, skiprows = skipRow)
		#mergedDF = pd.concat([df1,df2], axis=0)
		#mergedDF.drop_duplicates(keep=False, inplace=True) 
		#mergedDF.reset_index(drop=True, inplace=True)
		#print(mergedDF)
		#for col in df1.columns: 
		#	print(col) 
		diff = compare(
			load_csv(open(currentFile)),
			load_csv(open(databaseFile)))
		print(diff)

				#check_set = set(row.split(',')[column].strip().upper())
		#print(check_set)
		#with open(filepath, 'r') as in_file:
			#for row in in_file:
				#for column in row.split('","'):
					#print('checking line')
					#print('row = ', row)
					#print('column = ', column)
					#print('check_set = ', check_set)
					#if column not in check_set:
						#print('not the same: ', column)
#from csv_diff import load_csv, compare
#diff = compare(
#			load_csv(open(filedestination)),
#			load_csv(open(filepath)))
#		print(diff)