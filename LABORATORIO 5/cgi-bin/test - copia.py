import math
import time
import urllib.request
import cgi, cgitb
cgitb.enable()

def cargar_med():
    archivo_med = open("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\cgi-bin\\medicamentos.dat")
    for linea in archivo_med:
        med = linea.split(",")
        if med[1] == medicamento:
            return med[0] #devuelve el codigo del medicamento
        
def cargar_farmacias_med():
    archivo_farm_med = open("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\cgi-bin\\farm-med.dat")
    lista = []
    for linea in archivo_farm_med:
        farm = linea.strip().split(",")
        if farm[1] == cargar_med():
            lista.append(farm[0])

    return lista #devuelve los numeros de farmacia que tienen el medicamento

def cargar_ubicacion_persona():
    ubicacion = ubicacion1
    url = "http://nominatim.openstreetmap.org/search/"
    formato = "json"
    response = urllib.request.urlopen(url+"?q="+ubicacion.replace(" ","%20")+"&format="+formato)
    respuesta = response.read().decode("UTF-8")
    respuesta = respuesta#lista con latitud y longitud
    return respuesta




print(cargar_farmacias_med())
print(cargar_ubicacion_persona())
print(cargar_ubicaciones_farmacias())

