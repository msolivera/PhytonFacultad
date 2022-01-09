#PREPARACION CUARTO LABORATORIO

#EJERCICIO 1:

def obtener_cadena():
    cadena=input("Ingrese cadena deseada: ")

    if cadena != "fin":
        
        if len(cadena)<1:
            print("ingrese al menos un caracter: ")
            cadena=input("Ingrese cadena deseada: ")
        if "1" in cadena or "2" in cadena or "3" in cadena or "4" in cadena or "5" in cadena or "6" in cadena or "7" in cadena or "8" in cadena or "9" in cadena or "0" in cadena:
            print("No puede ingresar numeros: ")
            cadena=input("Ingrese cadena deseada: ")
            
        print(cadena)

    if cadena == "fin":

        print("Ha finalizado la escritura")    
       
#obtener_cadena()    


#EJERCICIO 2:

def palindromos (cadena):

    resultado = []

    cadena=cadena.lower().split(" ")

    for palabra in cadena:
        if palabra == palabra [::-1]:
            resultado.append(palabra)

    return resultado

print(palindromos("Hay que reconocer seres extraterrestres"))

    

    
