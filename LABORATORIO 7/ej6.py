# Laboratorio 7 - Ejercicio 6


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


#Programa principal
carta1 = Baraja('Basto', 5)
carta2 = Baraja('Copa', 1)
print(carta1)
print(carta2)
