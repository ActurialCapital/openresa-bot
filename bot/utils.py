
import logging 
from selenium import webdriver
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

########################
# Logging functionality
########################

class FilterLogging(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level
    
def logging_options():
    # Create a logger
    logger = logging.getLogger('bot - logs')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('logs.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Set filter to log only INFO lines
    handler.addFilter(FilterLogging(logging.INFO))
    logger.addHandler(handler)
    
    return logger

#######################
# Chrome functionality
#######################

def chrome_options():
    """Set chrome options"""
    try:
        display = Display(visible=0, size=(800, 800))  
        display.start()
        # Check if the current version of chromedriver exists
        # and if it doesn't exist, download it automatically,
        # then add chromedriver to path
        chromedriver_autoinstaller.install()  
        # Create a new instance of Chrome
        chrome_options = webdriver.ChromeOptions()    
        # Add your options as needed    
        for option in [
                "--window-size=1200,1200", #"--window-size=1920,1200",
                "--ignore-certificate-errors"
                #"--headless",
                #"--disable-gpu",
                #"--disable-extensions",
                #"--no-sandbox",
                #"--disable-dev-shm-usage",
                #'--remote-debugging-port=9222'
            ]:
            chrome_options.add_argument(option)
    except:
        chrome_options = None
    return chrome_options