import sys
import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

class UnicodeTextConverter(TextConverter):
    """ Writes text in unicode instead of str """
    def write_text(self, text):
        if type(text) is str:
            text = text.decode(self.codec)
        self.outfp.write(text)

def pdf_to_str(filename):
    """ Takes a PDF filename and returns its contents in unicode """

    buf = io.StringIO()

    laparams = LAParams()
    rsrcmgr = PDFResourceManager()
    device = UnicodeTextConverter(rsrcmgr, buf, laparams=laparams)

    with file(filename, 'rb') as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp, set(), check_extractable=True):
            interpreter.process_page(page)

    return buf.getvalue()


if __name__ == '__main__':
    filename = sys.argv[1]
    content = pdf_to_str(filename)
    print content
