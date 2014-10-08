# Thu May 29 02:04:12 EDT 2014

from lxml import html
import requests
import re
import sys
import json
import tempfile

"""scrape web content except reviews
"""
web_content = {}

asin = str(sys.argv[1])
#asin = 'B00EFILPHA'
url = 'http://www.amazon.com/dp/' + asin + '/'
page = requests.get(url)
tree = html.fromstring(page.text)

# this extracts the list of features 
feature_bullets = tree.xpath('//div[@id = "featurebullets_feature_div"]/div[@id = "feature-bullets"]/ul[@class = "a-vertical a-spacing-none"]/li/span[@class = "a-list-item"]/text()')
web_content['feature_bullets'] = feature_bullets

# average customer rating
ave_cus_rating = tree.xpath('//*[@id="detail-bullets"]/table/tbody/tr/td/div/ul/li[7]/span/span/a/span/title')

# Date first available at Amazon.com
date_ava = tree.xpath('//*[@id="detail-bullets"]/table/tbody/tr/td/div/ul/li[9]/text()')

# Amazon Best Sellers Ranks
seller_rank = tree.xpath('//*[@id="SalesRank"]/text()')
# seller_rank = seller_rank[1].strip(' \t\n\r')
web_content['seller_rank'] = seller_rank

# Product Description 
pro_des = tree.xpath('//*[@id="productDescription"]/div/p/text()')
web_content['pro_des'] = pro_des

# Product Description Wrapper
product_des_list = tree.xpath('//div/div[@class = "bucket"]/div[@class = "content"]/div[@class = "productDescriptionWrapper"]/text()')
product_des = [item for item in product_des_list if re.search(r'[a-zA-Z0-9]+', item)]
web_content['product_des'] = product_des

# Popular Discussion Topics
topic_list = tree.xpath('//*[@id="rtb-button-container"]/ul/li/span/span/span/span/text()')
topics = [item.replace('\n','').replace('\r', '') for item in topic_list if re.search(r'[a-zA-Z]+', item)][: -1]
web_content['topics'] = topics

with open('data.txt', 'w') as outfile:
   json.dump(web_content, outfile)
