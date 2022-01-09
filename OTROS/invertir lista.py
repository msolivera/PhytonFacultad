def invertir (lista):
    resultado=[]
    for i in range (len(lista)):
        resultado.append(lista[-i-1])
    return resultado
