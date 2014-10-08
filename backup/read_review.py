# Tue Jun  3 03:46:42 EDT 2014

"""
give review file, return dic as userID:review
for this asin
input: asin
output: review dic
"""

import json
import re

def read_review(asin):
   # import data
   reviews = {}
   fin = open(asin, 'rb')
   # read data
   data_list = fin.readlines()
   fin.close()
   data_list = [item.rstrip('\n') for item in data_list]

   count = 1
   for item in data_list:
      # find userID
      match = re.search(r'[0-9A-Z]{14}', item)
      if match:
         name = match.group()
      else:
         name = str(count)
      # store review for this user
      if name in reviews:
         reviews[name] += item
      else: 
         reviews[name] = item 
      count = count + 1
      # return reviews
      """
      with open('amazon_review.json', 'wb') as outfile:
         json.dump(reviews, outfile)
      """
