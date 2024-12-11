from start_drive import start_drive
from dotenv import load_dotenv

import os

load_dotenv()

def ct0001() -> None:
    browser = start_drive()

    url_page = 'http://sga.leiteviana.com:8080/'
    browser.get(url_page)

    xpath_register_link = '/html/body/div/div/div/form/div[3]/a'
    button_register_link = browser.find_element('xpath', xpath_register_link)
    button_register_link.click()

    xpath_email_field = '//*[@id="email"]'
    email_field = browser.find_element('xpath', xpath_email_field)
    email_field.send_keys(os.getenv('emailCT001'))

    xpath_username_field = '//*[@id="user"]'
    username_field = browser.find_element('xpath', xpath_username_field)
    username_field.send_keys(os.getenv('usernameCT001'))

    xpath_password_field = '//*[@id="senha"]'
    password_field = browser.find_element('xpath', xpath_password_field)
    password_field.send_keys(os.getenv('passwordCT001'))

    xpath_register_button = '/html/body/div[1]/div/div/form/button'
    register_button = browser.find_element('xpath', xpath_register_button)
    register_button.click()

ct0001()