import sys

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

rsrcmgr = PDFResourceManager()

outfp = sys.stdout
codec = 'utf-8'
laparams = LAParams()
pagenos = set()
maxpages = 0

device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams)

filename = sys.argv[1]

with file(filename, 'rb') as fp:

    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.get_pages(fp, pagenos, check_extractable=True):
        interpreter.process_page(page)

device.close()
