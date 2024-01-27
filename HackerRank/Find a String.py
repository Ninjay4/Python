#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Given a string and a substring, print the number of times that the substring occurs in the string 
# String traversal will take place from left to right, not from right to left
# NOTE: String letters are case-sensitive


# In[10]:


# Create a "Count_Substring" Funtion
def count_substring(string, sub_string):
    c = 0 # Create a counter
    x = len(string) - len(sub_string) # Find the number of iterations needed
    for i in range(x+1):
        if string.startswith(sub_string, i):
            c +=1
    return c


# In[11]:


# Create the inputs
# The first line of input contains the original string
# The next line contains the substring
# The "strip" Function removes any leading and ending spaces by default
# Enter "ABCDCDC" as the string
# Enter "CDC" as the substring
string = input("Enter the string: ").strip()
sub_string = input("Enter the sub_string: ").strip()


# In[12]:


# Find the result
result = count_substring(string, sub_string)
print(result)


# In[ ]:




