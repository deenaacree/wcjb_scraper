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

    location = div.find('a')['href']
    prefix = "http://www.wcjb.com"
    new_url = "http://www.wcjb.com" + str(location)
    html = urlopen(new_url)
    bsObj = BeautifulSoup(html, "html.parser")


    headline = bsObj.findAll("h2", attrs={'class' : 'pane-title'}, limit=1)
    text = bsObj.findAll("p", limit=3)
    print(new_url, headline, text)
    n.write(new_url + str(headline) + str(text) + "\n")


p.close()
n.close()


# everything above this currently works correctly

def email():
    yag = yagmail.SMTP('acreedeena')
    to = 'acreedeena@gmail.com'
    subject = "Your WCJB Local News for Today"
    body = 'This is the Latest in Local News from WCJB for today. Find more news <a href="http://www.wcjb.com/local-news">here</a>.'


    yag.send(to, subject, contents = [body, 'file://local/wcjb_scraper2.txt'])

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
