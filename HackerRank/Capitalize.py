#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Given a first and last name, capitalize the 1st letters of each word
# A single line of input contains the full name


# In[2]:


# Create a capitalization function
# This function only works when a name section does NOT have
# any apostrophe's nor hyphens
#def solve(s):
#    caps = s.title()
#    return caps


# In[5]:


# Create another capitalization function
import string
def solve(s):
    caps = string.capwords(s, " ")
    return caps


# In[8]:


# Create the input string
# Enter "chris alan" in lowercase letters
s = input("Enter the first and last name: ")


# In[9]:


# Run the function
result = solve(s)
print(result)


# In[ ]:




