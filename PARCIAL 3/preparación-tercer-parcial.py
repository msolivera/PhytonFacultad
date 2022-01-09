##La función deberá recibir el nombre de un archivo como parámetro y elaborar la siguiente
##estadística:
##1. Cantidad de líneas en el archivo.
##2. Cantidad de caracteres en el archivo (incluyendo caracteres de control).
##3. Cantidad de caracteres de la línea con mayor cantidad de caracteres.
##4. Promedio de la cantidad de caracteres por línea (sin contar la líneas que estén
##vacías, es decir que solo tengan espacios o caracteres de control)
def estadistica_archivo(nombre_archivo):
    archivo = open(nombre_archivo)

    cant_lineas = 0
    cant_lineas_no_vacia = 0
    cant_cars = 0
    cant_cars_linea = 0

    for linea in archivo:
        cant_lineas += 1
        ##  contamos las líneas no vacías
        if linea.strip() != "":
            cant_lineas_no_vacia +=1
        
        cant_cars += len(linea)

        ## guardamos el largo de la linea que tiene más caracteres
        if len(linea) > cant_cars_linea:
            cant_cars_linea = len(linea)

    archivo.close()
    return [cant_lineas, cant_cars, cant_cars_linea, cant_cars/cant_lineas_no_vacia]

print(estadistica_archivo("c:\\temp\\IntelGFXCoin.log"))


import random

class Persona():
    def __init__(self,nombre,apellido,email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def cargar_personas(nombre_archivo):
        archivo = open(nombre_archivo)

        lista_personas = []

        for linea in archivo:
            datos = linea.strip().split("|")

            persona = Persona(datos[0], datos[1], datos[2])

            lista_personas.append(persona)

        archivo.close()

        return lista_personas

    def sorteo(lista):
        indice = random.randint(0,len(lista)-1)

        return lista[indice]
        

    def grabar_persona(self):
        archivo = open(self.nombre+"."+self.apellido,"w")

        archivo.write(self.email)

        archivo.close()



personas = Persona.cargar_personas("c:\\temp\\personas.txt")

persona_sorteo = Persona.sorteo(personas)

persona_sorteo.grabar_persona()


class Email():
    def __init__(self, remitente, destinatarios, asunto, cuerpo):
        self.remitente = remitente
        self.destinatarios = destinatarios
        self.asunto = asunto
        self.cuerpo = cuerpo


    def validar(correo):
        datos = correo.split("@")

        ## verificamos que la lista tenga 2 cadenas con contenido
        if len(datos) != 2 or len(datos[0])==0 or len(datos[1])==0:
            return False

        datos1 = datos[1].split(".")

        ## verificamos que la lista tenga 3 cadenas con contenido
        if len(datos1) != 3 or len(datos1[0]) == 0 or len(datos1[1]) == 0 or len(datos1[2]) == 0:
            return False

        return True

        
    def validar_destinatarios(self):
        for mail in self.destinatarios:
            if Email.validar(mail) == False:
                return False
        return True

    def crear_email(personas, remitente, asunto, cuerpo):

        destinatarios = []

        ## agregamos los destinarios
        for per in personas:
            destinatarios.append(per.email)

        return Email(remitente, destinatarios, asunto, cuerpo)


mail = Email.crear_email(personas,"remitente@ucu.edu.uy","Prueba","Contenido")
print(mail.asunto)
print(mail.destinatarios)
        
            
        
