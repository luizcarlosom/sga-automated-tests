from start_drive import start_drive
from dotenv import load_dotenv
import os

load_dotenv()

def ct0003() -> None:
    browser = start_drive()

    url_page = 'http://sga.leiteviana.com:8080/'
    browser.get(url_page)

    # CT001
    xpath_register_link = '/html/body/div/div/div/form/div[3]/a'
    button_register_link = browser.find_element('xpath', xpath_register_link)
    button_register_link.click()

    xpath_email_field = '//*[@id="email"]'
    email_field = browser.find_element('xpath', xpath_email_field)
    email_field.send_keys(os.getenv('emailCT003'))

    xpath_username_field = '//*[@id="user"]'
    username_field = browser.find_element('xpath', xpath_username_field)
    username_field.send_keys(os.getenv('usernameCT003'))

    xpath_password_field = '//*[@id="senha"]'
    password_field = browser.find_element('xpath', xpath_password_field)
    password_field.send_keys(os.getenv('passwordCT003'))

    xpath_register_button = '/html/body/div[1]/div/div/form/button'
    register_button = browser.find_element('xpath', xpath_register_button)
    register_button.click()
    
    # CT002

    xpath_username_field = '//*[@id="user"]'
    username_field = browser.find_element('xpath', xpath_username_field)
    username_field.send_keys(os.getenv('usernameCT003'))

    xpath_password_field = '//*[@id="senha"]'
    password_field = browser.find_element('xpath', xpath_password_field)
    password_field.send_keys(os.getenv('passwordCT003'))

    xpath_login_button = '/html/body/div[1]/div/div/form/button'
    login_button = browser.find_element('xpath', xpath_login_button)
    login_button.click()

    # CT003

    xpath_register_student_link = '/html/body/section/div[2]/div/div[1]/a'
    register_student_link = browser.find_element('xpath', xpath_register_student_link)
    register_student_link.click()

    xpath_student_name = '//*[@id="nome"]'
    register_student_name = browser.find_element('xpath', xpath_student_name)
    register_student_name.send_keys('luizin')

    xpath_generate_matricula_button = '/html/body/div[1]/form/div[3]/div/button'
    generate_matricula_button = browser.find_element('xpath', xpath_generate_matricula_button)
    generate_matricula_button.click()

    xpath_save_student_button = '/html/body/div[1]/form/div[6]/button'
    save_student_button = browser.find_element('xpath', xpath_save_student_button)
    save_student_button.click()

    xpath_edit_student_button = '/html/body/div/table/tbody/tr[1]/td[6]/a[1]'
    edit_student_button = browser.find_element('xpath', xpath_edit_student_button)
    edit_student_button.click()

    xpath_student_name = '//*[@id="nome"]'
    register_student_name = browser.find_element('xpath', xpath_student_name)
    register_student_name.send_keys('vai ser apagado')

    xpath_save_student_button = '/html/body/div[1]/form/div[6]/button'
    save_student_button = browser.find_element('xpath', xpath_save_student_button)
    save_student_button.click()

    xpath_delete_student_button = '/html/body/div/table/tbody/tr[1]/td[6]/a[2]'
    delete_student_button = browser.find_element('xpath', xpath_delete_student_button)
    delete_student_button.click()

ct0003()