import random

def dados (tiradas):
    numero_tirada=1
    while numero_tirada <= tiradas:
        a= random.randint (1,6)
        b= random.randint (1,6)
        promedio= ((a+b)/2)
        numero_tirada +=1
        print ("dado a")
        print (a)
        print ("pado b")
        print (b)
        print ("promedio")
        print (promedio)
        
        

dados(10)        
