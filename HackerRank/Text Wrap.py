#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Given a string and a maximun width, "max_width"
# Wrap the string into a paragraph of where
# Each line does NOT exceed the maximum width


# In[2]:


# wrap has the following parameters:
# string: a long string
# int max_width: the width to wrap to
# Constraints:
# 0 < string length < 1,000
# 0 < max_width < string length


# In[3]:


# Returns a string: a single string with newline characters ('\n') 
# where the breaks should be


# In[4]:


# import the textwrap function
import textwrap


# In[5]:


# Create a wrap function
# The "wrap" function returns a list
# So the print must be converted from a list
# into a string of new lines
# Where each line is of width, "w"
def wrap(string, max_width):
    twstring = textwrap.wrap(string, max_width)
    return '\n'.join(twstring)


# In[6]:


# Input Format
# The first line contains the string
# The second line contains the max_width
# Create the inputs
# Use string = "abcdefghijklmnopqrstuvwxyz"
# Use 4 as the max_width
string = input("Enter the String: ")
max_width = int(input("Enter the maximum width of each new line: "))


# In[7]:


# Call the wrap function as a result
result = wrap(string, max_width)


# In[8]:


# Print the result
print(result)

