archivo1=open("texto.txt")
archivo2=open("pruebaVOCALES.txt","w")
linea=archivo1.readline()
resultado=""
contador=1
for linea in archivo1:
	if linea[i] in "aeiou":
		resultado+=" "
		contador=contador+1
		linea=archivo1.readline()
	else:
		resultado+= linea[i]
	archivo2.write(resultado)




archivo1.close()
archivo2.close()
print(archivo1)
