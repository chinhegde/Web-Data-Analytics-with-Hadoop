#!/usr/bin/env python
# coding: utf-8

# In[12]:


# importing libraries/packages

import requests
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[13]:


# creating a dataframe with the data

full = pd.DataFrame(columns = ["type","conference_acronym","conference_name","conference_date","conference_location"])
df = pd.DataFrame(columns = ["conference_acronym","conference_name","conference_date","conference_location"])


# In[14]:


# Crawling the "Big Data" CFP pages 

data = list()

wiki = "http://www.wikicfp.com/cfp/call?conference=big%20data%20&page="

for i in range(1,21):
    url = wiki + str(i)
    page = urlopen(url)
    sleep(10)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    data.extend(soup.find_all("tr",attrs={"bgcolor": {"#f6f6f6","#e6e6e6"}}))
    
for i in range(0,len(data),2):
    k1 = data[i].findChildren()
    k2 = data[i+1].findChildren()
    
    df.loc[len(df)] = [k1[0].text,k1[2].text,k2[0].text.split(' - ')[0],k2[1].text]
    full.loc[len(full)] = ["Big Data",k1[0].text,k1[2].text,k2[0].text.split(' - ')[0],k2[1].text]

    
df.to_csv('bigdata.tsv',sep = '\t',index = False)


# In[15]:


# Crawling the "Machine Learning" CFP pages 
df = pd.DataFrame(columns = ["conference_acronym","conference_name","conference_date","conference_location"])
data = list()

wiki = "http://www.wikicfp.com/cfp/call?conference=machine%20Learning&page="

for i in range(1,21):
    url = wiki + str(i)
    page = urlopen(url)
    sleep(10)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    data.extend(soup.find_all("tr",attrs={"bgcolor": {"#f6f6f6","#e6e6e6"}}))

for i in range(0,len(data),2):
    k1 = data[i].findChildren()
    k2 = data[i+1].findChildren()
    
    df.loc[len(df)] = [k1[0].text,k1[2].text,k2[0].text.split(' - ')[0],k2[1].text]
    full.loc[len(full)] = ["Machine Learning",k1[0].text,k1[2].text,k2[0].text.split(' - ')[0],k2[1].text]


df.to_csv('machinelearning.tsv',sep = '\t',index = False)    


# In[16]:


# Crawling the "Data Mining" CFP pages 
df = pd.DataFrame(columns = ["conference_acronym","conference_name","conference_date","conference_location"])

data = list()

wiki = "http://www.wikicfp.com/cfp/call?conference=data%20mining&page="

for i in range(1,21):
    url = wiki + str(i)
    page = urlopen(url)
    sleep(10)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    data.extend(soup.find_all("tr",attrs={"bgcolor": {"#f6f6f6","#e6e6e6"}}))
    
for i in range(0,len(data),2):
    k1 = data[i].findChildren()
    k2 = data[i+1].findChildren()
    
    df.loc[len(df)] = [k1[0].text,k1[2].text,k2[0].text.split(' - ')[0],k2[1].text]
    full.loc[len(full)] = ["Data Mining",k1[0].text,k1[2].text,k2[0].text.split(' - ')[0],k2[1].text]


df.to_csv('datamining.tsv',sep = '\t',index = False)    


# In[17]:


full.to_csv('cfp_data1.tsv',sep = '\t',index = False)


# In[ ]:




