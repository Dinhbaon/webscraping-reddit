import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidArgumentException
import re
import numpy as np
from list import ecslist, unilist, genderlist, racelist, majorlist

dftotal = pd.DataFrame()

options = Options()
options.headless = True
options.add_argument("--disable-web-security") 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--start-maximized")
options.add_argument("--enable-automation")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-gpu")
options.add_argument('--blink-settings=imagesEnabled=false')
driver  = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options = options)

filteredlinkscsv =  pd.read_csv("./csvfiles/newfilteredlinks.csv")
filteredlinks = filteredlinkscsv.iloc[:,1].to_list()

existing_processed_data = pd.read_csv("./csvfiles/processeddata.csv")

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


numofloops = len(filteredlinks)
appended_data = pd.DataFrame([])
for i in range(numofloops): 
    try:
        if(filteredlinks[i]):
            print(filteredlinks[i])
            print(i)
            driver.get(filteredlinks[i])
            # https://www.reddit.com/r/collegeresults/comments/tvk76r/a_roller_coaster_ride_with_a_happy_outcome/
            url = [] 
            print(f'the links is {filteredlinks[i]}')
            url.append(filteredlinks[i])


            try: 
                scrape_rejects = driver.find_elements(By.XPATH,'//div[@class="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4"]/descendant::p[preceding::*[contains(.,"Waitlist") or contains(.,"Reject") or contains(.,"Rejections") or contains(.,"Denied")]or self::p[contains(.,"Waitlist") or contains(.,"Reject") or contains(.,"Denied")]]')
            except NoSuchElementException: 
                scrape_rejects = [' ']
            try: 
                scrape_accept = driver.find_elements(By.XPATH,'//div[@class="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4"]/descendant::p[preceding::*[contains(.,"Acceptance") or contains(.,"Accept")]or self::p[contains(.,"Acceptance") or contains(.,"Accept")]]')
            except NoSuchElementException: 
                scrape_accept = [' ']
                
                
            try: 
                full_post = driver.find_element(By.XPATH,'//div[@class="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root"]').text
            except NoSuchElementException: 
                full_post = '[]'
            
            try: 
                gender = driver.find_element(By.XPATH,'//div[@class="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4"]/descendant::p[contains(.,"Gender:") or contains(.,"gender:")]').text
            except NoSuchElementException: 
                # gender.append("[]")
                try: 
                    gender = driver.find_element(By.XPATH,'//div[@class="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4"]/descendant::p[contains(.,"emographics")]').text
                except NoSuchElementException: 
                    gender = "[]"
                    
        
            try: 
                driver.implicitly_wait(1)
                SAT = driver.find_element(By.XPATH,'//div[@class="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root"]//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(.,"SAT") or contains(.,"SAT I")]').text
            except NoSuchElementException: 
                SAT = ("[]")
        
            try: 
                driver.implicitly_wait(1)
                ACT = driver.find_element(By.XPATH,'//div[@class="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root"]//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(.,"ACT")]').text
            except NoSuchElementException: 
                ACT = "[]"
        
            try: 
                race = driver.find_element(By.XPATH,'//div[@class="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4"]/descendant::p[contains(.,"Race") or contains(.,"Ethnicity")]').text
            except NoSuchElementException:
                race = "[]"
                # try: 
                #     race.append(driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(.,"emographics")]'))
                # except NoSuchElementException: 
                    
            
            # try:
            #     hooks.append(driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(text(),"Hooks:") or contains(text(),"hooks:") or contains(text(),"Hooks (Recruited Athlete, URM, First-Gen, Geographic, Legacy, etc.):")]').text)
            # except  NoSuchElementException: 
            #     hooks.append("")
            
        
            try: 
                major = driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(.,  "Intended Major") or contains(., "Major:") or contains(.,"major")] ').text
            except  NoSuchElementException:
                major = "[[]]"
                
        

            ## append text in to list (make webobject into text)
    
        
            scrape_rejects = list(map(lambda x : x.text.lower(), scrape_rejects))
            
            scrape_accept = list(map(lambda x:x.text.lower(), scrape_accept))

            #filter out paragraphs
            scrape_rejects = list(filter(lambda x : len(x)<200,scrape_rejects))
            scrape_accept  = list(filter(lambda x : len(x)<200,scrape_accept))

            if len(scrape_accept)>1: 
                for element in range(len(scrape_accept)): 
                    print(scrape_accept[element])
                    if re.match('rejections',scrape_accept[element]) or re.match('defer', scrape_accept[element]) or re.match('waitlist',scrape_accept[element]) or re.match('to be determined',scrape_accept[element]) or re.match('waiting', scrape_accept[element]) or re.match('denied', scrape_accept[element]): 
                        scrape_accept  =scrape_accept[0:element]
                        break
        
            if len(scrape_rejects)>1: 
                for element in range(len(scrape_rejects)): 
                    if re.match('additional info.',scrape_rejects[element]) or re.match('accept', scrape_rejects[element]) or re.match('final thoughts',scrape_rejects[element]): 
                        scrape_rejects  =scrape_rejects[0][0:element]
                        break

            #check all unis in the post       
            proacceptances = []
            for i in range(len(unilist)):
                if not scrape_accept: 
                    scrape_accept = ''
                if any(a in ' '.join(map(str, scrape_accept))for a in unilist[i]): 
                    proacceptances.append(unilist[i][0])
            scrape_accept = proacceptances


        
            prorejectsonly = []
            for i in range(len(unilist)):
                if not scrape_rejects: 
                    scrape_rejects=''
                if any(b in ' '.join(map(str, scrape_rejects)) for b in unilist[i]): 
                    prorejectsonly.append(unilist[i][0])
            scrape_rejects = prorejectsonly


            #filter unis in post with rejections
        
            scrape_accept = list(set(scrape_accept)-set(scrape_rejects))
            gender= gender.lower().partition("gender") 
        
            if not gender[2]: 
                gender = gender[0].lower().partition("demographics") 
            SAT = SAT.partition("SAT")
            ACT = ACT.partition("ACT")
            race = race.lower().partition('race')
            # if not race[0][2]: 
            #     race[0] = race[0].lower().partition("demographics")
            major = major.lower().partition('major')
    ## make in to dictionary
            submajor = []
            for j in range(len(majorlist)):
                if any(a in major[2] for a in majorlist[j]): 
                    submajor.append(majorlist[j][0])
            major = submajor
        
            subecs = []



            for j in range(len(ecslist)):
                if any(a in full_post.lower() for a in ecslist[j]): 
                    subecs.append(ecslist[j][0])

            full_post = subecs
            # print(full_post[0])
            # print(final_ecs)



            if any(a in gender[2] for a in genderlist[1]): 
                gender = 'Female'
            elif any(b in gender[2] for b in genderlist[0]): 
                gender = 'Male'
            else: 
                gender = 'Other/LGBTQ+'
        
        
                    
        
            race = ([i for i in racelist if i in race[2]])
                    
            try: 
                SAT = int(re.findall("[1][0-6][0-9][0-9]", SAT[2])[0])
            except: 
                SAT = ' '

            try: 
                ACT = (re.search(r"\b[2-3]{1}[0-6]{1}\s",ACT[2]).group(0))
            except: 
                ACT  = ''
            student = Student([gender],[race], [major], [SAT], [ACT], [full_post], [scrape_accept], [scrape_rejects],url).__dict__

            dftotal = dftotal.append(pd.DataFrame.from_dict(student))

            list(np.array(filteredlinks)[[x for x in dftotal.index.tolist()]])
            dftotal = dftotal.astype(str).replace(["[]",' ',''], np.nan)
            dftotal = dftotal.dropna(thresh=6 )
            dftotal = dftotal.replace(np.nan,'[]',regex=True)

        else: 
            continue
    except InvalidArgumentException:
        continue
        


existing_processed_data = existing_processed_data.iloc[:, 1: ]
newdata = pd.DataFrame(np.concatenate([dftotal,existing_processed_data]))
newdata.to_csv('./csvfiles/processeddata.csv', header=None)