#!/usr/bin/env python
# coding: utf-8

# # Problem 1

# In[2]:


import pandas as pd
cars = pd.read_csv("Cars data.csv") # This loads the .csv file into a data frame
cars


# In[3]:


FirstFive = cars.head() # First 5 Rows
LastFive = cars.tail() # Last 5 Rows

Table = [FirstFive, LastFive] 

result = pd.concat(Table) # Concatenates the Table

result


# In[ ]:




