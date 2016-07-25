#!/usr/bin/env python3
"""
Takes seed words and a test file as input and returns a title based
on most probable word to follow.

Ripped off key bits of code from Esdal Maijer with <3
https://github.com/esdalmaijer/markovbot/blob/master/markovbot/markovbot.py
"""

##########################################################################
## Imports
##########################################################################

import os
from nltk import word_tokenize
import random

##########################################################################
## Module Variables/Constants
##########################################################################

corpusPath = './tests/corpora/'

##########################################################################
## Class
##########################################################################
#
# THIS MAY BE A MORE EFFICIENT SOLUTION BUT WILL REQUIRE SIGNIFICANT WORK
#class markovEngine():
#    """
#    Class to generate a random title with a Markov chain based on the input.
#    Length is also determined by the variance in title length from the given
#    title corpus.
#    """

#    def __init__(self):
#        """
#        Initialize the engine.
#        """
#        self.data = {'default':{}}

#    def generateText(self, maxlength, seedword=None, database='default', verbose=False, maxtries=10):
#        """
#        Generates random text based on the provided database and defined maxlength.
#        Returns a Title.
#        """
        # Spit out error if no data available
#        if self.data == {}:
#            self._error('generate text', "There's nothing in ''%s'...Did you feed me any titles yet?" % (database))
#
        # Some minor voodoo that I stole without understanding
#        error = True
#        attempts = 0

        # Make keyword string into list of keywords
#        if type(seedword) in [str, unicode]:
#            seedword = [seedword]

#        while error:
#            try:

#            except:
#                attempts += 1
#                if verbose:
#                    self._message('generate message', "Ran into a bit")


##########################################################################
## Functions
##########################################################################

def nltkPrep(corpName, dirPath):
    """
    Takes the name of the file and it's directory path as inputs, and makes a
    raw text file ready for nltk analysis.
    """
    if corpName[-4:] == '.txt':  #looking at the file type
        print('Thank you for entering a valid file type ' + '(' + str(corpName[-4:]) + ')')
    else:
        corpName = '{}.txt'.format(str(corpName)) # adding extension to filename, in case it wasn't included

    grabFile = os.path.join(dirPath, corpName) # specifying where the file is
    specs = open(grabFile, 'r') # open file
    rawtxt = str(specs.read()) # looking at the file
    toke = word_tokenize(rawtxt) #tokenizing the file
    cleanText = nltk.Text(toke) # the file is now stored in memory as an nltk ready file (may cause performance issues)
    return cleanText

def generateText(maxlength, seedword=None, corpus, filepath, verbose=False, ):
    """
    Takes seedword inputs and a length, and uses bigram analysis of a given
    corpus to respond with a randomly generated text (markove chain)
    """
    text = ntlkPrep(corpus, filepath)

    if seedword == None:
        seedword = random.choice(text)

    # converting user inputs to list of words (in case there are multiple words)
    inputs = seedword.split()
    

def main():
    # do something, maybe?

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
