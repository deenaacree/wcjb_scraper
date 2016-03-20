import schedule # this is the "program" you use to run this scheduled job. You have to install it first with "pip install schedule"
import time

# this function is what I will replace with the final scraper:
def job():
    print("Doing a job now... Done.")
    # to make it run the job only once (for testing maybe), use the following line:
    # return schedule.CancelJob

schedule.every(30).seconds.do(job) # this sets the job up to run every 30 seconds (for testing)
schedule.every().day.at("09:00").do(job) # this sets the job up to run at 9am every day
schedule.every().day.at("21:00").do(job) # this sets the job up to run at 9pm every day

# not sure exactly why this is needed, but it's part of the schedule "program" and without it, it won't run even once
while True:
    schedule.run_pending()
    time.sleep(1)
