#EJERCICIO 2:
def tiene_bingo (lista_carton,lista_sorteados):
    for i in lista_carton:
        if lista_carton == lista_sorteados:
            return True
        return False
#print(tiene_bingo([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[89,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))



#EJERCICIO 3:


def va_por_uno (lista_carton,lista_sorteados):

    nueva_lista = []
    contador = 1
    
    for i in lista_sorteados:
        if i not in lista_carton:
            nueva_lista.append(i)
            contador= contador+1
            
            if len(nueva_lista) == 1 :
                return True
            else:
                return False
        

            
        
print(va_por_uno([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[123,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))           
