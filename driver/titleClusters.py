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
from pprint import pprint

##########################################################################
## Module Variables/Constants
##########################################################################

#where all my dummy files are located
dataPath = glob.glob('./tests/data/*.txt')
# initializing nested dictionary that will house all titles and instance counts
masterDic = {'us': {'':0}, 'ca': {'':0}, 'uk': {'':0}, 'in': {'':0}, 'au': {'':0}}

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

def file_iterator(country, dirPath):
    """
    Uses a janky loop to iterate over files and uses grab_titles() to
    generate a dictionary (with title lists) based on the country you entered.
    Feeds into genCorpus() nicely.
    """
    if country in masterDic: #quick check to make sure we've got an actual country code to work with
        for doc in dirPath: #for loop iterates over all files in dirPath list
            # grab the titles and dump them into a list
            country_titles = grab_titles(doc)
            # Read every title and add any that aren't in masterDic to masterDic
            for item in country_titles: #looks at every title in the list
                #if it's not there, add new title to dictionary
                if item not in masterDic[country]:
                    masterDic[country].update({item: 1})
                #if it is there, add one to the instance ticker
                else:
                    original_val = masterDic[country][item]
                    new_val = original_val + 1
                    masterDic[country].update({item: new_val})
        return masterDic #hands back the populated dictionary for whatever use you see fit. Like generating a title corpus, perhaps?
    else:
        print('You\'ve got to specify an actual country code. Hint: only two characters')

def genCorpus(country):
    """
    Takes all titles from file_iterator's dictionary data and dumps them
    into a single .txt file based on the country you enter.
    Giving you a country-specific corpus.
    """
    # new_filename = str(country) #make sure it's a string
    # (NOTHING TO SEE HERE)
    # with open(new_filename, 'w') as f:
    #   print(STUFF)
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
    test = input("Enter country code:").lower() # just running a simple test here
    file_iterator(test, dataPath)

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
