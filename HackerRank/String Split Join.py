#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Given a string, split it on a " " (space) delimiter and join using a - hyphen


# In[2]:


# Create a "Split and Join" Function


# In[3]:


def split_and_join(line):
    # sl = line.split(" ") # Splits the given line into a list with elements separated by a space " "
    # js = "-".join(sl) # This joins the elements in the list together, attached by a hyphen "-"
    # return js # Returns the line that has been split then rejoined
    sj = "-".join(line.split(" ")) # The short and most efficient way that combines the steps above into one statement
    return sj


# In[4]:


# The one line contains a string consisting of space separated words
# Enter the given line "this is a string"
line = (input("Enter the string: "))


# In[5]:


# Call the "split and join" function as a "result"
result = split_and_join(line)


# In[6]:


# Print the result
print(result)


# In[ ]:




