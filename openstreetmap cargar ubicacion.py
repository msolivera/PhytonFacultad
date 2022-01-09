import urllib.request
url = "http://nominatim.opentreetmap.org/search/"
ubicacion = "Avda. 8 de octubre 2738, Montevideo"
formato = "json"

response = urllib.request.urlopen(url+"?q="+ubicacion.replace(" ","%20"))
respuesta = response.read().decode("UTF-8")

print (respuesta)

try:
    contenido = urllib.request.urlopen("http://nominatim.opentreetmap.org/search/")
except urllib.error.URLError:
    print ("url incorrecta")
    
