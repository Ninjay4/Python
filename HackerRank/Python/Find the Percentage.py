#!/usr/bin/env python
# coding: utf-8

# In[2]:


# HackerRank Challenge: Finding the Percentage
# The provided code stub will read in a dictionary 
# containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal. 


# In[3]:


# import the mean function from the Statistics library
# This will help to automatically calculate the average value of a list 
from statistics import mean


# In[4]:


# Create the dictionary using Curly Brackets
student_marks = {}


# In[6]:


student_marks['alpha'] = [20, 30, 40]
student_marks['beta'] = [30, 50, 70]
student_marks['Krishna'] = [67, 68, 69]
student_marks['Arjun'] = [70, 98, 63]
student_marks['Malika'] = [52, 56, 60]


# In[12]:


# Select a name
query_name = 'Arjun'


# In[13]:


# Use mean to calulate the average value
# Use format to convert the answer to a decimal number of 2 places
average = format(mean(student_marks[query_name]), ".2f")


# In[14]:


# Print the answer
print(average)


# In[ ]:




