import logging
from datetime import datetime, timedelta
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

from config import Config
from openresa import main

if __name__ == "__main__":
    
    # params
    tomorrow = datetime.today() + timedelta(days=1)
    club_name = "les-pyramides"
    date = tomorrow.strftime("%d/%m/%Y")
    court_id = '48097'

    main(Config, club_name, date, court_id)