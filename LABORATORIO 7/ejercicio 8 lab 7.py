import random
class carta:
    def __init__ (self, palo,valor):
        self.palo=palo
        self.valor=valor
       
    def __repr__ (self):
        return "Carta: "+str(self.valor)+ " de " + self.palo
#definimos la carta


#FALTA HACER QUE ELIMINE LAS CARTAS QUE VAN SALIENDO DEL MAZO
def def_mazo(): #genera un mazo de 40 cartas
    mazo =[]
    for i in range (12):
        if i+1 != 8 and i+1 !=9:
            mazo.append(carta("oro",i+1))
            mazo.append(carta("copa",i+1))
            mazo.append(carta("basto",i+1))
            mazo.append(carta("espada",i+1))
    return mazo

print(def_mazo())


def def_mano(mazo): #saca 3 cartas del mazo
    mano=[]
    for i in range (3):
        mano.append(mazo[random.randint(0,len(mazo)-1)])
    return mano

mazo=def_mazo()
mano=def_mano(mazo)
print (mano)


def muestra(mazo): #saca una muestra del mazo
    return mazo[random.randint(0,len(def_mazo())-1)]

muestra_mano=muestra(mazo)
print(muestra_mano)

def flor_derecha(x): #define si las tres cartas que yo tengo con iguales
    if x[0].palo == x[1].palo and x[0].palo==x[2].palo:
        return True
    else:
        return False
    
print(flor_derecha(mano))

def pieza (mano,muestra):
    if mano[0].palo == muestra.palo and mano[0].valor in (2,4,5,10,12):
        return True
    elif mano[1].palo==muestra.palo and mano[1].valor in (2,4,5,10,12):
        return True
    elif mano[2].palo==muestra.palo and mano[2].valor in (2,4,5,10,12):
        return True
    else:
        return False



print(pieza(mano,muestra_mano))













    
