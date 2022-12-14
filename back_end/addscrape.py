import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import re
import numpy as np
from list import ecslist, unilist, genderlist, racelist, majorlist

dftotal = pd.DataFrame(columns=['Gender','Race','Major','SAT','ACT','Extracurriculars','Acceptances','Rejections','url'])

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


numofloops = len(filteredlinks)
appended_data = pd.DataFrame([])
for i in range(numofloops): 

        driver.get(filteredlinks[i])
        # https://www.reddit.com/r/collegeresults/comments/tvk76r/a_roller_coaster_ride_with_a_happy_outcome/
        url = [] 
        print(f'the links is {filteredlinks[i]}')
        url.append(filteredlinks[i])
        final_accept = []
        final_reject = []
        final_gender = []
        final_race=[]
        final_major=[]
        final_sat = []
        final_act=[]
        final_ecs = []
        accepts = []
        prohook = []
        major = []
        rejectlist = []
        prorejects = []
        proacceptances = []
        rejectsonly = []
        acceptsonly = []
        scrape_rejects = []
        scrape_accept = []
        gender =[]       
        race = []
        SAT = []
        ACT = []
        full_post = []


        try: 
            scrape_rejects = driver.find_elements(By.XPATH,'//div[@class="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4"]/descendant::p[preceding::*[contains(.,"Waitlist") or contains(.,"Reject") or contains(.,"Rejections") or contains(.,"Denied")]or self::p[contains(.,"Waitlist") or contains(.,"Reject") or contains(.,"Denied")]]')
        except NoSuchElementException: 
            scrape_rejects = [' ']
        try: 
            scrape_accept = driver.find_elements(By.XPATH,'//div[@class="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4"]/descendant::p[preceding::*[contains(.,"Acceptance") or contains(.,"Accept")]or self::p[contains(.,"Acceptance") or contains(.,"Accept")]]')
        except NoSuchElementException: 
            scrape_accept = [' ']
            
            
        try: 
            full_post.append(driver.find_element(By.XPATH,'//div[@class="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root"]').text)
        except NoSuchElementException: 
            full_post = [' ']
        
        try: 
            gender.append(driver.find_element(By.XPATH,'//div[@class="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4"]/descendant::p[contains(.,"Gender:") or contains(.,"gender:")]').text)
        except NoSuchElementException: 
            # gender.append("[]")
            try: 
                gender.append(driver.find_element(By.XPATH,'//div[@class="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4"]/descendant::p[contains(.,"emographics")]').text)
            except NoSuchElementException: 
                gender.append("[]")
                
       
        try: 
            driver.implicitly_wait(1)
            SAT.append(driver.find_element(By.XPATH,'//div[@class="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root"]//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(.,"SAT") or contains(.,"SAT I")]').text)
        except NoSuchElementException: 
            SAT.append("")
       
        try: 
            driver.implicitly_wait(1)
            ACT.append(driver.find_element(By.XPATH,'//div[@class="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root"]//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(.,"ACT")]').text)
        except NoSuchElementException: 
            ACT.append("")
       
        try: 
            race.append(driver.find_element(By.XPATH,'//div[@class="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4"]/descendant::p[contains(.,"Race") or contains(.,"Ethnicity")]').text)
        except NoSuchElementException:
            race.append(" ")
            # try: 
            #     race.append(driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(.,"emographics")]'))
            # except NoSuchElementException: 
                
        
        # try:
        #     hooks.append(driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(text(),"Hooks:") or contains(text(),"hooks:") or contains(text(),"Hooks (Recruited Athlete, URM, First-Gen, Geographic, Legacy, etc.):")]').text)
        # except  NoSuchElementException: 
        #     hooks.append("")
        
       
        try: 
            major.append(driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(.,  "Intended Major") or contains(., "Major:") or contains(.,"major")] ').text)
        except  NoSuchElementException:
            major.append("") 
            
    

        ## append text in to list (make webobject into text)
 
        for elementp in scrape_rejects: 
            prorejects.append(elementp.text.lower())
        for elementp in scrape_accept: 
            proacceptances.append(elementp.text.lower())

        #filter out paragraphs
        rejectsonly.append(list(filter(lambda x : len(x)<200,prorejects)))
        acceptsonly.append(list(filter(lambda x : len(x)<200,proacceptances)))
        print(acceptsonly)
        if len(acceptsonly[0])>1: 
            for element in range(len(acceptsonly[0])): 
                print(acceptsonly[0][element])
                if re.match('rejections',acceptsonly[0][element]) or re.match('defer', acceptsonly[0][element]) or re.match('waitlist',acceptsonly[0][element]) or re.match('to be determined',acceptsonly[0][element]) or re.match('waiting',acceptsonly[0][element]) or re.match('denied', acceptsonly[0][element]): 
                    acceptsonly  =acceptsonly[0][0:element]
                    break
       
        if len(rejectsonly[0])>1: 
            for element in range(len(rejectsonly[0])): 
                if re.match('additional info.',rejectsonly[0][element]) or re.match('accept.',rejectsonly[0][element]) or re.match('final thoughts',rejectsonly[0][element]): 
                    rejectsonly  =rejectsonly[0][0:element]
                    break

        #check all unis in the post       
        prouni = []
        prouniappend = []
        for i in range(len(unilist)):
            if not acceptsonly: 
                acceptsonly.append('')
            if any(a in ' '.join(map(str, acceptsonly))for a in unilist[i]): 
                prouniappend.append(unilist[i][0])
        prouni.append(prouniappend)


    
        prorejectsonly = []
        for i in range(len(unilist)):
            if not rejectsonly: 
                rejectsonly.append('')
            if any(b in ' '.join(map(str, rejectsonly)) for b in unilist[i]): 
                prorejectsonly.append(unilist[i][0])
        rejectlist.append(prorejectsonly)


        #filter unis in post with rejections
      
        accepts.append(list(set(prouni[0])-set(rejectlist[0])))
        gender[0] = gender[0].lower().partition("gender") 
       
        if not gender[0][2]: 
            gender[0] = gender[0][0].lower().partition("demographics") 
        SAT[0] = SAT[0].partition("SAT")
        ACT[0] = ACT[0].partition("ACT")
        race[0] = race[0].lower().partition('race')
        # if not race[0][2]: 
        #     race[0] = race[0].lower().partition("demographics")
        major[0] = major[0].lower().partition('major')
## make in to dictionary
        submajor = []
        for j in range(len(majorlist)):
            if any(a in major[0][2] for a in majorlist[j]): 
                submajor.append(majorlist[j][0])
        final_major.append(submajor)
    
        subecs = []



        for j in range(len(ecslist)):
            if any(a in full_post[0].lower() for a in ecslist[j]): 
                subecs.append(ecslist[j][0])

        final_ecs.append(subecs)
        # print(full_post[0])
        # print(final_ecs)

        final_accept.append(accepts[0])
        
        final_reject.append(rejectlist[0])

        if any(a in gender[0][2] for a in genderlist[1]): 
            final_gender.append('Female')
        elif any(b in gender[0][2] for b in genderlist[0]): 
            final_gender.append('Male')
        else: 
            final_gender.append('Other/LGBTQ+') 
       
    
                
       
        final_race.append([i for i in racelist if i in race[0][2]])
                
        try: 
            final_sat.append(int(re.findall("[1][0-6][0-9][0-9]", SAT[0][2])[0]))
        except: 
            final_sat.append(' ')

        try: 
            final_act.append(re.search(r"\b[2-3]{1}[0-6]{1}\s",ACT[0][2]).group(0))
        except: 
            final_act.append('')
        dftotal['Gender'] = final_gender
        dftotal['SAT'] = final_sat
        dftotal['ACT'] = final_act
        dftotal['Race']=final_race
        dftotal['Major'] = final_major
        dftotal['Extracurriculars'] = final_ecs
        dftotal['Acceptances'] = final_accept
        dftotal['Rejections'] = final_reject
        dftotal['url'] = url
        list(np.array(filteredlinks)[[x for x in dftotal.index.tolist()]])
        dftotal = dftotal.astype(str).replace(["[]",' ',''], np.nan)
        dftotal = dftotal.dropna(thresh=6 )
        dftotal = dftotal.replace(np.nan,'[]',regex=True)
        appended_data = pd.concat([dftotal,appended_data])
print(appended_data)
newdata = pd.DataFrame(np.concatenate([appended_data,existing_processed_data]), index=None)
newdata.to_csv('./csvfiles/processeddata.csv', header=None)