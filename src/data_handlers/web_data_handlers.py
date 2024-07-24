import urllib.request
from lxml import etree

#returns parsed HTML data from the specified url
def getHTMLData(url: str):
    return getDataFromUrl(url, etree.HTMLParser())

#returns parsed XML data tree from the specified url
def getXMLData(url: str):
    return getDataFromUrl(url, etree.XMLParser())

#returns parsed data from the specified url
#url: a string
#parser: a standard or custom parser object from lxml
def getDataFromUrl(url: str, parser):
    with urllib.request.urlopen(url) as response:
        raw_data = response.read()

    parsed_data = etree.fromstring(raw_data, parser)

    return parsed_data

#returns a list of data delimited by '\n' from a text file
#filepath: a string
def getLineDelimitedData(filepath: str):
    with open(filepath, 'r') as file:
        raw_data = file.read()

    parsed_data = raw_data.split('\n')

    return parsed_data
