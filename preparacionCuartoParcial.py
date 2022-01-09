"""def ejercicio1():
    cadena = input("Ingrese una cadena: ")
    abc = " abcdefghijklmnopqrstuvwxyz"
    listaLetras = []
    almacen = []
    if len(cadena) > 0:
        for i in cadena:
            if i in abc:
                listaLetras.append(i)
                cadenanueva = "".join(listaLetras)
                cadena = cadenanueva
            else:
                cadena = input("Ingrese una nueva cadena: ")
    print(cadena)
ejercicio1()"""




    
def ejercicio2(cadena):
    cadenaAlReves = cadena[::-1]
    listacadena = cadena.split(" ")
    listaalreves = cadenaAlReves.split(" ")
    almacen = []
    almacen2 = []
    almacen3 = []
    for i in listacadena:
        almacen.append(i)
    for a in listaalreves:
        if a in almacen:
            almacen2.append(a)
        else:
            almacen3.append(a)

        if almacen2 == []:
            almacen2.append("No hay palindromos en la cadena")
        else:
            return almacen2

funcionario = ["German Alvarez","Valeria Lorenzo", "Camila Alvarez", "Jose Perez"]
dicc = {}
dicc["19951115"] = [funcionario[0],funcionario[3]]
dicc["19970724"] = [funcionario[1]]
dicc["19970309"] = [funcionario[2]]

class Empleado:
    def __init__(self,nombre,apellido,ci,domicilio,nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.domicilio = domicilio
        self.nacimiento = nacimiento

    def fecha(self,nacimiento):
        año = int(nacimiento[0:4])
        mes = int(nacimiento[4:6])
        dia = int(nacimiento[6:8])
        if (((año >= 1900) and (año <= 2017)) and ((mes >= 1) and (mes <= 12)) and ((dia >=1) and (dia <= 30))):
            print("Fecha correcta")
        else:
            print("Fecha incorrecta")
    
    def verificaCi(self,cedula):
        nros = "0123456789"
        listaCedula = []
        contador = 0
        for i in cedula:
            listaCedula.append(i)    
        listaComprension = [a for a in listaCedula if a not in nros]
        if len(listaComprension) >= 1:
            print("Por favor solo numeros")
        else:
            print("CI correcta")

    def __repr__(self):
        return '(%s, %s, %s, %s, %s)' %(self.nombre,self.apellido,self.ci,self.domicilio,self.nacimiento)

    def nuevo(self,cedulanuevo):
        self.ci = cedulanuevo

    def cumple(self,fecha):
        funcionario = ["German Alvarez","Valeria Lorenzo", "Camila Alvarez", "Jose Perez"]
        dicc = {}
        dicc["19951115"] = [funcionario[0],funcionario[3]]
        dicc["19970724"] = [funcionario[1]]
        dicc["19970309"] = [funcionario[2]]
        for a in dicc:
            print(a)
            if a in dicc:
                return dicc[a]
        
##Funcion que permite verificar si la fecha es valida
"""funcionario = Empleado("German","Alvarez","4727623-0","carlos nery","19951115").fecha("4727623-0")"""
         
##Funcion que permite verificar si la cedula se ingreso correctamente
"""funcionario = Empleado("German","alvarez","4727623-0","carlos nery","19951115").verificaCi("4727623-0")"""

##Funcion que permite verificar si la cedula se ingreso correctamente
funcionario = Empleado("German","Alvarez","4727623-0","carlos nery","19951115").cumple("19951115")




        
        
    
