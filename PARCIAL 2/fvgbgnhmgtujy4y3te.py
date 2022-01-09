def separar(cadena):
    resultado=[]
    subcadena="|"
    contador=0
    for i in range (len(cadena)-len(subcadena)+1):
        if cadena[i:i+len(subcadena)]==subcadena:
            resultado.append(cadena)
            contador=contador+1
        
    return resultado

print(separar("uno|dos|tres"))
