Pre-condition:  Postgres must be setup and buzzrow table must have all the data

Scripts to convert multiple pulls into a clean data as follows:
— An instance is defined as 1 row, indexed by id (unique id for an article)
	and pull_cc (country where data was pulled from)
— An article may appear in multiple consecutive pulls from buzzfeed.
	Therefore, the assumption is that longer an article stays on a country’s
	buzzfeed’s page (as measured by in how many subsequent pull the 
	article shows up for each country).
— Another measure of vitality is the number of impressions for each article.  The
	number of impressions is assumed to be how often the article was clicked
	on.
— Clean records are directly added to the Postgres database as follows:
	> Pull data from buzz row table in the database and for each article:
		- Count how many times each appears in the country’s buzzed
		- Impressions in the difference between the minimum number of
			impressions and maximum number of impressions in that
			country
	> Capture any new primary_kw and tags and add to the list
— At the end, cleanbuzz table in postgres will have all the data


Follow the instructions to setup a table in postgres

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
freq		        Integer,
pull_ts         TIMESTAMP,
cc              CHAR (5),
impressions     Integer,
min_impres      Integer,
max_impres      Integer,
descr           VARCHAR (1500),
cat             VARCHAR (50),
cat_id          Integer,
title           VARCHAR (200),
metav           VARCHAR (25),
trending        VARCHAR (10),
primary_kw      VARCHAR (300),
tags            VARCHAR (3000)
);

Step 3.
CREATE INDEX cbindex ON cleanbuzz (id, pull_cc);


# PSEQUEL COMMAND TO LOAD DATA INTO POSTGRES...BE SURE TO CHANGE THE PATH NAME TO YOURS
COPY cleanbuzz FROM '/Users/anuragkhaitan/dropbox/...../datafeed.txt' (DELIMITER('|'));

# PSEQUEL COMMAND TO EXPORT A TABLE INTO A CSV FILE AT A SPECIFIED LOCATION
copy (SELECT * FROM cleanbuzz) TO '/Users/anuragkhaitan/capstone/wrangle/wpostgres/datadump.csv' WITH delimiter '|' CSV header;



