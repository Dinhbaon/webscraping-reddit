import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import re
from list import ecslist, unilist, genderlist, racelist, majorlist

dftotal = pd.DataFrame(columns=['Gender','Race','Major','SAT','ACT','Extacurriculars','Acceptances','Rejections'])

options = Options()
options.headless = True
options.add_argument("--disable-web-security") 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver  = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options = options)

filteredlinkscsv =  pd.read_csv("../csvfiles/filteredlinks.csv")
filteredlinks = filteredlinkscsv.iloc[:,0].to_list()


# hooks = []




final_accept = []
final_reject = []


driver.implicitly_wait(20)
final_gender = []
final_race=[]
final_major=[]
final_sat = []
final_act=[]
final_ecs = []
for i in range(15): 
        print(f'{i}')
        driver.get(filteredlinks[i])
        accepts = []
        prohook = []
        major = []
        rejectlist = []
        prorejects = []
        proacceptances = []
        rejectsonly = []
        scrape_rejects = []
        scrape_accept = []
        gender =[]       
        race = []
        SAT = []
        ACT = []
        full_post = []
        

        try: 
            scrape_rejects = driver.find_elements(By.XPATH,'//div[@class="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4"]/descendant::p[preceding::*[contains(text(),"Waitlist") or contains(text(),"Reject")]or self::p[contains(.,"Waitlist") or contains(.,"Reject")]]')
        except NoSuchElementException: 
            scrape_rejects = [' ']
            continue
        try: 
            scrape_accept = driver.find_elements(By.XPATH,'//div[@class="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4"]/descendant::p[preceding::*[contains(text(),"Acceptance")]or self::p[contains(.,"Acceptance")]]')
        except NoSuchElementException: 
            scrape_accept = [' ']
            continue
            
        try: 
            full_post.append(driver.find_element(By.XPATH,'//div[@class="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root"]').text)
        except: 
            continue
        
        try: 
            gender.append(driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(text(),"Gender:") or contains(text(),"gender:") or contains(text(),"emographics")]').text)
        except NoSuchElementException: 
            try: 
                gender.append('//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(text(),"emographics")]')
            except NoSuchElementException: 
                gender.append(" ")
       
        try: 
            driver.implicitly_wait(1)
            SAT.append(driver.find_element(By.XPATH,'//div[@class="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root"]//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(text(),"SAT") or contains(text(),"SAT I")]').text)
        except NoSuchElementException: 
            SAT.append("")
       
        try: 
            driver.implicitly_wait(1)
            ACT.append(driver.find_element(By.XPATH,'//div[@class="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root"]//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(text(),"ACT")]').text)
        except NoSuchElementException: 
            ACT.append("")
       
        try: 
            race.append(driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(text(),"Race") or contains(text(),"Ethnicity")]').text)
        except NoSuchElementException: 
            race.append("")
        
        # try:
        #     hooks.append(driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(text(),"Hooks:") or contains(text(),"hooks:") or contains(text(),"Hooks (Recruited Athlete, URM, First-Gen, Geographic, Legacy, etc.):")]').text)
        # except  NoSuchElementException: 
        #     hooks.append("")
        
       
        try: 
            major.append(driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(.,  "Intended Major") or contains(., "Major:")]').text)
        except  NoSuchElementException:
            major.append("") 
            
    

        ## append text in to list (make webobject into text)
        for elementp in scrape_rejects: 
            prorejects.append(elementp.text.lower())
        for elementp in scrape_accept: 
            proacceptances.append(elementp.text.lower())
        #filter out paragraphs
        
        rejectsonly.append(list(filter(lambda x : len(x)<250,prorejects)))
        
        #check all unis in the post       
        prouni = []
        prouniappend = []
        for i in range(len(unilist)):
            if not proacceptances: 
                proacceptances.append('')
            if any(a in ' '.join(proacceptances) for a in unilist[i]): 
                prouniappend.append(unilist[i][0])
        prouni.append(prouniappend)
        
        
    
        prorejectsonly = []
        for i in range(len(unilist)):
            if not rejectsonly[0]: 
                rejectsonly[0].append('')
            if any(b in ' '.join(rejectsonly[0]) for b in unilist[i]): 
                prorejectsonly.append(unilist[i][0])
        rejectlist.append(prorejectsonly)


        #filter unis in post with rejections
        accepts.append(list(set(prouni[0])-set(rejectlist[0])))
        gender[0] = gender[0].lower().partition("gender") 
        SAT[0] = SAT[0].partition("SAT")
        ACT[0] = ACT[0].partition("ACT")
        race[0] = race[0].lower().partition('race')
        major[0] = major[0].lower().partition('major')
## make in to dictionary
        
       



        submajor = []
        for j in range(len(majorlist)):
            if any(a in major[0][2] for a in majorlist[j]): 
                submajor.append(majorlist[j][0])
        final_major.append(submajor)

            

        final_ecs.append(ecslist.intersection(set(re.split(r'[);,.:/\s]\s*',full_post[0].lower()))))


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

            final_sat.append(re.findall("[1][0-6][0-9][0-9]", SAT[0][2]))
        except: 
            final_sat.append('')
 
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
print(dftotal['Extracurriculars'])
dftotal.to_csv('csvfiles\processeddata.csv')
     










#for act regex
# x = re.findall(r"\b[2-3]{1}[0-5]{1}", txt)
#for gpa number extraction 
#https://pythonguides.com/python-find-number-in-string/#:~:text=To%20find%20numbers%20from%20a,then%20it%20will%20return%20False.