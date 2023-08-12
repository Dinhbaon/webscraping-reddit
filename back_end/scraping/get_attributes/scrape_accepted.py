
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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from isInCustomList import isInCustomList
from list import ecslist, unilist, genderlist, racelist, majorlist
def scrape_accepted(driver, scrape_rejected):

    try: 
        scrape_accepts = WebDriverWait(driver, 2).until(
        EC.presence_of_all_elements_located((By.XPATH,'//shreddit-post/descendant::p[preceding::*[contains(.,"Acceptance") or contains(.,"Accept")]or self::p[contains(.,"Acceptance") or contains(.,"Accept")]]')))
    except TimeoutException:
        return
    #convert to text
    scrape_accepts = [acceptances.get_attribute('innerText').lower() for acceptances in scrape_accepts]

    #filter out paragraphs 
    scrape_accepts = list(filter(lambda x : len(x)<200,scrape_accepts))

    for index in range(len(scrape_accepts)):    
        if re.match('rejections',scrape_accepts[index]) or re.match('defer', scrape_accepts[index]) or re.match('waitlist',scrape_accepts[index]) or re.match('to be determined',scrape_accepts[index]) or re.match('waiting', scrape_accepts[index]) or re.match('denied', scrape_accepts[index]): 
            break

    if scrape_rejected == None:
        return isInCustomList(unilist, scrape_accepts)
    #make sure nothing on accept list is also on reject list
    return list(set(isInCustomList(unilist, scrape_accepts)) - set(scrape_rejected))