class persona ():

    def __init__ (self, nombre,apellido,cedula,telefono,direccion):
        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula
        self.telefono=telefono
        self.direccion=direccion

    def __repr__(self):
        return "nombre: "+self.nombre+" apellido: "+self,apellido+" cedula: "+str(self.cedula)+" telefono: "+str(self.telefono)+" direccion: "+self.direccion
    


    def guardar (lista):
        archivo=open("persona.csv","w")
        for p in lista:
            archivo.write(p.nombre+","+p.apellido+","+p.cedula+","+p.telefono+","+p.direccion+"\n")
            archivo.close()


    def cargar():
        archivo=open("persona.csv")
        lista=[]
        for lista in archivo:
            dato=linea.strip().split(",")
            per=persona(dato[0],dato[1],dato[2],dato[3],dato[4])
            lista.append(per)
        archivo.close()
        return lista

    def nueva ():
        nombre= input("ingrese nombre")
        apellido=input("ingrese apellido")
        cedula=input("ingrese cedula")
        telefono=input("Ingrese telefono")
        direccion=input("ingrese direccion")

        return persona (nombre,apellido,cedula,telefono,direccion)

    def buscar (lista,nombre):
        resultado=[]
        for p in lista:
            if p.nombre==nombre:
                resultado.append(p)

        return resultado


print("AGENDA")
print ("MENU PRINCIPAL \n 1-Guardar un Contacto \n 2-Cargar datos \n 3-Buscar un contacto \n 4-SALIR")
opciones=["1","2","3","4"]
x=""
lista_personas=[]

while x!="4":

    x=input ("ingrese opcion deseada")

    if x=="1":
        p1=persona.nueva()
        lista_personas.append(p1)
        persona.guardar(lista_personas)

    elif x=="2":
        lista_personas= persona.cargar()

    elif x=="3":
        nombre=input("ingrese nombre que desea buscar: ")
        lis=persona.buscar(lista_personas,nombre)
        for p in lis:
            print(p)

    else:
        print ("Usted ha finalizado el programa.")
a=input()    




#terminar


