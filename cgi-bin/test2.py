medicamento = "dorzomed"
ubicacion1 = "Avda. 8 de octubre 2738, Montevideo"
 
import math
import time
import urllib.request
import cgi, cgitb
cgitb.enable()
###
def cargar_med():
    archivo_med = open("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\cgi-bin\\medicamentos.dat")
    for linea in archivo_med:
        med = linea.split(",")
        if med[1] == medicamento:
            return med[0] #devuelve el codigo del medicamento
    archivo_med.close()
###        
def cargar_farmacias_med():
    archivo_farm_med = open("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\cgi-bin\\farm-med.dat")
    archivo_hora = open("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\cgi-bin\\farmacias.dat")
    hora = time.strftime("%H:%M:%S")
    hora_actual = hora.split(":")
    hora_actual = "".join(hora_actual)
    hora_actual = int(hora_actual)
    
    lista1 = []
    for linea in archivo_farm_med:
        farm = linea.strip().split(",")
        if farm[1] == cargar_med():
            lista1.append(farm[0])
    print(lista1)

    lista2 =[]
    for linea in archivo_hora:
        datos = linea.strip().split(",")
        hora_farm1= datos[4]
        hora_farm1= hora_farm1.split(":")
        hora_farm1= "".join(hora_farm1)
        hora_farm1= int(hora_farm1)
        hora_farm2= datos[5]
        hora_farm2= hora_farm2.split(":")
        hora_farm2= "".join(hora_farm2)
        hora_farm2= int(hora_farm2)
        if hora_actual > hora_farm1 and hora_actual < hora_farm2:
            lista2.append(datos[0])
    print(lista2)
    
    lista3 =[]
    for elem in lista1:
        if elem in lista2:
            lista3.append(elem)

    return lista3 #devuelve los numeros de farmacia que tienen el medicamento y estan abiertas
    archivo_farm_med.close()
    archivo_hora.close()

print("farmacias que tienen el medicamento: ",cargar_farmacias_med())
print ("")
