import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)
import os
import sys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from isInCustomList import isInCustomList
from list import ecslist, unilist, genderlist, racelist, majorlist

def scrape_gender(driver):
    try: 
        gender = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH,'//shreddit-post/descendant::p[contains(.,"Gender:") or contains(.,"gender:")]'))).get_attribute('innerText')
    except TimeoutException: 
        try: 
            gender = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH,'//shreddit-post/descendant::p[contains(.,"emographics")]'))).get_attribute('innerText')
        except TimeoutException: 
            return 'Other/LGBTQ+'
    gender= gender.lower().partition("gender")

    if not gender[2]: 
        gender = gender[0].lower().partition("demographics")  

    if any(a in gender[2] for a in genderlist[1]): 
        gender = 'Female'
    elif any(b in gender[2] for b in genderlist[0]): 
        gender = 'Male'
    else: 
        gender = 'Other/LGBTQ+'
        
    return gender
    