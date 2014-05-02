import sys
from pprint import pprint

from alchemyapi import AlchemyAPI
from pdfreader import pdf_to_str

LENGTH_LIMIT = 120000

def main():

    alchemyapi = AlchemyAPI()

    try:
        filename = sys.argv[1]
    except IndexError:
        print "Give a filename as the second argument!"
        sys.exit(1)

    text = pdf_to_str(filename)

    if len(text) >= LENGTH_LIMIT:
        print "PDF content is longer ({} characters) than the maximum \
of {}, skipping remainder".format(len(text), LENGTH_LIMIT)
        text = text[:LENGTH_LIMIT]


    print "KEYWORDS"
    response = alchemyapi.keywords('text', text)
    for keyword in response['keywords']:
        print '  - {}'.format(keyword['text'])

    print
    print "CONCEPTS"
    response = alchemyapi.concepts('text', text)
    for concept in response['concepts']:
        print '  - {}'.format(concept['text'])

main()
