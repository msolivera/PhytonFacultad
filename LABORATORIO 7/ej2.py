# Definicion de funciones


def eliminar_duplicados(lista):
    '''Elimina duplicados de una lista recibida por parámetro'''
    aux = []
    for elem in lista:
        if not (elem in aux):
            aux.append(elem)
    return aux


# Programa Principal
a = [1, 2, 3, 3, 6]
b = eliminar_duplicados(a)

print("Lista inicial {}  Resultado de la función {}".format(a, b))
