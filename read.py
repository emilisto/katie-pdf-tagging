import sys

from PyPDF2 import PdfFileReader
from emilisto.interact import interact

filename = sys.argv[1]

print "Reading %s" % (filename,)

f = open(filename, "rb")
reader = PdfFileReader(f)
page = reader.getPage(1)
text = page.extractText()
interact()
