#!/usr/bin/env python3
"""
Analyzing the persistence of titles of buzzes pulled from the 5 English BuzzFeed APIs.
Data was pulled hourly beginning on May 18, 2016. Data is kept in a PostgreSQL instance
and queried using the psycopg2 module.
"""

##########################################################################
## Imports
##########################################################################

import psycopg2


##########################################################################
## Module Variables/Constants
##########################################################################

conn = psycopg2.connect("dbname=buzzfood user=josh.erb") #coded to my [Josh's] Postgres instance
cur = conn.cursor()

##########################################################################
## Functions
##########################################################################

def main():

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
