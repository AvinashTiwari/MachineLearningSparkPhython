
# coding: utf-8

# In[4]:


get_ipython().magic('matplotlib inline')

import numpy as np
from pylab import *

def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)


pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount  = np.random.normal(50.0 , 10.0 , 1000 )
scatter(pageSpeeds , purchaseAmount)
covariance(pageSpeeds , purchaseAmount)


# In[5]:


purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)

covariance (pageSpeeds, purchaseAmount)


# In[6]:


def correlation(x, y):
    stddevx = x.std()
    stddevy = y.std()
    return covariance(x,y) / stddevx / stddevy  #In real life you'd check for divide by zero here

correlation(pageSpeeds, purchaseAmount)


# In[7]:


np.corrcoef(pageSpeeds, purchaseAmount)


# In[8]:


purchaseAmount = 100 - pageSpeeds * 3

scatter(pageSpeeds, purchaseAmount)

correlation (pageSpeeds, purchaseAmount)


# In[ ]:




