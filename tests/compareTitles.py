#!/usr/bin/env python3
"""
Testing ability to query API and look at data
"""

##########################################################################
## Imports
##########################################################################

import requests
import json

##########################################################################
## Module Variables/Constants
##########################################################################

au_url = 'https://www.buzzfeed.com/api/v2/feeds/trending?country=en-au'
ca_url = 'https://www.buzzfeed.com/api/v2/feeds/trending?country=en-ca'

caCall = requests.get(ca_url) #querying Canada trending API
auCall = requests.get(au_url) #querying Australia trending API

##########################################################################
## Functions
##########################################################################


caData = json.loads(caCall.text) # Passing stuff to JSON format
auData = json.loads(auCall.text)

def compareTitles(data1, data2):
    x = 1
    print('FIRST LIST OF TITLES')
    for art in data1['buzzes']:
        print(str(x) + '. ' + art['title'])
        x += 1

    y = 1
    print('SECOND LIST OF TITLES')
    for art in data2['buzzes']:
        print(str(y) + '. ' + art['title'])
        y += 1

def main():
    compareTitles(caData, auData)

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
