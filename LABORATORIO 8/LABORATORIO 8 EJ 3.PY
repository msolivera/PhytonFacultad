texto=""
guardado=""

while texto !="::q":
    texto=input("ingrese texto:\n ")
    if texto != "::q":
        guardado=guardado+"\n" + texto
    if texto =="::q":
        print("usted ha finalizado la escritura")

ubicacion_archivo=input("ingrese ubicacion del archivo en el que desea guardar el texto: \n")
archivo=open(ubicacion_archivo,"w")
archivo.write(guardado)

mostrar=input("desea ver el archivo?\n  ")
if mostrar=="si":
    print(guardado)

archivo.close()

#ruta: C:\\Temp\\LAB8EJ3.txt
