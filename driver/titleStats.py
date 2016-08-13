#!/usr/bin/env python3
"""
Analyzing the persistence of titles of buzzes pulled from the 5 English BuzzFeed APIs.
Data was pulled hourly beginning on May 18, 2016. Data is kept in a PostgreSQL instance
and queried using the psycopg2 module.
"""

##########################################################################
## Imports
##########################################################################

import os



##########################################################################
## Module Variables/Constants
##########################################################################

corpus_dir = '../tests/corpora/'


##########################################################################
## Functions
##########################################################################

def avg_title_leng(corpusname):
    """
    Reads a title corpus seperated by line breaks and calculates the title length
    """
    # Locate the file within the directory
    path = os.path.join(corpus_dir, corpusname)
    # Read the words from the file as one big string
    #with open(path, 'r') as f:
        # read the contents of the file
    corp_peak = open(path, 'r')

    # Initializing basic variables for computing averages
    count = 0
    tot = 0

    for row in corp_peak:
        if len(row) > 1:
            x = len(row)
            tot += x
            count += 1
        else:
            continue
    avg_leng = tot / count
    return "%.2f" % avg_leng # flare just to make sure we don't overwhelm with too many figures after the decimal

def main():
    # not very DRY way to get average
    uk = avg_title_leng('ukTitleCorpus.txt')
    print('The average title length in the UK is: %s characters.' % str(uk))
    us = avg_title_leng('usTitleCorpus.txt')
    print('The average title length in the US is: %s characters.' % str(us))
    ca = avg_title_leng('caTitleCorpus.txt')
    print('The average title length in Canda is: %s characters.' % str(ca))
    ind = avg_title_leng('inTitleCorpus.txt')
    print('The average title length in India is: %s characters.' % str(ind))
    au = avg_title_leng('auTitleCorpus.txt')
    print('The average title length in Australia is: %s characters.' % str(au))


##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
