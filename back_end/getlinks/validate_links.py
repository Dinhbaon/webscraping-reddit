import urllib.request, json 
import pandas as pd
import time 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time 

options = Options()
options.headless = True
options.add_argument("--disable-web-security") 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
service = Service()
driver = webdriver.Chrome(service=service, options=options)


def isValidPost(link : str):
    driver.get(link)
    try:
        driver.find_element(By.XPATH,"//div[contains(text(),'Sorry, this post was deleted by') or contains(text(),'Moderators remove posts from feeds for a variety of reasons') or contains(text(),'automated bots frequently filter posts') or contains(text(),'[deleted]')]")
    except NoSuchElementException:
        return True
    return False