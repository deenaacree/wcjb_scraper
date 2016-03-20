# WCJB News — Web Scraping Project

## Origins

I decided to undergo this particular scraping project because I have recently realized my lack of knowledge about local events and news in Gainesville, Florida. I don't have the time to search for local news each day, so I decided that a fun web scraping project could bring the information to me.

Initially, I wanted to scrape from a handful of small news organizations in Gainesville, but I decided that to do a small project like this all I really needed was one organization that doesn't already have an RSS feed.


## Goal

My task for this scraping project was to get local news delivered right to my inbox. Using scraping, I wanted to get:
- The links to top local stories for a local news organization (which did not have an RSS feed available), [WCJB](http://www.wcjb.com/).
- The headlines for these top stories
- The first two paragraphs of the stories

I wanted to have this information emailed to me at least once a day (preferably twice per day, depending on how often the stories change).


## Steps

#### Step 1: Gathering Background Information
- I started my search by inspecting the elements on the [WCJB Local News](http://www.wcjb.com/local-news) page. I learned how the top local stories for each page are formatted, so that I would be able to scrape the links later.
- In this case, the links are placed in a `div` with a specific class which is found only once:  `class="views-content-title"`
- I also learned about [yagmail](https://github.com/kootenpv/yagmail), a great utility that would making emailing my news stories to myself much more simple.

#### Step 2: Deciding on A Method
After doing a little bit of processing, I learned that in order to scrape the information that I wanted, I would have to:
- First, scrape the homepage of [WCJB Local News](http://www.wcjb.com/local-news) for links to the stories that are in the "Latest in Local News" section.
- Second, open each of those links and scrape both the headline and the first two paragraphs of the story.
- Third, save the link, the headline, and the paragraphs of the story.
- Fourth, email all of that information them to myself in a way that is understandable and clear.

#### Step 3: Setting up yagmail
In order to set up yagmail, I had to create a new Gmail account (allowing the account to be insecure so that I could send the automated emails to it). After setting up the new account, I had to install yagmail and lxml (which sends emails properly through yagmail).

Next, I had to store my Gmail username and password with yagmail. Finally, I sent a few test emails to myself to figure out how the system works.

The function, `yag.send(to, subject, contents = [body, html])` is what actually sends the email. Each of the variables except `content` (`to`, `subject`, `body`, and `html`) are defined earlier in the code.

#### Step 4: Setting up A Recurring Function
Since I was having trouble scraping just the links I wanted on the WCJB page, I decided that next I wanted to go ahead and figure out how to set up an automated script.

I found [a post on Stack Overflow](http://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day/15090893#15090893) which wrote out one of these functions, but the figuring required to set up the times for functions to run were too complicated for me to understand.

Instead, another comment on that post recommended [schedule](https://pypi.python.org/pypi/schedule), a job scheduler which allows you to write commands in human terms (thank goodness!). It's small but does the job that I need. There's even a handy command you can place at the end to tell the function to only run one time (useful for when I'm testing the function).

To use schedule, I put the yagmail code into a function, `email`, which I then tell to run twice per day, at 9 P.M. and 9 A.M., using `schedule.every().day.at("09:00").do(email)` and `schedule.every().day.at("21:00").do(email)`.

#### Step 5: Scraping WCJB for Links
Since I already discovered where the links were on the page (when I was gathering background information), I needed to set up my scraper to actually get the links in that div. 


#### Step 6: Scraping Headlines and Paragraphs
After scraping the latest news links, I needed to go to those stories and scrape the headline and the first two paragraphs of the story.


#### Step 7: Saving the HTML


#### Step 8: Emailing the File



## Problems

I was not expecting to, but I actually had a problem scraping the links from WCJB's website. I could scrape every single link from the site with no problem, but I had a lot of trouble figuring out how to properly dig into the DOM and get the links that I needed. I **finally** found the answer for pulling the link out of the div element from [this Stack Overflow thread](http://stackoverflow.com/questions/8551230/how-can-i-get-information-from-an-a-href-tag-within-div-tags-with-beautifuls).

Although [yagmail](https://github.com/kootenpv/yagmail) was a great help, figuring out how to set it up to send emails was not as simple as it seemed at first. I found that even though I could often get emails to send, Python would still give me an error about the sending of the email. I learned that to fix this, I needed to install lxml in addition to yagmail so that the emails would send without an error.

Another unexpected problem that I encountered was trying to figure out how to make my script run **by itself** at least once per day. I assumed that making the script run multiple times wouldn't be hard; however, trying to tell the script to run without me starting it up was a challenge. After struggling with examples of how to code this yourself (a lot of jargon and math I didn't really understand), I found [schedule](https://pypi.python.org/pypi/schedule), which does it perfectly with just a little understanding.
