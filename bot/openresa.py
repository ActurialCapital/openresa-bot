import logging 
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

from utils import mouseover_coordinates
from config import Config

class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level

# Create a logger
logger = logging.getLogger('bot - logs')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('logs.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# Set filter to log only INFO lines
handler.addFilter(MyFilter(logging.INFO))
logger.addHandler(handler)

#write an INFO line to log file
logger.info('This is a INFO message')
logger.warning('This is a WARNING message')
logger.error('This is an ERROR message')
logger.critical('This is a CRITICAL message')

display = Display(visible=0, size=(800, 800))  
display.start()
chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
for option in [
        "--window-size=1200,1200",
        "--ignore-certificate-errors"
        #"--headless",
        #"--disable-gpu",
        #"--window-size=1920,1200",
        #"--ignore-certificate-errors",
        #"--disable-extensions",
        #"--no-sandbox",
        #"--disable-dev-shm-usage",
        #'--remote-debugging-port=9222'
    ]:
    chrome_options.add_argument(option)

class BookingBot:
    def __init__(self, Config, driver, logger):
        self.config = Config
        self.driver = driver
        self.logger = logger

    def open_session(self, club_name):
        """First step, open session via URL"""
        url = self.config.URL.format(club_name=club_name)
        self.logger.info(url) 
        self.driver.get(url)

    def login(self):
        """Login website"""
        # Enter login credentials
        self.logger.info("Login: {username}, {password}".format(username=self.config.USERNAME, password=self.config.PASSWORD)) 
        self.driver.find_element(by=By.XPATH, value=self.config.USERNAME_INPUT).send_keys(self.config.USERNAME)
        # Enter passward
        self.driver.find_element(by=By.XPATH, value=self.config.PASSWORD_INPUT).send_keys(self.config.PASSWORD)
        # Submit the form
        self.driver.find_element(by=By.XPATH, value=self.config.CONNECTION_BUTTON).click()

    def switch_url(self, date, court_id):
        """Switch to the booking page"""
        scheduled_url = self.config.URL_SCHEDULED.format(date=date, court_id=court_id)
        self.logger.info(scheduled_url) 
        while self.driver.current_url != scheduled_url:
            self.driver.get(scheduled_url)

    def select_slots(self, offset_from_element, coordinates):
        """Book court with x and y coordinates"""
        mouseover_coordinates(self.driver, offset_from_element, coordinates)

    def select_partners(self, offset_from_element, list_coordinates):
        """Select members (minimum 2)"""
        # Wait for search bar to be loaded
        self.logger.info(self.driver.current_url) 
        WebDriverWait(
            self.driver, 5
        ).until(
            EC.presence_of_element_located((By.XPATH, self.config.SEARCH_BAR))
        )
        # Loop through partners
        for partner, coordinates in zip(self.config.PARTNERS, list_coordinates):
            # Find search bar and send partner ID
            self.driver.find_element(by=By.XPATH, value=self.config.SEARCH_BAR).send_keys(partner)
            # Tick name below
            mouseover_coordinates(self.driver, offset_from_element, coordinates)
            # Delete search bar before starting a new search
            self.driver.find_element(by=By.XPATH, value=self.config.SEARCH_BAR_CLEARED).click()

    def submit(self):
        """Submit booking"""
        # TODO : Add a timer to wait for the booking to be available
        self.driver.find_element(by=By.XPATH, value=self.config.SUBMIT_BUTTON).click()

def main(Config, club_name, date, court_id):
    # Launch the Chrome browser
    with webdriver.Chrome(options = chrome_options) as driver:
        try:
            # Initialize bot
            self = BookingBot(Config, driver, logger)
            # Open session
            self.open_session(club_name)
            # Navigate to the login page
            self.login()
            # Switch booking slots page
            self.switch_url(date, court_id)
            # Slot page
            self.select_slots(offset_from_element=(By.ID, 'widget-home'), coordinates=(200, 445))
            # Partners
            self.select_partners(offset_from_element=(By.ID, 'widget-menu'), list_coordinates=[(400, 238), (548, 322)])
            # Select names
            print(datetime.today())
            self.submit()
            # log
            logger.info('Success! You have booked a court.') 
        except Exception:
            logger.info('OOOPS! Please check it out.')