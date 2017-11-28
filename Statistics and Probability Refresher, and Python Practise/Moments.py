
# coding: utf-8

#         ## Moments : Mean , Variance , Skew  and Kutois

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

vals =  np.random.normal(0, 0.5, 10000)
plt.hist(vals, 50)
plt.show()


# In[3]:


np.mean(vals)


# In[4]:


np.var(vals)


# Thire momemt is Skew

# In[5]:


import scipy.stats as sp
sp.skew(vals)


# The fouth Moment is Kutois

# In[6]:


sp.kurtosis(vals)


# In[ ]:




