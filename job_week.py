from datetime import datetime, timedelta
from bot.openresa import main

def scheduled_job():
    tomorrow = datetime.today() + timedelta(days=1)
    club_name = "les-pyramides"
    date = tomorrow.strftime("%d/%m/%Y")
    slot = '14:00-15:30'
    court_id = '48097'
    hour = 17
    minute = 0
    second = 0 
    timezone = 'Europe/Paris'
    main(club_name, date, court_id, slot, hour, minute, second, timezone)

if __name__ == "__main__":

    scheduled_job()