#funcion que intercala archivos:
#toma la primer linea de una y la primer linea de la otra y la intercala
#con un for no se puede nrecorrer los dos 

def intercalar (ubicacion_archivo1,ubicacion_archivo2,salida):

    a1=open(ubicacion_archivo1)
    a2=open(ubicacion_archivo2)
    resultado=open(salida,"w")

    l1=a1.readline()
    l2=a2.readline()

    while l1!="" and l2!="":
        resultado.write(l1)
        resultado.write(l2)
        l1=a1.readline()
        l2=a2.readline()

    if l1=="":

        while l2 !="":

            resultado.write(l2)
            l2=a2.readline()

    if l2=="":
        while l1!="":
            resultado.write (l1)
            l1=a1.readline()

    a1.close()
    a2.close()
    resultado.close()
intercalar("c:\\Temp\\intercalar1.txt","C:\\Temp\\intercalar2.txt","C:\\Temp\\intercalar3.txt")
