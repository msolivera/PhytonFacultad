def buscar (ubicacion_archivo,cadena,nombre):

    archivo = open (ubicacion_archivo)
    c=0 #cuenta cuantas veces esta la cadena

    lineas=[] #cuenta numero de linea donde esta la cadena
    l=1 #contador de lineas

    indices=[]
    ind=1
    for linea in archivo:
        if cadena in linea:

            lineas.append(l) #parte que cuenta lineas
            l=l+1

            c+=linea.count(cadena) #parte que cuenta caracter
            
    
        
    mostrar=input("Desea ver el archivo?\n")
    if mostrar=="si":
            print("Estimad@ " + nombre + "\nla cadena " + cadena + " aparecio un total de " + str(c) + " veces en el archivo \nen las posiciones que se detallan a contunuacion:\nnro de linea                    ubicacion\n")
            for x in lineas:
               print(x,"                              ","inidices")
    else:
        print ("Hata luego")
       
    archivo.close()
    
print(buscar("C:\\Temp\\ej4.txt","dia","micaela"))


#FALTA SOLUCIONAR INDICES

