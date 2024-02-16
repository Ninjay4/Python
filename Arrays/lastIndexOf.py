#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a method called lastIndexOf
# That accepts an array of integers
# And an integer value as its parameters
# And returns the last index
# At which the value occurs in the array
# The method should return "-1" if the value is not found


# In[2]:


# Create the lastIndexOf function
def lastIndexOf(array, value):
    index = -1
    for i in range(len(array)):
        if array[i] == value:
            index = i
    return index


# In[8]:


# Create the input array
length = int(input("How many values are in your array?:  "))
array = []
for i in range(length):
    x = int(input("Enter value " + str(i + 1) + ":  "  ))
    array.append(x)

print(array) # Confirm the array


# In[10]:


# Run the lastIndexOf function
value = int(input("What integer value do you want to find the index of?  "))

print("The last index of the value " + str(value) + " is " + str(lastIndexOf(array, value)))


# In[ ]:




