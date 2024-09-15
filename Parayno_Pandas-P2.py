#!/usr/bin/env python
# coding: utf-8

# # Problem 2

# In[1]:


import pandas as pd
cars = pd.read_csv("Cars data.csv") # This loads the .csv file into a data frame
cars


# In[2]:


# Displays the first five rows with odd-numbered columns of cars.
cars[0:10] [1::2]


# In[3]:


# Displays the row that have the model of 'Mazda RX4'.
# .loc function attribute accesses a specific group of rows and columns within a DataFrame.

cars.loc[cars['Model'] == 'Mazda RX4']


# In[4]:


# Displays the number of cylinders that the car model 'Camaro Z28' have.
# This filters the rows in the cars Dataframe where the model is 'Camaro Z28',
# then selecs only the 'Model' and 'cyl' columns. 

cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]


# In[5]:


# Determines how many cylinders and what type of gear do the given car models have.
# .isin function filters and selects data within a data frame based on specific conditions.

cars[['Model', 'cyl', 'gear']][cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'])]


# In[ ]:




