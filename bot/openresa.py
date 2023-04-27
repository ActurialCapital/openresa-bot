from datetime import datetime, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from apscheduler.schedulers.blocking import BlockingScheduler

from bot.utils import logging_options, chrome_options
from bot.config import Config

logger = logging_options()
chrome_options = chrome_options()

def mouseover_coordinates(driver, offset_from_element, coordinates):
    """Locate items with coordinates"""
    # Chain actions
    actions = ActionChains(driver)
    # Initial coordinates
    WebDriverWait(
        driver, 10
    ).until(
        EC.presence_of_element_located(
            (offset_from_element[0], offset_from_element[1])
        )
    )
    base_coordinates = driver.find_element(offset_from_element[0], offset_from_element[1])
    xi, yi = base_coordinates.location["x"], base_coordinates.location["y"]
    # Offset from base coordinates
    actions.move_to_element_with_offset(base_coordinates, -xi, -yi)
    # Move and click to located point
    actions.move_by_offset(coordinates[0], coordinates[1]).click().perform()

class BookingBot:
    def __init__(self, driver):
        self.driver = driver

    def open_session(self, club_name):
        """First step, open session via URL"""
        url = Config.URL.format(club_name=club_name)
        self.driver.get(url)
        WebDriverWait(
            self.driver, 10
        ).until(
            EC.url_matches(url)
        )
        logger.info(f'Connection to {url}') 
        logger.info(f'Login page loaded') 
        logger.info(f'Current page is {self.driver.current_url}') 

    def login(self):
        """Login website"""
        # Enter login credentials
        self.driver.find_element(by=By.XPATH, value=Config.USERNAME_INPUT_XPATH).send_keys(Config.USERNAME)
        logger.info('Username entered') 
        # Enter passward
        self.driver.find_element(by=By.XPATH, value=Config.PASSWORD_INPUT_XPATH).send_keys(Config.PASSWORD)
        logger.info('Password entered') 
        # Submit the form
        self.driver.find_element(by=By.XPATH, value=Config.LOGIN_BUTTON_XPATH).click()
        logger.info('Login submitted') 

    def switch_url(self, date, court_id):
        """Switch to the booking page"""
        scheduled_url = Config.URL_SCHEDULED.format(date=date, court_id=court_id)
        while self.driver.current_url != scheduled_url:
            # Refresh page if not on the right page
            logger.info(f'Connection to {scheduled_url}') 
            self.driver.get(scheduled_url)
            WebDriverWait(
                self.driver, 10
            ).until(
                EC.url_matches(scheduled_url)
            )
            logger.info(f'Current page is {self.driver.current_url}') 


    def select_slots(self, slot, offset_from_element):
        """Book court with x and y coordinates"""
        coordinates = Config.SLOTS[slot]
        mouseover_coordinates(self.driver, offset_from_element, coordinates)
        logger.info(f'Slot selected') 

    def wait_partner_page_loaded(self, date, court_id):
        url = Config.URL_PARTNERS.format(date=date, court_id=court_id)
        WebDriverWait(
            self.driver, 10
        ).until(
            EC.url_matches(url)
        )
        logger.info('Partners page loaded') 
        logger.info(f'Current page is {self.driver.current_url}') 

    def select_partners(self, offset_from_element, list_coordinates):
        """Select members (minimum 2)"""
        # Wait for search bar to be loaded
        WebDriverWait(
            self.driver, 10
        ).until(
            EC.presence_of_element_located(
                (By.XPATH, Config.SEARCH_BAR_XPATH)
            )
        )
        logger.info('Search bar loaded') 
        # Loop through partners
        logger.info('Selecting partners...') 
        for partner, coordinates in zip(Config.PARTNERS, list_coordinates):
            # Find search bar and send partner ID
            self.driver.find_element(by=By.XPATH, value=Config.SEARCH_BAR_XPATH).send_keys(partner)
            # Tick name below
            mouseover_coordinates(self.driver, offset_from_element, coordinates)
            # Delete search bar before starting a new search
            self.driver.find_element(by=By.XPATH, value=Config.SEARCH_BAR_CLEARED_XPATH).click()
        logger.info('Partners selected')

    def submit(self):
        """Submit booking"""
        # Submit booking
        self.driver.find_element(by=By.XPATH, value=Config.SUBMIT_BUTTON_XPATH).click()
        logger.info('Booking submitted')

    def scheduled_submit(self, hour=17, minute=0, second=0, timezone='Europe/Paris'):
        """Submit booking"""
        # Add a timer to wait for the booking to be available
        run_date = datetime.combine(datetime.today(), time(hour=hour, minute=minute, second=second))
        sched = BlockingScheduler(timezone=timezone)
        sched.add_job(self.submit, run_date=run_date)
        # Starts the Scheduled jobs
        logger.info(f'Job ready to execute at {run_date}, in progress...')
        sched.start() 
        logger.info(f'Job exectuted at {datetime.today()}')

def main(
        club_name: str, 
        date: str, 
        court_id: str,
        slot: str, 
        hour: int, 
        minute: int, 
        second: int,
        timezone: str
):
    # Launch the Chrome browser
    with webdriver.Chrome(options = chrome_options) as driver:
        # try:
        # driver = webdriver.Chrome()
        # Initialize bot
        self = BookingBot(driver)
        # Open session
        self.open_session(club_name)
        # Navigate to the login page
        self.login()
        # Switch booking slots page
        self.switch_url(date, court_id)
        # Slot page
        self.select_slots(slot, offset_from_element=(By.ID, 'widget-home'))
        # wait for partners page to be loaded
        self.wait_partner_page_loaded(date, court_id)
        # Partners page?
        if self.driver.current_url != Config.URL_PARTNERS.format(date=date, court_id=court_id):
            logger.info(f'Connection failed to reach the partners page. Court {court_id} is currently not available.') 
            # Stop the bot
            logger.info('OOOPS! Booking failed.')
        else:
            # Select partners
            self.select_partners(offset_from_element=(By.ID, 'widget-menu'), list_coordinates=[(400, 238), (548, 322)])
            # scheduled booking and submit
            self.scheduled_submit(hour, minute, second, timezone)
            # log
            logger.info('Success! Booking done.') 