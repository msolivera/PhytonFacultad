def numero_suerte (n):
    suma = 0
    while n != 0:
        n=n//10
        resto=n%10
        suma += resto
    if suma==21:
        print ("numero de la suerte")
    else:
        print("numero cualquiera")
    
numero_suerte(993)
    

