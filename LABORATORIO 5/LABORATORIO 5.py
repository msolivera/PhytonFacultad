#Laboratorio 5
#ejercicio 1:

def reemplazar (cadena):
    resultado=""
    contador=1
    for i in range (len(cadena)):
        if cadena [i] in " ":
            resultado+=";"
            contador=contador + 1
        else:
            resultado+=cadena[i]
    return resultado
print(reemplazar("h o l a"))

#ejercicio 2:

def fecha_nueva(fecha):
    reemplazo=""
    contador=1
    s=fecha
    s1=s[:2]
    s2=s[3:5]
    s3=s[6:]
    for i in range (len(fecha)):
        if fecha [i] in "/":
            reemplazo="--"
            contador=contador+1
            resultado=s3+reemplazo+s2+reemplazo+s1
    return resultado
print (fecha_nueva("04/03/1994"))
        

#ejercicio 3:
def extraño (parametro):
    cadena1= parametro.lower()
    cadena2="abcdefghijklmnopqrstuvwxyzñ"
    contador=1
    for i in range (len(cadena2)):
        if cadena2[i] in cadena1:
            contador=contador+1
    if contador==28:
        return "PANGRAMA"
    else:
        return "nop" 
    

print(extraño("El viejo Señor Gómez pedía queso, kiwi y habas, pero le ha tocado un saxofón"))

#ejercicio 4:
def lipograma (parametro):
    cadena1= parametro.lower()
    cadena2="abcdefghijklmnopqrstuvwxyzñ"
    contador=1
    for i in range (len(cadena2)):
        if cadena2[i] in cadena1:
            contador=contador+1
    if contador==27:
        return "lipograma"
    else:
        return "nop" 
    

print(lipograma("El viejo Señor Gómez pedía queso, kiwi y habas, pero le ha tocado un saxofón"))

#desafio 1:

def gematria(subcadena):
    abecedario=subcadena.lower()
    contador=0
    cadena="abcdefghijklmnñopqrstuvwxyz"
    for i in range (len(abecedario)):
        x=cadena.find(abecedario[i])
        contador=contador+(x+1)

    return contador

print(gematria("aaa bbb"))

#desafio 2:
def magica(subcadena):
    abecedario=subcadena.lower()
    contador=0
    cadena="abcdefghijklmnñopqrstuvwxyz"
    for i in range (len(abecedario)):
        x=cadena.find(abecedario[i])
        contador=contador+(x+1)
    if contador==21:
        print("MAGICO")
    else:
        print ("numero comun")

    return contador

print(magica("hola"))

#desafio 3:

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



def decodificar_cesar(texto2):
    resultado3=""
    abecedario=texto2.lower()
    contador=0
    cadena="abcdefghijklmnñopqrstuvwxyz"
    for i in range (len(abecedario)):
        x=cadena.find(abecedario[i])+1       
        resultado=texto2[i]       
        y =cadena.find(abecedario[i])-3       
        resultado2=cadena[y]
        resultado3+=resultado2
        contador=contador+1
    return resultado3
print(decodificar_cesar("krñd"))
