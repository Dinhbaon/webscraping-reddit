import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import re


from list import ecslist, unilist, genderlist, racelist, majorlist


options = Options()
options.headless = True
options.add_argument("--disable-web-security") 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver  = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options = options)

filteredlinkscsv =  pd.read_csv("csvfiles/filteredlinks.csv")
filteredlinks = filteredlinkscsv.iloc[:,0].to_list()
gender =[]


race = []
hooks = []
SAT = []
ACT = []
gpa= []
major = []
post = []
rejects = []
rejectsonly = []
totalunis = []

driver.implicitly_wait(10)

for i in range(10): 
        driver.get(filteredlinks[i])
        accepts = []
        progender = [] 
        proSAT = []
        prorace = []
        prohook = []
        proACT=[]
        progpa= []
        promajor= []
        proecs = []
        prouni = []
        rejectlist = []
        prorejects = []
        

        try: 
            rejects.append(driver.find_elements(By.XPATH,'//div[@class="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4"]/descendant::p[preceding::*[contains(text(),"aitlist") or contains(text(),"Reject")]]'))
        except NoSuchElementException: 
            rejects.append([['']])
            continue
        
            
            


        try: 
            totalunis.append(driver.find_elements(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"]'))
        except: 
            continue

        try: 
            post.append(driver.find_element(By.XPATH,'//div[@class="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root"]').text)
        except: 
            continue

        try: 
            gender.append(driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(text(),"Gender:") or contains(text(),"gender:")]').text)
        except NoSuchElementException: 
            gender.append("")
       
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
        
        try:
            hooks.append(driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(text(),"Hooks:") or contains(text(),"hooks:") or contains(text(),"Hooks (Recruited Athlete, URM, First-Gen, Geographic, Legacy, etc.):")]').text)
        except  NoSuchElementException: 
            hooks.append("")
        
        try: 
            gpa.append(driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(text(),"GPA") or contains(text(),"gpa")]').text)
        except  NoSuchElementException:  
            gpa.append("")
       
        try: 
            major.append(driver.find_element(By.XPATH,'//p[@class="_1qeIAgB0cPwnLhDF9XSiJM"][contains(.,  "Intended Major") or contains(., "Major:")]').text)
        except  NoSuchElementException:
            major.append("") 
            
        

        ## append text in to list (make webobject into text)
        for j in range(len(rejects[i])): 
            prorejects.append(rejects[i][j].text.lower())
        #filter out paragraphs

        rejectsonly.append(list(filter(lambda x : len(x)<250,prorejects)))


        #check all unis in the post       
        for j in range(len(post)):
            prouniappend = []
            for i in range(len(unilist)):
                if any(a in post[j].lower() for a in unilist[i]): 
                    prouniappend.append(unilist[i][0])
            prouni.append(prouniappend)
        
        for j in range(len(rejectsonly)):
            prorejectsonly = []
            accept = []
            for i in range(len(unilist)):
                if not rejectsonly[j]: 
                    rejectsonly[j].append([''])
                if any(b in ' '.join(rejectsonly[j]) for b in unilist[i]): 
                    prorejectsonly.append(unilist[i][0])
            rejectlist.append(prorejectsonly)


        #filter unis in post with rejections
        for j in range(len(rejectlist)):
            accepts.append([x for x in prouni[j]  if x not in rejectlist[j]])
        
    
        #split strings in to data
        for i in range(len(gender)): 
            progender.append(gender[i].lower().partition("gender"))   
            proSAT.append(SAT[i].partition("SAT")) 
            proACT.append(ACT[i].partition('ACT'))
            prorace.append(race[i].lower().partition('race'))
            prohook.append(hooks[i].split(":",1))
            progpa.append(gpa[i].split(":",1))
            promajor.append(major[i].lower().partition('major'))

        print(promajor)
## make in to dictionary
        dictgender ={'Gender':[]}
        dictrace= {'Race':[]}
        dictmajor = {'Major':[]}
        dictsat = {'SAT':[]}
        dictact = {'ACT':[]}
        dictecs = {'ECs':[]}
        dictaccept = {'Acceptances':[]}
        dictrejects = {'Rejections':[]}

        for i in range(len(promajor)): 
            submajor = []
            for j in range(len(majorlist)):
                if any(a in promajor[i][2].lower() for a in majorlist[j]): 
                    submajor.append(majorlist[j][0])
            dictmajor['Major'].append(submajor)

        print(len(dictmajor['Major']))
        for i in range(len(post)):
            proecs.append(ecslist.intersection(set(re.split(r'[);,.:\s]\s*',post[i].lower()))))
            dictecs['ECs'].append(proecs[i])

        for i in range(len(accepts)): 
            dictaccept['Acceptances'].append(accepts[i])
        for i in range(len(rejectlist)): 
            dictrejects['Rejections'].append(rejectlist[i])
        

        for j in range(len(progender)): 
            if any(a in progender[j][2] for a in genderlist[1]): 
                dictgender['Gender'].append('Female')
            elif any(b in progender[j][2] for b in genderlist[0]): 
                dictgender['Gender'].append('Male')
            else: 
                dictgender['Gender'].append('Other/LGBTQ+')
        for j in range(len(prorace)): 
            subrace = []
            gen =  [i for i in racelist if i in prorace[j][2]]
            subrace.extend(gen)
            dictrace['Race'].append(subrace)
                # subrace.extend(re.findall(f'{racelist[i]}',prorace[j][2]))
                # dictrace['Race'].append(subrace)
                   

        for j in range(len(proSAT)): 
            try: 
                dictsat['SAT'].append(re.findall("[1][0-6][0-9][0-9]", proSAT[j][2]))
            except: 
                dictsat['SAT'].append('')
            

        for j in range(len(proACT)): 
            try: 
                dictact['ACT'].append(re.search(r"\b[2-3]{1}[0-6]{1}\s",proACT[j][2]).group(0))
            except: 
                dictact['ACT'].append('')
        dfgender = pd.Series(dictgender)
        dfsat = pd.Series(dictsat)
        dfact = pd.Series(dictact)
        dfrace = pd.Series(dictrace)
        dfecs = pd.Series(dictecs)
        dfaccept = pd.Series(dictaccept)
        dfreject = pd.Series(dictrejects)
        dftotal = pd.DataFrame([dictgender,dictrace,dictsat,dictact,dictecs,dictaccept,dictrejects])
        print(dictmajor)
        dftotal.to_csv('csvfiles\processeddata.csv')

        








#for act regex
# x = re.findall(r"\b[2-3]{1}[0-5]{1}", txt)
#for gpa number extraction 
#https://pythonguides.com/python-find-number-in-string/#:~:text=To%20find%20numbers%20from%20a,then%20it%20will%20return%20False.