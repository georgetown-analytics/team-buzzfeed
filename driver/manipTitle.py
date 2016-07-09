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
from nltk import Text
from nltk import word_tokenize

##########################################################################
## Module Variables/Constants
##########################################################################

#coded to my [Josh's] file structure where all my dummy files are located
dataList = glob.glob('./tests/data/*.txt') #generates a list of all .txt files in the given directory
# initializing nested dictionary that will house all titles and instance counts
masterDic = {'us': {'':0}, 'ca': {'':0}, 'uk': {'':0}, 'in': {'':0}, 'au': {'':0}}
#coded to my [Josh's] file structure
corpusPath = './tests/corpora/'

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

    for item in jsonfile['buzzes']:
        title_list.append(item['title']) # grabbing all the titles we can find

    return title_list # it's important to share our findings

def file_iterator(country, dataNames): # this one's working!
    """
    Uses a janky loop to iterate over files and uses grab_titles() to
    generate a dictionary (with title lists) based on the country you entered.
    Feeds into genCorpus() nicely.
    """
    if country in masterDic: #quick check to make sure we've got an actual country code to work with
        for doc in dataNames: #for loop iterates over all files in dirPath list
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
        print('You\'ve got to specify an actual country code. Hint: only two characters, lower case')

def twoWeeks(country, dataNames): #might not be working correctly...lists seem to be identical regardless of country
    """
    Lists the titles that were trending for approx. two weeks
    """
    file_iterator(country, dataNames) #grabbing titles and number of hours trending
    i = 1 # there's probably a better way to show list numbers...
    for thing in masterDic[country]: #read the title dictionary
        if masterDic[country][thing] >= 336: #only titles that are in at least 2 weeks worth of API pulls
            print(str(i) + '. ' + str(thing) + ': ' + str(masterDic[country][thing]))
            i += 1
        else:
            continue

def genCorpus(country, dirPath, dataNames): #currently spitting out same corpus regardless of country
    """
    Takes all titles from file_iterator's dictionary data and dumps them
    into a single .txt file based on the country you enter. Thus,
    giving you a country-specific corpus.
    """
    # use inputs to generate a new file name & path
    new_filename = str(country) + 'TitleCorpus' #generate a corpus title based on which country was entered
    path = os.path.join(dirPath, '{}.txt'.format(new_filename))
    #use other functions to generate a dictionary with titles
    file_iterator(country, dataNames) #files the MasterDict for the given country
    with open(path, 'w') as f:  #writes each title in a .txt file with a line break
        for item in masterDic[country]:
            f.write(item + '\n\r')

def monsterCorpus(dirPath, dataNames): #working but doesn't perform optimally, probably because it's a huge f'in list
    """
    Uses the masterDic's keys in combo with genCorpus() to creat a corpus with every
    title ever in the data you've provided.
    """
    path = os.path.join(dirPath, '{}.txt'.format('compiledCorpus'))
    #populate the dictionary that has all titles and occurences
    for country in masterDic:
        file_iterator(country, dataNames)
    #write all of the titles into a single text file
    with open(path, 'w') as f:
        for title in masterDic[country]:
            f.write(title + '\n\r')

def articleType(): # not sure if this is relevant/needed anymore
    """
    Guesses the article type based on the contents of the title
    """
    pass

def nltkPrep(corpName, dirPath):
    """
    Preps a text file for nltk analysis. Enter corpName without the .txt at
    the end.
    """
    filename = '{}.txt'.format(str(corpName)) # adding extension to filename I'll add conditionality later
    grabFile = os.path.join(dirPath, filename) # specifying where the file is
    # open file
    fo = open(grabFile, 'r')
    rawtxt = str(fo.read())
    response = word_tokenize(rawtxt)
    print(len(response))

def lexicalDiversity(corpName, dirPath):
    """
    Takes a corpus in the form of a .txt and computes number of unique words
    divided by total words
    """
    # nltkPrep(corpName, dirPath)
    pass

def main():
    """
    Runs the manipTitle program as its creator intended it to be run!
    """
    # currently only using for testing functions -> not quite sure
    # what the actual program should do
    nltkPrep('compiledCorpus', corpusPath)
    # test = input('gimme a country:')
    # genCorpus(test, corpusPath, dataList)
    # twoWeeks(test, dataList)

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()