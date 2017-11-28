
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
vals = np.random.normal(0, 0.5, 10000)
plt.hist(vals , 50)
plt.show()


# In[2]:


np.percentile(vals,50)


# In[ ]:




