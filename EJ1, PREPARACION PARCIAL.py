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
