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
    if medicamento=="remedio" and ubicacion=="mi casa":
        print("hola agus")
        print("<html><head><title>Ejemplo del uso de formularios - aprenderaprogramar.com</title> </head> <body><form method=\"get\" action=\"C:\Users\usuario\Desktop\2do Obligatorio mica-agus\web.html\"> <button type=\"submit\"> </button> </form></body></html>")
  
    else:
        print("Medicación o ubicación no válidas")
        """ejemplo para que pongas y pruebes el resultado
        esto hay que modificarlo con todas las funciones
        pone en medicamento remedio y en ubucacion mi casa"""
        
