#esercizio 7
# dadi

import random
massimo = 3600

lista = [[random.randint(1,6) for i in range(2)] for j in range(massimo)]
print(lista)

somme = [sum(row) for row in lista]
print(somme)

dizionario = {}

for c in range(len(somme)):
    if (somme[c] in dizionario):
        dizionario[somme[c]]+=1
    else:
        dizionario[somme[c]]=1

print(dizionario)
