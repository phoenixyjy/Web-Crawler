#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Writer: Phoenix(Jiayu) Yan
# Python Version: 3.6
# Purpose: Scripting all the postcode of all Austrilia states for data collection purpose and write into csv files
# Required library: Selenium, re, time, csv


# In[85]:


# importing all required libraries and functions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import csv


# In[86]:


# initializing default pramater
PostCode = ['3134','3135']
PATH = "C:\Program Files (x86)\chromedriver.exe"
# assign web driver
service = Service(PATH)
chrome = webdriver.Chrome(service = service)


# In[87]:


# listing all states
states = ['vic','act','nsw','nt','qld','sa','tas','wa']


# In[101]:


# scripting all states and write into csv file
for each in states:
    website  = 'https://postcodes-australia.com/state-postcodes/%s'%each
    print(website)
    time.sleep(4)
    chrome.get(website)
    content = WebDriverWait(chrome,10).until(EC.presence_of_element_located((By.CLASS_NAME ,"pclist"))).text
    post_code = re.findall("\d{4}",content)
    #exec('{}ZipCode = {}'.format(each,post_code))
    with open(f'{each}_ZipCode.csv','w',newline = '') as f:
        writer = csv.writer(f)
        for x in post_code:
            writer.writerow(str(x).split(','))


# In[ ]:




