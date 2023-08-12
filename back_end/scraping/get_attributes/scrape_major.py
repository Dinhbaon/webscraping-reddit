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
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from isInCustomList import isInCustomList
from list import ecslist, unilist, genderlist, racelist, majorlist

def scrape_major(driver):

    try: 
        major = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH,'//shreddit-post/descendant::p[contains(.,  "Intended Major") or contains(., "Major:") or contains(.,"major")] '))).get_attribute('innerText')
    except  TimeoutException:
        return 

    major = major.lower().partition('major')

    ## make in to dictionary
    return isInCustomList(majorlist, major)