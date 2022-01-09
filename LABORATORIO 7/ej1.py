# Ejercicio 1 - Definir una función que retorna

import random


def lista_random(n):
    ''' Retorna una lista de enteros entre 1 y 6, en forma randomica'''

    aux = []
    for i in range(n):
        aux.append(random.randint(1, 6))
    return aux


print(lista_random(5))
print(lista_random(5))
print(lista_random(4))
