import urllib.request, json 
import pandas as pd
import time 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


options = Options()
options.headless = True
options.add_argument("--disable-web-security") 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver  = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options = options)

links = []
epoch = time.time()
before_date = ['1660132463']
# def get_size(): 
#     with urllib.request.urlopen(f'https://api.pushshift.io/reddit/search/submission/?subreddit=collegeresults&metadata=true&size=0') as url:
#         findsizefile = json.loads(url.read()) 
#         size = findsizefile['metadata']['total_results']
#         return size 
        
# for j in range(get_size()):
#     with urllib.request.urlopen(f"https://api.pushshift.io/reddit/search/submission/?subreddit=collegeresults&size=500&before={before_date[j]}") as url:
#         jsonfile = json.loads(url.read())  
#         for i in range(len(jsonfile['data'])):
#             links.append(jsonfile['data'][i]['url'])
#     before_date.append(jsonfile['data'][len(jsonfile['data'])-1]['created_utc'])
#     df=pd.DataFrame(links)
#     df.to_csv("csvfiles\rawlinks.csv",header=None, index=None)


#Filter out links
linkcsv = pd.read_csv('csvfiles/rawlinks.csv') 
links = linkcsv.iloc[:,0].to_list()
deadlinks= []
for i in range(len(links)): 
    driver.get(links[i])
    try: 
        driver.find_element(By.XPATH,"//div[contains(text(),'Sorry, this post was deleted by') or contains(text(),'Moderators remove posts from feeds for a variety of reasons') or contains(text(),'automated bots frequently filter posts') or contains(text(),'REMOVED')]")
        deadlinks.append(links[i])
        df=pd.DataFrame(deadlinks)
        df.to_csv("csvfiles\deadlinks.csv",header=None, index=None)
    except NoSuchElementException: 
        continue

