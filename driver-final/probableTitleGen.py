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
from random import randint
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

def clean_list(a_list):
    """
    Apparently the only way to drop all of the unwanted characters
    """
    # I don't want these in my title
    undesirables = [',', '``', '`', ' `', '` ', "'", '"', '""', "''", '/', '{', '}', '(', ')', '[', ']']
    new_list = [x for x in a_list if x not in undesirables]
    return new_list

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
            title_list.append(str(row[:-1]))
        else:
            continue
    # tell the user how many titles we've looked at
    print('We analyzed {} unique titles!'.format(len(title_list)))

    # Make the list a string, because that's how NLTK likes it
    title_list = str(title_list)
    # Tokenize the string and spit back an NLTK ready object
    tokens = nltk.word_tokenize(title_list)
    tokens = clean_list(tokens)
    clean_text = nltk.Text(tokens)
    return clean_text

def list_tup_iter(trigram_list, seedword):
    """
    Meant to find the first instance in a word in a list of tuples and return
    the subsequent word in the tuple.
    """
    trigram_list = clean_list(trigram_list)

    for tup in trigram_list:
        for word in tup:
            if word == seedword and tup.index(word) != 2:
                ind = tup.index(seedword) + 1
                new_seedword = tup[ind] #grab the subsequent word
                break
            else:
                continue
    # hand the word back to whomever called the function
    return new_seedword

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
    seed = str(seedword)
    seed = seed.title()

    if seed not in text: # accounting for possibility that the word isn't in the corpus
        random_index = randint(0, len(text))
        seed = text[random_index]
        word_list = [seed]
    else:
        word_list = [seed] # initialize our list of title words

    # initializing the measurment tool from NLTK
    metrics = nltk.collocations.TrigramAssocMeasures()

    # Going to use a while loop to grab all likely words until we have a title
    # of sufficient length
    while len(word_list) < length:
        # initiate the filter with the seed
        word_filter = lambda *w: seed not in w
        # grab a coopy of the trigram list
        finder_fltr = TrigramCollocationFinder.from_words(text)
        # apply the word filter
        finder_fltr.apply_ngram_filter(word_filter)
        # find the best five trigrams
        best_trigram = finder_fltr.nbest(metrics.likelihood_ratio, 5)
        # grab one of these trigrams at random
        winner = best_trigram[randint(0, 3)]
        # what's our seed's index?
        seed_index = winner.index(seed)
        # make sure there's something there to grab
        if seed_index < 2:
            new_word = winner[int(seed_index + 1)] # << Every so often this is going to thrown an error... how do I mitigate?
            word_list.append(new_word)
        else:
            new_word = winner[int(seed_index - 1)]
            word_list.append(new_word)

        # Replace old-seed with the new one!
        seed = new_word

    buzz_title = '' # preparing for our final title
    for word in word_list:
        buzz_title += word + ' '

    # Now make it pretty
    buzz_title = buzz_title[:-1]
    return buzz_title

def main():
    # solicit a seed from the user
    seed = input('Please enter a seed word for the title generator: ')
    # clean up a corpus
    clean_text = nltkPrep('usTitleCorpus.txt', '/Users/josh.erb/repos/feed-the-buzz/tests/corpora')
    # use the provided seed and the cleaned up corpus to generate a title
    output = generate_title(seed, clean_text)
    # show me what that title is
    print(output)

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
