from datetime import datetime, timedelta
from openresa import main

if __name__ == "__main__":
    
    # params
    tomorrow = datetime.today() + timedelta(days=1)
    club_name = "les-pyramides"
    date = tomorrow.strftime("%d/%m/%Y")
    slot = '14:00-15:30'
    court_id = '48097'
    hour = 17
    minute = 23
    second = 0 
    timezone = 'Europe/Paris'

    main(club_name, date, court_id, slot, hour, minute, second, timezone)