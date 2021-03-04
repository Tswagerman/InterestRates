import pandas as pd
from csv_diff import load_csv, compare
import difflib
from csv import DictReader

class CompareCSV:
	def compareCSV(self, currentFile, databaseFile):
		print('compare here')
		diff = compare(
			load_csv(open(currentFile)),
			load_csv(open(databaseFile)))
		print(diff)