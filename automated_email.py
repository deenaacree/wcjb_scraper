import schedule  # this is the "program" you use to run this scheduled job. You have to install it first with "pip install schedule"
import time
import yagmail # imports yagmail; You have to install it first with "pip install yagmail"
import lxml # imports lxml so that the emails will send without an error; You have to install it first with "pip install lxml"

# this is the function that runs
def email():
    yag = yagmail.SMTP('acreedeena')
    to = 'acreedeena@gmail.com'
    subject = "This is the automated test for today"
    body = 'This is the Latest in Local News from WCJB. Find more <a href="http://www.wcjb.com/local-news">here</a>.'
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
