#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a method that returns the range of values in an array of integers
# The range = the difference between the maximum and minimum values 
# in the array, plus one
# Assume that the array has at least one element


# In[2]:


# Create the input
values = list(map(int, input("Enter all the integer values separated with a space: ").split()))
print("The list of values is : ", values) # To verify the list


# In[3]:


# Use sorted so that the values are ordered
# from the smallest to the largest
slist = sorted(values)
print("The sorted list of values is : ", slist) # To verify the sorted list


# In[4]:


# Create the "Range" method
def range(slist):
    # Subtract the first value "0" from the last value "-1"
    # Then add one
    r = slist[-1] - slist[0] + 1
    return r


# In[5]:


# Call and print the range
print(range(slist))


# In[ ]:




