# Fri May 30 00:17:39 EDT 2014

"""running command line. glue each file together
and produce the result in json format"""

import os
import pickle
from subprocess import call
import json
from read_review import *  

"""
# output all the asins
os.system("python asin_spider.py")
"""

amazon_data = {}
amazon_review = {}

# iterate over all asins and store result in json format
asin_dict = pickle.load(open( "asins.p", "rb"))
asins = asin_dict['ASIN']
asins_number = len(asins)
count = 1
for asin in asins:
   asins_number = asins_number - count
   print asins_number
   # get web content except reviews
   call(["python", "scrapper.py", asin])
   with open("data.txt") as json_file:
      json_data = json.load(json_file)
   amazon_data[str(asin)] = json_data

   # get reviews 
   call(["./downloadAmazonReviews.pl", "com", asin])
   review_dir = './amazonreviews/com/' + asin + '/'
   my_cmd = ["./extractAmazonReviews.pl", review_dir]
   with open(asin, "wb") as outfile:
      call(my_cmd, stdout=outfile)
  
   # create review file for each asin
   read_review(asin) 
   """
   reviews = read_review(asin)
   # if asin not in amazon_review: amazon_review[asin] = ""
   amazon_review[str(asin)] = reviews     
   """
  
   # clean dir
   # call(["rm", asin])
   call(["rm", "-r", review_dir]) 

# store web content and reviews in json format
with open('amazon_data.json', 'wb') as outfile:
   json.dump(amazon_data, outfile)
"""
with open('amazon_review.json', 'wb') as outfile:
   json.dump(amazon_review, outfile)
"""
