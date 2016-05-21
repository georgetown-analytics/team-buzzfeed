# Feed-the-buzz
Team Buzzfeed Georgetown Data Science Capstone Project

**Team Members**: Anurage Khaitan, Josh Erb, & Walter Tyrna

**Domain Chosen**: New Media/Trending Content Analysis

##Hypothesis or project topic:
The project aims to analyze trends in the top articles across Buzzfeed’s six, country-specific, English-language websites (United States, United Kingdom, India, Australia, and Canada). We expect a correlation between cultural norms and content virality.  Our primary goal is to present an interactive visual that classifies and groups content types depending on different variables among countries. If time permits, we intend to develop a model to assess the probability of a given articles virality based on what keywords or phrases are included in the title and the country in which it is released.

##Available data sources (where we're going to get the data):
Buzzfeed API - we will pull data from APIs corresponding to each of the five countries
Google Trends data available from each country

##A brief description of what we aim to do:
**Ingestion** - Write a python program that will load and read the buzzfeed trending API for all the six countries at various points throughout day or a program written for each country’s data feed.

**Wrangling** - The python program would send this data to a database (we plan on using MongoDB). This process should be dynamic at the scheduled interval times we have specified.   During this stage we will also be combining the various country feeds if Python script only allows us to pull from one API feed at a time.

**Normalization** - Converting the appropriate fields to its corresponding data type. After data has been normalized, use Tableau to spot check outliers.

**Computation** - Using classifying and clustering methods to describe the content type of these trending articles. Which would then be used to create a model to predict the probability of a future article’s success/virality based on these classifications, its reach in terms of impressions (“page views”), and the length of time in terms of hours of it being deemed as a “trending” article by Buzzfeed.

**Feedback Loop** - Ultimately, this project aims to deliver an interactive map, possibly a word cloud, that displays what content is or has been trending in each of the five countries, as well as take keywords as input and display their probability of going viral in a given country. If we are able to house the database on a cloud server, this product could be a web application.

##Questions or avenues of exploration required for the project
What factors contribute to article popularity (culture, geography, keywords, relevancy in search, headline, headlines, etc)? What factors contribute most to virality?
Do certain article tags fair better in certain countries as opposed to others? And do articles/categories published in other countries also do as well? Is it _even possible_ to predict the probability that something will go viral based on the title and the country it's in?
