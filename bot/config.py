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
    PARTNERS = ['1502845', '1487058']