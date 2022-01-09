def ejercicio1(nombrearchivo):
    archivo=open(nombrearchivo)
    contadorA=0
    contadorB=0
    contadorC=0
    contadorD=0
    dicc={}
    for linea in archivo:
        if linea!="":
            contadorA+=1

        palabras=linea.split()
        contadorB+=len(palabras)
        carac=linea.strip()
        contadorC+=len(carac)
        for i in linea:
            if i=="?" or i=="¿" or i=="!" or i=="¡" or i==".":
                contadorD+=1

    dicc["lineas"]=contadorA
    dicc["palabras"]=contadorB
    dicc["caracteres"]=contadorC
    dicc["simbolos"]=contadorD
    archivo.close()
    return dicc
##Funciona

def ejercicio2(archivo1,archivo2):
    dicc1= ejercicio1(archivo1)
    dicc2= ejercicio1(archivo2)
    dicc3={}
    if int(dicc1["lineas"])<int(dicc2["lineas"]):
        lineasporcentaje= (int(dicc1["lineas"])/int(dicc2["lineas"]))*100

    elif int(dicc2["lineas"])<int(dicc1["lineas"]):
        lineasporcentaje= (int(dicc2["lineas"])/int(dicc1["lineas"]))*100

    elif int(dicc1["lineas"])==0 or int(dicc2["lineas"])==0:
        lineasporcentaje= 0

    else:
        lineasporcentaje= (int(dicc1["lineas"])/int(dicc2["lineas"]))*100
                                      
                                       
    if int(dicc1["palabras"])<int(dicc2["palabras"]):
        palabrasporcentaje= (int(dicc1["palabras"])/int(dicc2["palabras"]))*100

    elif int(dicc2["palabras"])<int(dicc1["palabras"]):
        palabrasporcentaje= (int(dicc2["palabras"])/int(dicc1["palabras"]))*100

    elif int(dicc1["palabras"])==0 or int(dicc2["palabras"])==0:
        palabrasporcentaje= 0
                                       
    else:
        palabrasporcentaje= (int(dicc1["palabras"])/int(dicc2["palabras"]))*100
    
    if int(dicc1["caracteres"])<int(dicc2["caracteres"]):
        caracteresporcentaje= (int(dicc1["caracteres"])/int(dicc2["caracteres"]))*100

    elif int(dicc2["caracteres"])<int(dicc1["caracteres"]):
        caracteresporcentaje= (int(dicc2["caracteres"])/int(dicc1["caracteres"]))*100

    elif int(dicc1["caracteres"])==0 or int(dicc2["caracteres"])==0:
        caracteresporcentaje= 0
    else:
        caracteresporcentaje= (int(dicc1["caracteres"])/int(dicc2["caracteres"]))*100
                                            

    if int(dicc1["simbolos"]) < int(dicc2["simbolos"]):
        simbolosporcentaje= (int(dicc1["simbolos"])/int(dicc2["simbolos"]))*100

    elif int(dicc2["simbolos"])<int(dicc1["simbolos"]):
        simbolosporcentaje=(int(dicc2["simbolos"])/int(dicc1["simbolos"]))*100
    elif int(dicc1["simbolos"])==0 or int(dicc2["simbolos"])==0:
        simbolosporcentaje=0
    else:
        simbolosporcentaje= (int(dicc1["simbolos"])/int(dicc2["simbolos"]))*100
                                          
        

    dicc3["lineas"]=str(lineasporcentaje)+"%"
    dicc3["palabras"]=str(palabrasporcentaje)+"%"
    dicc3["caracteres"]=str(caracteresporcentaje)+"%"
    dicc3["simbolos"]=str(simbolosporcentaje)+"%"

    return dicc3
##Funciona





class Oferta():
    def __init__(self,codigo,precio,precio_oferta):
        self.codigo = codigo
        self.precio = precio
        self.precio_oferta = precio_oferta
        self.envio_gratis = False

    def __repr__(self):
        return str(self.codigo)+" "+str(self.precio)+" "+str(self.precio_oferta)

    def get_precio(self):
        return self.precio

    def set_precio(self,nuevo_precio):
        self.precio = nuevo_precio

    def get_envio_gratis(self):
        return self.envio_gratis

    def set_envio_gratis(self,nuevo_valor):
        self.envio_gratis = nuevo_valor

    def ParteB(lista):
        return[x for x in lista if (x.precio_oferta*100/x.precio)<50]

    def ParteC(self):
        self.set_envio_gratis(True)

    def ParteD(listaofertas):
        for oferta in listaofertas:
            oferta.ParteC()

class Tienda():
    def __init__(self, nombre, direccion, listadeofertas):
        self.nombre = nombre
        self.direccion = direccion
        self.listadeofertas = listadeofertas

    def borrar(self):
        self.listadeofertas = []

    def cargar(archivoofertas):
        archiv1=open(archivoofertas)
        listaof=[]
        for linea in archiv1:
            datos=linea.strip().split(",")
            ofer = Oferta(datos[0],datos[1],datos[2],datos[3])
            listaof.append(ofer)
        archivo.close()
        return listaof
##Funciona


oferta1=Oferta(19845,15,8)
print(oferta1)
print(oferta1.envio_gratis)
oferta2=Oferta(19245,14,9)
print(oferta2)
Oferta.ParteC(oferta1)
print(oferta1.envio_gratis)

        

            
        
        
        

    
    
