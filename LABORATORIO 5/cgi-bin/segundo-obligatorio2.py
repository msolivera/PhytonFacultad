import urllib.request
import cgi, cgitb
cgitb.enable()

print ("Content-Type: text/html")
print ("")

params = cgi.FieldStorage()

if "medicamento" not in params or "mi_ubicacion_actual" not in params:
    print("<h1>Ups.. ha ocurrido un error!</h1><br><h3><i>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp....Rellena los campos para obtener una respuesta.</i></h3>")

else:
    medicamento = params.getvalue("medicamento")
    ubicacion= params.getvalue("mi_ubicacion_actual")
    #if medicamento=="remedio" and ubicacion=="mi casa":
      #  print("hola agus")
   # else:
       # print("Medicación o ubicación no válidas")
      #  """ejemplo para que pongas y pruebes el resultado
       # esto hay que modificarlo con todas las funciones
      #  pone en medicamento remedio y en ubucacion mi casa"""
        
#cargar mi ubicacion
#cargar el medicamento
#cargar farmacias con medicamento
#cargar ubicacion de las farmacias
#calcular las distancias a todas
#Definir cual es la menor distancia
#calcular la hora
#comparar hora para ver si está abierto
#mostrar farmacia, y si esta abierto
def cargar_ubicacion():
    url = "http://nominatim.openstreetmap.org/search/"+ubicacion
    formato = "json"

    response = urllib.request.urlopen(url+"?q="+ubicacion.replace(" ","%20")+"&format="+formato)
    ubicacion_persona = response.read().decode("UTF-8")

    return ubicacion_persona

def cargar_codigo_med():
    archivo_med = open("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\cgi-bin\\medicamentos.dat")
    for linea in archivo_med:
        med = linea.split(",")
        if med[1] == medicamento:
            return med[0]

medic = cargar_codigo_med()

def cargar_farmacias_med(medic):
    archivo_farm_med = open("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\cgi-bin\\farm-med.dat")
    for linea in archivo_farm_med:
        farm = linea.split(",")
        list_farm = []
        if farm[1] == cargar_codigo_med():
            lista_farm.append(farm[0])
            
    return list_farm

a = cargar_ubicacion(ubicacion)
b = cargar_codigo_med (medicamento)
c = cargar_farmacias_med(medic)

print(a,b,c)

