"""
cSourceCodeTokenisationTest.py

Testing various methods of tokenisation on C source code.

Sample Data used: exampleText.c - a C17 program.

Authors
-------
  Jesse Phillips <james@jamesphillipsuk.com>

"""

import nltk # Natural Language Processing Toolkit
import string # String lib - used to remove punctuation
from nltk.text import Text # Text class - methods for parsing a text.

# nltk.download() # Open NLTK package Downloader

def lexer(text):
  """
  This method, given a string of language (C, in thic case), will perform natural language lexical analysis on it, and use that to tokenise the string.
  
  Parameters
  ----------
  text: string
    The string of language.
    
  Returns
  -------
  list
    The list of tokens.
  """
  # TODO: build lexical analyser
  # SEE: https://github.com/gcc-mirror/gcc/blob/master/libcpp/lex.c
  # SEE: https://gcc.gnu.org/onlinedocs/cppinternals/Lexer.html
  textList = text.split(" ")
  textList = [y  for x in textList for y in x.split('\n')]
  textList = [y  for x in textList for y in x.split('{')]
  textList = [y  for x in textList for y in x.split('}')]
  return textList

def tokeniseText(text, method):
  """
  This method, given a text string containing words, will attempt to tokenise it using the method provided.
  
  Parameters
  ----------
  text: string
    The text to tokenise.
  method: string
    The method by which to tokenise the text (word_native, word_naive_with_spaces, lexical_analysis).
    
  Returns
  -------
  list
    The list of tokenised words.
  """
  tokItems = []
  if (method == "word_native"):
    tokens = nltk.tokenize.word_tokenize(text) # Tokenise the text
    # Strip out punctuation tokens
    tokItems = ["".join(j.lower() for j in i if j not in string.punctuation)
      for i in tokens]
  elif (method == "word_naive_with_spaces"):
    tokItems = text.split(" ")
  elif (method == "lexical_analysis"):
    tokItems = lexer(text)
    
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
  # Run tests using NLTK's native word tokenisation.
  tokenisedItems = tokeniseText(sampleData, "word_native")
  freq = buildFrequencyDistributionData(tokenisedItems)
  freq.plot(50, cumulative=False) # Plot a frequency graph (first 50 words)
  print("Finding concordance data for word-tokeinsed C")
  dataText = Text(tokenisedItems)
  print("Finding \"include\"")
  dataText.concordance("include")
  print("Finding \"#include\"")
  dataText.concordance("#include")

  # Run tests using a naive method of tokenisation with spaces.
  tokenisedItems = tokeniseText(sampleData, "word_naive_with_spaces")
  print("Finding concordance data for naively-tokenised C")
  dataText = Text(tokenisedItems)
  print("Finding \"include\"")
  dataText.concordance("include")
  print("Finding \"#include\"")
  dataText.concordance("#include")

  # Run tests using custom lexical analysis.
  tokenisedItems = tokeniseText(sampleData, "lexical_analysis")
  print("Finding concordance data for lexical-analysis-tokenised C")
  dataText = Text(tokenisedItems)
  print("Finding \"include\"")
  dataText.concordance("include")
  print("Finding \"#include\"")
  dataText.concordance("#include")

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
