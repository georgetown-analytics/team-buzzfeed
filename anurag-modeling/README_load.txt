
# PSEQUEL QUERY TO CREATE THE TABLE
# pull_cc is the country for which the API call was made
# pull_ts is the timestamp of when the API call was made
# Rest are the same as JSON returned, just abbreviated here
# Only other difference: tags is a string of tags separated by '*'; we will just need to process it when
# and strip out the '*' when moving onto the next step of the flow
# freq is a counter to track how long an article stayed on buzzfeed
# trending is the tag for an article that's trending
# primary_kw is the primary keyword tag

Step 1.

CREATE TABLE cleanbuzz (
id              Integer,
pull_cc         CHAR (2),
freq		 Integer,
pull_ts         TIMESTAMP,
cc              CHAR (5),
impressions     Integer,
descr           VARCHAR (1500),
cat             VARCHAR (50),
cat_id          Integer,
title           VARCHAR (200),
metav           VARCHAR (25),
trending        VARCHAR (10),
primary_kw      VARCHAR (300),
tags            VARCHAR (3000)
);

Step 2.
CREATE INDEX cbindex ON cleanbuzz (id, pull_cc);

Step 3.
# PSEQUEL COMMAND TO LOAD DATA INTO POSTGRES...BE SURE TO CHANGE THE PATH NAME TO YOURS
COPY cleanbuzz FROM '/Users/anuragkhaitan/dropbox/.datafeed.txt' (DELIMITER('|'));

*********************************************************************

Few more helpful too to play with postgres

SELECT SUM(freq) FROM cleanbuzz;

SELECT DISTINCT PRIMARY_kw FROM cleanbuzz WHERE freq>100 AND impressions>1000000 AND pull_cc='us';

SELECT  pull_cc, PRIMARY_kw, freq, impressions FROM cleanbuzz WHERE freq>100 AND impressions>1000000;

SELECT  id, metav, pull_cc, trending, PRIMARY_kw, freq, impressions FROM cleanbuzz WHERE freq>100 ORDER BY freq, impressions;

*********************************************************************

Here’s how to spit data from Postgres into a file pretty quickly. The string
within the brackets can be any valid SQL string.  And make sure your output file
path/name is valid.

copy (SELECT * FROM cleanbuzz) TO '/Users/anuragkhaitan/Google Drive/02_Buzzfeed Parsed Data/wrangled/datafeed.txt' WITH delimiter '|' CSV header;

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
