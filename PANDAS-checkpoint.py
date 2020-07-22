#!/usr/bin/env python
# coding: utf-8

# In[77]:


import pandas as pd
import numpy as np
import xlrd
import seaborn as sns


# In[78]:


df = pd.read_csv("https://s3-us-west-2.amazonaws.com/learn-assets.galvanize.com/gSchool/ds-curriculum/sql-block/universities.csv")


# In[79]:


df.describe()


# In[80]:


df.info()


# In[81]:


df.head()


# In[82]:


df.tail()


# In[83]:


df.dropna(inplace = True) 
df.info()


# In[84]:


df = df.reset_index()


# In[85]:


# The mean by the type of University
mean_type = df.groupby('Type')
mean_type = mean_type.mean().sort_values(by='Size',ascending=True)
mean_type


# In[86]:


# The mean by the type of University
median_type = df.groupby('Type')
median_type = median_type.median().sort_values(by='Size',ascending=True)
median_type 


# In[87]:


add = df['address']


# In[88]:


add = add.str.strip()
add = add.str.split("," ,expand = True)
add


# In[89]:


add.loc[add[3].notna() == True]


# In[90]:


add = df['address']
add = add.str.strip()
add = add.str.rsplit(',',2,expand=True)
add


# In[91]:


df['state_zip']= add[2]
df


# In[92]:


df['city']= add[1]
df


# In[93]:


new2 = df["state_zip"].str.split(" ",n = 2 ,expand = True)
df['state'] = new2[1]
df['zipcode'] = new2[2]
df


# In[94]:


df = df.drop(columns=[ 'state_zip','index'])


# In[95]:


df


# In[96]:


associates = []
for i in df['Type']:
    if 'primarily' in i:
        associates.append(1)
    else:
        associates.append(0)


# In[97]:


df["associates"] = associates


# In[98]:


df


# In[101]:


Profit_or_non = []
for i in df['Type']:
    if 'not-for' in i:
        Profit_or_non.append('Not-For-Profit')
    elif  'Public' in i:
        Profit_or_non.append('Not-For-Profit')
    else:
        Profit_or_non.append('Profit')


# In[102]:


df["Profit"] = Profit_or_non


# In[103]:


df.head(30)


# In[104]:


Sector = []
for i in df['Type']:
    if 'Pulic' in i:
        Sector.append('Public')
    else:
        Sector.append('Private')


# In[105]:


df['Sector'] = Sector
df


# In[117]:


df.groupby(['state']).sum()


# In[118]:


df.describe()

