import requests, bs4, datetime
output = []
def main(key):
    search = key
    x = 'https://smartnet.niua.org'
    res = requests.get('https://smartnet.niua.org/tenders?date=2018-10')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    elements= soup.select('.views-field-title')
    linkList = []
    
    count=1
    for i in elements:
        i=str(i)
        exSoup = bs4.BeautifulSoup(i,"lxml")
        aElements= exSoup.select('a')
        textElem= exSoup.select('.cal-dot')
        text=textElem[0].get('title')
        link = aElements[0].get('href')
        link = x+link
        if search in text.lower():
            if link not in linkList:
                linkList.append(link)
    for i in linkList:
        resp = requests.get(i)
        resp.raise_for_status()
        docSoup = bs4.BeautifulSoup(resp.text, "lxml")
        data = docSoup.select('.views-field-views-conditional')
        dateSoup = bs4.BeautifulSoup(str(data[1]), "lxml")
        date = dateSoup.select('span')[0].getText()
        #print(date)
        pdfSoup = bs4.BeautifulSoup(str(data[0]),"lxml")
        pdfLink = pdfSoup.select('a')[0].get('href')
        output.append(pdfLink)
    return output
    '''pdfres = requests.get(pdfLink)
    pdfres.raise_for_status()
    with open ('smartnet tender'+str(count)+'.pdf','wb') as f:
        for c in pdfres.iter_content(100000):
            f.write(c)
    count+=1'''


