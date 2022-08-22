#!/usr/bin/env python
# coding: utf-8

# In[55]:


import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time


# In[56]:


def scroll_down(driver,speed):
    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, speed):
        driver.execute_script("window.scrollTo(0, {});".format(i))


# In[57]:


driver = uc.Chrome()
driver.get("https://www.rba.gov.au/statistics/cash-rate/")
time.sleep(5)
scroll_down(driver,50)
header = driver.find_element(By.CSS_SELECTOR,'thead')
header = [each.text for each in header.find_elements(By.CSS_SELECTOR,'th')]
body = driver.find_element(By.CSS_SELECTOR,'tbody')
row_content = body.find_elements(By.CSS_SELECTOR,'tr')
content =[]
for each in row_content:
    row = []
    first = each.find_element(By.CSS_SELECTOR,'th').text
    row.append(first)
    others = each.find_elements(By.CSS_SELECTOR,'td')
    for every in others:
        row.append(every.text)
    content.append(row)
driver.quit()


# In[58]:


header = [each.replace('\n',' ') for each in header]
content.insert(0,header)


# In[59]:


import pandas as pd


# In[75]:


df = pd.DataFrame(content[1:],columns = content[0])
df.drop(['Related Documents','Change % points'], axis = 1,inplace = True)


# In[77]:


df[['Date','Month','Year']] = df['Effective Date'].str.split(' ',expand = True)


# In[79]:


df.drop('Effective Date', axis = 1, inplace = True)


# In[81]:


df.to_csv('Cash_Rate_full.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




