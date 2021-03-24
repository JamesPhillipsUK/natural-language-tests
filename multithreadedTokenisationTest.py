# Experiment in multithreading to increase efficiency of word tokenisation.                   #
# Sample Data used: The King James Version of the Bible, courtesy of Project Gutenberg.       #
#                   The Complete Works of William Shakespeare, courtesy of Project Gutenberg. #
#                   HG Wells: The Time Machine, courtesy of Project Gutenberg.                #
#                   Victor Hugo: Les Miserables, courtesy of Project Gutenberg.               #

import nltk # Natural Language Processing Toolkit
import urllib.request # Python Website Crawler
import time # time library
import string # String lib - used to remove punctuation
import multiprocessing # multithreading

# nltk.download() # Open NLTK package Downloader

def tokeniseText(text):
  '''
  This method, given a text string containing words, will attempt to tokenise it using NLTK.
  
  Parameters
  ----------
  text: string
    The text to tokenise.
    
  Returns
  -------
  list
    The list of tokenised words.
  '''
  tokens = nltk.tokenize.word_tokenize(text) # Tokenise the text
  # Strip out punctuation tokens
  tokItems = ["".join(j.lower() for j in i if j not in string.punctuation)
    for i in tokens]
  return tokItems

def buildFrequencyDistributionData(tokItems):
  '''
  This method, given a list of "word" data and corresponding frequencies, will plot a frequency graph of it using NLTK.
  
  Parameters
  ----------
  tokItems: list
    The words and their respective frequencies.
    
  Returns
  -------
  FreqDist
    The frequency distribution plot.
  '''
  freq = nltk.FreqDist(tokItems) # Build the frequency data
  # TODO: Draw the graphs overlapping.
  return freq

def pullText():
  '''
  This method uses urllib to pull the test data from Project Gutenberg's online repository.
    
  Returns
  -------
  list
    A list of all of the data from Project Gutenberg in string format.  We load all this straight into memory to save the overhead of grabbing it later.
  '''
  kJV = urllib.request.urlopen(urllib.request.Request(url='https://www.gutenberg.org/files/10/10-0.txt', headers={'User-Agent': 'Mozilla/5.0'})) # get the text from the URL
  worksOfShakespeare = urllib.request.urlopen(urllib.request.Request(url='https://www.gutenberg.org/files/100/100-0.txt', headers={'User-Agent': 'Mozilla/5.0'}))
  theTimeMachine = urllib.request.urlopen(urllib.request.Request(url='https://www.gutenberg.org/files/35/35-0.txt', headers={'User-Agent': 'Mozilla/5.0'}))
  lesMis = urllib.request.urlopen(urllib.request.Request(url='https://www.gutenberg.org/files/135/135-0.txt', headers={'User-Agent': 'Mozilla/5.0'}))
  return [str(kJV.read()),str(worksOfShakespeare.read()),str(theTimeMachine.read()),str(lesMis.read())]
  
def runTests(sampleData):
  '''
  This method times and runs the two tests: tokenisation and frequency distribution.
  
  Parameters
  ----------
  sampleData: string
    The test data to run the tests on.
  '''
  startTime = time.time()
  tokenisedItems = tokeniseText(sampleData)
  print ("  Tokenisation time: \t", time.time() - startTime)
  startTime = time.time()
  freq = buildFrequencyDistributionData(tokenisedItems)
  print ("  Frequency Distribution time: \t", time.time() - startTime)
#  freq.plot(500, cumulative=False) # Plot a frequency graph (first 500 words)

def main():
  '''
  Entrypoint: gets the data then runs the tests.
  
  This runs the tests on a single thread, supervised by Python's GIL, then across the whole CPU using the multiprocessing library.
  '''
  sampleData = pullKJVText()
  print ("Single-threaded: ")
  startTime = time.time()
  for text in sampleData:
    runTests(text)
  print ("Total single-threaded time: \t", time.time() - startTime)
  
  print ("Multithreaded: ")
  startTime = time.time()
  with multiprocessing.Pool() as pool:
    pool.map(runTests, sampleData)
  print ("Total multithreaded time: \t", time.time() - startTime)

if __name__ == "__main__":
  main()
