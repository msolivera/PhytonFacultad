# Laboratorio 7 - ej4


def top_five(lista):

    lista.sort()
    lista.reverse()
    if len(lista) >= 5:
        return lista[:5]
    else:
        return lista


lista = [1, 4, 1, 2, 6, 4, 4, 3, 3, 5]
print(lista, "=>", top_five(lista))
