def estadistica (nombre_archivo):

    archivo = open (nombre_archivo, "r")

    dicc={}
    

    cant_lineas_no_vacias = 0
    cant_palabras = 0
    cant_cars = 0
    cant_cars_especiales = 0

    for linea in archivo:
        
        ##cuento lineas no vacias
        if linea !="":
            cant_lineas_no_vacias += 1

        ##cuento cantidad de palabras
        p=linea.split()
        cant_palabras+=len(p)
        #cuento cantidad de caracteres
        caracteres=linea.strip()
        cant_cars+=len(caracteres)  
        
        for p in linea:
           if p=="?" or p=="¿" or p=="!" or p=="¡" or p==".":
                ##cuento simbolos si estan en linea
                cant_cars_especiales += 1

            

    dicc["Lineas "]=cant_lineas_no_vacias
    dicc["Palabras "]=cant_palabras
    dicc["Caracteres"]=cant_cars
    dicc["Simbolos "] =  cant_cars_especiales
    return dicc
            
    archivo.close()
    
            
#print(estadistica("C:\\Temp\\EJERCICIO1.txt"))
a=estadistica("C:\\Temp\\EJERCICIO1.txt")
b=estadistica("C:\\Temp\\EJERCICIO2.txt")


def comparacion():

    dicc1={'Lineas ': 9, 'Palabras ': 140, 'Caracteres': 864, 'Simbolos ': 7}
    dicc2={'Lineas ': 6, 'Palabras ': 79, 'Caracteres': 468, 'Simbolos ': 3}

    dicc_result={}

    if int((dicc1['Lineas '])<int(dicc2['Lineas '])):
           dicc_result["LINEAS"]=(int(dicc1['Lineas '])/int(dicc2['Lineas ']))*100
    elif int((dicc2['Lineas '])<int(dicc1['Lineas '])):
             dicc_result["LINEAS"]=(int(dicc2['Lineas '])/int(dicc1['Lineas ']))*100

    if int((dicc1['Palabras '])<int(dicc2['Palabras '])):
           dicc_result["PALABRAS"]=(int(dicc1['Palabras '])/int(dicc2['Palabras ']))*100
    elif int((dicc2['Palabras '])<int(dicc1['Palabras '])):
             dicc_result["PALABRAS"]=(int(dicc2['Palabras '])/int(dicc1['Palabras ']))*100


    if int((dicc1['Caracteres'])<int(dicc2['Caracteres'])):
           dicc_result["CARACTERES"]=(int(dicc1['Caracteres'])/int(dicc2['Caracteres']))*100
    elif int((dicc2['Caracteres'])<int(dicc1['Caracteres'])):
             dicc_result["CARACTERES"]=(int(dicc2['Caracteres'])/int(dicc1['Caracteres']))*100

    if int((dicc1['Simbolos '])<int(dicc2['Simbolos '])):
           dicc_result["SIMBOLOS"]=(int(dicc1['Simbolos '])/int(dicc2['Simbolos ']))*100
    elif int((dicc2['Simbolos '])<int(dicc1['Simbolos '])):
             dicc_result["SIMBOLOS"]=(int(dicc2['Simbolos '])/int(dicc1['Simbolos ']))*100
             

    return dicc_result
   

#print(comparacion())



class oferta():

    def __init__ (self,codigo,precio,precio_oferta):

        self.codigo = codigo
        self.precio = precio
        self.oferta = precio_oferta
        self.envio_gratis == False

    def __repr__ (self):

        return "CODIGO: "+str(self.codigo)+" PRECIO: "+str(self.precio)+" OFERTA: "+str(self.oferta)
        

    def get_precio(self):
        return self.precio
    def set_precio(self):
        ##el precio del articulo debera ser mayor a cero para ser valido
        if self.precio>0:
            return self.precio
    

    def get_envio (self):
        return self.envio_gratis

    def set_envio(self,cambio_envio):
        self.envio_gratis = cambio_envio   
    
    def cambiar_envio(self):
        return self.set_envio(True)

    def cambiar_todos_los_envios(lista):
        for elemento in lista:
            elemento.cambiar_envio()
        return elemento

def solo_ofertas (lista):
    return [x for x in lista if (x.oferta*100/x.precio)<50]


class Tienda ():

    def __init__ (self,nombre,direccion,ofertas):

        self.nombre=nombre
        self.direccion=direccion
        self.oferta=ofertas

    def borra_todas_ofertas (self):
        self.ofertas=[0]
        return self.ofertas

def cargar_lista (nombre_archivo):
    archivo1 = open(nombre_archivo)
    lista_ofertas = []

    for linea in archivo1:

        dato = linea.strip().split(",")

        oferta1=oferta(dato[0],dato[1],dato[2],dato[3])

        lista_ofertas.append(oferta1)

    return lista_ofertas

    archivo1.close()

            

            
    
tomates=oferta(1234,30,25)
papas=oferta(5678,40,10)
print(tomates)
print(tomates.cambiar_envio())
print(solo_ofertas([tomates,papas]))
print(cambiar_todos_los_envios([tomates,papas]))
print(cargar_lista("C:\\Temp\\EJERCICIO3.txt"))
#funciona si no tomo en cuenta self.envio

        







