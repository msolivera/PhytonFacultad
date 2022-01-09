archivo1 = open("prueba.txt")
for linea in archivo1:
    print(linea.upper())

archivo1.close()
#----------------------------------------------------
#otra forma
archivo1=open("prueba.txt")
linea=archivo1.readline()
while linea !="":
    print (linea.upper())
    linea=archivo1.readline()

archivo1.close()

archivo2=open("archivo_nuevomica.txt","w")
archivo2.write("hola"+"\n")  #\n salto de linea
archivo2.write("¿como estas?")
archivo2.close()
#-----------------------------------------------------
archivo1=open("prueba.txt")
archivo2=open("pruebaMAYUSCULA.txt","w")
linea=archivo1.readline()
for linea in archivo1:
    if linea.strip() !=" ":#funcion strip saca espacios y caracteres de control
        archivo2.write(linea.strip())
archivo1.close()
archivo2.close()   #abre los dos archivos uno para lectura y otro para escritura
                    #a mediada que lee las lineas del archivo uno escribe en el archivo 2

#------------------------------------------------------
 #que escriba todo menos vocales
