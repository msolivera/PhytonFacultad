import cgi, cgitb
cgitb.enable()

print ("Content-Type: text/html")
print ("")

params = cgi.FieldStorage()
if "usuario" not in params or "contrasena" not in params:
    print ("Debes ingresar usuario y contrase&ntilde;a")
else:
    usuario = params.getvalue("usuario")
    password = params.getvalue("contrasena")
    if usuario == "yo" and password == "yo":
        print ("Bienvenido!")
    else: print ("Credenciales incorrectas")

