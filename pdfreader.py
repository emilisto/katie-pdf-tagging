import sys
import io

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter, HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter

class UnicodeTextConverter(TextConverter):
    def write_text(self, text):
        self.outfp.write(text.decode(self.codec))

class PDFReader(object):
    """ PDFReader - convert PDF's to text. """

    def __init__(self, outfp=sys.stdout):

        self.rsrcmgr = PDFResourceManager()
        self.device = TextConverter(self.rsrcmgr, outfp)

    def read(self, filename):
        """ Reads the given PDF and outputs text to the supplied outfp """

        pagenos     = set()
        maxpages    = 0
        layoutmode  = 'normal'
        scale       = 1

        with file(filename, 'rb') as fp:

            interpreter = PDFPageInterpreter(self.rsrcmgr, self.device)
            for page in PDFPage.get_pages(fp, pagenos, check_extractable=True):
                interpreter.process_page(page)

if __name__ == '__main__':
    filename = sys.argv[1]

    reader = PDFReader()
    reader.read(filename)
