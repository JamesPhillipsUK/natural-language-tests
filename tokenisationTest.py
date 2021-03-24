import nltk # Natural Language Processing Toolkit #
import urllib.request # Python Website Crawler. #
from bs4 import BeautifulSoup # Python HTML Disassembler. #
import string # String lib - used to remove punctuation. #
# nltk.download() # Open NLTK package Downloader. #

# get the page from the URL
response = urllib.request.urlopen(urllib.request.Request(url='https://cy.wikipedia.org/wiki/COVID-19', headers={'User-Agent': 'Mozilla/5.0'}))
# print(response.read())

# parse it as HTML
soup = BeautifulSoup(response.read(), 'html5lib')

# strip the contents of head, script, or style tags.
for erroneousData in soup(["head", "script", "style"]):
  erroneousData.extract()

# Get the text from the HTML
text = soup.get_text(strip = True)
# print(text)

# Tokenise the text
tokens = nltk.tokenize.word_tokenize(text)
# Strip out punctuation tokens
tokItems = ["".join(j.lower() for j in i if j not in string.punctuation)
  for i in tokens]

# Build the frequency data
freq = nltk.FreqDist(tokItems)
for key, value in freq.items():
  print(str(key) + ':' + str(value))
# Plot a requency graph
freq.plot(cumulative=False)
