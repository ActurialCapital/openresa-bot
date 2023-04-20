from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler

from bot.openresa import main

sched = BlockingScheduler(timezone='Europe/Paris') # 'utc'
@sched.scheduled_job('cron', id='main', day_of_week='mon-sat', hour=17, minute=00, second=00)
def run_scheduled_job():
    main(club_name, date, court_id, hour, minute, second, timezone)

if __name__ == "__main__":
    
    # params
    tomorrow = datetime.today() + timedelta(days=1)
    club_name = "les-pyramides"
    date = tomorrow.strftime("%d/%m/%Y")
    court_id = '48097'
    hour = 16
    minute = 20
    second = 0 
    timezone = 'Europe/Paris'

    sched.start()