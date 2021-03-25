"""
tokenisationTest.py

Testing word tokenisation of a large natural language text using NLTK.

Sample Data used: https://cy.wikipedia.org/wiki/COVID-19

Authors
-------
  Jesse Phillips <james@jamesphillipsuk.com>

"""
import nltk # Natural Language Processing Toolkit
import urllib.request # Python Website Crawler
from bs4 import BeautifulSoup # Python HTML Disassembler
import string # String lib - used to remove punctuation
# nltk.download() # Open NLTK package Downloader
def main():
  """
  Entrypoint: runs the test.
  
  This runs NLTK's word tokenisation on a piece of natural language, and plots the resultant frequency data of words in the source material.
  The source material for this is the Wikipedia article on COVID-19 in Welsh.
  """
  # get the page from the URL
  response = urllib.request.urlopen(urllib.request.Request(url='https://cy.wikipedia.org/wiki/COVID-19', headers={'User-Agent': 'Mozilla/5.0'}))
  soup = BeautifulSoup(response.read(), 'html5lib') # parse it as HTML

  # strip the contents of head, script, or style tags.
  for erroneousData in soup(["head", "script", "style"]):
    erroneousData.extract()

  text = soup.get_text(strip = True) # Get the text from the HTML
  tokens = nltk.tokenize.word_tokenize(text) # Tokenise the text
  # Strip out punctuation tokens
  tokItems = ["".join(j.lower() for j in i if j not in string.punctuation)
    for i in tokens]

  freq = nltk.FreqDist(tokItems) # Build the frequency data
  for key, value in freq.items():
    print(str(key) + ':' + str(value))
  freq.plot(cumulative=False) # Plot a frequency graph

if __name__ == "__main__":
  main()
