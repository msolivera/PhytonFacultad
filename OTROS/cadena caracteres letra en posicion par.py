def cars_pares (cadena):
    resultado=""
    for i in range(0,len(cadena),2):
        resultado +=cadena[i]
    return resultado
print(cars_pares("miercoles"))

#la cadena resultado
#esta "vacia" porque ahi vamos a ui guardando los caracteres que me sirven.
#len(cadena) representa en este caso el maximo que puede llegar a twener
#la cadena
#resultado += es para que me de el resultado de la posicion del caracter
#ej:2,4,6

res=cars_pares("viernes")

