
import urllib2
import json
import datetime
import os
import glob

from pprint import pprint
from loadbuzz import BuzzRec

def get_filename_old (fname, dirname, extension):
    # REMOVE DIRECTORY AND EXTENSION
    fname = fname.replace(dirname,"")
    fname = fname.replace(extension,"")
    return fname

def get_filename_new (fname, dirname, extension):
    # REMOVE DIRECTORY AND EXTENSION
    print "in: " + fname
    fname = fname.replace(extension,"")
    fnamelen = len(fname)
    fname = fname[fnamelen-16:fnamelen]
    print "out: " + fname
    return fname


def get_country(fname):
    # GET COUNTRY CODE FROM FILENAME
    return fname[:2]

def get_timestamp(fname):
    # GET TIMESTAMP FROM FILENAME
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

def extractdata(jsondata_dir):
    for infile in glob.glob( os.path.join(jsondata_dir, '*.txt') ):
        # Extract timestamp and COUNTRY from the filename
        file_name = get_filename_old (infile, jsondata_dir, ".txt")
        country_name = get_country (file_name)
        time_stamp = get_timestamp (file_name)
        # Read json record
        datafile=open(infile, 'r')
        data = datafile.read()
        parse_json (country_name, time_stamp, data)
        datafile.close()


def main():
    extractdata("../worm/may/")
    extractdata("../worm/june/")
    extractdata("../worm/july/")


if __name__ == "__main__":
    main()
