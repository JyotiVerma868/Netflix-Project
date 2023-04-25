#!/usr/bin/env python
# coding: utf-8
#                         Netflix Dataset Netflix Movies and TV Shows 2021#         This Netflix Dataset has information about the TV shows and Movies available on Netflix till 2021.#      This dataset is collected from flexible which is third party Netflix search engine and availble on Kaggle for free.
# In[1]:


# Importing the dataset

import pandas as pd
data = pd.read_csv(r"C:\Users\97474\Downloads\8. Netflix Dataset.csv")


# In[2]:


data

# Getting some basic information from this Dataset
# # Head

# In[5]:


data.head(5)


# # Tail

# In[6]:


data.tail()


# # Shape

# In[7]:


data.shape


# # Size

# In[8]:


data.size


# # Columns

# In[9]:


data.columns


# # dtypes

# In[11]:


data.dtypes


# # Info

# In[13]:


data.info()


# # Task 1 find the Duplicate Records

# # Duplicate

# In[14]:


data.duplicated()


# In[15]:


data[data.duplicated()]


# # To remove the Duplicate Records

# In[16]:


data.drop_duplicates()

## After running the duplicates you will see that No.of rows have changed## These changes are not permanent to make permanent changes run Inplace= True command
# In[18]:


data.drop_duplicates(inplace= True)


# # Null values

# In[19]:


data


# In[20]:


data.head()


# In[21]:


data.isnull()

To check the count of Null Values use sum function 
# In[22]:


data.isnull().sum()


# # Seaborn Libarary (Heat-Map)

# In[23]:


##Import seaborn

import seaborn as sns


# In[24]:


sns.heatmap(data.isnull())


# # Q1. For 'House of Cards', what is the show id and who is the Director of this show?

# In[26]:


data.head()


# In[27]:


data[data['Title'].isin(['House of Cards'])]     ##with .isin method


# In[29]:


data[data['Title'].str.contains("House of Cards")]    ## with .str.contains method


# # Q2. In which Year highest number of the TV shows and Movies were released? Show with the Bar Graph.

# In[30]:


data.dtypes


# In[32]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[34]:


data.head()


# In[35]:


data.dtypes


# In[36]:


data['Date_N'].dt.year.value_counts()


# In[37]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# # Q.3 How many Movies & TV Shows are in the dataset ? Show with Bar Graph.
# 

# In[39]:


data.groupby('Category').Category.count()


# In[40]:


data.groupby('Category').Category.count().plot(kind = 'bar')


# In[41]:


sns.countplot(data['Category'])


# # Q.4 Show all the Movies that were released in year 2000.
# 

# In[42]:


data.head()


# In[43]:


data['Year'] = data['Date_N'].dt.year


# In[44]:


data['Year']


# In[47]:


data.head(2)


# In[54]:


data[(data['Category'] =='Movie') & (data['Year'] == 2000)]


# In[53]:


data[(data['Category'] =='Movie') & (data['Year'] == 2020)]


# # Q.5 Show only the Titles of all TV Shows that were released in India only.

# In[55]:


data.head(2)


# In[57]:


data[(data['Category'] =='TV Show') & (data['Country'] == 'India')]['Title']


# # Q.6 Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?
# 

# In[58]:


data.head(2)


# In[59]:


data['Director'].value_counts()


# In[60]:


data['Director'].value_counts().head(10)


# # Q.7 Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".
# 

# In[61]:


##data[(data['Category'] =='Movie') & (data['Type'] == 'Comedies')]

data.head(2)


# In[62]:


data[(data['Category'] =='Movie') & (data['Type'] == 'Comedies')]


# In[63]:


data[(data['Category'] =='Movie') & (data['Type'] == 'Comedies')|(data['Country'] == 'United Kingdom')]


# # Q.8 In how many movies/shows, Tom Cruise was cast ?
# 

# In[64]:


data.head(2)


# In[66]:


data[data['Cast'] == 'Tom Cruise']


# In[67]:


data[data['Cast'].str.contains('Tom Cruise')]


# In[ ]:


## Remove null values


# In[68]:


data_new = data.dropna()


# In[70]:


data_new.head(2)


# In[72]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# # Q.9 What are the different Ratings defined by Netflix ?
# 

# In[74]:


data.head(2)


# In[76]:


data['Rating'].nunique()   ## total values or to find the count


# In[77]:


data['Rating'].unique()   ## to know the different unique values


# # Q.9.1 How many Movies got the 'TV-14' rating, in Canada ?
# 

# In[80]:


data[(data['Category'] =='Movie') & (data['Rating'] == 'TV-14')]


# In[81]:


data[(data['Category'] =='Movie') & (data['Rating'] == 'TV-14')].shape


# In[78]:


data[(data['Category'] =='Movie') & (data['Rating'] == 'TV-14') & (data['Country'] == 'Canada')]


# # Q.9.2 How many TV Shows got the 'R' rating, after year 2018 ?
# 

# In[82]:


data.head(2)


# In[85]:


data[(data['Category'] =='TV Show') & (data['Rating'] == 'R')]


# In[87]:


data[(data['Category'] =='TV Show') & (data['Rating'] == 'R') & (data['Year'] > 2018)]


# # Q.10 What is the maximum duration of a Movie/Show on Netflix ?
# 

# In[88]:


data.head(2)


# In[91]:


data['Duration'].unique()


# In[92]:


data.Duration.dtypes


# In[95]:


data[['Minutes','Unit']] = data['Duration'].str.split(' ', expand = True)


# In[96]:


data.head(2)


# In[98]:


data['Minutes'].max()


# In[99]:


data['Minutes'].min()


# In[100]:


data['Minutes'].mean()


# # Q.11 Which individual country has the Highest No. of TV Shows ?
# 

# In[89]:


data.head(2)


# In[102]:


data_tvshow = data[data['Category'] == 'TV Show']


# In[103]:


data_tvshow


# In[104]:


data_tvshow.Country.value_counts()


# In[105]:


data_tvshow.Country.value_counts().head(1)


# # Q.12 How can we sort the dataset by Year ?
# 

# In[106]:


data.head(2)


# In[107]:


data.sort_values(by='Year')


# In[108]:


data.sort_values(by='Year', ascending = False)


# # Q.13 Find all the instances where: Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' & Type is 'Kids' TV'

# In[109]:


data.head(2)


# In[111]:


data[(data['Category'] =='Movie') & (data['Type'] == 'Dramas')]


# In[114]:


data[(data['Category'] =='TV Show') & (data['Type'] == "Kids' TV")]


# In[115]:


data[(data['Category'] =='Movie') & (data['Type'] == 'Dramas') | (data['Category'] =='TV Show') & (data['Type'] == "Kids' TV")]


# In[ ]:




