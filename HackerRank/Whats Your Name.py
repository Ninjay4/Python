#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Given the firstname and lastname of a person on two different lines
# read them and print the following:
# Hello firstname lastname! You just delved into python.


# In[5]:


# Create a function to print the full name
def print_full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return print("Hello " + full_name + "!  You just delved into python.")


# In[9]:


# Create two inputs: first_name and last_name on two different lines
# Enter "Ross" as first_name - No parentheses needed
# Enter "Taylor" as last_name -- No parentheses needed
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")


# In[10]:


# Run the print_full_name function
print_full_name(first_name, last_name)


# In[ ]:




