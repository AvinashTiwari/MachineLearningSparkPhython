
# coding: utf-8

# # Uniform Distribution 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

values = np.random.uniform(-10.0, 10.0 , 100000)
plt.hist(values, 50)
plt.show()


# # Normal / Gaussian

# #visualize Probality density function

# In[4]:


from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.arange(-3,3,0.001)
plt.plot(x , norm.pdf(x))
plt.show()


#     #Generate some random number with normal distruction . "mu" is the desired mean , sigma is the standard deviation

# In[6]:


import numpy as np
import matplotlib.pyplot as plt

mu = 0.5
sigma = 2.0

values = np.random.normal(mu, sigma , 1000)
plt.hist(values , 50)
plt.show()


# #Exponential PDF / "Power Law"

# In[7]:


from scipy.stats import expon
import matplotlib.pyplot as plt

x = np.arange(0,10,0.001)
plt.plot(x , expon.pdf(x))
plt.show()


# #Binomial Probability Mass function

# In[8]:


from scipy.stats import binom
import matplotlib.pyplot as plt

n , p = 10 , 0.5
x =  np.arange(0,10,0.001)
plt.plot(x ,binom.pmf(x,n,p) )
plt.show()

#Binomial Probability Mass function . It knowing proabity to increase percentage example Now I have 500 apples what is probablity of 550 apples
# In[12]:


from scipy.stats import poisson
import matplotlib.pyplot as plt

mu = 500
x = np.arange(400 , 600, 0.5)
plt.plot(x ,poisson.pmf(x, mu) )
plt.show()


# In[ ]:




