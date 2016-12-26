#!/usr/bin/env python
#coding:utf-8
#Author:Cooper  Created: 2016/11/23

import pandas as pd
import urllib2,urllib,requests,re
from urllib2 import URLError

l_id=[]
l_price=[]
l_name=[]

url1 = r"https://inman.tmall.com/i/asynSearch.htm?mid=w-14532052791-0&wid=14532052791&path=/search.htm"
#ws1 = urllib.urlopen(url1).read()
#ws1 = ws1.geturl()


class MyHTTPRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)
    http_error_301 = http_error_303 = http_error_307 = http_error_302

cookieprocessor = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(MyHTTPRedirectHandler, cookieprocessor)
urllib2.install_opener(opener)

#ws1 = urllib2.urlopen(url1).read()
#print ws1
#pages = re.search(r'<b class=\\"ui-page-s-len\\">1/(\d+)</b>',ws1).group(1)

#for page in range(1,pages+1)
url2 = "https://inman.tmall.com/i/asynSearch.htm?mid=w-14532052791-0&wid=14532052791&path=/search.htm&pageNo=1"
ws2 = urllib2.urlopen(url2).read()
print ws2

ids = re.search(r'defaultSort.*null(.*?)tmallshop',ws2).group(1)
prices = re.findall(r'search(.*?)null',ws2)[4]


l_id = re.findall(r"(\d+)",ids)
l_price = re.findall(r"(\d+\.\d+)",prices)
l_name = re.findall(r"' >(\S.*?) </a>",ws2)
 
print len(l_name)

#for id in l_id:

url3 = "https://mdskip.taobao.com/core/initItemDetail.htm?itemId="+str(l_id[0])

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36 TheWorld 7',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
       'Accept-Encoding': 'gzip, deflate, sdch',
       'Accept-Language': 'zh-CN,zh;q=0.8',
       'Connection': 'keep-alive'}

print 'step'
rep = urllib2.Request(url1,headers=headers).read()
ws3 = urllib2.urlopen(req).read()

print ws3


#ws3 = urllib2.urlopen("https://mdskip.taobao.com/core/initItemDetail.htm?itemId="+str(l_id[0])).read()
ws4 = urllib2.urlopen("https://dsr-rate.tmall.com/list_dsr_info.htm?itemId="+str(l_id[0])).read()

saleall = re.search(r'rateTotal":(\d+),"sellerId',ws3).group(1)
rateall = re.search(r'rateTotal":(\d+),"sellerId',ws3).group(1)

#print len(l_id),len(l_price),len(l_name)

