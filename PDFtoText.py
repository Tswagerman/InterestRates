import io
import requests
from PyPDF2 import PdfFileReader

class Converter:

	def convertPDFtoText(self, url):
		r = requests.get(url)
		f = io.BytesIO(r.content)
		reader = PdfFileReader(f)
		contents = reader.getPage(0).extractText().split('\n')
		file2write=open("example.txt",'a')
		file2write.write('############BEGINNING OF FILE###############\n')
		for i in range(len(contents)):
			file2write.write(contents[i])
		file2write.write('############END OF FILE############\n')
		file2write.close()
		return contents