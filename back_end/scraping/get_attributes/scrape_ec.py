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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from isInCustomList import isInCustomList
from list import ecslist, unilist, genderlist, racelist, majorlist

def scrape_ec(driver):
    try: 
        full_post = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH,'//div[@class="mb-sm mb-xs px-md xs:px-0"]'))).get_attribute('innerText')
    except TimeoutException: 
        return
    subecs = []

    for j in range(len(ecslist)):
        if any(a in full_post.lower() for a in ecslist[j]): 
            subecs.append(ecslist[j][0])
    return subecs
