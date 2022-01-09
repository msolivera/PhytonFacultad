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
print(genera_contraseña(8,2))
print(genera_contraseña(8,2))
print(genera_contraseña(8,2))
print(genera_contraseña(8,2))
    
        
    
