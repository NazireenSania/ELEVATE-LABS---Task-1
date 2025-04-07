#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Step 1: Importing required libraries

import pandas as pd


# In[2]:


#checking the location of the repository

import os
print(os.getcwd())


# In[3]:


#Step 2:loading the dataset

df = pd.read_csv("netflix_titles.csv", encoding='ISO-8859-1')
df


# In[4]:


# Step 3: View basic info

print("Initial dataset shape:", df.shape)
print("\nColumn-wise missing values:\n", df.isnull().sum())


# In[5]:


#Step 4:removing duplicates

df = df.drop_duplicates()
print("\nShape after removing duplicates:", df.shape)


# In[6]:


#Step 5:Standardize column names (lowercase and replace spaces with underscores)

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


# In[7]:


#Step 6: Converting 'date_added' column to datetime format

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')


# In[8]:


#Step 7:Handling missing values


#(1) Filling missing values with a placeholder or mode (depends on context)
df['country'] = df['country'].fillna("Unknown")
df['director'] = df['director'].fillna("Not Specified")
df['cast'] = df['cast'].fillna("Not Specified")


# In[9]:


df.shape
df.isnull().sum()


# In[10]:


#(2) Drop rows with missing values (if very few and non-critical)

df = df.dropna(subset=['rating', 'duration', 'date_added'])


# In[11]:


df.shape


# In[12]:


#Step 8:Rechecking  missing values

print("\nMissing values after cleaning:\n", df.isnull().sum())


# In[13]:


# Step 9: Check data types


print("\nData types:\n", df.dtypes)


# In[14]:


# Step 10: Export the cleaned dataset to a new CSV file


df.to_csv("netflix_titles_cleaned.csv", index=False)
print("\nCleaned dataset saved as 'netflix_titles_cleaned.csv'")


# In[ ]:




