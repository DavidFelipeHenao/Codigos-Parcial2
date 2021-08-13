#!/usr/bin/env python
# coding: utf-8

# In[22]:
'''
Este codigo imprime en pantalla los n primeros terminos de la sucesion de
Fiibonacci.

Parametros de entrada:
    n: cantidad de terminos a generar.

Autor: DAvid Felipe Henao
Ultima actualizaicion: 13 agosto, 2021
'''

n = int(input("Ingrese cuantos numeros de fibonacci quiere generar: "))

# Numeros para iniciar la serie
f1=1
f2=1

if n == 1:
    print('0')
elif n == 2:
    print('0','1')
else:
    
    # Imprime los numeros que inician la serie
    print('0')
    print(f1)
    print(f2)
    for i in range(n-3):
        fn = f1 + f2
        
        # Actualiza los numeros 
        f2 = f1
        f1 = fn
        print(fn)





# In[ ]:





# In[ ]:




