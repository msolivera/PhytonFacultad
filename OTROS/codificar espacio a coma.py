def codificar(cadena):
    resultado=""
    contador=1
    for i in range (len(cadena)):
        if cadena [i] in " ":
            resultado+=";"
            contador=contador+1
        else:
            resultado+=cadena[i]
    return resultado


print(codificar("h o l a "))
