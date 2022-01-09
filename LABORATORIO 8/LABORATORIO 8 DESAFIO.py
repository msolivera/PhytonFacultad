print ("BIENVENIDO")
print ("")

archivo = open ("C:\\Temp\\valores.csv")
archivo2 = open("c:\\temp\\valores_salida.txt","w")
archivo.readline()


opcion=""
while opcion != "xx":
    opcion= input("\nIngrese opcion deseada, \no \'xx' para salir del programa\n") #este rsera el comando que ingrese el usuario
    opcion = opcion.split(" ") #separa los comandos separados por un espacio

    for i in opcion:
        if len(i)==4 and i[0]=="-" and i[1] =="s"and i[2]=="=": #verifica que el comando este correcto
        
            for linea in archivo:
            
                lista1=i
                aux=linea.split(",") #quita las comas de la linea del archivo
                aux2=lista1[3].join(aux) #une las lineas por la letra modificadora
                print(aux2)
            
        elif "-c=" in i :
                aux=i
                aux=aux.split("=") #separo comando de las columnas
                print(aux)
                for c in aux[1]: #recorro solo las columnas
                    c=aux[1].split(",") #separo las colummnas individualmente
                    print (c)
                    for linea in archivo:
                        datos=linea.strip().split(",")
                        print(datos)
                        if c == "0":
                            archivo2.write(datos[0]) #¿esta bien?
                            
                            
                        
            

