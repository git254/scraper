# set up parameters used in program using shelve
import shelve

s = shelve.open('parameter.db')
try:
    s['url'] = 'http://www.amazon.com/s/ref=sr_kk_3?rh=i%3Aaps%2Ck%3Asmartphone&keywords=smartphone&ie=UTF8&qid=1412452184'
    s['url_before'] = 'http://www.amazon.com/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Asmartphone&page=1'
    s['url_after'] = '&keywords=smartphone&ie=UTF8&qid=1412452219'
    # add more
finally:
    s.close()
