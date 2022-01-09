#Ej1

def ej1():
	limitador= True
	num="1234567890"
	txt1=""
	while limitador:
		txt=input("Ingrese texto sin numeros (para terminar ingrese Fin) : ")
		txt2=[i for i in txt if i in num]
		if len(txt2) > 0 or len(txt) == 1:
			print("Texto no válido por favor ingrese otro")
		elif txt == "Fin":
			limitador= False
		else:
			print("Texto válido por favor ingrese otra linea")
			txt1=txt
	return(txt1)
	
#prueba=ej1()
#print(prueba)

#Ej2

def ej2(cadena):
	aux=cadena.lower().strip().split()
	resultado=[i for i in aux if i[::-1]==i]
	if len(resultado) > 0:
		return resultado
	else:
		return ("No hay palíndromos")
	

#prueba2=ej2("Hay que recoNocer SereS extrAteRrestres")
#print(prueba2)

#Ej3
import time

class empleado:
	def __init__(self,n,a,c,d,f):
		self.nombre=n
		self.apellido=a
		self.cedula=c
		self.dom=d
		self.cumple=f
	def validar_fecha(fecha):
		aux=fecha.strip().split("/")
		año=int(time.strftime("%Y")) - 20
		if int(aux[0]) <= 0 or int(aux[0]) > 30 or int(aux[1]) <= 0 or int(aux[1]) >= 12 or int(aux[2]) < 1900 or int(aux[2]) > año:
			x=input("Nueva fecha correcta: ")
		else: 
			x=fecha
		return x
	def validar_cedula(ci):
		num="1234567890"
		x=[c for c in ci if c not in num]
		if len(x)>0:
			s=str(input("Nueva cedula: "))
		else:
			s=ci
		return s
	def nuevo():
		no=str(input("Nombre: "))
		ap=str(input("Apellido: "))
		ci=str(input("C.I.: "))
		dom=str(input("Domicilio: "))
		fn=str(input("Fecha de nacimiento: "))
		aux=empleado.validar_fecha(fn)
		aux2=empleado.validar_cedula(ci)
		return empleado(no,ap,aux2,dom,aux)
	def __repr__(self):
		return("{},{},{},{},{}".format(self.nombre,self.apellido,self.cedula,self.dom,self.cumple))
	def guardar(lista):
		archivo=open("datos.csv","w")
		for i in lista:
			archivo.write(str(i))
			archivo.write("\n")
	def cargar():
		archivo=open("datos.csv")
		lista=[]
		for l in archivo:
			aux=l.strip().split(",")
			lista.append(empleado(aux[0],aux[1],aux[2],aux[3],aux[4]))
		return lista
	def cumples(lista):
		dic={}
		for e in lista:
			if str(e.cumple) not in dic:
				dic[str(e.cumple)]=[e]
			else:
				dic[str(e.cumple)].append(e)
		return dic
	def cumple_por_fecha(fecha,lista):
		aux=[e for e in lista if e.cumple==fecha]
		return aux
		
em1=empleado.nuevo()
print(em1)
em2=empleado.nuevo()
em3=empleado.nuevo()



listae=[em1,em2,em3]

empleado.guardar(listae)

opa=empleado.cargar()

cump=empleado.cumples(opa)
print(cump)
print (" ")
ej3=empleado.cumple_por_fecha("24/05/1996",opa)
print(ej3)
