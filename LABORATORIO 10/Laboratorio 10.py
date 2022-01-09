#LABORATORIO 10

#EJERCICIO 1:

def parametro (num):
    return[x for x in range (num) if x%2==0]

#print(parametro(10))

#EJERCICIO 2:

def ejercicio():
    
    return[(x+1)*(x-1) for x in range (1,1000) if (x+1)*(x-1)<1000]

#print(ejercicio())

#EJERCICIO 3:

def transformacion(cadena):

    return[ "".join(c.upper() for c in cadena if c != "." and c != "," and c !=" ") ]

#print(transformacion("hoy es, un gran.dia"))

#EJERCICIO 4:

def fecha (cadena):

    return[elem[3:6]+elem[0:3]+elem[6:-1] for elem in cadena.split(",")]

#print(fecha("10/11/2016,01/02/2016"))

#EJERCICIO 5:

class Mail():
    
    def __init__(self, asunto, cuerpo, destinatarios):
        
        self.asunto = asunto
        self.cuerpo = cuerpo
        self.destinatarios = [elem  for elem in destinatarios if elem !="@ucu.edu.uy" and elem !="@gmail.com" ]
        self.copia = [ elem for elem in destinatarios if elem in "@ucu.edu.uy"  ]
        self.copia_oculta = [elem for elem in destinatarios if elem in "@gmail.com"  ]

    def __repr__ (self):
        return "Asunto: "+self.asunto+" Cuerpo: "+self.cuerpo+" Destinatarios: "+str(self.destinatarios)+ " Copia: "+str(self.copia)+" Copia Oculta: "+str(self.copia_oculta)

correo=Mail("asunto","cuerpo",["molivera@ucu.edu.uy","molivera@gmail.com","molivera@yahoo.com","molivera@hotmail.com"])
print(correo)

#AYUDAAAAAAAA




