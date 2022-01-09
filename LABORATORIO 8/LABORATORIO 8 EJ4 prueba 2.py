def buscar (ubicacion_archivo,cadena,nombre):

    archivo = open (ubicacion_archivo)
    c=0 #cuenta cuantas veces esta la cadena

    lineas=[] #cuenta numero de linea donde esta la cadena
    l=1 #contador de lineas

    indices=[]
    ind=1


    for linea in archivo:

        frase=linea.strip().split(" ")
        
        if cadena in frase:

            lineas.append(l) #parte que cuenta lineas
            l=l+1

            c+=frase.count(cadena) #parte que cuenta caracter

            ###indices.append(frase.index(cadena))
        
               
    mostrar=input("Desea ver el archivo?\n")
    if mostrar=="si":
        print("Estimad@ " + nombre + "\nla cadena " + cadena + " aparecio un total de " + str(c) + " veces en el archivo \nen las posiciones que se detallan a contunuacion:\nnro de linea                    ubicacion\n")
        for x in lineas:
            ###for y in indices:
                print(x,"                              ","y")
    else:
        print ("Hata luego")

    
       
    archivo.close()
    
print(buscar("C:\\Temp\\ej4.txt","dia","micaela"))


#FALTA SOLUCIONAR INDICES
#SOLUCIONAR CUANDO CADENA NO ESTA EN ARCHIVO

