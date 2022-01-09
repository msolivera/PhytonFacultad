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
            lista.append(farm[0])

    lista2 =[]
    for linea in archivo_hora:
        hora_farm1= linea.strip().split(",")[





            

    return lista #devuelve los numeros de farmacia que tienen el medicamento
    archivo_farm_med.close()
    archivo_hora.close()
###
def cargar_ubicacion_persona():
    ubicacion = ubicacion1
    url = "http://nominatim.openstreetmap.org/search/"
    formato = "json"
    response = urllib.request.urlopen(url+"?q="+ubicacion.replace(" ","%20")+"&format="+formato)
    respuesta = response.read().decode("UTF-8")
    datos = respuesta.split("],")
    a = datos[1]
    lat = float(a.split(",")[0].replace("\"lat\":\"","").replace("\"",""))
    lon = float(a.split(",")[1].replace("\"lon\":\"","").replace("\"",""))
    lat_lon = [lat,lon]
    return lat_lon#devuelve una lista con los numeros latitud y longitud
###
def cargar_ubicaciones_farmacias():
    archivo = open("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\cgi-bin\\farmacias.dat")
    dicc = {}
    for linea in archivo:
        url = "http://nominatim.openstreetmap.org/search/"
        formato = "json"
        datos1 = linea.strip().split(",")
        if datos1[0]in cargar_farmacias_med():
            ubicacion = datos1[2]
            response = urllib.request.urlopen(url+"?q="+ubicacion.replace(" ","%20")+"&format="+formato)
            respuesta = response.read().decode("UTF-8")
            datos = respuesta.split("],")
            a = datos[1]
            lat = float(a.split(",")[0].replace("\"lat\":\"","").replace("\"",""))
            lon = float(a.split(",")[1].replace("\"lon\":\"","").replace("\"",""))
            lat_lon = [lat,lon]
            dicc[datos1[0]]= lat_lon
    return dicc #devuelve un diccionario con los codigos de farmacias y la lista lat y lon
    archivo.close()

###  
def calcular_distancias():
    distancias = {}
    punto_ref = cargar_ubicacion_persona()
    puntos_farm = cargar_ubicaciones_farmacias()
    for elem in puntos_farm:
        print(puntos_farm[elem][0])
        print(puntos_farm[elem][1])
        print(punto_ref[0])
        print(punto_ref[1])
        
        distancias[elem]=(math.sqrt((((puntos_farm[elem][0])-(punto_ref[0]))**2)+(((puntos_farm[elem][1])- (punto_ref[1]))**2)))

    return distancias #devuelve un diccionario con los codigos de las farmacias y las distancias a la persona
'''
def abierta():
    archivo = open("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\cgi-bin\\farmacias.dat")
    hora = time.strftime("%H:%M:%S")
    hora_actual = hora.split(":")
    hora_actual = "".join(hora_actual)
    hora_actual = int(hora_actual)
    
    lista_distancias =[]
    distancias = calcular_distancias()
    for elem in distancias:
        lista_distancias.append(distancias[elem])
    lista_distancias = lista_distancias.sort()
        
    for distancia in lista_distancias:
        x=0
        if x ==0 or distancias[distancia]<x and #esta abierta:
            x = distancias[distancia]
    return distancias.keys(x)'''
        
    
print ("Content-Type: text/html")
print ("")

params = cgi.FieldStorage()


if "medicamento" not in params or "mi_ubicacion_actual" not in params:
    print("<h1>Ups.. ha ocurrido un error!</h1><br><h3><i>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp....Rellena los campos para obtener una respuesta.</i></h3>")
else:
    medicamento = params.getvalue("medicamento")
    ubicacion1= params.getvalue("mi_ubicacion_actual")


print("farmacias que tienen el medicamento: ",cargar_farmacias_med())
print ("")
print("ubicacion de la persona: ",cargar_ubicacion_persona())
print ("")
print("ubicaciones de farmacias: ",cargar_ubicaciones_farmacias())
print ("")
print("distancias: ",calcular_distancias())

print(34.9057809-34.88873745)
