#!/usr/bin/env python3
"""
Analyzing the titles of buzzes pulled from the 5 English BuzzFeed APIs.
Data was pulled hourly beginning on May 18, 2016.
"""

##########################################################################
## Imports
##########################################################################

import os
import glob
import json
import requests

##########################################################################
## Module Variables/Constants
##########################################################################

dataPath = glob.glob('./tests/data/*.txt')

##########################################################################
## Functions
##########################################################################
def grab_titles(filename): # this one's functioning properly!
    """
    Grabs all the buzzes' titles in the provided json file and loads them into a list
    """
    title_list = [] #initializing an empty list where the titles will go
    f = open(str(filename), 'r') #opening the file
    jsonfile = json.loads(f.read()) #taking a peak inside and assuming we can understand it as a json

    for item in jsonfile['buzzes']: #only looking at the article level
        if item['title'] in title_list: #don't want no repeats
            continue
        else:
            title_list.append(item['title']) #if it's a unique title, let's add it to our list!

    return title_list

def file_iterator():
    """
    Uses a janky while loop to iterate over files and uses grab_titles() to
    generate a dictionary organized by country
    """
    pass

def genCorpus(country):
    """
    Takes all titles from file_iterator's dictionary data and dumps them
    into a single .txt file based on the country you enter.
    Giving you a country-specific corpus.
    """
    pass

def articleType():
    """
    Guesses the article type based on the contents of the title
    """
    pass

def lexicalDiversity(corpus):
    """Takes a corpus and computes number of unique words
    divided by total words"""
    pass

def main():
    grab_titles(dataPath[5099]) # just running a simple test here

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
