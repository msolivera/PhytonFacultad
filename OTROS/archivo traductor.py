#archivo que perminte realizar un traductor
#funcion recibe una lista  con palabras en español, y otra con palabras en ingles
#de a cuerdo a su posicion vamos a saber cual es la traduccion

def traductor (archivo_original,archivo_traducido,lista_idioma1,lista_idioma2):
    original =open("archivo_original.txt")
    traducido=open("archivo_traducido.txt","w")

    for linea in original:

        palabras=linea.split()

        for i in range (len(palabras)):

            idx= lista_idioma1.index(palabras[i].strip())

            if idx !=-1:
                palabras [i] =lista_idioma2[idx]

            traducido.write (" ".join(palabras)+"\n")

    original.close()
    traducido.close()

lista_idioma1=["mi","nombre","es","micaela"]
lista_idioma2=["my","name","is","Micaela"]

traductor("archivo_original.txt","archivo_traducido.txt",lista_idioma1,lista_idioma2)
