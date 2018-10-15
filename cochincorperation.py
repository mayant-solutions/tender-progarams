import requests,bs4 ,re, os, datetime
output = []

def extract(i):
    soups = str(i)
    td = bs4.BeautifulSoup(soups,"lxml")
    tdList = td.findAll('td')
    url = td.select('a')
    sample_urls = url[1].get('href')
    urls = "http://tender.lsgkerala.gov.in"+sample_urls[2:]
    LB_name= tdList[0]
    tender_No= tdList[1].getText()
    Tender_description = tdList[3].getText()
    Closing_Date = tdList[4].getText()
    
    return LB_name, tender_No, Tender_description, Closing_Date, urls

def main(key):
    s=1
    l =0
    count=1
    search = str(key)
    while s<50:
        res = requests.get('http://tender.lsgkerala.gov.in/pages/displayTender.php?Start='+str(s)+'&Index='+str(l))
        if s%10==0:
            l+=1
        s+=1
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text,"lxml")
        elements= soup.findAll(True,{"class":["clsLBContentLT","clsLBContent"]})

        for i in elements:
            LB_name, tender_no, tender_des, close_date, urlForDownload= extract(i)
            
            #print(close_date)
            if search in tender_des:
                output.append(urlForDownload)
                
    return output
                
'''download = requests.get(urlForDownload)
download.raise_for_status()
                
with open ('tender'+str(count)+'.pdf','wb') as f:
    for c in download.iter_content(100000):
        f.write(c)
count+=1'''
        
