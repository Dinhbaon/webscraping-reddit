# getting the name of the directory
# where the this file is present.
import os
import sys


current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from isInCustomList import isInCustomList 
from list import ecslist, unilist, genderlist, racelist, majorlist
import time
def scrape_rejected(driver):

    try:
        scrape_rejects =WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH,'//shreddit-post/descendant::p[preceding::*[contains(.,"Waitlist") or contains(.,"Reject") or contains(.,"Rejections") or contains(.,"Denied")]or self::p[contains(.,"Waitlist") or contains(.,"Reject") or contains(.,"Denied")]]')))
    except TimeoutException:
        return
    #convert to text
    
    scrape_rejects = [rejections.get_attribute('innerText').lower() for rejections in scrape_rejects]

    #filter out paragraphs 
    scrape_rejects = list(filter(lambda x : len(x)<200,scrape_rejects))

    for index in range(len(scrape_rejects)):    
        if re.match('additional info.',scrape_rejects[index]) or re.match('accept', scrape_rejects[index]) or re.match('final thoughts',scrape_rejects[index]): 
            scrape_rejects  =scrape_rejects[0:index]
            break

    return isInCustomList(unilist, scrape_rejects)
