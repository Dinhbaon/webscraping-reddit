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
from list import ecslist, unilist, genderlist, racelist, majorlist

def scrape_race(driver):
    try: 
        race = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH,'/shreddit-post//descendant::p[contains(.,"Race") or contains(.,"Ethnicity")]'))).get_attribute('innerText')
    except TimeoutException:
        return

    race = race.lower().partition('race')

    race = ([i for i in racelist if i in race[2]])

    return race