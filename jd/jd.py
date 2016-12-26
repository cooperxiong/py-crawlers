#!/usr/bin/env python
#coding:utf-8
#Author:Cooper  Created: 2016/11/27
import pandas as pd
import urllib2,re,random,time,sys

l_id,l_name,l_price,l_cmt=[],[],[],[]

url1 = "https://mall.jd.com/advance_search-112147-37335-35324-0-0-0-1-1-60.html" #京东旗舰店 搜本店 地址栏地址

sysEncode = sys.getfilesystemencoding()
ws1 = urllib2.urlopen(url1).read().decode('utf-8').encode(sysEncode)

amount = int(re.search(r'<em>(\d+)</em>',ws1).group(1))
pages = amount / 60 if amount - (amount / 60)==0 else (amount / 60)+1
print pages

for page in range(1,pages+1)[:2]:
    print "page %i" % page
    url2 =  url1[:-9]+str(page)+url1[-8:]
    ws2 = urllib2.urlopen(url2).read().decode('utf-8').encode(sysEncode)
    # get id comment name
    groups = re.findall(r'<a href="//item.jd.com/(\d+).html#comment" target="_blank">.*?<em>(\d+)</em>.*?</a>[\s\S]*?target="_blank">(.*?)</a>',ws2)
    
    l_id_copy=[]
    for group in groups:
        l_id.append(group[0])
        l_id_copy.append(group[0])
        l_cmt.append(group[1])
        l_name.append(group[2])
    # get price
    for id in l_id_copy:
        url3 = "https://p.3.cn/prices/mgets?skuids=J_"+id+"&type=2&callback=callBackPriceService"
        ws3 = urllib2.urlopen(url3).read().decode('utf-8').encode(sysEncode)
        l_price.append(re.search(r'"p":"(.*?)","m"',ws3).group(1))
        
    print l_cmt
    time.sleep(random.randint(5,10)/10.0)

print len(l_id),len(l_name),len(l_price)
df = pd.DataFrame({"id":l_id,
                   "name":l_name,
                   "price":l_price,
                   "comment":l_cmt})
df.to_csv('jd.csv',index=False)
print "done.."
import winsound
winsound.Beep(600,2000)