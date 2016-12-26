#!/usr/bin/env python
#coding:utf-8
#Author:Cooper  Created: 2016/12/6
import pandas as pd
import urllib2,re,random,time

l_level,l_type1,l_type2,l_time,l_cmt=[],[],[],[],[]

itemId = "520970357724"
userId = "130974249"# 这两个id在商品页地址中可以找到
pages = 2

for page in range(1,pages+1):
    print "Page %i ..." % page
    
    url = "https://rate.tmall.com/list_detail_rate.htm?itemId="+itemId+"&sellerId="+userId+"&order=3&currentPage="+str(page)
    
    ws1 = urllib2.urlopen(url).read()
    
    groups = re.findall(r'"auctionSku":".{1,8}:(.*?);.{1,8}:(.*?)","auctionTitle".*?"rateContent":"(.*?)","rateDate":"(.*?)","reply":".*?","sellerId":\d+,"serviceRateContent":"","structuredRateList":.*?,"tamllSweetLevel":(\d+),',ws1)
    
    for g in groups:
        l_type1.append(g[0])
        l_type2.append(g[1])
        l_cmt.append(g[2])    
        l_time.append(g[3])
        l_level.append(g[4])
    time.sleep(random.randint(5,10)/10.0)
    
df = pd.DataFrame({"l_type1":l_type1,
                "l_type2":l_type2,
                "l_cmt":l_cmt,
                "l_time":l_time,
                "l_level":l_level})

df.to_csv('file.csv',index=False)
print "done.."
import winsound
winsound.Beep(600,2000)
