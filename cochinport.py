import requests,bs4
s=1
while s<4:
    res =requests.get('http://cochinport.gov.in/index.php?opt=tenders&cat=ct&page='+str(s))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    elements = soup.select('.lister tr')
    
    print(elements[1:])
    s+=1
    '''for i in elements:
        soups = str(i)
        td = bs4.BeautifulSoup(soups,"lxml")
        lists= td.select('td')
        if len(lists)<8:
            continue
        print(i)'''
