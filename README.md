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
Since I already discovered where the links were on the page (when I was gathering background information), I needed to set up my scraper to actually get the links in that div. In order to do this, I had to:
- 1. Find all of the `div` elements with the `class` of `views-content-title`.
- 2. Find all of the links in this `div` -- by finding all of the `a` tags and taking the `href` element out of it (figuring this out took the longest of the entire project.)
- 3. Store the new links in a file (this is not necessary, but it makes knowing what links were scraped easier).
This is done with the `p.write()` command. The links are written into the file `wcjb_scraper.txt`.

#### Step 6: Scraping Headlines and Paragraphs
After scraping the latest news links, I needed to go to those stories and scrape the headline and the first two paragraphs of the story. To do this, I had to:
- 1. Find the **first** `h2` on the page with the `class` of `pane-title` (I assumed that there would only be one of these, but I was very wrong.)
- 2. Find the text for the first **three** `p` tags (the site uses an empty `p` tag for spaces betweek paragraphs, so to get the first two paragraphs I needed to grab the first three tags).
- 3. Store the new links, headline, and paragraphs all in a file (this **is** necessary for this part).
This is done with the `n.write()` command. The links are written into the file `wcjb_scraper.txt`.
I wanted to make this part of the project a separate function, but I quickly discovered that it was much easier to get each story's information as that link was written (otherwise, I had to try and create new variables and lists using the same words -- it got very confusing, very quickly).

After this step was finished, I closed both files using `p.close()` and `n.close()`.

#### Step 7: Saving the HTML
The link to the story and the HTML (headline, first 2 paragraphs) are saved to a new file, `wcjb_scraper2.html`.

I discovered that the only way to have the file display in the email properly was to save the information as a `.html` file.

In order to remove the brackets from around the items that were interpreted using `str()`, I had to use `.strip()` on them. This works for the `.txt` file, but does not work for printing.

#### Step 8: Emailing the File
Using yagmail was supposed to make this step extremely easy--and it makes a lot of the problems much easier. I was quickly able to set up a subject and body to send.

Attaching the file was much harder than I expected it to be, and the creator of yagmail didn't have much documentation for how to do so.

After playing with the settings, I was finally able to do so by copying the file's direct path from it's file information.

I was unable to get the file to format properly until I discovered that saving it as a `.html` file would make the html tags display properly.


## Problems

**The only problem that I was unable to fix** was getting the html to format correctly in a way that would remove the extra paragraphs. 

I was not expecting to, but I actually had a problem scraping the links from WCJB's website. I could scrape every single link from the site with no problem, but I had a lot of trouble figuring out how to properly dig into the DOM and get the links that I needed. I **finally** found the answer for pulling the link out of the div element from [this Stack Overflow thread](http://stackoverflow.com/questions/8551230/how-can-i-get-information-from-an-a-href-tag-within-div-tags-with-beautifuls).

Stripping the `h2` tags from each story's page was pretty difficult at first, until I realized that I should apply the limits (from where I was scraping `p` tags) as well as the specific way that scraping for links had worked (using the `attrs={}` method).

Although [yagmail](https://github.com/kootenpv/yagmail) was a great help, figuring out how to set it up to send emails was not as simple as it seemed at first. I found that even though I could often get emails to send, Python would still give me an error about the sending of the email. I learned that to fix this, I needed to install lxml in addition to yagmail so that the emails would send without an error.

After getting yagmail to send emails, I struggled with getting it to send attachments properly. This was difficult because there are no answers to questions about a specific module, and there was no documentation about attaching files. I was finally able to find a solution by copying the direct path to the file in question, placing it into a variable (`html = '/Users/deenaacree/Documents/Python/scraping/wcjb_scraper2.txt'`), and then adding that variable to the `contents` list.

Another unexpected problem that I encountered was trying to figure out how to make my script run **by itself** at least once per day. I assumed that making the script run multiple times wouldn't be hard; however, trying to tell the script to run without me starting it up was a challenge. After struggling with examples of how to code this yourself (a lot of jargon and math I didn't really understand), I found [schedule](https://pypi.python.org/pypi/schedule), which does it perfectly with just a little understanding.

## Note 

I am including a PDF of one of the emails that was sent. The only thing that I’m unhappy with about this is the formatting—-the extra spacing is because of the way WCJB formats their articles.(I could not figure out how to remove the extra spacing; stripping did not work successfully to do that and neither did any other fixes that I found). 


