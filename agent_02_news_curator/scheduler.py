# scheduler.py

import schedule
import time
from main import main

def job():
    print("[Scheduler] Running agent job...")
    main()
    print("[Scheduler] Job complete.\n")

def start_scheduler():
    # Schedule the job once per day at 7:00 AM
    schedule.every().day.at("07:00").do(job)

    print("[Scheduler] Agent 02 will run daily at 7:00 AM.")
    print("[Scheduler] Press CTRL+C to stop.\n")

    while True:
        schedule.run_pending()
        time.sleep(60)  # check every minute

if __name__ == "__main__":
    start_scheduler()
