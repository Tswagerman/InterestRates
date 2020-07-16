import io
import requests
from PyPDF2 import PdfFileReader

class Converter:

	def convertPDFtoText(self, url):
		r = requests.get(url)
		f = io.BytesIO(r.content)
		reader = PdfFileReader(f)
		contents = reader.getPage(0).extractText().split('\n')
		return contents