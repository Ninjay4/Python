#!/usr/bin/env python
# coding: utf-8

# ### You are given three integers (x, y and z) representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by i, j, and k; on a 3D grid where the sum of i+j+k is not equal to n. Here, 0 is less than or the same as i, which is less than or the same as x; 0 is less than or the same as j, which is less than or the same as y; and 0 is less than or the same as k, which is less than or the same as z. Please use list comprehensions rather than multiple loops, as a learning exercise. 

# ## Do NOT use Loops for this challenge!

# In[2]:


# Here are the given integers
x = 1
y = 1
z = 1
n = 2


# In[4]:


# Print out all possible combinations of x,y, and z
# that do NOT equal n when they are added together
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!= n])


# In[ ]:




