#!/usr/bin/env python
#coding:utf-8
#Author:Cooper  Created: 2016/12/25
import requests,sys,json,os
import pandas as pd

reload(sys)
sys.setdefaultencoding('utf-8')
sysEncode = sys.getfilesystemencoding()

cookie = "swfstore=269547; cna=4d/TEEJNrTYCAW/IVxEM9eba; thw=cn; _med=dw:1280&dh:720&pw:1920&ph:1080&ist:0; uc3=sg2=BvKCvMwsk6cXSS4rB%2F7ckGqBkSydOHZYpBgoXN2QCi4%3D&nk2=VP6XlLE%3D&id2=UonTGyH6d3sUyg%3D%3D&vt3=F8dARHYoVXXggdZzBnM%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; uss=BdYOZCPn0oelE61rRM9ldbV0LhYj1Sfip%2BpkmwnMnvtWmGRiBYMcRuea5A%3D%3D; lgc=7%5Cu5F26%5Cu6850; tracknick=7%5Cu5F26%5Cu6850; _cc_=W5iHLLyFfA%3D%3D; tg=0; mt=ci=-1_0; t=d75443363bd1904f00e70f1cb3ddb1b3; cookie2=1c66d14088d7660a331bef312e575188; v=0; _tb_token_=785be0643b6e3; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; uc1=cookie14=UoW%2FX9vjNaTyUQ%3D%3D; l=AhcXPj0yt59IbHfrQuH7ybwVJ4FhHeu9; isg=Ajc32kcAI1FU3afM15BDuTecxiLATQteTdmUR4nkEoZuOFd6kcybrvWYfC-c"

def main():

    if os.path.exists('data.csv'):
        data = pd.read_csv("data.csv")
    else:
        data = pd.DataFrame()

    if os.path.exists('cache_url.txt'):
        f = open('cache_url.txt')
    else:
        f = open('cache_url.txt','w+')
    cache = f.read().split('\n')
    f.close()

    def setPages(num):
        urls = []
        for p in range(num):
            url = "https://list.taobao.com/itemlist/mini/list.htm?pSize=60&json=on&_input_charset=utf-8&cat=1512&viewIndex=1&as=0&atype=b&s=" + str(
                p * 60) + "&style=grid&q=%E6%89%8B%E6%9C%BA&same_info=1&isnew=2&data-key=s&data-value=" + str(
                p * 60 + 60) + "&data-action&module=page"
            urls.append(url)
        return urls

    def sendRequest(url):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Cookie": cookie
        }
        res = requests.get(url, headers=headers)
        res = res.content.decode('gbk').encode(sysEncode)
        return res

    urls = setPages(3)
    # print cache
    for url in urls:
        # print url
        if url in cache:
            print "%s PASS" % url
            pass
        else:
            res = sendRequest(url)
            j = json.loads(res)
            statusCode = j['status']['code']
            if statusCode == "200":
                # get data
                df = pd.DataFrame.from_dict(j['itemList'])
                data = pd.concat([data, df], axis=0)
                # write cache
                f = open('cache_url.txt', 'a')
                f.write("\n" + url)
                f.close()
                print "%s OK" % url
            else:
                print url + " FAIL,please change the cookie and re-run.",

    data.to_csv("data.csv", index=False)
    print "Done.."

if __name__ == '__main__':
    main()