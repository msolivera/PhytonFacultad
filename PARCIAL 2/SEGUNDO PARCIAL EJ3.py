def mas_larga (lista):
    resultado = []
    for listas in range (len(lista)):
        if len(str(lista[0])) > len(str(lista[1])) and len(str(lista[0])) > len(str(lista[2])):
            resultado.append(lista[0])
        elif len(str(lista[1])) > len(str(lista[0])) and len(str(lista[1])) > len(str(lista[2])):
            resultado.append(lista[1])
        elif len(str(lista[2])) > len(str(lista[0])) and len(str(lista[2])) > len(str(lista[1])):
            resultado.append(lista[2])
    return resultado[0]

print(mas_larga([["hola como estas?"],["bien y tu?"],["muy bien, hasta luego"]]))

