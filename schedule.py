# The code is for Automatice scheduling job

import schedule
import datetime
import time

def job():
    current_date_and_time = datetime.datetime.now()
    print("Current date and time:", current_date_and_time)
    print("Executing code 5 seconds before every 15 minutes of the hour.")
    
def schedule_job():
    schedule.every(15).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_job()
