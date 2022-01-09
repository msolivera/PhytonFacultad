#EJERCICIO 1:


ubicacion_archivo=input("Ingrese Nombre del archivo: ")

texto = ""
guardado = ""

texto = input ("Ingrese una linea: ")

while texto != "":
    texto = input ("Ingrese una linea: ")
    for i in texto:
        if i in "abcdefghijklmnopqrstuvwxyz":
            texto = texto.title()
            
        
    guardado = guardado + "\n" + texto
    


    if texto == "":
        print ("Fin.")


archivo = open (ubicacion_archivo, "w")
archivo.write(guardado)
archivo.close()


        


#len (0,-2)==. return false
