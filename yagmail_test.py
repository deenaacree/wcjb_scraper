import yagmail  # imports yagmail; You have to install it first with "pip install yagmail"
import lxml  # imports lxml so that the emails will send without an error; You have to install it first with "pip install lxml"

# this is the test email; it is set up similarly to the format that the recurring email will be in

yag = yagmail.SMTP('acreedeena')
# defining the yag variable as being my username, which is already stored in keychain
# to do this, you have to run:  yagmail.register('mygmailusername', 'mygmailpassword') first
# then run yag = yagmail.SMTP('acreedeena').
# it will then ask you to enter your password and ask you y/n if it's ok to store the password
# they talk about setting up a .yagmail file, but I couldn't get this to work

to = 'acreedeena@gmail.com'  # this can be "to" anyone

subject = "This is the test for today"  # still trying to figure out how to get the date in the subject; can't use it as a normal variable or as a modulus

body = 'This is the Latest in Local News from WCJB. Find more <a href="http://www.wcjb.com/local-news">here</a>.'  # found this to be interesting -- I can add HTML tags into the body as well

html = '<h2><a href="">Headline goes here</a></h2><p>This is the story p1.</p><p>This is the story p2.</p>'  # using the html tag (the way the yagmail creator did) is an easy way to define what's the news stories and what's the message body

yag.send(to, subject, contents = [body, html])
