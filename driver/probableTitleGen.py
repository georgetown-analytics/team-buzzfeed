#!/usr/bin/env python3
"""
Takes a corpus of raw text as input and calculates comprehensive Markov
probabilities. Which then feeds into a function that solicits a seed word and a
'sentence length' parameter in order to generate probabilistic text
"""

##########################################################################
## Imports
##########################################################################

import os
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.collocations import *

##########################################################################
## Functions
##########################################################################

def avg_title_len(corpName, corpPath=None): # Not a necessary part of the title generator pipeline, but helped inform the default value
    """
    Takes a raw text, title corpus as input and returns the average title length
    (in words)
    """
    # Defining path where the file is, based on inputs
    if corpPath != None:
        path = os.path.join(corpPath, corpName)
    else:
        path = corpName

    with open(path, 'r') as f:
        text = f.readlines()

    # initializing the variables that will be used to calculate the average
    total_len = 0
    n_titles = 0

    # Read every actual title in the corpus
    for row in text:
        if len(row) > 1:
            words = row.split()
            word_len = len(words)
            total_len += word_len
            n_titles += 1
        else:
            continue

    avg_len = int(total_len / n_titles)
    return avg_len

def nltkPrep(corpName, dirPath=None): # Step 1
    """
    Takes the name of the file and it's directory path as inputs, and tokenizes
    it for use with nltk modules.
    """
    if dirPath != None:
        path = os.path.join(dirPath, corpName)
    else:
        path = corpName

    with open(path, 'r') as f:
        text = f.readlines()

    # initialize the list that we'll use to hold all the titles in the given corpus
    title_list = []

    for row in text:
        if len(row) > 1:
            title_list.append(row[:-1])
        else:
            continue

    # Make the list a string, because that's how NLTK likes it
    title_list = str(title_list)
    # Tokenize the string and spit back an NLTK ready object
    tokens = word_tokenize(title_list)
    clean_text = nltk.Text(tokens)
    return clean_text


def generate_title(seedword, text, length=10):
    """
    Takes an NLTK-prepped text and uses it to analyze trigrams and their associated
    frequencies.

    This analysis is then used to generate a plausible title, based on a provided
    seedword and a specified title length.

    Solving this problem required heavy reliance on this StackOverflow post:
    http://stackoverflow.com/questions/21165702/nltk-collocations-for-specific-words
    """
    # prepare for the title!
    seedword = str(seedword)
    word_list = [seedword]

    # initializing the measurment tool from NLTK
    metrics = nltk.collocations.TrigramAssocMeasures()

    # initializing a finder (similar to a cursor object with psycopg)
    finder = TrigramCollocationFinder.from_words(text)

    # Going to use a while loop to grab all likely words until we have a title
    # of sufficient length
    while len(word_list) <= length:
        # Make sure we're reloading the trigrams after every append
        # finder = TrigramCollocationFinder.from_words(text)
        print(seedword) # Just trying to see what's my problem is, looks like punctuation...

        # this will be used to filter trigram data based on the provided seedword
        word_filter = lambda *w: seedword not in w
        # here's where it gets tricky, find the most common ngram using the seedword
        filter_apply = finder
        # using a NLTK's likelihood ratio calculator, find the most likely trigram for the seedword
        best_trigram = filter_apply.nbest(metrics.likelihood_ratio, 1)
        # find the seedword in the best tuple
        winner = best_trigram[0]
        seedword_index = winner.index(seedword) # << current source of frustration

        # use the returned index to grab the next word and append it to the word list
        if seedword_index < 2 and seedword.isalpha():
            seedword_index += 1
            seedword = best_trigram[seedword_index]# use most recent word as new seedword
            word_list.append(seedword) # append new word to our list
        else:
            #seedword = best_trigram[seedword_index]
            #word_list.append(seedword)
            continue # don't use any trigrams in which the seedword is the last instance

    buzz_title = '' # preparing for our final title
    for word in word_list:
        buzz_title += word + ' '

    # Now make it pretty
    buzz_title = buzz_title[:-1]
    return buzz_title.title()

def main():
    # do something, maybe?
    nu_word = input('Please enter a seed word for the title generator: ')
    clean_text = nltkPrep('usTitleCorpus.txt', '/Users/josh.erb/repos/feed-the-buzz/tests/corpora')
    output = generate_title(nu_word, clean_text)
    print(output)

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
