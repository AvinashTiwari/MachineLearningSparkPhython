
# coding: utf-8

#  # Standard Deviation 

# In[14]:


import numpy as np
import matplotlib.pyplot as plt

incomes  = np.random.normal(200.0, 25.89, 10000)

plt.hist(incomes, 50)
plt.show()


# In[15]:


incomes.std()


# In[16]:


incomes.var()


# In[ ]:




