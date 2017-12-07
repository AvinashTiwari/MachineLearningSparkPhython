
# coding: utf-8

# #Multi Regression

# In[1]:


import pandas as pd

df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')


# In[2]:


df.head()


# In[3]:


import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

X = df[['Mileage', 'Cylinder', 'Doors']]
y = df['Price']

X[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(X[['Mileage', 'Cylinder', 'Doors']].as_matrix())

print (X)

est = sm.OLS(y, X).fit()

est.summary()


# In[4]:


y.groupby(df.Doors).mean()


# In[ ]:




