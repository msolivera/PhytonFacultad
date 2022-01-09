#medicamento = "omeoprazol ion"
#ubicacion1 = "Avda. 8 de octubre 2738, Montevideo"
 
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

    lista3 =[]
    for elem in lista1:
        if elem in lista2:
            lista3.append(elem)
   
    return lista3 #devuelve los numeros de farmacia que tienen el medicamento y estan abiertas
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

        distancias[elem]=(math.sqrt((((puntos_farm[elem][0])-(punto_ref[0]))**2)+(((puntos_farm[elem][1])- (punto_ref[1]))**2)))

    return distancias #devuelve un diccionario con los codigos de las farmacias y las distancias a la persona

def mas_cercana_abierta_con_medicamento():
    distancias = calcular_distancias()
    mas_cercana = 0
    for elem in distancias:
        if (distancias[elem]) < mas_cercana or mas_cercana ==0:
           mas_cercana = distancias[elem]
           respuesta = elem
    
    return respuesta #devuelve el codigo de la farmacia mas cercana con el medicamento y que este abierta
    
print ("Content-Type: text/html")
print ("")

params = cgi.FieldStorage()


if "medicamento" not in params or "mi_ubicacion_actual" not in params:
    print("<h1>Ups.. ha ocurrido un error!</h1><br><h3><i>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp....Rellena los campos para obtener una respuesta.</i></h3>")
else:
    medicamento = params.getvalue("medicamento")
    ubicacion1= params.getvalue("mi_ubicacion_actual")
    try:
        print(mas_cercana_abierta_con_medicamento())
    except IndexError:
        print("Error: verifique los datos de direccion y medicamento")
    except UnboundLocalError:
        print("no hay farmacias abiertas en este momento")
       
			


'''
print("farmacias que tienen el medicamento: ",cargar_farmacias_med())
print ("")
print("ubicacion de la persona: ",cargar_ubicacion_persona())
print ("")
print("ubicaciones de farmacias: ",cargar_ubicaciones_farmacias())
print ("")
print("distancias: ",calcular_distancias())'''
#print(mas_cercana_abierta_con_medicamento())# esta es la unica salida


