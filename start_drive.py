from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def start_drive() -> webdriver:
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    service = Service(ChromeDriverManager().install())

    browser = webdriver.Chrome(service=service, options=chrome_options)

    return browser
