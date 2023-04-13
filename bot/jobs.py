from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler

from bot.openresa import main
from bot.config import Config

sched = BlockingScheduler(timezone='Europe/Paris') # 'utc'
@sched.scheduled_job('cron', id='main', day_of_week='mon-fri', hour=16, minute=12, second=55)
def run_scheduled_job():
    main(club_name, date, court_id)

if __name__ == "__main__":
    
    # params
    club_name = "les-pyramides"
    tomorrow = datetime.today() + timedelta(days=1)
    date = tomorrow.strftime("%d/%m/%Y")
    court_id = '48097'

    sched.start()