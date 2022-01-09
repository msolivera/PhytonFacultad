import random

aleatorio = random.randint(1,100)
intentos = 0
resultado = int(input ("Introduzca un numero del 1 al 100  "))

while intentos < 10 and resultado != aleatorio:
    if resultado<aleatorio:
        intentos = intentos +1
        resultado=int(input ("Introduzca un numero mayor  "))
    if resultado>aleatorio:
        intentos = intentos +1
        resultado=int(input ("Introduzca un numero menor  "))
if resultado == aleatorio:
    print("ganaste")
else:
    print("Has intentado muchas veces")
