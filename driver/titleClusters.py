#!/usr/bin/env python3
"""
Analyzing the titles of buzzes pulled from the 5 English BuzzFeed APIs.
Data was pulled hourly beginning on May 18, 2016.
"""

##########################################################################
## Imports
##########################################################################

import os
import json

##########################################################################
## Module Variables/Constants
##########################################################################

Path = os.path.join('/tests/data')

##########################################################################
## Functions
##########################################################################
def buzz_list():
    """
    Finds all buzzes in the provided folder and loads them into a json format
    """
    titleList = [] #list where I'll dump all the titles
    for article in Path:
        formatted = json.loads(article)
        buzz = formatted['buzzes']
        print(titleList)
        return titleList.append(buzz['title'])

def genCorpus():
    """
    Takes all titles from available data and dumps them into a single .txt
    file to be used as a corpus.
    """
    messTitles = buzz_list()
    for title in messTitles:
        with open(filepath, 'w') as f:
            f.write(buzzes['title'], '\n')

def articleType():
    """
    Guesses the article type based on the contents of the title
    """
    pass

def lexicalDiversity():
    """Takes a corpus and computes number of unique words
    divided by total words"""
    pass

def main():
    buzz_list()

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
