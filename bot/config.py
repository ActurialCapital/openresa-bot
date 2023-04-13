from dataclasses import dataclass

@dataclass
class Config:
    URL = "https://ballejaune.com/club/{club_name}"
    USERNAME_INPUT = '//*[@id="form-username"]'
    PASSWORD_INPUT = '//*[@id="form-password"]'
    CONNECTION_BUTTON = '//*[@id="auth-form"]/div[4]/div[2]/button'
    URL_SCHEDULED = 'https://ballejaune.com/reservation/week#action=0&date={date}&panel=0&schedule={court_id}'
    SEARCH_BAR = '//*[@id="members-table-search"]/input'
    SEARCH_BAR_CLEARED = '//*[@id="members-table-search"]/div[2]/div[1]/i'
    SUBMIT_BUTTON = '//*[@id="reservation-toolbar-buttons"]/div/div/div[2]/button'
    PARTNERS = ['1502845', '1487058']