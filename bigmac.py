#@Cooper 16.5.23
import urllib2,re
import pandas as pd
l_year=[]
year = 1985
while year<2015:
    year=year+1
    l_year.append(year)
print l_year

l_years = []
l_cty = []
l_lp = []
l_de = []
l_dp = []
l_ppp = []
l_dv = []

for year in l_year:
    print "collect "+str(year)+"..."
    url_t = r"http://bigmacindex.org/"+str(year)+"-big-mac-index.html"
    raw_t = urllib2.urlopen(url_t).read()    
    if year>1998:      
        pat1 = '''<td class="column-1">(.*?)</td><td class="column-2">(.*?)</td><td class="column-3">(.*?)</td><td class="column-4">(.*?)</td><td class="column-5">(.*?)</td><td class="column-6">(.*?)</td>'''     
        result = re.compile(pat1).findall(raw_t)
        for groups in result[:50]:
            l_years.append(year)
            l_cty.append(groups[0])
            l_lp.append(groups[1])
            l_de.append(groups[2])
            l_dp.append(groups[3])
            l_ppp.append(groups[4])
            l_dv.append(groups[5])
        #print l_lp 
    else:
        pat2 = '''<td class="column-1">(.*?)</td><td class="column-2">(.*?)</td><td class="column-3">(.*?)</td><td class="column-4">(.*?)</td><td class="column-5">(.*?)</td>'''     
        result = re.compile(pat2).findall(raw_t)
        for groups in result[:50]:
            l_years.append(year)
            l_cty.append(groups[0])
            l_lp.append(groups[1])
            l_de.append(groups[3])
            l_dp.append(groups[2])
            l_ppp.append(groups[4])
            l_dv.append("NAN")
#print l_lp         
   
submission = pd.DataFrame({"year":l_years,"country": l_cty,"local price":l_lp,"dollar exchange":l_de,"dollar price":l_dp,"dollar PPP":l_ppp,"dollar valuation":l_dv})
submission.to_csv("bigmac.csv", index=False)
print "finished..."
import winsound 
winsound.Beep(600,2000)

