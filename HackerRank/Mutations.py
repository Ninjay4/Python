#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Make changes to an "immutable" String
# This means that string [i] = "c", can NOT be used
# You can either change the string into a list and then make the change above
# Or you can use slicing, which is what I will use


# In[2]:


# Create a mutate_string Function
# That includes the string (s), the position that needs to be changed (i),
# And the new replacement character, (c).
def mutate_string(s, i, c):
    s2 = s[:i] + c + s[(i+1):]
    return s2


# In[3]:


# Create the inputs
# Use "abracadabra" for (s)
s = input("Enter the string: ")
# Use 5 for (i) and "k" for (c)
# Enter as "5 k", separated by a space
i, c = input("Enter the position as a number and the replacement letter: ").split()


# In[4]:


# Run the mutate_string Function as a new_string
new_string = mutate_string(s, int(i), c)
print(new_string)


# In[ ]:




