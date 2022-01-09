# Laboratorio 7 - Ejercicio 7

import random


class Baraja(object):
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def mismo_palo(self, otra_carta):
        if self.palo == otra_carta.palo:
            return True
        else:
            return False

    def __str__(self):
        return self.palo + ":" + str(self.valor)


def inicializo_mazo():
    '''Retorna una lista que representa el mazo de cartas '''
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ["Copa", "Basto", "Espada", "Oro"]

    mazo = []

    for palo in palos:
        for valor in valores:
            baraja = Baraja(palo, valor)
            mazo.append(baraja)

    return mazo


def reparto_barajas(mazo, n):
    ''' Retorna una lista con la mano de cada participante.
        mazo = Lista de Barajas
        n = cantidad de participantes (valores pueden ser 2 o 4)'''

    mano = []

    if n == 2 or n == 4:
        # Inicializo la lista que contendra la mano, cada elemento
        # corresponde a la mano de un participante
        for i in range(n):
            mano.append([])

        # Reparto de cartas (usa randint, no se baraja)
        for i in range(3):  # en cada iteración le asigna
                            # una baraja a cada participante
            for participante in range(n):
                pos = random.randint(0, len(mazo) - 1)
                mano[participante].append(mazo[pos])
                del(mazo[pos])

    return mano


def obtengo_muestra(mazo):
    '''Retorna una carta que va a ser la muestra'''
    pos = random.randint(0, len(mazo) - 1)
    muestra = mazo[pos]
    del(mazo[pos])
    return muestra


# Programa principal
mazo = inicializo_mazo()
mano = reparto_barajas(mazo, 4)
muestra = obtengo_muestra(mazo)

print("Muestra: {}\n".format(muestra))
for participante in range(4):
    print("Participante: {}".format(participante + 1))
    for carta in mano[participante]:
        print("\t{}".format(carta))
    print()


