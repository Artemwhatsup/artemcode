#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# In the hole in the ground there lived a hobbit


# In[ ]:


s = "In the hole in the ground there lived a hobbit"


# In[4]:


s = "In the hole in the ground there lived a hobbit"
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)


# In[ ]:




