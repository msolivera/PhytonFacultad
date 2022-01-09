import cgi, cgitb
cgitb.enable()
print ("Content-Type: text/html")
print ("")
params = cgi.FieldStorage()
logueado = False
mensaje_error = None
usuario = params.getvalue("usuario")
password = params.getvalue("contrasena")
if not usuario or not password:
mensaje_error = "Debes ingresar usuario y contrase&ntilde;a"
elif usuario == "yo" and password == "yo":
logueado = True
else:
mensaje_error = "Credenciales incorrectas"
# Abrimos la pagina HTML
print ("""
<html>
<head>
<title>Formulario HTML</title>
</head>
<body>
""")
# Si las credenciales fueron correctas, mostramos bienvenida
if logueado:
print ("Bienvenido,", usuario)
# Si no esta logueado, mostramos formulario
else:
# Si ocurre un error, mostramos el mensaje antes del form
if mensaje_error:
print (mensaje_error)
# Mostramos el formulario de ingreso
print ("""
<form method="post">
<label>Usuario</label>
<input type="text" name="usuario" />
<label>Contrase&ntilde;a</label>
<input type="password" name="contrasena" />
<input type="submit" value="Ingresar" />
</form>
""")
# Finalizamos el HTML
print ("""
</body>
</html>
""")
