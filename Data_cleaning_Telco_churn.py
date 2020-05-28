#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[10]:


data = pd.read_csv("cust_churn.csv")


# In[13]:


data.head()


# In[14]:


data.columns


# In[16]:


#target class distribution
data["Churn"].value_counts()


# Customers who have not churned are more than double of customers who have churned. class is imbalanced

# In[17]:


data.describe()


# In[23]:


#Missing value analysis
data.isnull().sum().values.sum()


# In[30]:


missing = list()

for x in data.columns:
    if data[x].isnull().sum() != 0:
        print(x,data[x].isnull().sum())
        missing.append(x)


# In[31]:


#Director Assisted Calls
data["DirectorAssistedCalls"].describe()


# it is when customers wanted to talk to the manager. Mostly they are 0's. 
# However, Let us determine their effect on churn. 

# In[34]:


data[data["DirectorAssistedCalls"]!=0]["Churn"].value_counts()


# In[36]:


data= data.fillna(0)


# In[38]:





# In[42]:




