#!/usr/bin/env python
# coding: utf-8

# In[45]:
'''
Este codigo crea una funcion que obtiene los terminos de la sucesion de Fibonacci
y que devuelve el cociente entre los dos ultimos terminos consecutivos para obtener una
aproximacion a la razon aurea.

Parametros de entrada: 
    n: Numero de razones a calcular

Autor: David Felipe Henao
Ultima actualizacion: 13 agosto, 2021    
'''

def fib(n):
    
    rAurea =  1.618033988

    # Numeros para iniciar la serie
    f0 = 0
    f1 = 1
    
    for k in range(1, n+1):
        fn = f1+f0
        
        # Actualiza los numeros
        f0 = f1
        f1 = fn
    
    # Imprime el cociente entre los dos ultimos numeros consecutivos
    print(f"El cociente obtenido es {f1/f0}")
    print(f"La diferencia respecto a la razon aurea es {abs((f1/f0)-rAurea)}") 
fib(10)
    


# In[ ]:





# In[ ]:




