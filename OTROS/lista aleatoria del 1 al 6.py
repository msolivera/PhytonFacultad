import random

def lista(x):
    resultado=[]
    for i in range (x):
        resultado.append(random.randint(1,6))
    return resultado
print (lista(10))
