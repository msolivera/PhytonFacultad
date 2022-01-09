def separar(cadena):
    resultado=[]
    for i in range (len(cadena)):
        if i !="|":
            resultado.append(i)
        
    return resultado

print(separar("uno|dos|tres"))
