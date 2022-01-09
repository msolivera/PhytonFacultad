import random

def sanitizar (cadena):
    dicc={}
    dicc["á"]="a"
    dicc["é"]="e"
    dicc["í"]="i"
    dicc["ó"]="o"
    dicc["ú"]="u"
    dicc["?"]="-"
    dicc["¿"]="-"
    dicc["!"]="-"
    dicc["¡"]="-"
    dicc[" "]="_"
    dicc["ñ"]="n"
    alfabeto="abcdefghijklmnñopqrstuvwxyz"
    
    
    for i in cadena:
        if i in dicc:
            cadena=cadena.replace(i,dicc[i])
        elif i not in alfabeto:
            cadena= cadena.replace(i,"")
                
    return cadena

#print(sanitizar("hola!, como estás?"))

def quitarduplicados(lista):
    dicc={}
    lista2=[]
    for i in lista:
        if i not in dicc:
            lista2.append(i)
            dicc[i]=i
            
    return lista2
#print(quitarduplicados(["hola","mica","jorge","hola",1,2,2,3,3]))


def get_artistas(cancion):
    dicc={}
    dicc["All my loving"]= "The Beatles"
    dicc["All along the watch"] = "Bob Dylan","Jimi Hendrix"
    dicc["Fury of the storm"] = "Dragonforce"
    return dicc[cancion]

#print(get_artistas("All along the watch"))


def probabilidad():
    resultado={}
    for j in range(10000):
        a=random.randint(1,6)
        if a in resultado:
            resultado[a]= resultado[a]+1
        else:
            resultado[a]=1
            
    for b in resultado:
        resultado[b]=(resultado[b]/10000*100)
    return resultado


def mismaletrainicial(archivo1):
    archivo=open(archivo1)
    repeticiones={}
    for linea in archivo:
        cadena=linea.strip()
        palabras= cadena.lower().split()
        for i in range(len(palabras)-1):
            
            if palabras[i][0] in repeticiones:
                repeticiones[palabras[i][0]]= repeticiones[palabras[i][0]] + 1

            else:
                repeticiones[palabras[i][0]]= 1

    print("Letra inicial   Frecuencia")
    print("-------------------------------")
    abecedario="abcdefghijklmnñopqrstuvwxyz"
    for a in abecedario:
        if a in repeticiones:
            print(a+"                       "+str(repeticiones[a]))
        else:
            print(a+"                       "+"0")
        
    
    

mismaletrainicial("C:\\Users\\usuario\\AppData\\Local\\Programs\\Python\\Python36-32\\LABORATORIO 9\\archivo.txt")








    
