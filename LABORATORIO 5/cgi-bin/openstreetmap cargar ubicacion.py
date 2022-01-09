import urllib.request

url = "http://nominatim.openstreetmap.org/search/"
ubicacion = "Avda. Gral. Rondeau 1404"
formato = "json"

response = urllib.request.urlopen(url+"?q="+ubicacion.replace(" ","%20")+"&format="+formato)
respuesta = response.read().decode("UTF-8")
datos = respuesta.split("],")
a = datos[1]
lat = float(a.split(",")[0].replace("\"lat\":\"","").replace("\"",""))
lon = float(a.split(",")[1].replace("\"lon\":\"","").replace("\"",""))


print(lat)
print(lon)
