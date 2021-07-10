"""
stem.py

Testing stemming methods with multiple large texts.

Sample Data used: The King James Version of the Bible, courtesy of Project Gutenberg.
                  The Complete Works of William Shakespeare, courtesy of Project Gutenberg.
                  HG Wells: The Time Machine, courtesy of Project Gutenberg.
                  Victor Hugo: Les Miserables, courtesy of Project Gutenberg.

Authors
-------
  Jesse Phillips <james@jamesphillipsuk.com>

"""

import nltk # Natural Language Processing Toolkit
import urllib.request # Python Website Crawler
import time # time library
import multiprocessing # multithreading

# nltk.download() # Open NLTK package Downloader

def stemText(text, method):
  stemmedText = []
  import string
  noPunctuationText = text.translate(str.maketrans({a:None for a in string.punctuation})) # Strip punctuation
  tokenisedText = nltk.word_tokenize(noPunctuationText)
  #Strip any stopwords
  from nltk.corpus import stopwords
  stopWords = set(stopwords.words('english'))
  unstoppedTokens = []
  for word in tokenisedText:
    if word not in stopWords and word.lower not in stopWords:
      unstoppedTokens.append(word)
  
  if method == "snowball": # stem using Snowball stemmer
    from nltk.stem import SnowballStemmer
    stemmer = SnowballStemmer("english")
  else: # stem using Porter stemmer
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()
  
  for word in unstoppedTokens:
    stemmedText.append(stemmer.stem(word))

  return stemmedText

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
  This method uses urllib to pull the test data from Project Gutenberg's online repository.
    
  Returns
  -------
  list
    A list of all of the data from Project Gutenberg in string format.  We load all this straight into memory to save the overhead of grabbing it later.
  """
  kJV = urllib.request.urlopen(urllib.request.Request(url='https://www.gutenberg.org/files/10/10-0.txt', headers={'User-Agent': 'Mozilla/5.0'})) # get the text from the URL
  worksOfShakespeare = urllib.request.urlopen(urllib.request.Request(url='https://www.gutenberg.org/files/100/100-0.txt', headers={'User-Agent': 'Mozilla/5.0'}))
  theTimeMachine = urllib.request.urlopen(urllib.request.Request(url='https://www.gutenberg.org/files/35/35-0.txt', headers={'User-Agent': 'Mozilla/5.0'}))
  lesMis = urllib.request.urlopen(urllib.request.Request(url='https://www.gutenberg.org/files/135/135-0.txt', headers={'User-Agent': 'Mozilla/5.0'}))
  return [str(kJV.read()),str(worksOfShakespeare.read()),str(theTimeMachine.read()),str(lesMis.read())]
  
def runTests(sampleData):
  """
  This method times and runs the two tests: tokenisation and frequency distribution.
  
  Parameters
  ----------
  sampleData: string
    The test data to run the tests on.
  """
  import matplotlib.pyplot as plt
  plt.ion()

  startTime = time.time()
  stemmedText = stemText(sampleData, "snowball")
  print ("  Snowball Stemming time: \t", time.time() - startTime)
  startTime = time.time()
  freq = buildFrequencyDistributionData(stemmedText)
  print ("  Frequency Distribution time: \t", time.time() - startTime)
  print ("  Frequency distribution graph of the top 100 word stems:")
  title = "Stem of: " + sampleData.split("\\r")[0].split("Gutenberg eBook of ")[1]
  freq.plot(100, cumulative=False, title=title) # Plot a frequency graph (first 100 words)
  #freq.tabulate(100, cumulative=False, title=title)
  
  startTime = time.time()
  stemmedText = stemText(sampleData, "porter")
  print ("  Porter Stemming time: \t", time.time() - startTime)
  startTime = time.time()
  freq = buildFrequencyDistributionData(stemmedText)
  print ("  Frequency Distribution time: \t", time.time() - startTime)
  print ("  Frequency distribution graph of the top 100 word stems:")
  freq.plot(100, cumulative=False) # Plot a frequency graph (first 100 words)
  #freq.tabulate(100, cumulative=False, title=title)

  plt.ioff()
  plt.show()

def main():
  """
  Entrypoint: gets the data then runs the tests.
  
  This runs the tests on a single thread, supervised by Python's GIL, then across the whole CPU using the multiprocessing library.
  """
  sampleData = pullText()
  print ("Running.  This may take a while: ")
  with multiprocessing.Pool() as pool:
    pool.map(runTests, sampleData)

if __name__ == "__main__":
  main()
