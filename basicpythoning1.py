#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


tf.__version__


# In[3]:


print("hello world")


# In[4]:


a = 9
b = 8


# In[5]:


a+b


# In[6]:


print(a+b)


# In[7]:


print(8 * 8)


# In[8]:


a = {2 ,3 ,45, 5}


# In[9]:


a[2]


# In[10]:


a{2}


# In[11]:


type(a)


# In[12]:


dd(a)


# In[13]:


a.keys()


# In[14]:


print(a)


# In[15]:


a= {'car': 10000, 'van':5000}


# In[16]:


print(a['car'])


# In[17]:


print(a)


# In[18]:


del a['car']


# In[19]:


print(a)


# In[20]:


type(a)


# In[21]:


b = [4 , 5, 10]


# In[22]:


print(b)


# In[23]:


type(b)


# In[24]:


c = (1,2,3,4)


# In[25]:


type(c)


# In[26]:


d = 11.1


# In[27]:


type(d)


# In[28]:


c(2)


# In[29]:


f = 4


# In[30]:


if f > 5 :
    print("f is bigger than 5")
elif f < 3 :
    print("f is smaller than 3")
else :
    print("f is between 3 and 5")


# In[31]:


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# In[32]:


def f(x,y,z):
    print(x + y + z)


# In[33]:


f(1,2,3)


# In[35]:


def g(x,y,z):
    return(x * y * z)


# In[36]:


g(3,4,5)


# In[37]:


h = g(3,4,5)


# In[38]:


print(h)


# In[39]:


import os 
dir_path = os.path.dirname(os.path.realpath(__file__))


# In[ ]:




