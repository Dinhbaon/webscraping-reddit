import urllib.request, json 
import pandas as pd
import time 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time 


options = Options()
options.headless = True
options.add_argument("--disable-web-security") 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver  = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options = options)


epoch = time.time()

before_date = [f'{int(epoch)}']
after_date = pd.read_csv('./csvfiles/afterdate.csv').iloc[:,1].tolist()
print(after_date)
df = pd.DataFrame(columns=['links','time'])
addlinks = [] 

with urllib.request.urlopen(f"https://api.pushshift.io/reddit/search/submission/?subreddit=collegeresults&size=500&before={before_date[0]}&after={after_date[0]}&sort=desc") as url:
        jsonfile = json.loads(url.read())  
        after_date = jsonfile['data'][0]['created_utc']
        links = [] 
        times = []
        for i in range(len(jsonfile['data'])):
            links.append(jsonfile['data'][i]['full_link']) 
            times.append(jsonfile['data'][i]['created_utc'])
df['links'] = pd.Series(links)
df['time'] = pd.Series(times)
print(df['links'])
     
before_date.append(jsonfile['data'][-1]['created_utc'])

pd.DataFrame([after_date]).to_csv('./csvfiles/afterdate.csv')

    
# Filter out links

deadlinks= []
for i in range(len(df['links'])): 
    driver.get(df['links'][i])
    try: 
        driver.find_element(By.XPATH,"//div[contains(text(),'Sorry, this post was deleted by') or contains(text(),'Moderators remove posts from feeds for a variety of reasons') or contains(text(),'automated bots frequently filter posts') or contains(text(),'[deleted]')]")
        deadlinks.append(df['links'][i])
    except NoSuchElementException: 
        continue
filteredlinks = pd.DataFrame([x for x in df['links'] if x not in deadlinks])
filteredlinks.to_csv('./csvfiles/newfilteredlinks.csv')
existingfilterlinks = pd.read_csv('./csvfiles/filteredlinks.csv')

pd.concat([filteredlinks,existingfilterlinks]).to_csv('./csvfiles/filteredlinks.csv')
