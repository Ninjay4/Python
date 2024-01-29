#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Draw the HackerRank Logo with code, using Justify methods
# Must incorporate Center, Left, and Right Justify


# In[4]:


# Create input to enter the width (thickness) value
width = int(input("Enter the width: "))
# Enter '5'
h = "H"


# In[30]:


# Create functions for each logo section


# In[24]:


# Top Cone
# Right justify the left side
# Add the center character(s)
# Then Left justify the right side

def topCone(width):
    for i in range(width):
        print((h*i).rjust(width - 1) + h + (h*i).ljust(width - 1))
    
topCone(width)


# In[26]:


# Pillars (For both Top and Bottom)
# Center the pillars horizontally
# Repeat for the desired width
# Top Pillars:

def pillars(width):
    for i in range(width + 1):
        print((h*width).center(width*2) + (h*width).center(width*6))
    
pillars(width)


# In[28]:


# Middle Belt
# Center the belt horizontally 
# Repeat for the desired width

def belt(width):
    for i in range((width + 1)//2):
        print((h*width*5).center(width*6))
        
belt(width)


# In[14]:


# Bottom Pillar
# Use pillars() Function


# In[29]:


# Bottom Cone
# Right justify the left side
# Add the center character(s)
# Left justify the right side

def bottomCone(width):
    for i in range(width):
        print(((h*(width-i-1)).rjust(width) + h + (h*(width-i-1)).ljust(width)).rjust(width*6))

bottomCone(width)


# In[31]:


# Put all of the methods together to draw the complete logo
topCone(width)
pillars(width)
belt(width)
pillars(width)
bottomCone(width)


# In[ ]:




