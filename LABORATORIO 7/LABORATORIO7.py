#LABORATORIO 7
#EJERCICIO 1:

import random
def lista (x):
    resultado=[]
    for i in range (x):
        resultado.append(random.randint(1,6))
    return resultado
print(lista(2))

#EJERCICIO 2:
lista_original=["mica","jorge","mica"]
lista_nueva = []
for i in lista_original:
    if i not in lista_nueva:
        lista_nueva.append(i)

print(lista_nueva)
#EJERCICIO 3:

lista1=[1,2,3,7,8,10]
lista2=[4,5,6,9,10]
deferencia_simetrica=[]
for i in lista1:
    if i not in lista2:
        deferencia_simetrica.append(i)  
for i in lista2:
    if i not in lista1:
        deferencia_simetrica.append(i) 
print(deferencia_simetrica)

#EJERCICIO 4:
#.sort para ordenar numeros(de menor a mayor)
#.reverse para invertir el orden.
#pop para quitar elementos segun su indice
def top5 (lista):
    lista.sort()
    lista.reverse()
    while len(lista)>5:
        lista.pop(-1)
    return lista
    


print(top5([1,2,3,4,5,6,6,5]))

#EJERCICIO 5:
def concatenar (per1, per2):
    persona1= " ".join(per1)
    persona2= " ".join (per2)

    resultado=[persona1,persona2]
    return resultado

print(concatenar(["rocky","balboa"],["muhamad","ali"]))
#verdadero correcta
def TRANSFORMAR_NOMBRES (lista):
    resultado=[]
    for i in range (len(lista)):
        resultado.append (lista [i][0]+" "+lista[i][1])
    return resultado
                          

print(TRANSFORMAR_NOMBRES([["rocky","balboa"],["muhamad","ali"]]))




#EJERCICIO 6:
class carta:
    def __init__ (self,palo,valor):
        self.palo=palo
        self.valor=valor
    def __repr__ (self):
        return "<palo: " + self.palo +">" + ":"+"<valor: "+str(self.valor)+">"
    def comparar (self, otra_carta):
        return self.palo == otra_carta.palo

carta1= carta ("oro", 3)
carta2= carta ("oro",3)
print (carta2.comparar(carta1))
print (carta1)

#EJERCICIO 7:

#una lista que represente una mazo de 40 cartas
#un elemento por carta
#cada mano son 3 cartas
#hay que hacer una lista de cuatro manos, es decir una lista de cuatro elementos de tres cartas

import random
mazo = []
palos = ["Oro","Basto","Copa","Espada"]
for palo in palos:
    for numero in range (1,13):
        if numero != 8 and numero != 9:
            mazo.append (str(str (numero)+ " de " + str(palo)))
print (mazo)
jugador1=[]
jugador2=[]
jugador3=[]
jugador4=[]
carta =[]

muestra = mazo[random.randint(1,len(mazo)-1)]
m = mazo.index(muestra)
mazo.pop (m)
for i in range (3):
    carta = mazo[random.randint(1,len(mazo)-1)]
    jugador1.append(carta)
    j = mazo.index(carta)
    mazo.pop (j)
for i in range (3):
    carta = mazo[random.randint(1,len(mazo)-1)]
    jugador2.append(carta)
    j = mazo.index(carta)
    mazo.pop (j)
for i in range (3):
    carta = mazo[random.randint(1,len(mazo)-1)]
    jugador3.append(carta)
    j = mazo.index(carta)
    mazo.pop (j)
for i in range (3):
    carta = mazo[random.randint(1,len(mazo)-1)]
    jugador4.append(carta)
    j = mazo.index(carta)
    mazo.pop (j)
lista = [jugador1,jugador2,jugador3,jugador4]

print ("")
print (muestra)
print ("")
print (jugador1)
print ("")
print ("")

print (mazo)
print ("")
print ("")
print (lista)

#EJERCICIO 8:

