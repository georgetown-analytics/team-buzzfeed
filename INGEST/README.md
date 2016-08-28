Step 1: collect buzzfeed data on EC2.  This is the code currently running on AWS EC2.
  code: pullBuzzFeed.py
  data: files in worm directory


Step 2: Clean up buzzes and structure data for ingestion.  This is the code we use to parse through each of the
        JSON to clean up into a string, which can be loaded into Postgres.  The program dumps the records as
        a string as STDOUT (onto the screen).
        To save this into a file, when running the program, direct the output to a file as follows:
        python parse.py > datafeed.txt
        Now you can you can use datafeed.txt to load it into postgres.
  code: loadbuzz.py (Module/class)
        parse.py (Main)

  note: To parse Json, run:  python parse.py > data_for_postgres.txt
        This will clean up all records and put the results in the file data_for_postgres.txt.  Field are sepearated
        by "|".  See additional instructions below:
        If longer strings appear in the data, you may have to increase the length of the fields below.

To load data into postgres, create a table, buzzrow and read data in the table
# PSEQUEL QUERY TO CREATE THE TABLE
# pull_cc is the country for which the API call was made
# pull_ts is the timestamp of when the API call was made
# Rest are the same as JSON returned, just abbreviated here
# Only other difference: tags is a string of tags separated by '*'; we will just need to process it when
# and strip out the '*' when moving onto the next step of the flow

CREATE TABLE buzzrow (
pull_cc         CHAR (2),
pull_ts         TIMESTAMP,
u_name          VARCHAR (50),
last_upd        CHAR (10),
pub             CHAR (10),
pub_ts          TIMESTAMP,
cc              CHAR (5),
impressions     Integer,
lang            CHAR (2),
id              Integer,
descr           VARCHAR (1500),
cat             VARCHAR (50),
cat_id          Integer,
u_id            Integer,
title           VARCHAR (200),
status          VARCHAR (10),
metav           VARCHAR (25),
tags            VARCHAR (3000),
comment_stat    VARCHAR (50)
);


# PSEQUEL COMMAND TO LOAD DATA INTO POSTGRES...BE SURE TO CHANGE THE PATH NAME TO YOURS
COPY buzzrow FROM '/Users/anuragkhaitan/ec2/datafeed.txt' (DELIMITER('|'));


*********************************************************************


#### FIELDS THAT I FOUND IN THE JSON I HAVE IGNORED, I.E., NOT LOADED SINCE THEY WEREN"T OF ANY APPARENT username
#### LOOK AT BYLINES...DID SEE ANYTHING OF VALUE, BUT YOU MIGHT DISAGREE, IN WHICH CASE LETS DISCUSS TOMORROW
images
format
bylines         *** NOT SURE
uri
flags           *** NOT SURE
login_type
summary_columns
summary_splash
summary_sub_buzz
longform_custom_header
datelines
disclaimer_top
disclaimer_bottom
short_description
