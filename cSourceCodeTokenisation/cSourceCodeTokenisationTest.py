"""
cSourceCodeTokenisationTest.py

Testing NLTK's word tokenisation on C source code.

Sample Data used: exampleText.c - a  C17 program.

Authors
-------
  Jesse Phillips <james@jamesphillipsuk.com>

"""

import nltk # Natural Language Processing Toolkit
import string # String lib - used to remove punctuation
from nltk.text import Text # Text class - methods for parsing a text.

# nltk.download() # Open NLTK package Downloader

def tokeniseText(text):
  """
  This method, given a text string containing words, will attempt to tokenise it using NLTK.
  
  Parameters
  ----------
  text: string
    The text to tokenise.
    
  Returns
  -------
  list
    The list of tokenised words.
  """
  tokens = nltk.tokenize.word_tokenize(text) # Tokenise the text
  # Strip out punctuation tokens
  tokItems = ["".join(j.lower() for j in i if j not in string.punctuation)
    for i in tokens]
  return tokItems

def buildFrequencyDistributionData(tokItems):
  """
  This method, given a list of "word" data and corresponding frequencies, will plot a frequency graph of it using NLTK.
  
  Parameters
  ----------
  tokItems: list
    The words and their respective frequencies.
    
  Returns
  -------
  FreqDist
    The frequency distribution plot.
  """
  freq = nltk.FreqDist(tokItems) # Build the frequency data
  return freq

def pullText():
  """
  This method pulls the test Hello World Program source code from the file and formats it as a string.
    
  Returns
  -------
  string
    The example source code.
  """
  with open('cSourceCodeTokenisation/exampleText.c', 'r') as file:
    data = file.read()
  return data
  
def runTests(sampleData):
  """
  This method times and runs the two tests: tokenisation and frequency distribution.
  
  Parameters
  ----------
  sampleData: string
    The test data to run the tests on.
  """
  tokenisedItems = tokeniseText(sampleData)
  freq = buildFrequencyDistributionData(tokenisedItems)
  print("Finding concordance data for word-tokeinsed C")
  dataText = Text(tokenisedItems)
  print("Finding \"include\"")
  dataText.concordance("include")
  print("Finding \"#include\"")
  dataText.concordance("#include")


  print("Finding concordance data for naively-tokenised C")
  dataText = Text(sampleData.split(" "))
  print("Finding \"include\"")
  dataText.concordance("include")
  print("Finding \"#include\"")
  dataText.concordance("#include")
  freq.plot(50, cumulative=False) # Plot a frequency graph (first 50 words)

def main():
  """
  Entrypoint: gets the data then runs the tests.
  
  This runs the tests on a single thread, supervised by Python's GIL, then across the whole CPU using the multiprocessing library.
  """
  sampleData = pullText()
  print ("Tokenising: ")
  runTests(sampleData)

if __name__ == "__main__":
  main()
