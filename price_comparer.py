import urllib2
from bs4 import BeautifulSoup

AMAZON_URL = "http://www.amazon.in/"

FLIPKART_URL = "http://www.flipkart.com/"

SEARCH_KEYWORD = raw_input("Enter the product name to compare :")

SEARCH_KEYWORD = SEARCH_KEYWORD.lower()

SPLITTED_KEYWORD = SEARCH_KEYWORD.split()

SEARCH_FLIPKART_URL = FLIPKART_URL + "searchq?" 

for i in range(len(SPLITTED_KEYWORD)):
	SEARCH_FLIPKART_URL = SEARCH_FLIPKART_URL + "+" + SPLITTED_KEYWORD[i]

def searcher(url):
	requester = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
	url_opener = urllib2.urlopen(requester)

	reader = url_opener.read()

	soup = BeautifulSoup(reader, "lxml")

	print soup

searcher(SEARCH_FLIPKART_URL)
