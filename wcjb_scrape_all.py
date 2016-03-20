# this file scrapes all of the links on the WCJB page.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import schedule
import time
import yagmail
import lxml

html = urlopen("http://www.wcjb.com/local-news")
bsObj = BeautifulSoup(html, "html.parser")

t = open("wcjb_scrape_all.txt", 'w')

for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        # print(link.attrs['href'])
        # instead of print to screen (above), print to the file
        # all the a tags that have an href attribute, one per line
        t.write(str(link.attrs['href']) + "\n")

t.close()
