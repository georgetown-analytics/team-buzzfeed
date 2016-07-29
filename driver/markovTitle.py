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
import random
from nltk import word_tokenize

##########################################################################
## Module Variables/Constants
##########################################################################

corpus_dir = './tests/corpora/'
filename = ''

##########################################################################
## Markov Engine Class
##########################################################################

class MarkovEngine():
    """
    Class to generate text with a Markov chain, based on inputs of a corpus,
    seed word(s), and desired length.
    """

    def __init__(self):
        """
        Turns on the engine.
        """
        # carving out some space for the data
        self.data = {'default':{}}
        # key inputs
        self.keywords = None
        self.prefix = None
        self.suffix = None

    def clear_data(self, database=None):
        """
        Makes sure we've got a clear internal database for each instance.
        """
        # Overwrite data
        if database == None:
            self.data = {'default':{}}
        else:
            try:
                self.data.pop(database)
            except KeyError:
                self._error('clear_data', "There was no database named '%s'" % (database))

    def generate_title(self, maxlength, seedword=None, database='default', maxtries=100):
        """
        Generates a random title based on the given database and provided inputs.

        Key definitions:
        - seedword = a string or list that indicates what word(s) should be in the sentence
        - database = a string that indicates the name of the database to be used
        - maxtries = amount of times the function is allowed to attempt to generate random text
        """

        # Exception if there's no data in the database
        if self.data[database] == {}:
            self._error('generate_title', "No data is available yet in database '%s'. Have you given your Engine anything to read yet?")

        # If it's a single word, make sure it's in the form of a single item list
        if type(seedword) is str:
            seedword = [seedword]

        # Constants to ensure an actual title is generated
        error = True
        attempts = 0

        while error:
            try:
                # Grab all word duos in the database
                keys = list(self.data[database].keys())
                random.shuffle(keys)

                # Choose a random seed to fall back on when the seedword does
                # not appear in the dictionary
                seed = random.randint(0, len(keys))
                w1, w2 = keys[seed]

                # Find a word duo that contains the seed word
                if seedword != None:
                    #Loop through all potential seedwords
                    while len(seedword) > 0:
                        # Loop through all the keys of words that occured
                        # together in the text
                        for i in range(len(keys)):
                            if seedword[0] in keys[i] or (tuple(seedword[0].split(' ')) == keys[i]):
                                # Choose the words
                                w1, w2 = keys[i]
                                # Get rid of the seedwords
                                seedword = []
                                break
                        if len(seedword) > 0:
                            seedword.pop(0)

                # Empty list to contain the generated words for the title
                title_words = []

                # Loop to get as many words as requested for each title
                for i in range(maxlength):
                    # Add the current word first
                    title_words.append(w1)
                    # Generate a new first and second word based on the database
                    w1, w2 = w2, random.choice(self.data[database][(w1, w2)])
                # Add final word to the sentence
                title_words.append(w2)

                ### Captilize all words in the title
                ### >>> Don't think this is necessary based on title corpus inputs...
                ### for i in range(0, len(title_words)):
                ###    title_words[i] = title_words[i].capitalize()

                # Check if the word might typically be followed by some sort of
                # emphatic punctuation
                emph = 0
                for i in range(len(title_words)-1, 0, -1):
                    # Checks whether the current word ends with relevant
                    # punctuation. If it does, use the current word as the last word.
                    if title_words[i][-1] in ['!', '?']:
                        emph = i + 1
                    else:
                        words[i][-1] = ' '
                    # Break if we found a word with emphatic punctuation
                    if emph > 0:
                        break

                # Cut back to the last word with emphatic punctuation
                title_words = title_words[:emph]

                # Combine the words into a comprehensive title
                title = ' '.join(title_words)

                if title != '':
                    error = False

            except:
                # count one more failed attempt
                attempts += 1
                # if too many errors occur, stop trying
                if attempts >= maxtries:
                    self._error('generate_title', "Made %d attempts to generate text, but all failed." % (attempts))
        return title

    def study_titles(self, filepath, filename, database='default', overwrite=False):
        """
        Reads raw text file, tokenizes it with nltk, and adds stats to the internal data.
        """
        # find the file in the directory
        location = os.path.join(filepath, filename)
        # Clear the current data, if necessary
        if overwrite:
            self.clear_data(database=database)

        if not self._check_file(location):
            self._error('study_titles', "file does not exist: '%s'" % (filename))

        # get the full filepath
        file_loc = os.path.join(filepath, filename) # specifying where the file is
        # Read the words from the file as one big string
        with open(file_loc, 'r') as f:
            # read the contents of the file
            contents = f.read()

        # Split all the words into a list
        words = contents.split()

        # Initialize a new database, if necessary
        if not database in self.data.keys():
            self.data[database] = {}

        # Add words and their likely following words into the database as tuples
        for w1, w2, w3 in self._triples(words):
            # Only use actual words
            if self._isalphapunct(w1) and self._isalphapunct(w2) and \
                self._isalphapunct(w3):
                # dictionary key is a word duo tuple
                key = (w1, w2)
                # see if the key is already part of the dictionary
                if key in self.data[database]:
                    # if it is, add the third word to the list
                    self.data[database][key].append(w3)
                else:
                    # if not, make a new list for it and then add the new word
                    self.data[database][key] = [w3]


    def _check_file(self, filename, allowedext=None):
        """
        Verifys that a file exists, and has a certain extension.
        """
        # does the file exist?
        ok = os.path.isfile(filename)

        # check whether the extension is allowedext
        if allowedext != None:
            name, ext = os.path.splitext(filename)
            if ext not in allowedext:
                ok = False

        return ok

    def _error(self, methodname, msg):
        """
        Raises an Exception on behalf of the responsible method.
        """
        raise Exception("ERROR in Markovbot.%s: %s" % (methodname, msg))

    def _isalphapunct(self, string):
        """
        Returns true if all characters in the given string are alphabetic or punctuation.
        """
        if string.replace('.','').replace(',','').replace(';','').\
            replace(':','').replace('!','').replace('?','').\
            replace("'",'').isalpha():
            return True
        else:
            return False

    def _triples(self, words):
        """
        Moves over the words and returns tuples of three consecutive words at a time.
        """

        if len(words) < 3:
            return

        for i in range(len(words) - 2):
            yield (words[i], words[i+1], words[i+2])

##########################################################################
## Functions
##########################################################################

def start_engine(filepath, country, length=15):
    # initiate the Markov Engine Class
    spit_title = MarkovEngine()

    # Use the given country to determine the filename
    filename = country + 'TitleCorpus.txt'

    # Have the engine read the specified file
    spit_title.study_titles(filepath, filename)

    # Ask user to give inputs
    user_input = str(input('Please enter a word or phrase to generate your title:'))

    # Turn those inputs into a list of keywords
    keywords = user_input

    # Use the given keywords to generate a title
    output = spit_title.generate_title(length, seedword=keywords)
    print(output)

def main():
    user_input = str(input('Which country do you want to generate a title for?'))
    start_engine(corpus_dir, user_input)

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
