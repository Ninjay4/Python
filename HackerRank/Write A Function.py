#!/usr/bin/env python
# coding: utf-8

# In[1]:


#  Determine if a given year is a leap year
#  In the Gregorian calendar, three conditions are used to identify leap years:
#  The year can be evenly divided by 4, is a leap year, unless:
#  The year can be evenly divided by 100, it is NOT a leap year, unless:
#  The year is also evenly divisible by 400. Then it is a leap year.


# In[2]:


#  Given a year, determine whether it is a leap year.    
#  If it is a leap year, return the Boolean True, otherwise return False.


# In[6]:


def is_leap(year):  # Create the "is_leap" function
    leap = False  # Make False the default value
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # List the conditions
        leap = True  # If the conditions are met, then the value is True for a Leap Year
    return leap # The return value closes the function


# In[11]:


year = int(input("Please enter the year: "))


# In[12]:


is_leap(year)


# In[ ]:




