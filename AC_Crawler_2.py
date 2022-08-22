#!/usr/bin/env python
# coding: utf-8

# In[68]:


# Python Version: 3.7
# Author: Phoenix Yan
# Required libraries: Selenium, undetected_chromedriver


# In[69]:


# pip install undetected_chromedriver --upgrade


# In[70]:


# use undetected chrome driver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import random
import pandas as pd
from datetime import date


# In[78]:


# allowing the website to scroll down, and give time for the webstie to load element
def scroll_down(driver,speed):
    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, speed):
        driver.execute_script("window.scrollTo(0, {});".format(i))
        
        

def get_urf_info(places):
    url_collection = []
    for place in places:
        driver = uc.Chrome()
        web =f'website/{place}'
        driver.get(web)
        time.sleep(2)
        scroll_down(driver,50)
        letters = driver.find_elements(By.CSS_SELECTOR,'section')
        for letter in letters:
            suburbs = letter.find_elements(By.CLASS_NAME,'styles__StyledArticle-sc-s3xgfo-6.kqSJgk')
            for suburb in suburbs:
                sub,post = suburb.find_element(By.CSS_SELECTOR,'h4').text.split(',')
                post = str(post.strip())
                url = [sub,place,post]
                url_collection.append(url)
                #sub = sub.replace(' ','-').lower()            
        driver.quit()
    return url_collection


def current_page(each,driver,AUCTION):
    sub = each[0].replace(' ','-').lower()
    state = each[1]
    post = each[2]    
    url = f"web/{sub}-{state}-{post}"
    driver.get(url)
    driver.implicitly_wait(30)
    property_list = driver.find_elements(By.CLASS_NAME,'LinkBase-sc-12oy0hl-0.kZtRHK.styles__ContentRightLink-sc-1hl8egg-6.hRvLYF')
    for prop in property_list:
        current_page = []
        current_page.extend([sub,post,state])
        divs = prop.find_element(By.CSS_SELECTOR,'div').text
        divs = divs.split("\n")
        current_page.extend(divs)
        print(current_page)
        AUCTION.append(current_page)
    return AUCTION

# def get_proxy(driver):
def get_proxy():
    driver = uc.Chrome()
    driver.get("https://free-proxy-list.net/")
    driver.implicitly_wait(30)
    proxy_table = driver.find_element(By.CSS_SELECTOR,'table')
    header = proxy_table.find_elements(By.CSS_SELECTOR,'th')
    header = [each.text for each in header]
    body = proxy_table.find_elements(By.CSS_SELECTOR,'tr')
    content = [[every.text for every in each.find_elements(By.CSS_SELECTOR,'td')] for each in body]
    content[0] = header
    content_df = pd.DataFrame(content[1:], columns = content[0])
    elite = content_df[content_df['Anonymity'] =='elite proxy'].reset_index(drop=True)
    elite = elite[(elite['Google'] == 'yes') & (elite['Https']=='yes')].reset_index(drop=True)
    elite['ip_port'] = elite['IP Address']+':'+elite['Port']
    proxy_list = list(elite['ip_port'])
    driver.quit()
    return proxy_list

def randome_row(elite):
    row = elite.sample()
    ip = row['IP Address']
    port = row['Port']
    return ip,port


# In[83]:


places = ['nsw','vic','sa','act','qld']#'wa','tas','nt'
y = get_urf_info(places)
AUCTION =[]


# In[ ]:


# main body
while len(y) > 0:
    driver = uc.Chrome()
    select =  random.randint(15,30)
    if len(y)>select:
        max_end = select
    else:
        max_end = len(y)
    for i in range(max_end):
        each = y[0]
        try:
            AUCTION = current_page(each,driver,AUCTION)
        except:
            driver.close()
            time.sleep(120)
            driver = uc.Chrome()
            AUCTION = current_page(each,driver,AUCTION)
        del y[0]
        time.sleep(random.uniform(3,5))
    driver.close()
driver.quit()
    
    
    
    
#     if remainder >= 30:
#         add = random.randint(20,30)
#         Max += add
#         for i in range(Min, Max):
#             each = y[i]
#             try:
#                 AUCTION = current_page(each,driver,AUCTION)
#                 print("Request access normally")
#                 time.sleep(random.uniform(3,5))
#             except:
#                 print("Crawler has been detected, need to cool down and reboost")
#                 driver.close()
#                 time.sleep(300)
#                 driver =uc.Chrome()
#                 AUCTION = current_page(each,driver,AUCTION)
#                 time.sleep(random.uniform(3,5))
#         Min = Max
#         remainder -= add
#         print("Suburb Remain: ",remainder)
#         driver.close()
#         time.sleep(random.uniform(6,10))
#     else:
#         Max += remainder
#         for i in range(Min,Max):
#             each = y[i]
#             try:
#                 AUCTION = current_page(each,driver,AUCTION)
#                 print("Request access normally")
#             except:
#                 print("Crawler has been detected, need to cool down and reboost")
#                 driver.close()
#                 time.sleep(300)
#                 driver =uc.Chrome()
#                 AUCTION = current_page(each,driver,AUCTION)
#         remainder = 0
#         driver.close()


# In[82]:


AUCTION


# In[ ]:


pd.set_option('display.max_rows', None)
for every in AUCTION:             
    if every[3] == "Passed in" and (every[4].startswith("Last bid") or every[4].startswith("Vendor bid")):
        every[4],every[3] = every[3],every[4]
    if every[3] =="Passed in" or every[3] == "Withdrawn" :
        every.insert(3,None)
    if len(every) == 7 or len(every[7]) > 2:
        every.insert(7,'0')
    every[0] =every[0].replace("-",' ')
df = pd.DataFrame(AUCTION)
df = df.iloc[:,0:8]
df.columns =['Sub','Zipcode','State','Price','Status','Address','Property Type','Beds']
df = df[['Sub','State','Address','Property Type','Beds','Status','Price','Zipcode']]
today = date.today()
df.to_csv(f".\AR_{today}_2.csv",index = False)


# In[ ]:


from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


# In[64]:


import requests
from itertools import cycle
import traceback
proxy_list = get_proxy()
# this function will return the first working proxy to be used for driver.
def proxy_test(proxy_list)
    proxy_pool = cycle(proxy_list)
    url = 'https://www.google.com/'
    for i in range(len(proxy_list)):
        proxy = next(proxy_pool)
        print("Request #%d"%i)
        try:
            response = requests.get(url,proxies={"http": proxy, "https": proxy})
            print('testing proxy')
            print(response.json())
            print(proxy)
            break
        except:
            print("Skipping. Connnection error")
            print(proxy)
    #     else:
    #         print('Found Working proxy')
    #         break
    return proxy


# In[63]:


# adding proxy to the chrome driver test
options = uc.ChromeOptions()
options.add_argument(f'--proxy-server=130.41.15.76:8080')
options.setAcceptInsecureCerts(true)
driver =uc.Chrome(options=options)
driver.get('https://www.google.com')

