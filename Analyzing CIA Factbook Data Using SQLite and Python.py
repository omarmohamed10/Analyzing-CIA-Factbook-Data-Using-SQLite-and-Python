#!/usr/bin/env python
# coding: utf-8

# # import libraries and Connect to Database

# In[6]:


import sqlite3
import pandas as pd

conn = sqlite3.connect("factbook.db")
q = "SELECT * FROM sqlite_master WHERE type='table';"
pd.read_sql_query(q,conn)


# In[8]:


q = "SELECT * FROM facts LIMIT 5"
pd.read_sql_query(q,conn)


# # Some Statistics

# In[10]:


q = "SELECT MIN(population),MAX(population) FROM facts"
pd.read_sql_query(q,conn)


# In[14]:


q = '''
SELECT MIN(population_growth),
MAX(population_growth) FROM facts
'''
pd.read_sql_query(q,conn)


# # Outliers

# In[20]:


q = '''
SELECT * FROM facts 
WHERE population = (SELECT MIN(population) FROM facts)
'''
pd.read_sql_query(q,conn)


# In[21]:


q = '''
SELECT * FROM facts 
WHERE population = (SELECT MAX(population) FROM facts)
'''
pd.read_sql_query(q,conn)


# # Histograms

# In[22]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

q = '''
select population, population_growth, birth_rate, death_rate
from facts
where population != (select max(population) from facts)
and population != (select min(population) from facts);
'''
pd.read_sql_query(q, conn).hist(ax=ax)


# # Which countries have the highest population density?

# In[24]:


q = '''

SELECT name Country_Name,CAST(population as float)/CAST(area as float) density
FROM facts
ORDER BY density DESC
LIMIT 10

'''
pd.read_sql_query(q,conn)


# In[ ]:




