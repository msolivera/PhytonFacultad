#1)
print([x+8 for x in range(3,7)])

#2)
print([c for c in "programa"])

#3)
print([[z,k] for z in range(3) for k in range(3,5)])

#4)
print([s.upper() for s in "hoy es viernes"])

#5)
print([len(z) for z in "hoy es viernes 24".split()])

##########################################
#Ej1)
print("\nEjercicio 1\n")
##1. Crear una función que retorne una lista creada por comprensión con los
##números pares hasta un número dado por parámetro.
def pareshastan(n):
    return [numero for numero in range(1,n+1) if numero%2==0]

print(pareshastan(25))

#Ej2)
print("\nEjercicio 2:\n")
##2. Utilizar comprensión de listas para obtener los números que se obtienen
##como “(n+1)*(n–1)” para n>1, y que son menores de 1000. La lista de
##estos números comienza con [0, 3, 8, 15, 24, ...].
print([(n+1)*(n-1) for n in range(1000) if n>1])

#Ej3)
print("\nEjercicio 3:\n")
##3. Utilizando listas por comprensión implementar una función que toma
##una cadena y devuelve la cadena en mayúsculas sin espacios en blanco
##ni símbolos de puntuación (los dígitos no se cambian).
def cadenalimpia(cadena):
    return "".join([letra.upper() for letra in cadena.strip() if not letra in "0123456789 :,;."])

print(cadenalimpia("Es 1 la idea, que vale por: 100, muchas palabras"))

#Ej4)
print("\nEjercicio 4:\n")
##4. Dado una cadena de caracteres con fechas en formato “MM/DD/YYYY”
##separadas por coma, obtener una lista de cadenas de caracteres con
##las fechas en formato “DD/MM/YYYY”
##Ej.: "10/11/2016,01/02/2016"  ['11/10/2016', '02/01/2016']

print(["{}/{}/{}".format(fecha.split("/")[1],fecha.split("/")[0],fecha.split("/")[2]) for fecha in "10/11/2016,01/02/2016,05/06/2017,07/31/2017".split(",")])

#Otra solución:

def reformatFecha(fecha):
    fecha_parts = fecha.split("/")
    return "{}/{}/{}".format(fecha_parts[1],fecha_parts[0],fecha_parts[2])

fechas = ["10/11/2016","01/02/2016","05/06/2017","07/31/2017"]
print([reformatFecha(fecha) for fecha in fechas])

#Ej5)
print("\nEjercicio 5:\n")
##5. Dada la siguiente clase:
##class Mail(object):
##  def __init__(self, asunto, cuerpo, destinatarios):
##      self.asunto = asunto
##      self.cuerpo = cuerpo
##      self.destinatarios = [ ... ]
##      self.copia = [ ... ]
##      self.copia_oculta = [ ... ]
##a. Utilizando listas por comprensión, completar el constructor de la
##clase a partir de la lista de destinatarios (cadenas de caracteres
##con las direcciones de email) que se recibe como parámetro
##siguiendo las siguientes condiciones:
##b. Las direcciones de email que pertenezcan al dominio “ucu.edu.uy”
##van en el campo (lista) copia.
##c. Las direcciones de email que pertenezcan al dominio “gmail.com”
##van en el campo (lista) copia_oculta.
##d. Todas las demás dirección van en la lista de destinatarios del mail.
class Mail(object):
    def __init__(self, asunto, cuerpo, destinatarios):
        self.asunto = asunto
        self.cuerpo = cuerpo
        self.destinatarios = [mail for mail in destinatarios if (not "ucu.edu.uy" in mail) and (not "gmail.com" in mail)]
        self.copia = [mail for mail in destinatarios if "ucu.edu.uy" in mail]
        self.copia_oculta = [mail for mail in destinatarios if "gmail.com" in mail]

mail = Mail("hola","saludo",["rroballo@ucu.edu.uy", "gpennino@ucu.edu.uy","rodolfo.roballo@gmail.com","fwagner@gmail.com","rroballo@genexus.com"])
print(mail.destinatarios)
print(mail.copia)
print(mail.copia_oculta)
            
