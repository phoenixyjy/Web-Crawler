# In[1]:


# importing all the essential library
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import date


# In[2]:


def scroll_down(driver,speed):
    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, speed):
        driver.execute_script("window.scrollTo(0, {});".format(i))


# In[3]:


cities = ['sydney','melbourne','brisbane','adelaide','canberra']
Properties = [['Suburb','State','City','Address','Type','Rooms','status','price']]
PATH = "C:\Program Files (x86)\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service =  service)
for city in cities:
    website = f"somewebsite/{city}/"
    driver.get(website)
    #iterating property information
    driver.implicitly_wait(10)
    scroll_down(driver,30)
    letters = driver.find_elements(By.CLASS_NAME,'css-11alnep')
    for x in letters:
        suburb =  x.find_elements(By.CLASS_NAME,'css-3xqrp1')
        # each represents all properties in the suburb
        for each in suburb:
            #select suburb's name
            sub_name = each.find_element(By.CSS_SELECTOR,'h3').text
            estates = each.find_elements(By.CLASS_NAME,'css-qflns9')
            for y in estates:
                Curr_Sub_Property = []
                Curr_Sub_Property.append(sub_name)
                Curr_Sub_Property.append(city)
                detail = y.find_elements(By.CSS_SELECTOR,'li')
                address = detail[0].text
                Curr_Sub_Property.append(address)
                for i in range(1,3):
                    left_section = detail[i].find_elements(By.CSS_SELECTOR,'span')
                    for z in left_section:
                        result = z.text
                        Curr_Sub_Property.append(result)
                Properties.append(Curr_Sub_Property)
driver.close()


# In[4]:


test= Properties


# In[5]:


for each in test:
    if each[1] == 'sydney':
        each.insert(1,'nsw')
    elif each[1] == 'melbourne':
        each.insert(1,'vic')
    elif each[1] == 'brisbane':
        each.insert(1,'qld')
    elif each[1] == 'adelaide':
        each.insert(1,'sa')
    elif each[1] == 'canberra':
        each.insert(1,'act')
    for x in range(len(each)):
        each[x] = each[x].lower()


# In[6]:


pd.set_option('display.max_rows', None)


# In[10]:


df =pd.DataFrame(test)
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header
today = date.today()
df['Timestamp'] = today


# In[11]:


df.to_csv(f'.\AR_{today}.csv', index = False)






