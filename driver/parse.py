
import urllib2
import json
import datetime
from pprint import pprint
from loadbuzz import BuzzRec

# REMOVE DIRECTORY AND EXTENSION
def get_filename (fname, dirname, extension):
    fname = fname.replace(dirname,"")
    fname = fname.replace(extension,"")
    return fname

# GET COUNTRY CODE FROM FILEMANTE
def get_country(fname):
    return fname[:2]

# GET TIMESTAMP FROM FILENAME
def get_timestamp(fname):
    # TIMESTAMP   YYYY                MM                 DD               HH                MM          SS
    tstmp = fname[2:6] + "-" + fname[6:8] + "-" + fname[8:10] + " " + fname[10:12] + ":" + fname[12:14] + ":00"
    return tstmp

def parse_json(ccode, tstamp, data):
    decoded_json = json.loads(data)
    # IF list, recurse on list b
    # IF dictionary, recurse on dictionary
    # Open Object, add countrycode, timestamp
    # IF list, recurse on list b
    # IF dictionary, recurse on dictionary
    buzzes = decoded_json['buzzes']
    for buzzcount in range(len(buzzes)):
        k = BuzzRec()
        # load country code and timestamp of when data was pulled
        k.add_pull_cc(ccode)
        k.add_pull_ts(tstamp)
        # load relevant buzz fields
        buzz = buzzes[buzzcount]
        # what is load buzz
        # load(buzz, k)
        k.add_buzz(buzz)
        k.display_buzz()
        #k.load_buzz()
        del k
        #exit()
        # READ ALL KEYS: Send ccode, tstamp, data.  Extract all dictionary keys.


def main():
    # Open Postgres database
    # ----- database_file = "./parseddb/buzzrecords"
    # ----- db = open (database_file, "w")
    # Find data DIRECTORY
    import os
    import glob
    # Create Master Key Object to keep a running list of keys
    # How do you pass the master key??? -- perhaps it is inside the object

    # get the filenames in data directory and parse records in each file
    jsondata_dir = "./buzzfeeddata/"
    for infile in glob.glob( os.path.join(jsondata_dir, '*.txt') ):
        # Extract timestamp and COUNTRY from the filename
        file_name = get_filename (infile, jsondata_dir, ".txt")
        country_name = get_country (file_name)
        time_stamp = get_timestamp (file_name)
        # Read json record
        datafile=open(infile, 'r')
        data = datafile.read()
        parse_json (country_name, time_stamp, data)
        datafile.close()
        # Have to write the record to the database at some point

    # Close database
    # ----- db.close()


if __name__ == "__main__":
    main()
