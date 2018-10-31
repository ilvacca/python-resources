# Exercise 6
#

import random

lista = [random.randint(1,100) for i in range(10)]

avanti = len(lista)-1 
lista2 = []
print(lista)

while avanti:
    lista2.append(lista[avanti])
    avanti-=1
    
lista2.append(lista[0])

print(lista2)
    
