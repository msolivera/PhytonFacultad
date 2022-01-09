def concatenar (lista,salida):

    salida=open(salida,"w")

    for elemento in lista:
        archivo=open(elemento)
        for linea in archivo:

            salida.write(linea+"\n")
            
    archivo.close()
    salida.close()

concatenar(["C:\\Temp\\LAB8EJ6-1.txt","C:\\Temp\\LAB8EJ6-0.5.txt","C:\\Temp\\LAB8EJ6-2.txt"],"C:\\Temp\\LAB8EJ6-3.txt")
