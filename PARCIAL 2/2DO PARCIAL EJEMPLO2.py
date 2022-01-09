#EJERCICIO 1
import random

abc = "abcdefghijklmnñopqrstuvwxyz"

def genera_contraseña(cars,nums):
    contraseña = ""

    letras = 0
    numeros = 0

    while len(contraseña)<cars:
        nl = random.randint(0,1)
        if nl == 0 and numeros<nums:
            n=  random.randint(0,9)
            contraseña+=str(n)
            numeros+=1
        elif nl==1 and letras<cars-nums:
            l=random.randint(0,len(abc)-1)
            contraseña +=abc[l]
            letras+=1
    return contraseña
#print(genera_contraseña(8,2))
    
        
#EJERCICIO 2
def riman (lista):
    if len(lista)<1:
        return False
    primera=lista[0]
    for palabra in lista:
        if len(palabra)<3:
            return False
        if primera [-3:] !=palabra[-3:]:
            return False
    return True
#print(riman(["lunes","viernes","tienes"]))

#EJERCICIO 3
class RecetaDeCocina():
    def __init__(self,nombre,calorias,ingredientes):
        self.nombre=nombre
        self.calorias=calorias
        self.ingredientes=ingredientes
    def engorda(self):
        return self.calorias>100 and "harina" in self.ingredientes

    def agregar_ingredientes (self, nuevos_ingredientes):
        for ing in nuevos_ingredientes:
            if ing[0] not in self.ingredientes:
                self.ingredientes.append(ing[0])
                self.calorias+=ing[1]

    def vegetariana (self):
        return "carne" not in self.ingredientes

    def __repr__ (self):
        return "receta: "+self.nombre+" calorias: "+str(self.calorias)+" ingredientes: "+",".join(self.ingredientes)
r1=RecetaDeCocina("panchos",500,["pancho","pan","mostaza"])
#print(r1)
#print(r1.vegetariana())
#print(r1.engorda())
r1.agregar_ingredientes([["mayonesa",100],["panceta",200],["mostaza",300]])
print(r1)




























