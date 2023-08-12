import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.support.ui import WebDriverWait
import numpy as np
from get_attributes.scrape_ACT import scrape_ACT
from get_attributes.scrape_SAT import scrape_SAT
from get_attributes.scrape_accepted import scrape_accepted
from get_attributes.scrape_ec import scrape_ec
from get_attributes.scrape_gender import scrape_gender
from get_attributes.scrape_major import scrape_major
from get_attributes.scrape_race import scrape_race
from get_attributes.scrape_rejected import scrape_rejected
from list import ecslist, unilist, genderlist, racelist, majorlist

dftotal = pd.DataFrame()

options = Options()
options.headless = True
options.add_argument("--disable-web-security") 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
service = Service()
driver = webdriver.Chrome(service=service, options=options)


filteredlinkscsv =  pd.read_csv("../csvfiles/newfilteredlinks.csv", header=None)
filteredlinks = filteredlinkscsv.iloc[:,1].to_list()

existing_processed_data = pd.read_csv("../csvfiles/processeddata.csv", header=None)

class Student: 
    def __init__(self,Gender,Race,Major,SAT,ACT,Extracurriculars,Acceptances,Rejections,url): 
        self.Gender = Gender
        self.Race = Race
        self.Major = Major
        self.SAT = SAT
        self.ACT = ACT
        self.extracurriculars = Extracurriculars
        self.Acceptances = Acceptances
        self.Rejections = Rejections
        self.url = url


appended_data = pd.DataFrame([])
for link in filteredlinks: 
    try:
        if(link):
            driver.get(link)

            print(link)

            url =link

            rejections = scrape_rejected(driver)

            acceptances = scrape_accepted(driver, rejections)
                
            ecs = scrape_ec(driver)
            
            gender = scrape_gender(driver)
            
            SAT = scrape_SAT(driver)
        
            ACT = scrape_ACT(driver)

            race = scrape_race(driver)
            
            major = scrape_major(driver)
                    
            student = Student([gender],[race], [major], [SAT], [ACT], [ecs] , [acceptances], [rejections],[url]).__dict__

            df = pd.DataFrame.from_dict(student)
            df = df.astype(str).replace(["[]",' ','', 'None'], np.nan)
            df = df.dropna(thresh=6 )
            df = df.replace(np.nan,'[]',regex=True)
            pd.concat([dftotal, df])


        else: 
            continue
    except InvalidArgumentException:
        continue
        
existing_processed_data = existing_processed_data.iloc[:, 1: ]
newdata = pd.concat(existing_processed_data, dftotal)
newdata.to_csv('./csvfiles/processeddata.csv', header=None)