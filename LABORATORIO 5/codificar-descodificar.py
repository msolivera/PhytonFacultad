def codificar_cesar (texto):
    resultado3=""
    abecedario=texto.lower()
    contador=0
    cadena="abcdefghijklmnñopqrstuvwxyz"
    for i in range (len(abecedario)):
        x=cadena.find(abecedario[i])+1       
        resultado=texto[i]       
        y =cadena.find(abecedario[i])+3       
        resultado2=cadena[y]
        contador=contador+1
        resultado3+=resultado2
    return resultado3
        

print(codificar_cesar("hola"))



#def decodificar_cesar(texto2):
#    resultado3=""
#    abecedario=texto2.lower()
#    contador=0
#    cadena="abcdefghijklmnñopqrstuvwxyz"
#    for i in range (len(abecedario)):
#        x=cadena.find(abecedario[i])+1       
#        resultado=texto2[i]       
#        y =cadena.find(abecedario[i])-3       
#        resultado2=cadena[y]
#        resultado3+=resultado2
#        contador=contador+1
#    return resultado3
#print(decodificar_cesar("krñd"))
