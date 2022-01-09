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



class Empleado:
    def __init__(self,nombre,apellido,ci,domicilio,nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.domicilio = domicilio
        self.nacimiento = nacimiento
    
    def cumple(self):
        funcionarioCumple = lista1[0:1]
        dicc = {}
        dicc["19951115"] = [funcionarioCumple]
        """dicc["19970724"] = [funcionarioCumple[1]],funcionarioCumple[3]]
        dicc["19970309"] = [funcionarioCumple[2]]
        listaComprensionCumple = [a for a in dicc if lista1[:1] in a]
        cadenaCumple = "".join(listaComprensionCumple)"""
        
        if cadenaCumple == lista1[:1]:
            return dicc[fecha]
        else:
            print("Nadie Cumple ese dia")

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
            print("Cedula Correcta")

    def __repr__(self):
        return '(%s, %s, %s, %s, %s)' %(self.nombre,self.apellido,self.ci,self.domicilio,self.nacimiento)

    def nuevo(self,cedulanuevo):
        self.ci = cedulanuevo

    def general(self):
        lista1 = []
        contador = -1
        coma = ","
        parder = ")"
        parizq = "("
        for a in almacen:
            resultadoMedio = str(a).split()
        for b in resultadoMedio:
            contador +=1
            if parizq in resultadoMedio[contador] and coma in resultadoMedio[contador]:
                cadena = b.replace(coma,"") 
                cadena2 = cadena.replace(parizq,"") 
                lista1.append(cadena2)
                
            elif coma in resultadoMedio[contador]:
                cadena = b.replace(coma,"")
                lista1.append(cadena)

            elif parder in resultadoMedio[contador]:
                cadena = b.replace(parder,"")
                lista1.append(cadena)

            
            elif contador == 3:
                lista1.append(b)       

        fechanacimiento = lista1[:1]
        print(fechanacimiento)
        resultadoFinal = " ".join(lista1)
        print(resultadoFinal)
    
##FUNCIONA SOLO CON ESTAS VARIABLES, SI SE LE CAMBIA, NO FUNCIONA LA FUNCION "diacumple"
almacen = []
resultado = Empleado("German","Alvarez","4727623-0","carlos nery","19961115")     
funcionario1 = almacen.append(resultado)


    

##Funcion que permite verificar si la fecha es valida
"""funcionario = Empleado("German","Alvarez","4727623-0","carlos nery","19961115").fecha("19951115")"""

##Funcion que permite verificar si la cedula se ingreso correctamente
"""funcionario = Empleado("German","alvarez","4727623-0","carlos nery","19951115").verificaCi("4727623-0")"""

##Funcion que permite verificar si la cedula se ingreso correctamente
funcionario = Empleado("German","Alvarez","4727623-0","carlos nery","19951115").cumple()

"""funcionario = Empleado("German","Alvarez","4727623-0","carlos nery","19951115").general()"""





        
        
    
