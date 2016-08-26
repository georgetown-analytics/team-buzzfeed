#!/usr/bin/env python3
"""
Takes a corpus of raw text as input and calculates comprehensive Markov
probabilities. Which then feeds into a function that solicits a seed word and a
'sentence length' parameter in order to generate probabilistic text
"""

##########################################################################
## Imports
##########################################################################

import os
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

##########################################################################
## Module Variables/Constants
##########################################################################

names = ['pull_cc', 'pull_ts', 'u_name', 'last_upd', 'pub', 'pub_ts', 'cc', 'impressions', 'lang', 'id', 'descr', 'cat', 'cat_id', 'u_id', 'title', 'status', 'metav', 'tags', 'comment_stat']
drop_names = ['pull_ts', 'u_name', 'last_upd', 'pub', 'pub_ts', 'cc', 'impressions', 'lang', 'id', 'descr', 'cat', 'cat_id', 'u_id', 'status', 'metav', 'tags', 'comment_stat']
datafeed = os.path.join('tests/data', 'datafeed.csv')
test_titles = ['24 Times Blake Lively Was Really Fucking Funny on Instagram', 'A Giant Ad Screen in Pune Apparently Started Streaming A Porn Site In Broad Daylight']

##########################################################################
## Functions
##########################################################################

def prep_data(csv_file, name_list, drop_list):
    """
    Takes the location of a csv_file with all of the BuzzFeed data and
    loads it into a pandas dataframe and preps it for the ML classifiers.
    """
    # load the dataframe
    data = pd.read_csv(csv_file, delimiter='|', header=0, names=name_list)
    #get rid of unnecessary columns
    data = data.drop(drop_list, 1)

    return data

def kNeighbors(str_input):
    """
    Takes the prepped dataframe and applies a KNeighborsClassifier model to it,
    and prints the

    Uses a Pipeline to transform a str for any variables that you'd like to predict

    Then calls the .predict() method and returns the most likely value.
    """
    # load the csv file into a dataframe and drop everything but title and the country the title was pulled from
    data = prep_data(datafeed, names, drop_names) # just realized that dropping the columns isn't that necessary actually

    # define X and y values that we'll use for our modeling
    X = data.title
    y = data.pull_cc

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    # initialize our vectorizer
    vect = CountVectorizer()

    # use the vectorizer to transform training data into numerical values
    X_train_dtm = vect.fit_transform(X_train)
    # Ditto for the test data
    X_test_dtm = vect.transform(X_test)

    # K Nearest Neighbors modeling goes here...
    kneigh = KNeighborsClassifier()
    kneigh.fit(X_train_dtm, y_train)
    y_pred_class = kneigh.predict(X_test_dtm)

    # evaluate our model's accuracy
    accu = metrics.accuracy_score(y_test, y_pred_class)
    accu *= 100
    print('Your model is predicting with an accuracy of {0:.2f}%'.format(accu))

    # set up a pipeline to transform any string values to a format that can be
    # tested against the model
    model = Pipeline([("vectorizer", CountVectorizer()),("classifier", KNeighborsClassifier()),])

    # fit the pipeline to the data
    model.fit(X,y)

    # show the model new data and generate a predicition as to where t
    result = model.predict(str_input)

    # tell the user where the model says these titles are most likely to go viral
    print('The title(s) you have provided are most likely to trend')
    print('in the following languages and locations, respectively:')
    for i in result:
        print(str(i))

def main():
    # run our modified K Nearest Neighbors and predict where the test titles
    # are most likely to go viral
    kNeighbors(test_titles)

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
