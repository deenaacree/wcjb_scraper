from urllib.request import urlopen
from bs4 import BeautifulSoup
import schedule
import time
import yagmail
import lxml

html = urlopen("http://www.wcjb.com/local-news")
bsObj = BeautifulSoup(html, "html.parser")

p = open("wcjb_scraper.txt", 'w')
n = open("wcjb_scraper2.txt", 'w')

linkList = bsObj.findAll('div', attrs={'class' : 'views-content-title'})
for div in linkList:
    # this line is to make sure that the links are being written without opening the file
    print(div.find('a')['href'])
    p.write("http://www.wcjb.com" + str(div.find('a')['href']) + "\n")

p.close()


for links in div:
    new_url = links
    html = urlopen(new_url)
    bsObj = BeautifulSoup(html, "html.parser")

    for links in newList:
        # this line is to make sure that the links are being written without opening the file
        print(div.find('a')['href'])
        n.write("http://www.wcjb.com" + str(div.find('a')['href']) + "\n")

n.close()


def email():
    yag = yagmail.SMTP('acreedeena')
    to = 'acreedeena@gmail.com'
    subject = "Your WCJB Local News for Today"
    body = 'This is the Latest in Local News from WCJB for today. Find more news <a href="http://www.wcjb.com/local-news">here</a>.'
    html = '<h2><a href="">Headline goes here</a></h2><p>This is the story p1.</p><p>This is the story p2.</p>'

    yag.send(to, subject, contents = [body, html])

    # use this line if only testing the function once:
    # return schedule.CancelJob

# this is for while I'm testing the code
schedule.every(30).seconds.do(email)

# this is for the daily emails, once at 9am and once at 9pm
schedule.every().day.at("09:00").do(email)
schedule.every().day.at("21:00").do(email)

while True:
    schedule.run_pending()
    time.sleep(1)
