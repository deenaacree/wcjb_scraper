from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.wcjb.com/local-news")
bsObj = BeautifulSoup(html, "html.parser")

t = open("scraping_wcjb.txt", 'w')

linkList = bsObj.findAll('div', attrs={'class' : 'views-content-title'})
for div in linkList:
    print(div.find('a')['href'])
    t.write("http://www.wcjb.com" + str(div.find('a')['href']) + "\n")

t.close()
