
# coding: utf-8

# In[1]:


import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('./ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('./ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)


# In[2]:


ratings.head()


# In[3]:


movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
movieRatings.head()


# In[4]:


starWarsRatings = movieRatings['Star Wars (1977)']
starWarsRatings.head()


# In[5]:


similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)
df.head(10)


# In[6]:


similarMovies.sort_values(ascending=False)


# In[7]:


import numpy as np
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
movieStats.head()


# In[8]:


popularMovies = movieStats['rating']['size'] >= 100
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]


# In[9]:


df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))


# In[10]:


df.head()


# In[11]:


df.sort_values(['similarity'], ascending=False)[:15]

