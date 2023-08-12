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
import re
from isInCustomList import isInCustomList

def scrape_ACT(driver):
    try: 
        ACT = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH,'//shreddit-post//p[contains(.,"ACT")]'))).get_attribute('innerText')
    except TimeoutException: 
        return 
    
    ACT = ACT.partition("ACT")

    try: 
        ACT = (re.search(r"\b[2-3]{1}[0-6]{1}\s",ACT[2]).group(0))
    except: 
        return
    
    return ACT
