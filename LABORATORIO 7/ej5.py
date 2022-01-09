# Laboratorio 7 - Ejercicop 5


def transformar_nombres(lista):
    aux = []
    for elem in lista:
        aux.append(', '.join(elem))
    return aux


lista = transformar_nombres([['Rocky', 'Balboa'], ['Muhammad', 'Ali']])
print(lista)
