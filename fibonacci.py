#!/usr/bin/env python
# coding: utf-8

# In[22]:


n = int(input("Ingrese cuantos numeros de fibonacci quiere generar: "))
a=1
b=1
j=1
if n == 1:
    print('0')
elif n == 2:
    print('0','1')
else:
    print('0')
    print(a)
    print(b)
    for i in range(n-3):
        total = a + b
        b =a
        a = total
        print(total)



# In[ ]:





# In[ ]:




