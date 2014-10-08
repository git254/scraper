from bs4 import BeautifulSoup
import requests
import pickle
from lxml import html
import shelve

"""grab ASIN for each camera on amzon
amazon ASIN: http://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number
"""

### construct url
s = shelve.open('parameter.db')
try:
    url = s['url']
    url_before = s['url_before']
    url_after = s['url_after']
finally:
    s.close()

### total page number on amazon
page = requests.get(url) 
tree = html.fromstring(page.text)
page_limit = tree.xpath('//*[@id="pagn"]/span[6]/text()')
page_limit = int(page_limit[0]) 
print "total", str(page_limit), "pages"
asin_set = set()

for p in range(page_limit):
   print str(p + 1)
   url = url_before + str(p + 1) + url_after
   r = requests.get(url)
   data = r.text
   soup = BeautifulSoup(data)
   for link in soup.find_all('a'):
      href = link.get('href')
      if href == None:
         continue 
      elif 'http://www.amazon.com' in href and '/dp/' in href:
         url_ele = href.split('/')
    	 asin = url_ele[-1][0:10]
         asin_set.add(asin)

asins = list(asin_set)
# write to file
fw = open("asins", "w")
for asin in asins:
    fw.write(asin + "\n");
fw.close()
