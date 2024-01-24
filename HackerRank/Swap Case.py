#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Demonstrate how to use the Swap Case Function


# In[2]:


# Swap the cases on a given string and your task
# In other words, convert all lowercase letters to uppercase letters and vice versa


# In[3]:


# Create a swap case function
# "s" is a single line containing a string
def swap_case(s):
    newstring = s.swapcase()
    return newstring


# In[4]:


# Create the input string, "s"
# Enter the string as "HackerRank.com presents "Pythonist 2"."
# Be sure to place the entire string within a pair of parentheses
s = input("Enter a single line string: ")


# In[5]:


# Call the swap_case Function as a result
result = swap_case(s)


# In[6]:


# Print the result
print(result)


# In[ ]:




