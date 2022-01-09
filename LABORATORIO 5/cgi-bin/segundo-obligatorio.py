import cgi, cgitb
cgitb.enable()

print ("Content-Type: text/html")
print ("")

params = cgi.FieldStorage()
print(type(params))

if "medicamento" not in params or "mi_ubicacion_actual" not in params:
    print("<h1>Ups.. ha ocurrido un error!</h1><br><h3><i>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp....Rellena los campos para obtener una respuesta.</i></h3>")
else:
    medicamento = params.getvalue("medicamento")
    ubicacion= params.getvalue("mi_ubicacion_actual")
    if medicamento=="remedio" and ubicacion=="mi casa":
        print("hola agus")
    else:
        print("Medicación o ubicación no válidas")
        """ejemplo para que pongas y pruebes el resultado
        esto hay que modificarlo con todas las funciones
        pone en medicamento remedio y en ubucacion mi casa"""
        
