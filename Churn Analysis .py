#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[3]:


data = pd.read_csv("cust_churn.csv")


# In[5]:


data.head()


# #Evaluating churn on features

# In[8]:


categorical = list()

for x in data.columns:
    if data[x].dtype == 'object':
        categorical.append(x)


# In[11]:


data[categorical].nunique()


# In[12]:


def plot_category(data, col = ''):
    plt.figure(figsize=(10,10))
    plt.grid(True)
    plt.bar(data[col][data.Churn=="Yes"].value_counts().index,
           data[col][data.Churn=="Yes"].value_counts().values)
    


# In[13]:


plot_category(data, col ="Occupation")


# In[14]:


plot_category(data, col ="HandsetPrice")


# In[16]:


plot_category(data, col ="CreditRating")


# In[17]:


plot_category(data, col ="PrizmCode")


# In[26]:


def distribution_plot(data, col = ""):
    plt.figure(figsize=(10,10))
    plt.grid(True)
    sns.distplot(data[col] [data.Churn =="Yes"])
    sns.distplot(data[col][data.Churn == "No"])
    plt.legend(["yes","no"])
    


# In[27]:


distribution_plot(data, col = "MonthlyRevenue")


# In[28]:


distribution_plot(data, col = "MonthlyMinutes")

