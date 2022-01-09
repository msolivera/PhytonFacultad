#dado un archivo de texto y una cadena de caracteres una
#funcion de que me de una linea que contiene esa cadena de caracteres

def buscar_en_archivo (nombre_archivo,buscar):

    archivo=open(nombre_archivo)

    lineas=[]

    nro=1 #variable permite contar en que numero de linea estamos

    for linea in archivo:

        if buscar in linea:

            lineas.append (nro)

            nro+=1

    archivo.close()

    return nro
   
print (buscar_en_archivo ("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\salida.txt","bien"))


