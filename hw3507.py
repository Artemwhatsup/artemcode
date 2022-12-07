#!/usr/bin/env python
# coding: utf-8

# In[8]:


a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print("3")
elif a == b | b == c | a == c:
    print("2")
else:
    print("0")


# In[ ]:




