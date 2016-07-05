#!/usr/bin/env python3
"""
Analyzing the titles of buzzes pulled from the 5 English BuzzFeed APIs.
Data was pulled hourly beginning on May 18, 2016.
"""

##########################################################################
## Imports
##########################################################################

from loadbuzz import BuzzRec
import os
import nltk
import gensim

##########################################################################
## Module Variables/Constants
##########################################################################

Path = ''

##########################################################################
## Functions
##########################################################################
def fetch_buzzes():
    for article in

def genCorpus():
    """
    Takes all titles from available data and dumps them into a single .txt
    file to be used as a corpus.
    """
    Buzzes = fetch_buzzes()
    for title in Buzzes:
        path = os.path.join('../tests/data', '{}.json'.format(article))
        with open(path, 'w') as f:
            f.write(buzzes['title'], '\n')

def articleType():
    """
    Guesses the article type based on the contents of the title
    """
    pass

def lexicalDiversity():
    """Takes a corpus and computes number of unique words
    divided by total words"""
    ## by the total number of words for all titles.

def main():
    for buzz in

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
