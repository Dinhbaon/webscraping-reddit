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

def scrape_SAT(driver):
    try: 
        SAT = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//shreddit-post//p[contains(.,"SAT") or contains(.,"SAT I")]'))).get_attribute('innerText')
    except TimeoutException: 
        return 

    SAT = SAT.partition("SAT")

    print(SAT)

    try:
        SAT = int(re.findall("[1][0-6][0-9][0-9]", SAT[2])[0])
    except:
        return

    return SAT
