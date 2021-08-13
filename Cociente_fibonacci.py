#!/usr/bin/env python
# coding: utf-8

# In[45]:


def fib(n):
    a = 0
    b = 1
    
    for k in range(1, n+1):
        c = b+a
        a = b
        b = c
    print(b/a) 
fib(5)
    


# In[ ]:





# In[ ]:




