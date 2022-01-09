#PREPARACION CUARTO LABORATORIO

#EJERCICIO 1:

def obtener_cadena():
    cadena=input("Ingrese cadena deseada: ")

    if cadena != "fin":
        
        if len(cadena)<1:
            print("ingrese al menos un caracter: ")
            cadena=input("Ingrese cadena deseada: ")
        if "1" in cadena or "2" in cadena or "3" in cadena or "4" in cadena or "5" in cadena or "6" in cadena or "7" in cadena or "8" in cadena or "9" in cadena or "0" in cadena:
            print("No puede ingresar numeros: ")
            cadena=input("Ingrese cadena deseada: ")
            
        print(cadena)

    if cadena == "fin":

        print("Ha finalizado la escritura")    
       
#obtener_cadena()    


#EJERCICIO 2:

def palindromos (cadena):

    resultado = []

    cadena=cadena.lower().split(" ")

    for palabra in cadena:
        if palabra == palabra [::-1]:
            resultado.append(palabra)

    return resultado

#print(palindromos("Hay que reconocer seres extraterrestres"))

    
#EJERCICIO 3:

class empleado():
    

    def __init__ (self,nombre,apellido,cedula,domicilio,fecha_nac):

        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula
        self.domicilio=domicilio
        self.fecha_nac=fecha_nac

#ESTO ANDAAA
    def __repr__ (self):

        return "EMPLEADO: "+self.nombre+" "+ self.apellido+" C.I: "+str(self.cedula)+" Domicilio: "+self.domicilio+" Fecha NAC: "+str(self.fecha_nac)
##ESTO ANDA
    def validar_fecha (self):
        año = int(self.fecha_nac[0:4])
        mes = int(self.fecha_nac[4:6])
        dia = int(self.fecha_nac[6:8])
        
        if (((año >= 1900) and (año <= 2017)) and ((mes >= 1) and (mes <= 12)) and ((dia >=1) and (dia <= 30))):
            return True
        else:
            return False

#ESTO ANDAAA
    def validar_ci (self):

        numeros=["1","2","3","4","5","6","7","8","9","0"]
        
        if "-" in self.cedula:
            ci=self.cedula.split("-")
            if len(ci[0])== 7 and len(ci[1])==1 and ci[1] in numeros:
                for n in ci[0]:
                    if n in numeros:
                      return True
                    else:
                        return False
            else:
                return False
        else:
             return False
#esto anda
def cumple_por_fecha(fecha,lista):
		aux=[e for e in lista if e.fecha_nac==fecha]
		return aux
#ANDA PERO NO POR COMPRESION    
def lista_nombres(lista):

    return [x.nombre+" "+x.apellido for x in lista]

#ESTO ANDAAA
def ingresar_empleado (lista):

    archivo = open("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\PARCIAL 4\\empleados.csv","w")

    dicc={}
    for e in lista:
        if e.cedula not in dicc:

            dicc[e.cedula]=e

            archivo.write(str(e) + "\n")
            
    return dicc
    archivo.close()

        

emp1=empleado("micaela","olivera","5230422-0","sebastopol 5665","19940304")
emp2=empleado("jorge","llagarias","4568987-0","sebastopol 5665","19900928")
emp3=empleado("pablo","perez","5897455-6","8 de octubre 5897","19940304")
#print(emp1)
#print(emp1.validar_fecha())
#print(emp1.validar_ci())
#print(ingresar_empleado([emp1,emp2,emp3]))
#print(lista_nombres([emp1,emp2,emp3]))
#print(cumple_por_fecha("19940304",[emp1,emp2,emp3]))        
