"""
taggingAndFindingSimilarWords.py

Part Of Speech (POS) tagging multiple texts.

Sample Data used: HG Wells: The Time Machine, courtesy of Project Gutenberg.
                  Victor Hugo: Les Miserables, courtesy of Project Gutenberg.

Authors
-------
  Jesse Phillips <james@jamesphillipsuk.com>

"""

import nltk # Natural Language Processing Toolkit
import urllib # Python Website Crawler
import time # time library
import string # String lib - used to remove punctuation
import multiprocessing # multithreading

# nltk.download() # Open NLTK package Downloader

def pOSTagText(text):
  """
  This method, given a text string containing words, will attempt to POS-tag those words using NLTK.
  
  Parameters
  ----------
  text: string
    The text to tag.
    
  Returns
  -------
  list
    The list of tagged words.
  """
  tokens = nltk.tokenize.word_tokenize(text) # Tokenise the text
  # Strip out punctuation tokens
  taggedWords = nltk.pos_tag(tokens)
  return taggedWords

def findSimilarWords(corporaString):
  wordSimilarityTuples = []
  corporaStringArr = nltk.word_tokenize(corporaString)
  corpora = nltk.Text(nltk.word_tokenize(corporaString))
  for word in corporaStringArr:
    print(word.lower())
    similarWords = corpora.similar(word.lower())
    if isinstance(similarWords, str):
      print(word.lower() + " is similar to: " + corpora.similar(word.lower()))
      similarWords = corpora.similar(word.lower()) # find words similar to the word
      wordSimilarityTuples.append((word, similarWords)) # prepare a tuple of the word and the similar ones
  # add all of those to a file
  print ("  Setting filepath.")
  filepath = "Similar Words in " + corporaString.split("\r")[0].split("Book of ")[1] + time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime()) + "GMT.txt"
  print ("  Writing file.")
  filePointer = open(filepath, "w")
  for data in wordSimilarityTuples:
    filePointer.write(data[0] + "/" + data[1] + "\n")
  print ("  Written!")
  filePointer.close()
  #
  pass

def pullText():
  """
  This method uses urllib to pull the test data from Project Gutenberg's online repository.
    
  Returns
  -------
  list
    A list of all of the data from Project Gutenberg in string format.  We load all this straight into memory to save the overhead of grabbing it later.
  """
  theTimeMachine = urllib.request.urlopen(urllib.request.Request(url='https://www.gutenberg.org/files/35/35-0.txt', headers={'User-Agent': 'Mozilla/5.0'}))
  lesMis = urllib.request.urlopen(urllib.request.Request(url='https://www.gutenberg.org/files/135/135-0.txt', headers={'User-Agent': 'Mozilla/5.0'}))
  return [str(theTimeMachine.read().decode('utf8')),str(lesMis.read().decode('utf8'))]

def runTests(sampleData):
  """
  This method times and runs the two tests: tokenisation and frequency distribution.
  
  Parameters
  ----------
  sampleData: string
    The test data to run the tests on.
  """
  print ("  Beginning test:")
  startTime = time.time()
  taggedText = pOSTagText(sampleData)
  print ("  POS Tagging time: \t", time.time() - startTime)
  print ("  Setting filepath.")
  filepath = "POS Tagged " + sampleData.split("\r")[0].split("Book of ")[1] + time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime()) + "GMT.txt"
  print ("  Writing file.")
  filePointer = open(filepath, "w")
  for data in taggedText:
    filePointer.write(data[0] + "/" + data[1] + "\n")
  print ("  Written!")
  filePointer.close()
  findSimilarWords(sampleData)

def main():
  """
  Entrypoint: gets the data then runs the tests.
  
  This runs the tests across the whole CPU using the multiprocessing library.
  """
  sampleData = pullText()
  startTime = time.time()
  with multiprocessing.Pool() as pool:
    pool.map(runTests, sampleData)
  print ("Total multithreaded time: \t", time.time() - startTime)

if __name__ == "__main__":
  main()
