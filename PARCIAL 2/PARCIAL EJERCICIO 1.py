def concatenar(lista,cadena):
    resultado=""
    
    for i in range(len(lista[0:])):
        resultado=str(lista[0])+str(cadena)+str(lista[1])+str(cadena)+lista[-1]
        
    return resultado
                       
        
print(concatenar(["lunes","martes","miercoles"],">"))
