# Laboratorio 7 - ejercicio 3


def difsim(lista1, lista2):
    aux = []
    for elem in lista1:
        if not (elem in lista2):
            aux.append(elem)
    for elem in lista2:
        if not (elem in lista1):
            aux.append(elem)
    return aux


a = [1, 2, 3]
b = [3, 4, 5]

print("a={}, b={}, difsim={}".format(a, b, difsim(a, b)))
