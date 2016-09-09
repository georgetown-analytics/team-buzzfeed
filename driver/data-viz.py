#!/usr/bin/env python3
"""
Using Seaborn & Bokeh to generate vizualisations using a .csv data file.
"""

##########################################################################
## Imports
##########################################################################

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import brewer

##########################################################################
## Constants
##########################################################################

path = os.getcwd()
timed_path = 'tests/data/datafeed.csv'
data_path = 'tests/data/alldata.csv'
viz_path = os.path.join(path, 'viz-ouput')
col_names = ['pull_cc', 'pull_ts', 'u_name', 'last_upd', 'pub', 'pub_ts', 'cc', 'impressions', 'lang', 'id', 'descr', 'cat', 'cat_id', 'u_id', 'title', 'status', 'metav', 'tags', 'comment_stat']

# Set the style for Seaborn graphs
sns.set_style("dark")
# Tools for Bokeh
bokeh_tools = "resize,pan,wheel_zoom,box_zoom,reset,box_select"

##########################################################################
## Functions
##########################################################################

def load_data(path, fn, NAMES=None):
    """
    Uses pandas to load a .csv that's delimited by the '|' symbol into a
    dataframe. Useful for quickly loading different datasets for vizualizations,
    IMO.
    """
    # identify the location of the data file
    data_loc = os.path.join(path, fn)

    # load it into a data frame using pandas
    if NAMES == None:
        df = pd.read_csv(data_loc, delimiter='|')
    else:
        df = pd.read_csv(data_loc, delimiter='|', names=NAMES, low_memory=False)
    # hand the data frame back to the programmer
    return df

def save_viz(viz_obj, file_path, file_name):
    """
    Takes a visualization object as input and saves it at the defined
    location with the defined name. (Not in use at this time)
    """
    #with open(os.path.join(file_path, file_name), 'w') as f:
    #    f.write(viz_obj.content)
    pass

def join_data(loaded_df_1, loaded_df_2):
    """
    Takes two buzzfeed data frames and does an inner join based on the 'pull_cc' column.
    """
    new_df = pd.merge(loaded_df_1, loaded_df_2, on='id', how='inner')
    return new_df

def sns_viz(dataframe):
    """
    Takes a merged buzzfeed data frame and generates a seaborn time series vizualization
    """
    # load the data locally
    data = dataframe.groupby('title')
    # drop the columns we won't be using
    #data = data.drop(['u_name', 'last_upd', 'pub', 'pub_ts', 'lang', 'id', 'descr', 'cat_id', 'u_id', 'title', 'status', 'metav', 'comment_stat'], 1)
    # Plot the data
    sns_plotter = sns.swarmplot(x='pull_cc', y='max_impres', data=data.grou)

    print(type(sns_plotter))
    # show the data, and make it pretty
    sns_plotter.plt.show()

def sns_ts_viz(dataframe):
    """
    http://stackoverflow.com/questions/22795348/plotting-time-series-data-with-seaborn
    """
    # Read in the data from the stackoverflow question
    # df = pd.read_clipboard().iloc[1:]

    # Convert it to "long-form" or "tidy" representation
    # df = pd.melt(df1, id_vars=["pull_ts"], var_name="condition")

    # Plot the average value by condition and date
    # ax = df.groupby(["condition", "pull_ts"]).mean().unstack("condition").plot()

    # Get a reference to the x-points corresponding to the dates and the the colors
    # x = np.arange(len(df.date.unique()))
    # palette = sns.color_palette()

    # Calculate the 25th and 75th percentiles of the data
    # and plot a translucent band between them
    # for cond, cond_df in df.groupby("condition"):
        # low = cond_df.groupby("date").value.apply(np.percentile, 25)
        # high = cond_df.groupby("date").value.apply(np.percentile, 75)
        # ax.fill_between(x, low, high, alpha=.2, color=palette.pop(0))

def bokeh_viz(loaded_df, filename, p_tools=bokeh_tools):
    """
    Takes a buzzfeed data frame with time series data as input and returns and outputs a static HTML
    file.
    """
    ## Code example taken from Bokeh documentation
    # Prepare the data
    # Define your X & Y axes
    X = loaded_df['pull_cc']
    Y = loaded_df['max_impres']
    radii = loaded_df['freq']
    # Define the colors
    bokeh_colors = brewer['Spectral'][6]

    # output to a static HTML file (with CDN resources)
    output_file(os.path.join(viz_path, "{}.html".format(filename)), title="graph_title", mode="cdn")

    # instantiate the new plot space with the tools you specify,
    # can optionally add an explicit range using syntax x_range=(0,100), y_range
    p = figure(tools=p_tools, y_range=(100, 5000))

    # add a circle renderer with vectorized olors and sizes
    p.circle(X, Y, radius=radii, fill_color=bokeh_colors, fill_alpha=0.6, line_color=None)

    # show the results
    show(space)

def main():
    # Load up both our data frames
    ts_data = load_data(path, timed_path, NAMES=col_names)
    data = load_data(path, data_path)
    # Merge data so we have time series and frequency in the same spot
    merged_data = join_data(ts_data, data)

    # generate and open a Seaborn viz with the merged data
    sns_viz(data)

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
