#!/usr/bin/env python
#coding:utf-8
#Author:Cooper  Created: 2016/11/25

import pandas as pd
import urllib2,re,random,time

l_id,l_name,l_price,l_sell,l_rate=[],[],[],[],[]
mycookie = raw_input("my cookie :\n")
shop_url = raw_input("shop url like https://inman.tmall.com :\n")

headers1 = {'Cookie':mycookie}

url1 = shop_url+"/i/asynSearch.htm?mid=w-14532052791-0&wid=14532052791&path=/search.htm"
ws1 = urllib2.urlopen(urllib2.Request(url1,headers=headers1)).read()
pages = re.search(r'<b class=\\"ui-page-s-len\\">1/(\d+)</b>',ws1).group(1)

print "A total of %s pages" % pages

pages = input("How many pages to get:\n")

for page in range(1,pages+1):
    print "page %i" % page
    url2 = shop_url+"/i/asynSearch.htm?mid=w-14532052791-0&wid=14532052791&path=/search.htm&pageNo="+str(page)

    ws2 = urllib2.urlopen(urllib2.Request(url2,headers=headers1)).read()

    ids = re.search('defaultSort.*null(.*?)tmallshop',ws2).group(1)
    prices = re.findall('search(.*?)null',ws2)[4]

    l_id_c = re.findall("(\d+)",ids)
    l_price_c = re.findall("(\d+\.\d+)",prices)
    l_name_c = re.findall("}' >(.{1,200}) </a>",ws2)[:len(l_id)]
    l_id.extend(l_id_c)
    l_price.extend(l_price_c)
    l_name.extend(l_name_c)
    
    #print l_price,l_name
    
    for iid in l_id_c:
        print iid
        # get sales
        headers2 = {'Referer':'https://mdskip.taobao.com/core/initItemDetail.htm?itemId='+iid}
        url3 = "https://mdskip.taobao.com/core/initItemDetail.htm?itemId="+iid
        ws3 = urllib2.urlopen(urllib2.Request(url3,headers=headers2)).read()
        sellCount = re.search('{"sellCount":(\d+),"success":true}',ws3).group(1)
        l_sell.append(sellCount)
        
        # get number of comments
        url4 = "https://dsr-rate.tmall.com/list_dsr_info.htm?itemId="+iid
        ws4 = urllib2.urlopen(url4).read()
        rateTotal = re.search('rateTotal":(\d+),"sellerId',ws4).group(1)
        l_rate.append(rateTotal)
        
        #print l_sell,l_rate
        time.sleep(random.randint(1,5)/10.0)

print len(l_id),len(l_sell),len(l_rate)
df = pd.DataFrame({"id":l_id,
                   "name":l_name,
                   "price":l_price,
                   "sell":l_sell,
                   "rate":l_rate})
df.to_csv('tmall.csv',index=False)
print "done.."
import winsound
winsound.Beep(600,2000)
