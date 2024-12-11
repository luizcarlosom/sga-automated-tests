from start_drive import start_drive
from dotenv import load_dotenv
import os

load_dotenv()

def ct0002() -> None:
    browser = start_drive()

    url_page = 'http://sga.leiteviana.com:8080/'
    browser.get(url_page)

    xpath_username_field = '//*[@id="user"]'
    username_field = browser.find_element('xpath', xpath_username_field)
    username_field.send_keys(os.getenv('usernameCT002'))

    xpath_password_field = '//*[@id="senha"]'
    password_field = browser.find_element('xpath', xpath_password_field)
    password_field.send_keys(os.getenv('passwordCT002'))

    xpath_login_button = '/html/body/div[1]/div/div/form/button'
    login_button = browser.find_element('xpath', xpath_login_button)
    login_button.click()

ct0002()