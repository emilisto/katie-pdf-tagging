import string
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

def _strip_non_printable_chars(s):
    """ Returns s with all non-printable characters removed """
    return filter(lambda x: x in string.printable, s)

def read_pdf(filename):
    """ Yields the content of a PDF """

    buf = io.StringIO()

    laparams = LAParams()
    rsrcmgr = PDFResourceManager()
    device = UnicodeTextConverter(rsrcmgr, buf, laparams=laparams)

    with file(filename, 'rb') as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp, set(), check_extractable=True):
            buf.truncate(0)
            interpreter.process_page(page)
            yield _strip_non_printable_chars(buf.getvalue())

def pdf_to_str(filename):
    """ Returns the contents of a PDF as a unicode string """

    content = ''
    for chunk in read_pdf(filename):
        content += chunk
    return content

if __name__ == '__main__':
    filename = sys.argv[1]
    for text in read_pdf(filename):
        print text.encode('utf8')
