from dataclasses import dataclass
from decouple import config as env_config

@dataclass
class Config:
    URL = "https://ballejaune.com/club/{club_name}"
    USERNAME_INPUT_XPATH = '//*[@id="form-username"]'
    PASSWORD_INPUT_XPATH = '//*[@id="form-password"]'
    USERNAME = env_config('USERNAME')
    PASSWORD = env_config('PASSWORD')
    LOGIN_BUTTON_XPATH = '//*[@id="auth-form"]/div[4]/div[2]/button'
    URL_SCHEDULED = 'https://ballejaune.com/reservation/week#action=0&date={date}&panel=0&schedule={court_id}'
    URL_PARTNERS = 'https://ballejaune.com/reservation/week#action=1&date={date}&panel=0&schedule={court_id}'
    SEARCH_BAR_XPATH = '//*[@id="members-table-search"]/input'
    SEARCH_BAR_CLEARED_XPATH = '//*[@id="members-table-search"]/div[2]/div[1]/i'
    SUBMIT_BUTTON_XPATH = '//*[@id="reservation-toolbar-buttons"]/div/div/div[2]/button'
    
    PARTNERS = [
        '1502845', # 'CHOUISSA, Alexandre': 
        '1487058', # 'RFID, 1': 
        # '1388390', # 'MEILHOC, Benjamin'

    ]
    SLOTS = {
        '8:00-9:30':   (200, 185),
        '9:30-11:00':  (200, 250),
        '11:00-12:30': (200, 315),
        '12:30-14:00': (200, 380),
        '14:00-15:30': (200, 440),
        '15:30-17:00': (200, 500),
        '17:00-18:30': (200, 565),
        '18:30-20:00': (200, 630),
        '20:00-21:30': (200, 700),

    }