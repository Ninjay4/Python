#!/usr/bin/env python
# coding: utf-8

# # Text Alignment

# In[10]:


# Exploring an better way to code this
# That looks better replicates the Logo


# ## Left Justify

# In[1]:


width = 20 # The width of the entire line
print('HackerRank'.ljust(width, '-'))


# ## Center

# In[2]:


print('HackerRank'.center(width, '-'))


# ## Right Justify 

# In[3]:


print('HackerRank'.rjust(width, '-'))


# In[19]:


# Create input
# Input contains the thickness value (must be an odd number)
# An odd integer between 0 and 50
thickness = int(input("Enter an odd integer between 0 and 50: "))
t = thickness


# In[20]:


# Left-Sided Top Cone
def lstcone(t):
    x = 1
    for i in range(t):
        print((('H')*(x+i)).center(2*t - 1))
        x += 1
        
lstcone(t)


# In[21]:


# Double Columns
def dcolumns(t):
    for i in range(t + 1):
        print((('H')*t).center(2*t - 1) + (('H')*0).ljust(2*t + 1) + (('H')*t).center(2*t - 1))
        
lstcone(t)
dcolumns(t)


# In[22]:


# Middle Belt
def mbelt(t):
    x = (t + 1)//2
    for i in range(x):
        print((('H')*(t*5)).rjust((t*5) + x - 1))
        
lstcone(t)
dcolumns(t)
mbelt(t)


# In[29]:


# Right-Sided Bottom Cone
def rsbcone(t):
    width = (t + 15)
    n = 9
    for i in range(t):
        print((('H')*0).rjust(width) + ('H')*n)
        width += 1
        n -= 2

dcolumns(t)
rsbcone(t)


# In[9]:


# Call the functions to draw the complete Logo
lstcone(t)
dcolumns(t)
mbelt(t)
dcolumns(t)
rsbcone(t)

