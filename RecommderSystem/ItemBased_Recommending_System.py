
# coding: utf-8

# In[1]:


import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('./ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('./ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

ratings.head()


# In[2]:


userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
userRatings.head()


# In[3]:


corrMatrix = userRatings.corr()
corrMatrix.head()


# In[4]:


corrMatrix = userRatings.corr(method='pearson', min_periods=100)
corrMatrix.head()


# In[5]:


myRatings = userRatings.loc[0].dropna()
myRatings


# In[6]:


simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print ("Adding sims for " + myRatings.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[myRatings.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * myRatings[i])
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)
    
#Glance at our results so far:
print ("sorting...")
simCandidates.sort_values(inplace = True, ascending = False)
print (simCandidates.head(10))


# In[7]:


simCandidates = simCandidates.groupby(simCandidates.index).sum()


# In[8]:


simCandidates.sort_values(inplace = True, ascending = False)
simCandidates.head(10)


# In[9]:


filteredSims = simCandidates.drop(myRatings.index)
filteredSims.head(10)

