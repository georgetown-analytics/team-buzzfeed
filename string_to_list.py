import pandas as pd 
from collections import Counter

document = pd.read_csv('') #plug in csv file
document = document[pd.notnull(document['tags'])] #selects cells within the tags column that are not blank
tags = document['tags']
big_list = [] #big_list will be where the wrangeled data will be stored
for tag in tags: #cleans the data and adds it to big_list
	keywords = tag.replace('heatmap','')
	keywords = keywords.replace('force-image-width-625','')
	keywords = keywords.replace('-',' ')
	keywords_list = keywords.split('*')
	for term in keywords_list:
		big_list.append(term)
for i in big_list: #removes spaces from tags starting with a space
	if i.startswith(' '):
		starts_with_space = []
		starts_with_space.append(i)
		i = i.strip()
		keywords_list.append(i)
		keywords_list = [x for x in keywords_list if x not in starts_with_space]
for i in big_list: #removes blank data
	if i == '':
		blank = []
		blank.append(i)
		big_list = [x for x in big_list if x not in blank]
for i in big_list: #removes tags that begin with 'mr'
	if i.startswith('mr'):
		starts_with_mr = []
		starts_with_mr.append(i)
		big_list.append(i)
		big_list = [x for x in big_list if x not in starts_with_mr]
big_list_count = Counter(big_list)
print big_list_count 