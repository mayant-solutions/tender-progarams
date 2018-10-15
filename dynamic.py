import requests, bs4, re
railway = []
links = []
otherA = []

def nextButtonLink(nextButtonList,partLink):

    for i in nextButtonList:
        if (i.getText()).lower() == 'next':
            nextLink = i.get('href')
            nextLink = partLink+nextLink

            getLink(nextLink)
            # print(nextLink)

def getLink(i):

    regex = re.compile('(.+)ShowAllTender')   # find regex for both text
    zoneLink = regex.findall(i)

    partOfLink = zoneLink[0]

    res1 = requests.get(i)
    res1.raise_for_status()
    soup2 = bs4.BeautifulSoup(res1.text, "lxml")
    tr1 = soup2.select('.sample tr')
    tr1 = tr1[1:]

    for i in tr1:
        soup3 = bs4.BeautifulSoup(str(i), "lxml")
        lists = soup3.select('a')
        link = lists[0].get('href')

        des = lists[0].getText()
        finalLink = partOfLink+link
        des = des.lower()

        if search in des:
            # print(des)
            links.append(finalLink)
            # print(finalLink)
    if mode == 1:
        nextButton = soup2.select('td > a')
        nextButtonLink(nextButton, partOfLink)
    '''else:
        try:
            nextButton2 = soup2.find('input', {'value': 'Next'}).parent
            print(nextButton2)
            otherlinks = nextButton2.get('action')
            # print(partOfLink + otherlinks)
            getLink(partOfLink+otherlinks)
        except:
            pass'''
def main(key):
    global search, mode
    search = key
    res = requests.get('http://www.indianrailways.gov.in/tenders.html')

    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    tbody = soup.select('tr')
    tbody = tbody[1:]
    
    for i in tbody:

        soup1 = bs4.BeautifulSoup(str(i), "lxml")
        tr = soup1.select('td')[0]
        soup2 = bs4.BeautifulSoup(str(tr), "lxml")
        a = soup1.select('a')
        a1 = a[0].get('href')
        if len(a) > 1:
            a2 = a[1].get('href')
            if 'ShowAllTender' in a2:
                otherA.append(a2)

        if 'ShowAllTender' in a1:
            railway.append(a1)
        



    for i in railway:
        mode =1
        getLink(i)


    for i in otherA:
        mode = 2
        getLink(i)
    return links


