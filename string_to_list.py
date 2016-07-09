import pandas as pd 
from collections import Counter
import json
import pprint

document = pd.read_csv('/Users/walter_tyrna/Documents/output.csv') #plug in csv file
document = document.drop_duplicates('id')
document = document[pd.notnull(document['tags'])] #selects cells within the tags column that are not blank
tags = document['tags']
big_list = [] #big_list will be where the wrangeled data will be stored
for tag in tags: 
	keywords = tag.replace('heatmap','')
	keywords = keywords.replace('force-image-width-625','')
	keywords = keywords.replace('-',' ')
	keywords_list = keywords.split('*')
	for term in keywords_list:
		term.strip()
		big_list.append(term)
for i in big_list: 
	if i.startswith(''):
		starts_with_space = []
		starts_with_space.append(i)
		i = i.strip()
		keywords_list.append(i)
		keywords_list = [x for x in keywords_list if x not in starts_with_space]
for i in big_list: 
	if '  ' in i:
		blank = []
		blank.append(i)
		big_list = [x for x in big_list if x not in blank]
for i in big_list: 
	if 'mr' in i:
		starts_with_mr = []
		starts_with_mr.append(i)
		big_list.append(i)
		big_list = [x for x in big_list if x not in starts_with_mr]
for i in big_list: 
	if 'test' in i:
		starts_with_test = []
		starts_with_test.append(i)
		big_list.append(i)
		big_list = [x for x in big_list if x not in starts_with_test]
big_list_count = Counter(big_list)
top_ten = big_list_count.most_common(9)
top_ten_list = []
for i in top_ten:
	top_ten_list.append(i[0])
top_ten_list = repr(top_ten_list)
pprint.pprint(top_ten)
with open('top_ten.txt', 'w') as f:
    f.write(top_ten_list)
