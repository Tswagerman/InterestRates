
class CompareCSV:
	def compareCSV(self, filepath, filedestination):
		print('compare here')
		with open(filedestination) as check_file:
			for row in check_file:
				for column in row.split('","'):
					#print('column = ', column)
					check_set = set(column)
					#check_set = set(row.split(',')[column].strip().upper())
		print(check_set)
		with open(filepath, 'r') as in_file:
			for row in in_file:
				for column in row.split('","'):
					#print('checking line')
					#print('row = ', row)
					print('column = ', column)
					print('check_set = ', check_set)
					if column not in check_set:
						print('not the same: ', column)
#from csv_diff import load_csv, compare
#diff = compare(
#			load_csv(open(filedestination)),
#			load_csv(open(filepath)))
#		print(diff)