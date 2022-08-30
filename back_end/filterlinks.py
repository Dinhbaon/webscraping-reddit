import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


linkcsv = pd.read_csv('/csvfiles/rawlinks.csv') 
links = linkcsv.iloc[:,0].to_list()

removelinkscsv  = pd.read_csv('/csvfiles\deadlinks.csv')
removelinks = removelinkscsv.iloc[:,0].to_list()

filterlinkscsv = pd.read_csv('/csvfiles/filteredlinks.csv')
filteredlinks = filterlinkscsv.iloc[:,0].to_list()

filterlinks = [x for x in links if x not in removelinks]
(pd.DataFrame(filterlinks)).to_csv('/csvfiles/filteredlinks.csv',header='links', index=None)


newlinks= []




    
