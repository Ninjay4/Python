#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Given an integer,"n", and "n" space-separated integers as input, 
# create a tuple,"t", of those "n" integers
# Then compute and print the result of hash(t) 


# In[7]:


n = int(input()) # Enter "2"


# In[8]:


integer_list = map(int, input().split()) # Enter "1 2" - separated by one space


# In[9]:


t = tuple(integer_list) # Create the tuple, t


# In[10]:


print(hash(t)) # Print hash(t)


# In[11]:


# Generates an answer of -3550055125485641917 with Python3
# This is different than the HackerRank answer of 3713081631934410656
# which may work with Pypy; Perhaps the answer needs to be
# updated in HackerRank


# In[ ]:




